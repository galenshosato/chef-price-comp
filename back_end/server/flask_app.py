from flask import Flask, jsonify, request, make_response, Response, session as browser_session
from back_end.server.extensions import *


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
app.secret_key = 'woo secret key'

db.init_app(app)
migrate.init_app(app, db)