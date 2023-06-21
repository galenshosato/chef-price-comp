from server.extensions import db
from sqlalchemy import JSON
from datetime import datetime


class Vendor(db.Model):
    __tablename__ = 'vendors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    products = db.relationship('Product', backref='vendor')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "products": [product.to_dict() for product in self.products]
        }
    
class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    unique_id = db.Column(db.String)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendors.id'))
    prices = db.relationship('Price', backref='product')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "unique_id": self.unique_id,
            "prices": [price.to_dict() for price in self.prices],
            "vendor_id": self.vendor_id,
            "vendor": self.vendor.name,
        }

class Price(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String)
    price_per_unit = db.Column(db.Integer)
    product_id = db.Column(db.String, db.ForeignKey('products.unique_id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    def to_dict(self):
        return {
            "price": self.price,
            "price_per_unit": self.price_per_unit,
            "product_id": self.product_id,
            "updated_at": self.updated_at
        }