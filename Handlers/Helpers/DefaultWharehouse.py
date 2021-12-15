import json
from pathlib import Path
import os
from Models.Product import Product
from os import path


class DefaultWarehouse:
    def __init__(self):
        self.relativePath = os.path.join("Data", "Stock")
        self.lastId = None
        self.data = []
        self.Initialize(self)

    def AddProduct(self, NName, NPrice, NNumberInStock):
        self.data.append(Product(NName, NPrice, NNumberInStock))
        self.lastId += 1

    def CheckRelativePath(self):
        current = os.getcwd()
        folders = self.relativePath.Split("/").ToList()
        try:
            for folder in folders:
                current += "/{}".format(folder)
                if not path.exists(current):
                    os.mkdir(current)
            if path.exists((current + "/{}".format(self.relativePath))):
                return True
            else:
                return False
        except Exception as e:
            raise Exception("Exception occurred when creating files directory", e)

    def AddOrOverwriteFile(self, fileName, jsonInput):
        current_path = os.getcwd()
        if not fileName.EndsWith(".json"):
            fileName += ".json"
        try:
            if self.CheckRelativePath():
                full_path = os.path.join(current_path, self.relativePath)
                with open(full_path, 'w') as outfile:
                    json.dump(jsonInput, outfile)
                if os.path.isfile(full_path):
                    return True
                else:
                    return False
            else:
                raise Exception("Unable to access proper directory. Relative path: {}".format(relativePath))
        except Exception as e:
            raise Exception("Unable to save data to a file", e)

    def Initialize(self):
        self.lastId = 1000
        self.AddProduct("Product#1", 25.99, 100)
        self.AddProduct("Product#2", 55.19, 60)
        self.AddProduct("Product#3", 99.99, 40)
        self.AddProduct("Product#4", 19.5, 300)
        self.AddProduct("Product#5", 40.99, 70)
        self.AddProduct("Product#6", 60, 100)
        self.AddProduct("Product#7", 75.15, 45)
        self.AddProduct("Product#8", 35.19, 110)
        self.AddProduct("Product#9", 115.99, 30)
        self.AddProduct("Product#10", 29.99, 120)
        self.AddProduct("Luxury#1", 599.5, 10)
        self.AddProduct("Luxury#2", 399.5, 20)
        self.AddProduct("Luxury#3", 5599.5, 5)
        self.AddProduct("Luxury#4", 3599.5, 5)

        for product in self.data:
            json_string = json.dumps(product.__dict__)
            self.AddOrOverwriteFile(product.name, json_string)

        return True
