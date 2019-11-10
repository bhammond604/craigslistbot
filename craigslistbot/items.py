# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# Specify the item to send data through pipeline
class CraigslistbotItem(scrapy.Item):
    # Fields for item
    name = scrapy.Field()
    link = scrapy.Field()
    identifier = scrapy.Field()
