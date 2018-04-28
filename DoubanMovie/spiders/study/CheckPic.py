# -*- coding: utf-8 -*-
"""
最后一步，对于要测试的验证码处理，然后进行预测，输出结果
"""
import time
import os
from study.cutPic import imgTransfer, segment
from study.getPicType import getBinaryPix
from study.svmPic import cross_validation

def cutPictures2(name):
    im = imgTransfer(name)
    pics = segment(im)
    for pic in pics:
        pic.save(u'pics_cut_temp/%s.jpeg' % (int(time.time() * 1000000)), 'jpeg')


def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)


def load_Predict(name):
    CUR_PATH = r'pics_cut_temp/'
    del_file(CUR_PATH)
    #
    cutPictures2(name)  # 切割图片

    dirs = u'pics_cut_temp/'
    fs = os.listdir(dirs)  # 获取图片名称
    clf = cross_validation()
    predictValue = []

    for fname in fs:
        fn = dirs + fname
        binpix = getBinaryPix(fn)
        predictValue.append(clf.predict([binpix]))

    predictValue = [str(int(i)) for i in predictValue]
    print("the picture number is :", "".join(predictValue))


name = u'15.jpg'
load_Predict(name)