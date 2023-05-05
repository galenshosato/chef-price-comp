import scrapy
import re


class WholeSpider(scrapy.Spider):
    name = "WholeSpider"
    
    start_urls = ['https://www.wholefoodsmarket.com/products/produce']

    cookies = {
    
        }


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback=self.parse)
    
    def parse(self, response):
        for div in response.css('div.w-pie--product-tile'):
            name = div.css('div.w-pie--product-tile__content > h2::text').get()
            price = div.css('div.w-pie--product-tile__content > div.w-pie--prices > ul > li > span.regular_price > b::text').get()
            number = float(price.replace('$', '').replace('/lb', '').replace('¢', ''))
            if number > 75:
                number = number / 100

            item = {}
            item['name'] = name
            item['price'] = number

            yield item