from back_end.server.extensions import db
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
    vendor_id = db.column(db.Integer, db.ForeignKey('vendors.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "vendor_id": self.vendor_id,
            "vendor": self.vendor.name,
        }

class Price(db.Model):
    __tablename__ = 'prices'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String)
    price_per_unit = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "price": self.price,
            "price_per_unit": self.price_per_unit,
            "updated_at": self.updated_at
        }