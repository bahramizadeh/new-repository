import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT


from security import athenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://ojhrjinhjhumlt:8c71e921f620fa35641c64e882814c2ae88d5266e9d9cb8e07dd2f285dfee4ca@ec2-34-240-75-196.eu-west-1.compute.amazonaws.com:5432/dfgvgi5be0ji7s', 'sqlite:///data.db')
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
    
    
    