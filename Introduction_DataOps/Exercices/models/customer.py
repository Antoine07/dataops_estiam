class Customer:
    """
    Classe représentant un client.

    Attributes:
        name (str): Nom du client.
        email (str): Adresse e-mail du client.
    """
    def __init__(self, name:str, email:str):
        self._name = name
        self._email = email
    @property
    def name(self) -> str:
        """Retourne le nom du client."""
        return self._name
    @property
    def email(self) -> str:
        """Retourne l'adresse e-mail du client."""
        return self._email
    @name.setter
    def name(self, name:str):
        """Modifie le nom du client."""
        self._name = name
    @email.setter
    def email(self, email:str):
        """Modifie l'adresse e-mail du client."""
        self._email = email
    def __repr__(self):
        """Retourne une représentation lisible de l'objet Customer."""
        return f"Customer({self.name}, {self.email})"
