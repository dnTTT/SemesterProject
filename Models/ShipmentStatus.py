from enum import Enum


class ShipmentStatus(Enum):
    Delivered = 0
    Cancelled = 1
    Shipped = 2
    Paid = 3
