# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from back_end.server.extensions import db
from back_end.server.app import app
from back_end.server.models import Product, Price

class ChefCompPipeline:
    def open_spider(self, spider):
        self.app_context = app.app_context()
        self.app_context.push()
    
    def close_spider(self, spider):
        self.app_context.pop()

    def process_item(self, item, spider):

        new_product = Product()
        new_product.name = item['name']
        new_product.vendor_id = 1
        new_product.unique_id = item['unique_id']

        new_price = Price()
        new_price.price = item['price']
        new_price.price_per_unit = item['ppu']
        new_price.product_id = item['unique_id']

        db.session.add(new_product)
        db.session.add(new_price)
        db.session.commit()

        return item
