import json
import os
from pathlib import Path

import Handlers.Helpers.FileHelper as FileHelper
from Handlers.Helpers.DefaultWharehouse import DefaultWarehouse


class WarehouseHandler:
    def __init__(self):
        self.relative_path = os.path.join("Data", "Stock")
        self.lastId = None
        self.data = []

    def data_initialization(self):
        if FileHelper.check_if_data_exists(self.relative_path):
            print("Data already initialized")
            return
        try:
            new_class = DefaultWarehouse()
            new_class.Initialize()
            print("Data has been initialized")
            return
        except Exception as e:
            print(e)
            print("Data could not be initialized")
            return

    def get_product(self, product_name):
        try:
            return FileHelper.get_object_from_file(self.relative_path, product_name)
        except Exception:
            return None

    def reserve_product(self, product, number_to_reserve):
        prod = self.get_product(product)
        prod["_Reserved"] += number_to_reserve
        FileHelper.add_or_overwrite_file(self.relative_path, product, json.dumps(prod))

    def cancel_order(self, products):
        for prod_name in products:
            prod_temp = self.get_product(prod_name)
            prod_temp["_Reserved"] = prod_temp["_Reserved"] - products[prod_name]
            FileHelper.add_or_overwrite_file(self.relative_path, prod_name, json.dumps(prod_temp))

    def complete_order(self, products):
        for prod_name in products:
            prod_temp = self.get_product(prod_name)
            prod_temp["_NumberInStock"] = prod_temp["_NumberInStock"] - products[prod_name]
            # if prod_temp["_Reserved"] > 0: Maybe because reserved is getting negative numbers
            prod_temp["_Reserved"] = prod_temp["_Reserved"] - products[prod_name]
            FileHelper.add_or_overwrite_file(self.relative_path, prod_name, json.dumps(prod_temp))

    def get_number_in_stock(self, product):
        product_info = self.get_product(product)
        if product_info is None:
            return 0

        value = product_info["_NumberInStock"] - product_info["_Reserved"]
        return value

    def get_item_price(self, product):
        return self.get_product(product)["_Price"]

