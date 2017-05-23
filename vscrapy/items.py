# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YeskyItem(scrapy.Item):
    domain = 'yesky.com'
    title = scrapy.Field()
    description = scrapy.Field()
    keywords = scrapy.Field()
    url = scrapy.Field()
    video_url = scrapy.Field()
    author = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
