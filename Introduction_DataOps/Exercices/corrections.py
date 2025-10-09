from datetime import datetime

CONTENT="mississippi"

dico={
    char : CONTENT.count(char)
    for char in set(CONTENT)
}

print(dico)


# entier signé ou non inversé -6523 donnerait -3256

NUMBER = -6523

result = int(str(NUMBER)[::-1]) if NUMBER >= 0 else -int(str(-NUMBER)[::-1])

# Correction Object


cleaned_data = [
  {"order_id": 1001, "customer": "Alice", "amount": 89.90, "date": "2024-04-05"},
  {"order_id": 1002, "customer": "Bob", "amount": 45.00, "date": "2024-04-07"},
]

class Order:
    """
    Classe représentant une commande.Représente une commande client.

    Attributes:
        order_id (int): Identifiant unique de la commande.
        customer (str): Nom du client.
        amount (float): Montant total de la commande.
        date (datetime): Date de la commande.
    """
    def __init__(self, order_id :int, customer:str, amount:float, date:datetime):
        self.order_id = order_id
        self.customer = customer
        self.amount = amount
        self.date = date

    def __repr__(self):
        """Retourne une représentation lisible de l'objet Order."""
        return f"Order({self.order_id}, {self.customer}, {self.amount}, {self.date})"

orders:list[Order] = [
    Order(
        order_id=entry["order_id"],
        customer=entry["customer"],
        amount=entry["amount"],
        date=datetime.strptime(entry["date"], "%Y-%m-%d")
    )
    for entry in cleaned_data
]

print(orders)


def total_sales(orders_list:list[Order]) -> float:
    """
    Calcule le montant total des ventes à partir d'une liste de commandes.

    Args:
        orders (list[Order]): Liste des objets Order.

    Returns:
        float: Montant total des ventes.
    """
    return sum(order.amount for order in orders_list)

def average_order_value(order_list:list[Order]) -> float:
    """
    Calcule la valeur moyenne des commandes à partir d'une liste de commandes.

    Args:
        orders (list[Order]): Liste des objets Order.

    Returns:
        float: Valeur moyenne des commandes.
    """
    if not order_list:
        return 0.0
    return total_sales(order_list) / len(orders)


def best_order(order_list:list[Order]) -> Order | None:
    """
    Trouve la commande avec le montant le plus élevé dans une liste de commandes.

    Args:
        order_list (list[Order]): Liste des objets Order.

    Returns:
        Order: Objet Order avec le montant le plus élevé.
    """
    if not order_list:
        return None
    return max(order_list, key=lambda order: order.amount)


print(total_sales(orders))
print(average_order_value(orders))
print(best_order(orders))

# Correction Nested Data

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

from models.customer import Customer
from models.orderItem import OrderItem
from models.order import Order as OrderModel


orders_nested:list[OrderModel] = [
    OrderModel(
        order_id=entry["order_id"],
        customer=Customer(
            name=entry["customer"]["name"],
            email=entry["customer"]["email"]
        ),
        items=[
            OrderItem(
                product=item["product"],
                quantity=item["quantity"],
                price=item["price"]
            )
            for item in entry["items"]
        ],
        date=datetime.strptime(entry["date"], "%Y-%m-%d")
    )
    for entry in raw_data
]

print(orders_nested)

total = sum(order.total_amount() for order in orders_nested)

print(total)

# Commande la plus élevée
best = max(orders_nested, key=lambda order: order.total_amount())
print(best)

# Filtrez les commandes supérieures à 500 €
high_value_orders = [order for order in orders_nested if order.total_amount() > 500]
print(high_value_orders)

# Affichez un résumé formaté de chaque commande.
summaries = [order.display_summary() for order in orders_nested]
for summary in summaries:
    print(summary)

# Calculez la dépense totale par client.


