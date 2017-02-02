#coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class XiaozhuSpider(CrawlSpider):

    name = 'xiaozhu'

    start_urls=[
        'http://sh.xiaozhu.com/search-duanzufang-p1-0/'
    ]

    def parse(self, response):
        selector = Selector(response)

        infos = selector.xpath("//ul[@class='pic_list clearfix']/li")

        for info in infos:

            price = info.xpath('div[2]/span[1]/i/text()').extract()[0]

            print price

            intro = info.xpath('div[2]/div/a/span/text()').extract()[0]

            print intro





















