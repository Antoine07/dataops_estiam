from datetime import datetime

cleaned_data = [
  {"order_id": 1001, "customer": "Alice", "amount": 89.90, "date": "2024-04-05"},
  {"order_id": 1002, "customer": "Bob", "amount": 45.00, "date": "2024-04-07"},
]

class Order:
    def __init__(self, order_id, customer, amount, date):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount
        self.date = datetime.strptime(date, "%Y-%m-%d")


def total_sales(orders):
    return sum(order.amount for order in orders)

def best_order(orders):
    return max(orders, key=lambda order: order.amount)
