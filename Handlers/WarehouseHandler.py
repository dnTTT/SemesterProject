import os
from pathlib import Path

from Handlers.Helpers import FileHelper
from Handlers.Helpers.DefaultWharehouse import DefaultWarehouse


class WarehouseHandler:
    def __init__(self):
        self.relativePath = os.path.join("Data", "Stock")
        self.lastId = None
        self.data = []

    def CheckIfDataExists(self):
        if self.relativePath.strip() == "":
            return False

        try:
            current = os.getcwd()
            return any(Path(os.path.join(current, self.relativePath)).iterdir())
        except Exception:
            return False

    def DataInitialization(self):
        if self.CheckIfDataExists():
            print("Data already initialized")
            return
        try:
            newClass = DefaultWarehouse
            newClass.Initialize()
            #DefaultWarehouse.__init__(self)
            print("Data has been initialized")
            return
        except Exception as e:
            print(e)
            print("Data could not be initialized")
            return


