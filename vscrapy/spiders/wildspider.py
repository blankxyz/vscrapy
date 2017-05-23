# -*- coding: utf-8 -*-
# 浙江视界爬虫
import scrapy
# import scrapy_splash
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from vscrapy.items import YeskyItem
from scrapy.conf import settings
import urllib
import json
from scrapy.http import Request, HtmlResponse

class CommonSpider(RedisCrawlSpider):
    name = "vsipder"
    allowed_domains = settings['ALLOWED_DOMAIN']
    # start_urls = (
    #     'http://www.zjol.com.cn/',
    # )
    redis_key = 'wildspider:start_urls'

    rules = (
        # follow all links
        Rule(LinkExtractor(allow=()), follow=True,callback='parse_page'),
        # Rule(LinkExtractor(allow=('wap.yesky.com')), follow=False, callback='parse_page')
        # Rule(LinkExtractor(allow='video/*.shtml'), callback='parse_page', follow=True),
    )

    # __init__方法必须按规定写，使用时只需要修改super()里的类名参数即可
    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        # domain = kwargs.pop('domain', settings['ALLOWED_DOMAIN'])
        self.allowed_domains = filter(None, settings['ALLOWED_DOMAIN'])

        # 修改这里的类名为当前类名
        super(CommonSpider, self).__init__(*args, **kwargs)

    # global splashurl;
    # splashurl = "http://localhost:8050/render.html";

    # splash 服务器地址
    # 此处是重父类方法，并使把url传给splash解析
    # def make_requests_from_url(self, url):
    #     global splashurl;
    #     url = splashurl + "?url=" + url;
    #     body = json.dumps({"url": url, "wait": 5, 'images': 0, 'allowed_content_types': 'text/html; charset=utf-8'})
    #     headers = {'Content-Type': 'application/json'}
    #     return Request(url, body=body, headers=headers, dont_filter=True)

    def parse_page(self, response):

        proto, rest = urllib.splittype(response.url)
        res, rest = urllib.splithost(rest)






