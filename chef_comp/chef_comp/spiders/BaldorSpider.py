import scrapy
import re
from chef_comp.items import BaldorItem

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    context = browser.new_context()

    page = browser.new_page()

    page.goto('https://www.baldorfood.com/users/default/new-login')
    page.fill('input#EmailLoginForm_email', '')
    page.fill('input#EmailLoginForm_password', '')
    submit_button = page.get_by_role('button', name='SIGN IN')
    submit_button.click()

    page.wait_for_load_state()
    
    cookies = page.context.cookies()
    context.add_cookies(cookies)

    page.goto('https://www.baldorfood.com/products/fruits/avocados')

    # page.wait_for_timeout(10000)

    context.close()
    browser.close()
    

    for cookie in cookies:
        if cookie['name'] == 'PHPSESSID':
            cookie_value = cookie['value']
        else:
            continue

class BaldorSpider(scrapy.Spider):
    name = 'baldor'
    start_urls = ['https://www.baldorfood.com/products/fruits/apples?viewall=1',
                  'https://www.baldorfood.com/products/fruits/avocados?viewall=1',
                  'https://www.baldorfood.com/products/fruits/bananas?viewall=1',
                  'https://www.baldorfood.com/products/fruits/berries?viewall=1',
                  'https://www.baldorfood.com/products/fruits/citrus?viewall=1',
                  'https://www.baldorfood.com/products/fruits/figs?viewall=1',
                  ]

    cookies = { 'PHPSESSID': cookie_value }

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, cookies=self.cookies, callback = self.parse)

    def parse(self, response):
        item = BaldorItem()
        for div in response.css('div.table-cover-back'):
                name = div.css('div.product-title-and-sku > div.pct-heading > h3 > a::text').get()
                price_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price::text').get()
                if not price_text:
                     continue
                price_int = float(price_text[1:6])
                unique_id = div.css('div.product-title-and-sku > span.product-sku-inline::text').get()
                quantity_text = div.css('div.product-title-and-sku > span.pct-price-unit > span.price > span.price-unit::text').get()
                numbers = []
                if quantity_text == '1/2 CRATE':
                    numbers = ['.5']
                elif quantity_text == 'DOZ':
                    numbers = ['12']
                else:
                   numbers = re.findall(r'\d+', quantity_text)
                quantity_int=''
                for number in numbers:
                    number = float(number)
                    if 1 <= number < 3:
                        quantity_int = number 
                    elif number >= 3:
                        quantity_int = number
                    elif 0 < number < 1:
                        quantity_int = number
                    else:
                        print('Still works')
                item['name'] = name
                item['price'] = price_text + quantity_text
                item['ppu'] = round(price_int / quantity_int, 2)
                item['unique_id'] = unique_id
                item['vendor_id'] = 1
                yield item

