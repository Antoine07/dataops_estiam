

raw_data = [
  {
    "order_id": 1,
    "customer": {"name": "Alice", "email": "alice@mail.com"},
    "items": [
        {"product": "Laptop", "quantity": 1, "price": 1200},
        {"product": "Mouse", "quantity": 2, "price": 25},
    ],
    "date": "2024-06-10"
  },
  {
    "order_id": 2,
    "customer": {"name": "Bob", "email": "bob@mail.com"},
    "items": [
        {"product": "Monitor", "quantity": 1, "price": 300},
    ],
    "date": "2024-06-12"
  }
]

class OrderItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email 
        
class Order:
    def __init__(self, order_id, customer, items, date):
        self.order_id = order_id
        self.customer = Customer(
            name=customer['name'], 
            email=customer['email']
        )
        self.items = [OrderItem(
            product=item['product'],
            quantity=item['quantity'],
            price=item['price']
            ) for item in items]
        self.date = date
        
    def display_summary(self) -> str:
        total_amount = sum(item.quantity * item.price for item in self.items)
        
        return f"Order {self.order_id} by {self.customer.name} on {self.date}: Total ${total_amount:.2f}"
       

orders : list[Order] = [Order(
    order_id=data['order_id'],
    customer=data['customer'],
    items=data['items'],
    date=data['date']
) for data in raw_data]       
       
"""
Calculez le chiffre d’affaires total

Trouvez la commande la plus élevée

Filtrez les commandes supérieures à 500 €

Affichez un résumé formaté de chaque commande.
"""

def total_sales(orders):
    return sum(
        item.quantity * item.price 
        for order in orders 
        for item in order.items
    )
    
def best_order(orders : list[Order]):
    return max(
        orders, 
        key=lambda order: sum(item.quantity * item.price for item in order.items)
    )
    
best_order(orders)