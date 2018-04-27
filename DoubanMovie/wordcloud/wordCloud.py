# coding: utf-8
import os

import jieba
from PIL import Image
from scipy.misc import imread  # 这是一个处理图像的函数
from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt

from DoubanMovie import settings

'''
集成生成词云的功能，仅需要配置如下几个参数即可


'''

'''

路径问题
import os

print '***获取当前目录***'
print os.getcwd()
print os.path.abspath(os.path.dirname(__file__))

print '***获取上级目录***'
print os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print os.path.abspath(os.path.dirname(os.getcwd()))
print os.path.abspath(os.path.join(os.getcwd(), ".."))

print '***获取上上级目录***'
print os.path.abspath(os.path.join(os.getcwd(), "../.."))

'''


class WordClout(object):

    def __init__(self):
        self.startPath = os.path.abspath(os.path.dirname(__file__)) + os.path.sep
        print("startPath:" + self.startPath)
        self.postfix = ".png"
        self.backgroundImg = self.startPath + "timg" + self.postfix  # 背景图
        self.textSource = self.startPath + "aaa.txt"  # 文字源文件
        # self.wordCloudImg = self.startPath + "wordCloudImg"+self.postfix   # 生成词云
        self.wordCloudImg = self.startPath + settings.DOUBAN_ID + self.postfix  # 生成词云
        self.stopwords = self.startPath + "stopwords.txt"  # 需要屏蔽的词汇
        self.jiebaWords = self.startPath + "jiebaworld.txt"  # 需要连接显示的词汇

    def getTextSource(self):
        return self.textSource

    # 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
    # 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
    def stop_words(self, texts):
        words_list = []
        word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
        with open(self.stopwords, encoding="utf-8") as f:
            unicode_text = f.read()
            f.close()  # stopwords文本中词的格式是'一词一行'
        for word in word_generator:
            if word.strip() not in unicode_text:
                words_list.append(word)
        return ' '.join(words_list)  # 注意是空格

    def makeCloud(self):
        back_color = imread(self.backgroundImg)  # 解析该图片

        wc = WordCloud(background_color='white',  # 背景颜色
                       max_words=1000,  # 最大词数
                       mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                       max_font_size=100,  # 显示字体的最大值
                       # stopwords=STOPWORDS.add('苟利国'),  # 使用内置的屏蔽词，再添加'苟利国'
                       font_path="C:/Windows/Fonts/STFANGSO.ttf",  # 解决显示口字型乱码问题，可进入C:/Windows/Fonts/目录更换字体
                       #  random_state=42,  # 为每个词返回一个PIL颜色
                       # width=1000,  # 图片的宽
                       # height=860  #图片的长
                       )
        # WordCloud各含义参数请点击 wordcloud参数

        # 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
        # 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
        with open(self.jiebaWords, 'r', encoding='utf8') as fin:
            for line in fin.readlines():
                line = line.strip('\n')
                jieba.add_word(line)
                # sep’.join（seq）以sep作为分隔符，将seq所有的元素合并成一个新的字符串

        # 打开词源的文本文件
        text = open(self.textSource, encoding="utf-8").read()
        text = self.stop_words(text)
        # print(text)
        wc.generate(text)
        # 基于彩色图像生成相应彩色
        image_colors = ImageColorGenerator(back_color)
        # 显示图片
        plt.imshow(wc)
        # 关闭坐标轴
        plt.axis('off')
        # 绘制词云
        plt.figure()
        plt.imshow(wc.recolor(color_func=image_colors))
        plt.axis('off')
        # 保存图片
        wc.to_file(self.wordCloudImg)
        img = Image.open(self.wordCloudImg)  # 打开图片
        img.show()
