---
marp: true
theme: default
paginate: true
---

# Classes en Python  
## Cours  (sans POO avancée)

---

## Définition d'une classe

- Une **classe** est un modèle pour créer des objets
- `__init__` : constructeur qui initialise l'objet
- `self` : référence à l'instance actuelle

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # attribut
        self.age = age

    def greet(self):
        return f"Hello, {self.name}!"
````

---

## Créer un objet

```python
p = Person("Alice", 25)
print(p.name)      # Alice
print(p.age)       # 25
print(p.greet())   # Hello, Alice!
```

* Instanciation : `Person(...)`
* Attributs : `objet.attribut`
* Méthodes : `objet.methode()`

---

## Attributs de classe

```python
class Person:
    species = "Homo sapiens"  # commun à toutes les instances

p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.species)  # Homo sapiens
print(p2.species)  # Homo sapiens
```

* **Attribut d'instance** : unique à l'objet
* **Attribut de classe** : partagé par toutes les instances

---

## Exercices 

## Objectif
Transformer des données nettoyées en **objets Python** exploitables.  
L'hydratation = remplir un modèle de données métier.

---

# Étape 1 — Créer un modèle `Order`

```python

class Order:
    pass
````

Jeu de données nettoyé :

```python

cleaned_data = [
  {"order_id": 1001, "customer": "Alice", "amount": 89.90, "date": "2024-04-05"},
  {"order_id": 1002, "customer": "Bob", "amount": 45.00, "date": "2024-04-07"},
]
```

---

# Étape 2 — Hydrater et exploiter

Hydrater les objets :


Calculer et analyser :

total_sales et best_order

--- 

# Analyse d'un jeu de données

```python

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

```

--- 

## Etape 1 - Hydrater exploiter 

Modélisation métier 

1. Créez trois classes :
   - `Customer` name, email 
   - `OrderItem`  product, quantity, unit_price, method `total()`
   - `Order` id, customer, list of items, date, method `total_amount()`

2. Ajoutez dans `Order` une méthode `display_summary()` qui affiche :
   - Le nom du client
   - Le nombre d'articles
   - Le montant total

--- 

## Etape 2 - Analyse

Analysez :

1. Calculez le chiffre d’affaires total

1. Trouvez la commande la plus élevée

1. Filtrez les commandes supérieures à 500 €

1. Affichez un résumé formaté de chaque commande.