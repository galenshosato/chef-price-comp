from flask import Flask, jsonify, request, make_response, Response, session as browser_session
from .extensions import *
from .models import Vendor, Product, Price
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = 'woo secret key'

db.init_app(app)
migrate.init_app(app, db)

@app.route('/api/vendors')
def get_vendors():
    vendors = Vendor.query.all()
    vendor_dict = [vendor.to_dict() for vendor in vendors]
    return make_response(jsonify(vendor_dict), 200)

@app.route('/api/<int:vendor_id>/products')
def get_products_for_vendor(vendor_id):
    vendor = Vendor.query.filter_by(vendor_id=id).first()
    products_to_dict = [product.to_dict() for product in vendor.products]
    return make_response(jsonify(products_to_dict), 200)




if __name__ == '__main__':
    app.run(port=5555, debug=True)