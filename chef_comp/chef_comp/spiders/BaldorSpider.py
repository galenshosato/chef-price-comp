import scrapy
import re

class BaldorSpider(scrapy.Spider):
    name = 'baldor'
    start_urls = ['https://www.baldorfood.com/products/fruits/apples?viewall=1',
                  'https://www.baldorfood.com/products/fruits/avocados?viewall=1',
                #   'https://www.baldorfood.com/products/fruits/bananas?viewall=1',
                #   'https://www.baldorfood.com/products/fruits/berries?viewall=1',
                #   'https://www.baldorfood.com/products/fruits/citrus?viewall=1',
                #   'https://www.baldorfood.com/products/fruits/figs?viewall=1',
                  ]

    cookies = { 'PHPSESSID': '5rovoo6scjhvd2r5j4l4n3oqe4'}

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback = self.parse)

    def parse(self, response):
        for div in response.css('div.table-cover-back'):
                name = div.css('div.product-title-and-sku > div.pct-heading > h3 > a::text').get()
                item ={}
                price_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price::text').get()
                if not price_text:
                     continue
                price_int = float(price_text[1:6])
                unique_id = div.css('div.product-title-and-sku > span.product-sku-inline::text').get()
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
                item['ppu'] = round(price_int / quantity_int, 2)
                item['unique_id'] = unique_id
                yield item
