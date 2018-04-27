import urllib
import scrapy
from PIL import Image
from scrapy import log
from scrapy.http import Request
from scrapy.selector import Selector

from DoubanMovie import settings
from DoubanMovie.items import DouBanDancerItem

'''
爬取豆瓣"这就是街舞"的影评
URL:https://movie.douban.com/subject/27199901/comments?start=0&limit=20&sort=new_score&status=P&percent_type=
过程特别说明：
1、如果不登录，只能爬取10页数据,已增加检测机制，不登录不能爬取数据
2、登录后爬取到最后一共400+留言
3、其中使用了更换useragent的方式
4、记录到数据库中，会自动去重
5、遇到新问题，登录有验证码，需要处理,以解决，使用的本地打开验证码，用户输入正确验证码的方式
6、如果验证码错误，增加了检测机制，重新输入验证码


问题说明：
1、如果使用用户名和密码登录，如果一直不成功，应该尝试在浏览器登录，避免因为帐号被锁定而测试不成功

使用说明：
* 如果需要爬取其他影评，需要修改settings.DOUBAN_ID(此为网址中电影ID)和settings.TABLE_NAME字段（此为数据库的表名）


运行代码:
scrapy crawl DoubanDancer

'''


class DoubanDancer(scrapy.Spider):
    name = "DoubanDancer"  # 爬虫的名称
    loginUrl = "https://www.douban.com/login"  # 登录的地址
    allowed_domains = ["movie.douban.com", "www.douban.com", "douban.com"]  # 白名单的地址
    url = "https://movie.douban.com/subject/" + settings.DOUBAN_ID + "/comments"  # 豆瓣影评的起始地址
    start_urls = [
        url + "?start=0&limit=20&sort=new_score&status=P&percent_type="]

    def start_requests(self):
        return [
            Request(url=self.loginUrl, callback=self.parseLogin)]  # 可以传递一个标示符来使用多个。如meta={'cookiejar': 1}这句，后面那个1就是标示符

    def parseLogin(self, response):
        print("开始验证登录过程.")

        captcha = response.xpath('//img[@id="captcha_image"]/@src').extract()  # 获取验证码图片的链接
        if len(captcha) > 0:
            print("需要输入验证码.")

            print("captcha:" + captcha[0])
            # 此时有验证码，需要处理
            local_filename, headers = urllib.request.urlretrieve(url=captcha[0])

            print("captcha:" + local_filename)  # 文件路径

            img = Image.open(local_filename)  # 打开验证码图片
            img.show()

            captcha_value = input('查看captcha.png,有验证码请输入:')
            print("验证码:" + captcha_value)

            realCaptchaId = response.xpath('//input[@name="captcha-id"]/@value').extract()[0]  # 获取验证码图片的链接

            data = {
                "form_email": settings.DOUBAN_USERID, "form_password": settings.DOUBAN_USER_PASSWORD,
                "captcha-solution": captcha_value, "captcha-id": realCaptchaId
            }
        else:
            data = {"form_email": settings.DOUBAN_USERID, "form_password": settings.DOUBAN_USER_PASSWORD, }
        return [
            scrapy.FormRequest(self.loginUrl, formdata=data, dont_filter=True,
                               callback=self.loginResult, )]

    # 模拟登录，不登陆只能访问10页数据
    def loginResult(self, response):
        # 登陆完成之后开始爬取数据
        # print u'成功？'
        print("登录结果判断:")
        '''  
            #如果登陆成功，会有如下代码
            <li class="nav-user-account">
            <a target="_blank" href="https://www.douban.com/accounts/" class="bn-more">
        '''
        isLoginSuccess = response.xpath('//li[@class="nav-user-account"]').extract()
        if (len(isLoginSuccess)) > 0:  # 登录成功
            print("登录成功.")
            yield Request(self.start_urls[0], dont_filter=True, callback=self.parse)
        else:
            print("登录失败.")
            # 此处需要添加don_filter，因为提交会跳转页面，所以需要过滤，不然会异常
            yield Request(self.loginUrl, dont_filter=True, callback=self.parseLogin)

    def parse(self, response):
        Movies = response.xpath('//div[@class="comment"]').extract()
        print(len(Movies))

        for eachMoive in Movies:
            # 因为此处返回的是字符串，已经没有选择器功能了，所以需要自建选择器
            selector = Selector(text=eachMoive)
            item = DouBanDancerItem()
            item['useableNumber'] = \
                selector.xpath('//span[@class="comment-vote"]/span[@class="votes"]/text()').extract()[0].strip()  # 有用
            item['time'] = \
                selector.xpath('//span[@class="comment-info"]/span[@class="comment-time "]/@title').extract()[
                    0].strip()  # time
            item['content'] = selector.xpath('//p/text()').extract()[0].strip()
            item['star'] = selector.xpath('//span[@class="comment-info"]/span/@title').extract()[0].strip()
            item['uid'] = selector.xpath('//span[@class="comment-vote"]/input/@value').extract()[0].strip()  # 有用

            # 如果用户没有评分，会取到添加时间，此处需处理数据,也可以添加pipLine处理
            if len(item['star']) > 2:
                item['star'] = "未看"

            self.log('item: %s' % item, level=log.WARNING)

            yield item  # 提交生成csv文件

        nextLink = response.xpath('//div[@class="center"]/a[@class="next"]/@href').extract()[0]
        # 第10页是最后一页，没有下一页的链接
        if nextLink:
            print(nextLink)

            headers = {
                'Accept-Encoding': 'gzip, deflate, sdch, br',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Connection': 'keep-alive',
                'Referer': 'https://movie.douban.com/',
            }  # 构造请求头

            yield Request(self.url + nextLink, callback=self.parse, headers=headers)
            # 递归将下一页的地址传给这个函数自己，在进行爬取
