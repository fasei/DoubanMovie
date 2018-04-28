# -*- coding:utf-8 -*-
import requests
import time

# 文件下载，主要下载训练集
def download_pics(pic_name):
    url = 'http://smart.gzeis.edu.cn:8081/Content/AuthCode.aspx'
    res = requests.get(url, stream=True)

    with open(u'downloadpics/%s.jpg' % (pic_name), 'wb') as f:
        print("download  " + pic_name + ".jpg")
        for chunk in res.iter_content(chunk_size=1024*1000):
            if chunk:
                f.write(chunk)
                f.flush()
        f.close()


if __name__ == '__main__':
    for i in range(0, 1200):
        pic_name = str(i)
        download_pics(pic_name)
        time.sleep(0.1)

