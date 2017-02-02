# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Field,Item


class XiaozhuItem(Item):

    url = Field()
    price = Field()
    rent_type = Field()
    beds = Field()
    num_of_people = Field()
    star = Field()
    comment_num = Field()
