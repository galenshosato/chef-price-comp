# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .app import app
from .extensions import db
from .models import Product, Price

class BaldorPipeline:

    def process_item(self, item, spider):
        with app.app_context():
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
