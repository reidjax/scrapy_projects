# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# Data columns as listed on espn.com
class players(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    college_team = scrapy.Field()
    player_and_nfl_team = scrapy.Field()
    position = scrapy.Field()