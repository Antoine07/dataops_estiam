---
marp: true
theme: default
paginate: true
---

# Classes en Python  
## Cours  (sans POO avancée)

---

## Définition d’une classe

- Une **classe** est un modèle pour créer des objets
- `__init__` : constructeur qui initialise l’objet
- `self` : référence à l’instance actuelle

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

* **Attribut d’instance** : unique à l’objet
* **Attribut de classe** : partagé par toutes les instances

---

## Exercices 

1. Crée une classe `Rectangle` avec `width` et `height`.
2. Ajoute une méthode `area()` qui renvoie l’aire.
3. Crée 2 rectangles et affiche leurs aires.
4. Ajoute un attribut de classe `shape_type = "Rectangle"` et affiche-le pour chaque instance.
