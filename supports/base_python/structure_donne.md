# Structure de données

##  Dictionnaires

Un dictionnaire stocke des données sous forme **clé → valeur**.

```python
personne = {
    "nom": "Alice",
    "age": 25,
    "ville": "Paris"
}

print(personne["nom"])       # accès à une valeur
personne["age"] = 26         # modification
personne["metier"] = "Dev"   # ajout d’une clé

for cle, valeur in personne.items():
    print(cle, ":", valeur)
```

---

##  Fonctions avec retour de valeur

Une fonction peut **renvoyer un résultat**.

```python
def carre(x):
    return x * x

resultat = carre(4)
print(resultat)  # 16
```

---

##  Arguments par défaut

```python
def saluer(nom="inconnu"):
    print("Bonjour", nom)

saluer()
saluer("Bob")
```

---

## Importer un module

Les **modules** sont des fichiers Python contenant du code réutilisable.

```python
import math

print(math.sqrt(16))  # racine carrée
print(math.pi)        # nombre pi
```

On peut aussi importer une partie :

```python
from math import sqrt
print(sqrt(9))
```

---

## Lecture et écriture de fichiers

```python
# Écriture
with open("test.txt", "w") as f:
    f.write("Bonjour\nPython")

# Lecture
with open("test.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

---

##  Classes (introduction)

Une **classe** regroupe des données et des fonctions liées.

```python
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def saluer(self):
        print("Bonjour, je m'appelle", self.nom)

p = Personne("Alice", 25)
p.saluer()
```
