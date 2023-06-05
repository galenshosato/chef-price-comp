# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy



class BaldorItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    ppu = scrapy.Field()
    unique_id = scrapy.Field()
    