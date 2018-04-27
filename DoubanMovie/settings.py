# -*- coding: utf-8 -*-

# Scrapy settings for DoubanMovie project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DoubanMovie'

SPIDER_MODULES = ['DoubanMovie.spiders']
NEWSPIDER_MODULE = 'DoubanMovie.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'DoubanMovie (+http://www.yourdomain.com)'

# Obey robots.txt rules
# 在setting里需要把ROBOTSTXT_OBEY设置为False，否则新的scrapy默认遵守robots协议
ROBOTSTXT_OBEY = False

RANDOMIZE_DOWNLOAD_DELAY = False
# 延时设置 单位s
DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS_PER_IP = 40

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#   'DoubanMovie.middlewares.TutorialSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 测试发现IP代理时，服务器拒绝

    # IP代理的中间件
    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 123,
    # 'DoubanMovie.middlewares.HTTPPROXY': 125,

    # 浏览器代理的中间件
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 2,
    'DoubanMovie.middlewares.USERAGENT': 1
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# item按数字从低到高的顺序，通过pipeline，通常将这些数字定义在0-1000范围内。
ITEM_PIPELINES = {
    'DoubanMovie.pipelines.TutorialPipeline': 300,
    'DoubanMovie.pipelines.WriteToFilePipeline': 310,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 设置编码格式
FEED_EXPORT_ENCODING = 'utf-8'

# start MySQL database configure setting
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'self'
MYSQL_USER = 'root'
MYSQL_PASSWD = '919536816'
# end of MySQL database configure setting

'''
这就是街舞的配置信息
#数据表名
DOUBAN_TABLE_NAME="dancer"
#电影的ID
DOUBAN_ID="27199901"
'''
DOUBAN_TABLE_NAME = "wonderboy"
# 电影的ID
DOUBAN_ID = "26787574"

# 豆瓣的用户名和密码
DOUBAN_USERID = "15128296802"  # 豆瓣的用户名
DOUBAN_USER_PASSWORD = "xiaoyuanyuan1314"  # 豆瓣的密码
