from models.customer import Customer
from models.orderItem import OrderItem

from datetime import datetime

class Order:
    """
    Classe représentant une commande.

    Attributes:
        order_id (int): Identifiant unique de la commande.
        customer (Customer): Objet Customer représentant le client.
        items (list[OrderItem]): Liste des objets OrderItem dans la commande.
        date (datetime): Date de la commande.
    """
    def __init__(self, order_id:int, customer:Customer, items:list[OrderItem], date:datetime):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.date = date
    def total_amount(self) -> float:
        """Calcule le montant total de la commande."""
        return sum(item.quantity * item.price for item in self.items)

    def display_summary(self) -> str:
        """Retourne un résumé de la commande."""
        item_summaries = ', '.join(f"{item.product} (x{item.quantity})" for item in self.items)
        return f"Order ID: {self.order_id}, Customer: {self.customer.name}, Items: [{item_summaries}], Date: {self.date.strftime('%Y-%m-%d')}, Total Amount: {self.total_amount():.2f}"
    def __repr__(self):
        """Retourne une représentation lisible de l'objet Order."""
        return f"Order({self.order_id}, {self.customer}, {self.items}, {self.date})"