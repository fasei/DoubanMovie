# -*- coding: utf-8 -*-
"""
对切割后的图片进行分类，及0-9
"""
from pytesseract import *
from PIL import Image, ImageEnhance
import os
import shutil


# ocr图像识别
def ocr(img):
    try:
        img = Image.open(img)

        enhancer = ImageEnhance.Color(img)
        enhancer = enhancer.enhance(0)
        enhancer = ImageEnhance.Brightness(enhancer)
        enhancer = enhancer.enhance(2)
        enhancer = ImageEnhance.Contrast(enhancer)
        enhancer = enhancer.enhance(8)
        enhancer = ImageEnhance.Sharpness(enhancer)
        img = enhancer.enhance(20)

        rs = image_to_string(img)
        print("result:" + rs)
    except:
        return 'none'
    return rs


# 使用ocr进行训练的预分类
def category(originfile, dirs, filename):
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    shutil.copyfile(originfile, dirs + filename)


if __name__ == '__main__':
    dirs = u'pics_cut/'

    # 将ocr识别的文件按照数组编号存放在相应的文件夹中
    for fr in os.listdir(dirs):
        f = dirs + fr
        print("f:" + f)
        if f.rfind(u'.DS_Store') == -1:
            rs = ocr(f)

            if '|' not in rs and '*' not in rs:
                if '?' not in rs and '<' not in rs and '>' not in rs:
                    category(f, u'category/%s/' % rs, fr)
