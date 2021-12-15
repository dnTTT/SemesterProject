class Product(object):
    def __init__(self):
        self._Id = None
        self._Name = None
        self._Price = None
        self._NumberInStock = None
        self._Reserved = None

    @property
    def id(self):
        return self._Id

    @id.setter
    def id(self, value):
        self._Id = value

    @property
    def name(self):
        return self._Name

    @name.setter
    def name(self, value):
        self._Name = value

    @property
    def price(self):
        return self._Price

    @price.setter
    def price(self, value):
        self._Price = value

    @property
    def numberInStock(self):
        return self._NumberInStock

    @numberInStock.setter
    def numberInStock(self, value):
        self._NumberInStock = value

    @property
    def reserved(self):
        return self._Reserved

    @reserved.setter
    def reserved(self, value):
        self._Reserved = value
