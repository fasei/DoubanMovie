# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

'''
豆瓣-这就是舞者的内容
'''


class DouBanDancerItem(scrapy.Item):
    uid = scrapy.Field()  # 唯一uid
    content = scrapy.Field()  # 内容
    useableNumber = scrapy.Field()  # 有用
    star = scrapy.Field()  # 评星
    time = scrapy.Field()  # 时间
