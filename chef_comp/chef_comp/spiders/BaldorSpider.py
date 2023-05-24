import scrapy
import re

class BaldorSpider(scrapy.Spider):
    name = 'BaldorSpider'
    start_urls = ['https://www.baldorfood.com/products/vegetables/artichokes?viewall=1',
                  'https://www.baldorfood.com/products/fruits/stone-fruit?viewall=1',
                  'https://www.baldorfood.com/products/vegetables/asparagus?viewall=1',
                  'https://www.baldorfood.com/products/vegetables/beans-peas?viewall=1',
                  'https://www.baldorfood.com/products/vegetables/broccoli?viewall=1',
                  'https://www.baldorfood.com/products/vegetables/radishes?viewall=1',
                  'https://www.baldorfood.com/products/vegetables/celery?viewall=1',
                  'https://www.baldorfood.com/products/fruits/bananas?viewall=1',
                  'https://www.baldorfood.com/products/fruits/citrus?viewall=1',
                  'https://www.baldorfood.com/products/fruits/apples?viewall=1'
                  ]

    cookies = { 'PHPSESSID': 'cvnjtu5rsm9vspd481bi4r5qmm'}

    def __init__(self, titles=None, *args, **kwargs):
         super(BaldorSpider, self).__init__(*args, **kwargs)
         self.titles = titles

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback = self.parse)

    def parse(self, response):
            for div in response.css('div.table-cover-back'):
                name = div.css('div.product-title-and-sku > div.pct-heading > h3 > a::text').get()
                name_lower = name.lower()
                for title in self.titles:
                    if title in name_lower:
                        item ={}
                        price_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price::text').get()
                        if not price_text:
                            continue
                        price_int = float(price_text[1:6])
                        quantity_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price > span.price-unit::text').get()
                        numbers = []
                        if quantity_text == '1/2 CRATE':
                            numbers = ['.5']
                        else:
                            numbers = re.findall(r'\d+', quantity_text)
                        quantity_int=''
                        for number in numbers:
                            number = float(number)
                            if number >= 3:
                                quantity_int = number
                            elif 0 < number < 1:
                                quantity_int = number
                            else:
                                print('Still works')
                        item['name'] = name
                        item['price'] = price_text + quantity_text
                        item['price per unit'] = round(price_int / quantity_int, 2)
                        yield item
