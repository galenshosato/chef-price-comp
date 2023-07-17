from flask import Flask, jsonify, request, make_response, Response, session as browser_session
from server import db, Vendor, Price, Product
from flask_migrate import Migrate
from urllib.parse import unquote



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = 'woo secret key'

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def welcome():
    return 'Welcome to the NHG API'

@app.route('/api/vendors')
def get_vendors():
    vendors = Vendor.query.all()
    vendor_dict = [vendor.to_dict() for vendor in vendors]
    return make_response(jsonify(vendor_dict), 200)

@app.route('/api/<int:vendor_id>/products')
def get_products_for_vendor(vendor_id):
    vendor = Vendor.query.filter_by(id=vendor_id).first()
    products_to_dict = [product.to_dict() for product in vendor.products]
    return make_response(jsonify(products_to_dict), 200)

@app.route('/api/<int:vendor_id>/products/<path:name>')
def get_spec_products(vendor_id, name):
    decoded_name = unquote(name)
    products = Product.query.filter(Product.vendor_id == vendor_id, Product.name.contains(decoded_name)).all()
    if not products:
        return make_response(jsonify({'Error':'No products match that query'}), 404)
    products_to_dict = [product.to_dict() for product in products]
    return make_response(jsonify(products_to_dict), 200)

@app.route('/api/<int:vendor_id>/exactproduct/<str:name>')
def get_exact_product(vendor_id, name):
    title_case_name = name.title()
    products = Product.query.filter(Product,vendor_id == vendor_id, Product.name == title_case_name).all()
    if not products:
        return make_response(jsonify({'Error':'No products match that query'}), 404)
    products_to_dict = [product.to_dict() for product in products]
    return make_response(jsonify(products_to_dict), 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True) 