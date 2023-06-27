from app import app
from server import Vendor, Product, db

if __name__ == '__main__':
    with app.app_context():
        Product.query.filter(Product.vendor_id == 2).delete()
        db.session.commit()
        