import json
import os
from Models.Product import Product
import Handlers.Helpers.FileHelper as FileHelper


class DefaultWarehouse:
	def __init__(self):
		self.relative_path = os.path.join("Data", "Stock")
		self.lastId = None
		self.data = []

	def AddProduct(self, product_name, product_price, product_stock):
		prod = Product()
		prod.id = self.lastId
		prod.name = product_name
		prod.price = product_price
		prod.numberInStock = product_stock
		prod.reserved = 0
		self.data.append(prod)
		self.lastId += 1

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
			FileHelper.add_or_overwrite_file(self.relative_path, product.name, json_string)

		return True
