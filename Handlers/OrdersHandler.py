import json

from Models.Order import Order
from Models.Order import OrderResponse
from Models.ShipmentStatus import ShipmentStatus
from Models.StatusSignal import StatusSignalMessage
from Models.StatusSignal import StatusSignal
from Handlers.WarehouseHandler import WarehouseHandler


def handle_order(new_order):
    response = OrderResponse()
    print("Processing Order with ID: {}".format(new_order["OrderId"]))

    try:
        if not check_if_in_stock(new_order):
            response.Message = "Not enough items in stock"
            response.OrderId = new_order['OrderId']
            response.Price = 0
            response.Status = ShipmentStatus.Cancelled
            return response
        else:
            price = calculate_price(new_order)
            reserve_products(new_order)
            response.Message = "Shipped order with an Id: {}".format(new_order["OrderId"])
            response.OrderId = new_order['OrderId']
            response.Price = price
            response.Status = ShipmentStatus.Shipped
            return response
    except Exception as e:
        response.Message = "Encountered error: {}".format(e)
        return response


def handle_status_signal(status):
    print("Processing status change for order with ID {}".format(status["OrderId"]))
    new_class = WarehouseHandler()
    status_cancelled = ShipmentStatus.Cancelled
    status_paid = ShipmentStatus.Paid
    if status["Status"] == status_cancelled.value:
        new_class.cancel_order(status["ProductsList"])
    elif status["Status"] == status_paid.value:
        new_class.complete_order(status["ProductsList"])

    status_signal = StatusSignal()
    status_signal.OrderId = status["OrderId"]
    status_signal.Status = status["Status"]
    return status_signal


def check_if_in_stock(new_order):
    new_class = WarehouseHandler()
    for prod_name in new_order['ProductsList']:
        in_stock = new_class.get_number_in_stock(prod_name)
        value = in_stock - new_order['ProductsList'][prod_name]
        if value <= 0:
            return False
    return True


def calculate_price(order):
    result = 0.0
    new_class = WarehouseHandler()
    for prod_name in order["ProductsList"]:
        price = new_class.get_item_price(prod_name)
        result += price * order["ProductsList"][prod_name]

    return result


def reserve_products(order):
    reservations = []
    new_class = WarehouseHandler()
    for prod_name in order["ProductsList"]:
        reservations.append(prod_name)
        new_class.reserve_product(prod_name, order["ProductsList"][prod_name])
