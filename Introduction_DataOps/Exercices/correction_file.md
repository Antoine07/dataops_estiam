## Contexte

Vous êtes data engineer pour une librairie en ligne.
Vous recevez un fichier CSV **brut et partiellement sale**. Votre mission : **nettoyer** les données, **hydrater** un modèle objet (POO) et produire des exports/analyses exploitables.

## Objectifs

* Nettoyer `raw_orders.csv` (formats incohérents, doublons, champs manquants)
* Hydrater des objets `Customer`, `OrderItem`, `Order` à partir des données nettoyées
* Analyser le CA et produire des fichiers de sortie (`cleaned_orders.json`, `report.csv`, `errors.log`)

### Fichier d’entrée (extrait `raw_orders.csv`)

```
order_id,customer_name,customer_email,product,quantity,price,date
1,Alice,alice@mail.com,Book A,2,12,50,2024/06/10
2,Bob,bob@mail.com,Book B,1,15.0,10-06-2024
3,Charlie, ,book C,1,€20.00,2024.06.12
4,alice ,ALICE@MAIL.COM,Book A,2,12.50,2024/06/10
5,Denis,denis@mail,Book D,0,8.00,2024/06/15
6,Eve,eve@mail.com,Book E,1,"13,5",15/06/2024
2,Bob,bob@mail.com,Book B,1,15.0,10-06-2024
```

---

# Étape A — Nettoyage (obligatoire) & Étape B — Modélisation / Hydratation

## À faire — Nettoyage

1. Normaliser les en-têtes et retirer les espaces superflus.
2. Nettoyer les champs :

   * `price` → float (gérer virgule, symbole €/$, guillemets)
   * `quantity` → int (filtrer ou corriger les quantités <= 0)
   * `date` → `YYYY-MM-DD` (gérer `2024/06/10`, `10-06-2024`, `15/06/2024`, etc.)
   * `customer_email` : valider le format ; si absent, créer `unknown+<order_id>@example.com` et logguer.
3. Dédupliquer les commandes (par `order_id`) : garder la première occurrence valide et logguer les doublons.
4. Enregistrer toutes les erreurs / lignes rejetées dans `errors.log` (ligne, raison).

## À faire — Modélisation et Hydratation

Créez les classes suivantes (code en anglais) :

```python
from datetime import datetime
from typing import List, Dict

class Customer:
    def __init__(self, name: str, email: str):
        self.name = name.strip()
        self.email = email.strip().lower()

    def to_dict(self) -> Dict:
        return {"name": self.name, "email": self.email}

class OrderItem:
    def __init__(self, product: str, quantity: int, unit_price: float):
        self.product = product.strip()
        self.quantity = int(quantity)
        self.unit_price = float(unit_price)

    @property
    def total(self) -> float:
        return self.quantity * self.unit_price

    def to_dict(self) -> Dict:
        return {"product": self.product, "quantity": self.quantity, "unit_price": self.unit_price}

class Order:
    def __init__(self, order_id: int, customer: Customer, items: List[OrderItem], date: datetime):
        self.order_id = int(order_id)
        self.customer = customer
        self.items = items
        self.date = date

    @classmethod
    def from_dict(cls, d: Dict):
        cust = Customer(d["customer"]["name"], d["customer"]["email"])
        items = [OrderItem(i["product"], i["quantity"], i["unit_price"]) for i in d["items"]]
        date = datetime.strptime(d["date"], "%Y-%m-%d")
        return cls(d["order_id"], cust, items, date)

    def total_amount(self) -> float:
        return sum(i.total for i in self.items)

    def to_dict(self) -> Dict:
        return {
            "order_id": self.order_id,
            "customer": self.customer.to_dict(),
            "items": [i.to_dict() for i in self.items],
            "date": self.date.strftime("%Y-%m-%d"),
            "total": self.total_amount()
        }
```

---

# Étape C — Pipeline, Analyse & Livrables

## Pipeline attendu (exemples de tâches — code en anglais)

1. Lire `raw_orders.csv` (use `csv` or `pandas`).
2. Appliquer les fonctions de nettoyage (`clean_price`, `parse_date`, `normalize_email`, ...).
3. Détecter et logguer erreurs dans `errors.log`.
4. Hydrater `Order.from_dict()` pour chaque ligne valide.
5. Produire analyses et exports.

### Exemple de squelette `main.py` (en anglais)

```python
import csv
import json
from collections import Counter
from datetime import datetime
# assume cleaning helpers and classes are implemented as above

cleaned_orders = []
errors = []

with open("raw_orders.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # cleaning functions: clean_row returns normalized dict or raises ValueError
            norm = clean_row(row)
            order = build_order_dict(norm)   # build dict matching Order.from_dict expected shape
            order_obj = Order.from_dict(order)
            cleaned_orders.append(order_obj)
        except Exception as e:
            errors.append((row.get("order_id"), str(e)))

# analyses
total_revenue = sum(o.total_amount() for o in cleaned_orders)
by_customer = {}
for o in cleaned_orders:
    by_customer.setdefault(o.customer.email, 0)
    by_customer[o.customer.email] += o.total_amount()

top_products = Counter()
for o in cleaned_orders:
    for it in o.items:
        top_products[it.product] += it.quantity

# exports
with open("cleaned_orders.json", "w", encoding="utf-8") as f:
    json.dump([o.to_dict() for o in cleaned_orders], f, ensure_ascii=False, indent=2)

import csv
with open("report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["metric", "value"])
    writer.writerow(["total_revenue", f"{total_revenue:.2f}"])
    writer.writerow(["unique_customers", len(by_customer)])
    for prod, qty in top_products.most_common(10):
        writer.writerow([f"product_{prod}", qty])

with open("errors.log", "w", encoding="utf-8") as f:
    for oid, msg in errors:
        f.write(f"order_id={oid} error={msg}\n")
```

## Livrables à rendre

* `models.py` (classes `Customer`, `OrderItem`, `Order`)
* `cleaning.py` (fonctions de nettoyage)
* `main.py` (pipeline : lecture → nettoyage → hydration → analyse → export)
* `cleaned_orders.json`, `report.csv`, `errors.log` (issus de l’exécution)

## Critères d’évaluation

* Robustesse du nettoyage (formats multiples acceptés, logs clairs)
* Correction de l’hydratation (`from_dict`/`to_dict`)
* Qualité des analyses (CA total, top products, clients)
* Code lisible, tests ou exemples d’exécution fournis

---
