from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity

from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

items = []

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items/')


if __name__ == "__main__":
    app.run(port=5001,host='0.0.0.0')
