# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import MySQLdb
from DoubanMovie import settings
from DoubanMovie.wordcloud import wordCloud

'''
数据清洗类

说明：
1、将数据写入数据库
2、去重数据，避免重复数据和暂停导致数据重复

'''


class TutorialPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = MySQLdb.connect(
            host=settings.MYSQL_HOST,
            port=3306,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()
        sql = """
                CREATE TABLE IF NOT EXISTS 
                    """ + settings.DOUBAN_TABLE_NAME + """
            (
            `uid` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '',
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `useableNumber` varchar(20) CHARACTER SET utf8 NOT NULL DEFAULT '',
            `content` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
            `time` varchar(19) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
            `star` varchar(20) COLLATE utf8_unicode_ci NOT NULL DEFAULT '',
            PRIMARY KEY (`id`)
            ) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
        """
        try:
            self.cursor.execute(sql)
            self.connect.commit()
            print('create table success.')
        except Exception as error:
            print('create table error:' + str(error))

    '''
      if item['id'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['id'])
            return item
    '''

    def process_item(self, item, spider):
        print('process_item.')
        try:
            # 查重处理
            self.cursor.execute("""select * from """ + settings.DOUBAN_TABLE_NAME + """ where uid = %s""",
                                [item['uid']])
            # 是否有重复数据
            repetition = self.cursor.fetchone()

            # 重复
            if repetition:
                print('has data.')
                pass
            else:
                # 插入数据
                self.cursor.execute(
                    """insert into """ + settings.DOUBAN_TABLE_NAME + """(uid, useableNumber, content, time ,star)
                    value (%s, %s, %s, %s, %s)""",
                    [item['uid'],
                     item['useableNumber'],
                     item['content'],
                     item['time'],
                     item['star']
                     ])

            # 提交sql语句
            self.connect.commit()
            print('insert success.')
        except Exception as error:
            # 出现错误时打印错误日志
            print('Exception: ' + str(error))
        return item

    def open_spider(self, spider):
        print('open_spider..................')

    def close_spider(self, spider):
        print('close_spider..................')


'''
打开方式:   r-->只读
            w-->只写
            r+ -->读写
            w+ -->读写
            a -->追加写
            a+ -->追加读写
​文件以w+打开后，读取出来的内容为空；而以r+打开，写入的内容为追加。
'''

'''
将内容写入文件,为生成词云做准备
'''


class WriteToFilePipeline(object):

    def __init__(self):
        self.cloud = wordCloud.WordClout()
        self.file = codecs.open(self.cloud.getTextSource(), 'w+', encoding='utf-8')

    def open_spider(self, spider):
        print('open_spider..................')

    def close_spider(self, spider):
        print('close_spider..................')
        self.file.close()
        self.cloud.makeCloud()

    def process_item(self, item, spider):
        print('process_item.')
        self.file.write(item['content'] + "\r\n")
        return item
