#coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

from xiaozhu.items import XiaozhuItem

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class XiaozhuSpider(CrawlSpider):

    name = 'xiaozhu'

    start_urls=[
        'http://sh.xiaozhu.com/search-duanzufang-p1-0/'
    ]

    def parse(self, response):

        item = XiaozhuItem()
        selector = Selector(response)

        infos = selector.xpath("//ul[@class='pic_list clearfix']/li")

        for info in infos:

            url = infos.xpath('a/@href').extract()[0]

            item['url'] = url

            price = info.xpath('div[2]/span[1]/i/text()').extract()[0]

            item['price']= int(price)


            intro = info.xpath('div[2]/div/a/span/text()').extract()[0]

            house = info.xpath('div[2]/div/em/text()').extract()[0]

            house = str(house).strip().split('/')

            item['rent_type'] = house[0]


            item['beds'] = int(filter(str.isdigit,house[1]))
            nums = filter(str.isdigit,house[0])

            item['num_of_people'] = int(filter(str.isdigit, house[2]))


            comment = str(info.xpath('div[2]/div/em/span/text()').extract()[0]).strip()

            start = 0
            comment_num = 0
            if comment.find('/') >0:

                comment = comment.split('/')

                item['star'] = int(filter(str.isdigit, comment[0]))

                item['comment_num'] = int(filter(str.isdigit, comment[1]))

            else:
                item['comment_num'] = int(filter(str.isdigit, comment))

                item['star'] =0


            yield item






        for i in range(2,14):
            nexturl = 'http://sh.xiaozhu.com/search-duanzufang-p%s-0/'%i

            yield Request(nexturl,callback=self.parse)





















