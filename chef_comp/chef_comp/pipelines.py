# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime
from scrapy.exceptions import DropItem
import os
import sys

project_root = os.path.abspath(os.path.join(
                  os.path.dirname(__file__),
                  os.pardir)
)
sys.path.append(project_root)

from app import app
from server import db, Product, Price

class ProductPipeline:

    def process_item(self, item, spider):
        with app.app_context():
            unique_id = item['unique_id']
            price = item['price']
            ppu = item['ppu']
            check_item = Product.query.filter_by(unique_id=unique_id).first()
            check_price = Price.query.filter(Price.product_id==unique_id).first()

            if check_price:
                if check_price.price == price and check_price.price_per_unit == ppu:
                    raise DropItem(f"Price did not change for {unique_id}")
                else:
                    check_price.price = price
                    check_price.price_per_unit = ppu
                    check_price.updated_at = datetime.utcnow()
                    print('Price was updated')

                    db.session.commit()
            
                    return item


            if check_item:
                raise DropItem("Item already exists in db")

            new_product = Product()
            new_product.name = item['name']
            new_product.vendor_id = item['vendor_id']
            new_product.unique_id = item['unique_id']

            new_price = Price()
            new_price.price = item['price']
            new_price.price_per_unit = item['ppu']
            new_price.product_id = item['unique_id']

            db.session.add(new_product)
            db.session.add(new_price)
            db.session.commit()

            return item

