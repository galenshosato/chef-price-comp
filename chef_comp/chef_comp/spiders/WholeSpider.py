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
            name = div.css('a.w-pie--product-tile__link > div.w-pie--product-tile__content > h2::text').get()
            sale_check = div.css('a.w-pie--product-tile__link > div.w-pie--product-tile__content > div.w-pie--prices > ul > li > span.sale_price::text').getall()
            if sale_check:
                if len(sale_check) > 1:
                    price = sale_check[1]
                else:
                    price = sale_check[0]
            else:
                price = div.css('a.w-pie--product-tile__link > div.w-pie--product-tile__content > div.w-pie--prices > ul > li > span.regular_price > b::text').get()
            number = float(price.replace('$', '').replace('/lb', '').replace('¢', ''))
            if number > 75:
                number = number / 100

            item = {}
            item['name'] = name
            if "lb" in price:
                item['price'] = price.replace('/lb', ' LB' )
            else:
                price = price + ' CT'
                item['price'] = price
            item['ppu'] = number
            item['unique_id'] = name
            item['vendor_id'] = 2
            yield item