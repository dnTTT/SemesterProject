class StatusSignal(object):
    def __init__(self):
        self._OrderId = None
        self._Status = None

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


class StatusSignalMessage(object):
    def __init__(self):
        self._OrderId = None
        self._Status = None
        self._ProductsList = None

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
    def ProductsList(self):
        return self._ProductsList

    @ProductsList.setter
    def ProductsList(self, value):
        self._ProductsList = value
