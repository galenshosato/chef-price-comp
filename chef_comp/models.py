from extensions import db
from sqlalchemy import JSON


class BaldorFood(db.Model):
    __tablename__ = 'baldorfoods'

    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String)
    price = db.Column(db.String)
    price_per_unit = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "product": self.product,
            "price": self.price,
            "price_per_unit": self.price_per_unit
        }