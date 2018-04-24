# DoubanMovie 
本项目为爬虫项目，主要是爬取的豆瓣上电影的短影评，将数据爬取完成后，
将影评数据存入数据库，同时生成影评的词云图

## 项目说明：
使用的Python的**Scrapy**框架，数据库为**Mysql**

## 包含的主要功能
1. 自动登录豆瓣用户，内置用户名和密码，如使用可修改为个人用户，多次爬取会出现验证码，项目会自动打开验证码图片，需要用户输入正确的验证码
2. 自动生成数据库中表，同时插入的数据会自动去重
3. 爬取完成后，自动打开生成的词云，请耐心等待

## 过程特别说明：
1. 如果不登录，只能爬取10页数据,已增加检测机制，不登录不能爬取数据【已解决】
2. 登录后爬取到最后一共400+留言【已解决】
3. 其中使用了更换useragent的方式【已解决】
4. 记录到数据库中，会自动去重【已解决】
5. 遇到新问题，登录有验证码，需要处理，使用的本地打开验证码，用户输入正确验证码的方式【已解决】
6. 如果验证码错误，增加了检测机制，重新输入验证码【已解决】


## 遇到的问题说明：
* 如果使用用户名和密码登录，如果一直不成功，应该尝试在浏览器登录，避免因为帐号被锁定而测试不成功

## 详细的使用说明：
* 如果需要爬取其他影评，需要修改**settings.DOUBAN_ID**(此为网址中电影ID)和**settings.TABLE_NAME**字段（此为数据库的表名）

### 运行代码:
运行如下代码即可：
```
scrapy crawl DoubanDancer
```

## 问题反馈
* 作者：王超
* QQ：919536816
* 注：有定制化需求自己下源码根据自己的需求改动，不要指望别人给你实现，这样永远没有成长！
* 本项目实现没有难度，只要静心看代码都能看的懂。我只提供最基础的功能，尽量满足大部分的开发需求。

## License

Copyright (c) 2018 Wangchao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

