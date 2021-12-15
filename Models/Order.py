class Order(object):
    def __init__(self):
        self._CustomerID = None
        self._OrderId = None
        self._ProductsList = None
        self._OrderDate = None
        self._Status = None

    @property
    def CustomerID(self):
        return self._CustomerID

    @CustomerID.setter
    def CustomerID(self, value):
        self._CustomerID = value

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, value):
        self._OrderId = value

    @property
    def ProductsList(self):
        return self._ProductsList

    @ProductsList.setter
    def ProductsList(self, value):
        self._ProductsList = value

    @property
    def OrderDate(self):
        return self._OrderDate

    @OrderDate.setter
    def OrderDate(self, value):
        self._OrderDate = value

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, value):
        self._Status = value


class NewOrder(object):
    def __init__(self):
        self._CustomerID = None
        self._ProductsList = None

    @property
    def CustomerID(self):
        return self._CustomerID

    @CustomerID.setter
    def CustomerID(self, value):
        self._CustomerID = value

    @property
    def ProductsList(self):
        return self._ProductsList

    @ProductsList.setter
    def ProductsList(self, value):
        self._ProductsList = value


class OrderResponse(object):
    def __init__(self):
        self._OrderId = None
        self._Status = None
        self._Price = None
        self._Message = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, value):
        self._OrderId = value

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, value):
        self._Status = value

    @property
    def Price(self):
        return self._Price

    @Price.setter
    def Price(self, value):
        self._Price = value

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, value):
        self._Message = value

    def ToString(self):
        return Message
