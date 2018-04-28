# -*- coding: utf-8 -*-
from PIL import Image
import pytesseract
import os

'''
此为pytesseract测试使用库
说明：
1、使用了几天 pytesseract 这个库，发现局限性很大，感觉应该使用机器学习的方式，训练
2、使用pytesseract 可以识别简单的字母，验证码图片和汉字无法识别

'''


# ,lang='chi_sim'

# 背景色处理，可有可无
# image = Image.open('D:/captcha.jpg')

def readText(path='', lang='eng'):
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'

    img = Image.open(path)  # PIL库加载图片
    # img = img.convert('RGBA')  # 转换为RGBA
    pix = img.load()  # 转换为像素
    for x in range(img.size[0]):  # 处理上下黑边框，size[0]即图片长度
        pix[x, 0] = pix[x, img.size[1] - 1] = (255, 255, 255, 255)
    for y in range(img.size[1]):  # 处理左右黑边框，size[1]即图片高度
        pix[0, y] = pix[img.size[0] - 1, y] = (255, 255, 255, 255)
    # img.save(path + '')
    img.save("temp.png")  # 由于tesseract限制，这里必须存到本地文件
    text = pytesseract.image_to_string(Image.open("temp.png"), lang=lang, config=tessdata_dir_config)
    os.remove('temp.png')
    # text = pytesseract.image_to_string(image=Image.open(path), lang=lang, config=tessdata_dir_config)
    print("text:" + text)


if __name__ == '__main__':
    print("readText:")
    startPath = os.path.abspath(os.path.dirname(__file__)) + os.path.sep
    print("startPath:" + startPath)
    readText(startPath + os.path.sep + '2.jpg')  # 可以识别ABC

    readText(startPath + os.path.sep + 'abc.png')  # 可以识别ABC
    readText(startPath + os.path.sep + 'chinese.png', 'chi_sim')  # 异常，未找到解决方法，放弃此方案
