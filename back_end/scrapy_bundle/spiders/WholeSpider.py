import scrapy



class WholeSpider(scrapy.Spider):
    name = "WholeSpider"
    
    start_urls = ['https://www.wholefoodsmarket.com/products/produce']

    cookies = {
        "csm-sid": "",
        "session-id-time": "",
        "_ga": "",
        "ubid-main": "",
        "wfm_store_d8": "",
        "wfm_store_weak": "",
        "session-token": "",
        "_gid": "",

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