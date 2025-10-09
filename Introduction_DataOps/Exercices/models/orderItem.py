class OrderItem:
    """
    Classe représentant un article dans une commande.

    Attributes:
        product (str): Nom du produit.
        quantity (int): Quantité commandée.
        price (float): Prix unitaire du produit.
    """
    def __init__(self, product:str, quantity:int, price:float):
        self.product = product
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        """Retourne une représentation lisible de l'objet OrderItem."""
        return f"OrderItem({self.product}, {self.quantity}, {self.price})"