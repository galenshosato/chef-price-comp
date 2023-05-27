import scrapy



class WalSpider(scrapy.Spider):
    name = "WalSpider"
    
    start_urls = ['https://www.walmart.com/browse/food/fresh-produce/976759_976793',]


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)
    
    def parse(self, response):
        for div in response.css('div.sans-serif.mid-gray.relative.flex.flex-column.w-100.hide-child-opacity'):
            name = div.css('a.absolute.w-100.h-100.z-1.hide-sibling-opacity > span.w_iUH7::text').get()
            # price = div.css('div.w-pie--product-tile__content > div.w-pie--prices > ul > li > span.regular_price > b::text').get()
            # number = float(price.replace('$', '').replace('/lb', '').replace('¢', ''))
            # if number > 75:
            #     number = number / 100

            item = {}
            item['name'] = name
            # item['price'] = number

            yield item