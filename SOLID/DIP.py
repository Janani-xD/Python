# Dependency Inversion principle
# It allows us to change logic without having to replace the entire application
# NOTE : A high level module should not depend on a low level module
# Once the payment is initiate how the payment is processed should not impact the calling function


class PaymentGateway: # we may add any business logic here
    def process_payment(self, amount):
        print("Making payment on Stripe")
        pass

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_id, items, payment_gateway):
        self.order_id  = order_id
        self.items = items
        self.payment_gateway = payment_gateway

    def calculate_total(self):
        return sum(item.price for item in self.items)

    def place_order(self):
        total = self.calculate_total()
        # perform order placement logic
        self.payment_gateway.process_payment(total)

# high level module
class OrderManager:
    def __init__(self, order):
        self.order = order

    def place_order(self):
        self.order.place_order()

payment_gateway = PaymentGateway()
order_items = [
    Item("Product 1", 10),
    Item("Product 2", 20),
    Item("Product 3", 30)
]
order = Order(123, order_items, payment_gateway)
order_manager = OrderManager(order)