# SRP - Single Responsibility Principle
# This principle tries to say that at any point of time. The Class or method is supposed to have only one
# responsibility to be handled.

class Items:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

class OrderManager:
    def place_order(self, order):
        total = order.calculate_total()
        print(f'The Total is {total}')

items = [
    Items("item1", 10),
    Items("item2", 20),
    Items("item3", 30)
]

order = Order(123,items)
order_manager = OrderManager()
order_manager.place_order(order)