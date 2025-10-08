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
        
    def display_summary(self):
        total_amount = sum( item.quantity * item.price for item in self.items )

        # le f permet devant la chaine de caractères d'insérer dans les accolades des variables dynamiquement
        return f"Order {self.order_id} by {self.customer.name} on {self.date}: Total ${total_amount}"
       


orders = [ Order(**data) for data in raw_data ]


def total_sales(orders):
    total = 0
    for order in orders:
        for item in order.items:
            total += item.quantity * item.price # 

    return total 

# Trouvez la commande la plus élevée

def best_order(orders):
    best = None
    best_total = 0

    for order in orders:
        total = 0
        for item in order.items:
            total += item.quantity * item.price

        if best is None or total > best_total:
            best = order
            best_total = total

    return best

# Filtrez les commandes supérieures à 500 €
def filter_orders_above(orders, threshold):
    filtered = []
    for order in orders:
        total = 0
        for item in order.items:
            total += item.quantity * item.price

        if total > threshold:
            filtered.append(order)

    return filtered

# Affichez un résumé formaté de chaque commande.
def display_summaries(orders):
    for order in orders:
        print(order.display_summary())
    return None 