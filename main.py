# noinspection PyArgumentList

from Handlers.WarehouseHandler import WarehouseHandler


class Program(object):
    @staticmethod
    def Main():
        newClass = WarehouseHandler()
        newClass.DataInitialization()


if __name__ == '__main__':
    Program.Main()
