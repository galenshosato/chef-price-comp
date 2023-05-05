import scrapy
import re

class BaldorSpider(scrapy.Spider):
    name = 'BaldorSpider'
    start_urls = ['https://www.baldorfood.com/products/vegetables/artichokes',
                  'https://www.baldorfood.com/products/fruits/stone-fruit',
                  'https://www.baldorfood.com/products/vegetables/asparagus',
                  'https://www.baldorfood.com/products/vegetables/beans-peas',
                  'https://www.baldorfood.com/products/vegetables/broccoli',
                  'https://www.baldorfood.com/products/vegetables/radishes',
                  'https://www.baldorfood.com/products/vegetables/celery',
                  'https://www.baldorfood.com/products/fruits/bananas',
                  'https://www.baldorfood.com/products/fruits/citrus',
                  'https://www.baldorfood.com/products/fruits/apples'
                  ]

    cookies = { 'PHPSESSID': ''}

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
                        price_int = float(price_text.replace('$', '').replace(' ', '').replace('/', ''))
                        quantity_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price > span.price-unit::text').get()
                        numbers = re.findall(r'\d+', quantity_text)
                        quantity_int=''
                        for number in numbers:
                            number = int(number)
                            if number >= 3:
                                quantity_int = number
                            else:
                                print('Still works')
                        item['name'] = name
                        item['price'] = price_text + quantity_text
                        item['price per unit'] = round(price_int / quantity_int, 2)
                        yield item
