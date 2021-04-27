import os
import re

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import athenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
uri = app.config['SQLALCHEMY_DATABASE_URI']
if uri.startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, athenticate, identity)  
    
api.add_resource(Store, '/store/<string:name>')    
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
    
    
    