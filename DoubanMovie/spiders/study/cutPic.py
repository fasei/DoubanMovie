# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter
import time

# 图片切割
def segment(im):
    s = 12
    w = 40
    h = 81
    t = 0
    im_new = []

    for i in range(4):
        im1 = im.crop((s + w * i, t, s + w * (i + 1), h))
        im_new.append(im1)
    return im_new


# 图片预处理，二值化，图片增强
def imgTransfer(f_name):
    im = Image.open(f_name)
    im = im.filter(ImageFilter.MedianFilter())
    # enhancer = ImageEnhance.Contrast(im)
    # im = enhancer.enhancer(1)
    im = im.convert('L')

    return im


def cutPictures(img):
    im = imgTransfer(img)
    pics = segment(im)
    for pic in pics:
        pic.save(u'pics_cut/%s.jpeg' % (int(time.time() * 1000000)), 'jpeg')

    # 读取某文件夹下的所有图片


import os


def getAllImages(folder):
    assert os.path.exists(folder)
    assert os.path.isdir(folder)
    imageList = os.listdir(folder)
    imageList = [os.path.abspath(item) for item in imageList if os.path.isfile(os.path.join(folder, item))]
    return imageList


if __name__ == '__main__':

    files_name = getAllImages(u'downloadpics//')

    for i in files_name:
        # cutPictures()
        files = i.replace('\\', '/')
        s = files.split('/')
        name = ''
        for j in s[:-1]:
            name = name + j + '/'
        name = name + 'downloadpics/' + s[-1]

        cutPictures(name)
