from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required

items = []


class Item(Resource):
    @jwt_required()
    def get(self, name):
        # for item in items:
        # if item['name'] == name:
        # return item
        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': item}, 200 if item else 404  # Not found

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return{'message': "Already item there"}

        data = request.get_json()  # (force,silent = true)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201  # 201 create, 202 Accepted

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}
