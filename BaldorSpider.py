import scrapy
from scrapy import FormRequest

class BaldorSpider(scrapy.Spider):
    name = 'Baldor Food'
    start_urls = ['https://www.baldorfood.com/products/vegetables/artichokes', 'https://www.baldorfood.com/products/fruits/stone-fruit']

    cookies = {
        
    }

    def start_requests(self):
         for url in self.start_urls:
              yield scrapy.Request(url, cookies = self.cookies, callback = self.parse)

    def parse(self, response):
            for div in response.css('div.table-cover-back'):
                item = {}
                item['title'] = div.css('div.product-title-and-sku > div.pct-heading > h3 > a::text').get()
                price_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price::text').get()
                quantity_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price > span.price-unit::text').get()
                item['price'] = price_text + quantity_text
                yield item
    
