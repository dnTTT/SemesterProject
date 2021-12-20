# noinspection PyArgumentList
import json

from Handlers.WarehouseHandler import WarehouseHandler
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import Handlers.OrdersHandler as OrderHandler
import pandas as pd
from Models.Order import Order


def Main():
    new_class = WarehouseHandler()
    new_class.data_initialization()

class StatusSignal(Resource):
    def post(self):
        content = request.get_json(silent=True)
        try:
            response = OrderHandler.handle_status_signal(content)
            return {'data': content}, 200  # return data with 200 OK
        except Exception:
            return {'data': 'Error message 500'}, 500  # return data with 200 OK

class Order(Resource):
    def post(self):
        content = request.get_json(silent=True)
        try:
            response = OrderHandler.handle_order(content)
            return {'data': content}, 200  # return data with 200 OK
        except Exception:
            return {'data': 'Error message 500'}, 500  # return data with 200 OK


if __name__ == '__main__':
    #Main()
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Order, '/order')
    api.add_resource(StatusSignal, '/statussignal')
    app.run()
