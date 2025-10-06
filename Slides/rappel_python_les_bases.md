---
marp: true
theme: default
paginate: true
---

# Chapitre 1 : Python  

## Variables, structures de données et expressions de liste

---

## Portée des variables (LEG)

- **L (Local)** : définie dans une fonction, accessible uniquement dedans  
- **E (Enclosing)** : dans une fonction parente, modifiable avec `nonlocal`  
- **G (Global)** : définie à l’extérieur, accessible partout dans le module  
- **B (Builtin)** : noms intégrés Python (`print`, `len`, etc.)

```python
x = 10  # Global

def outer():
    y = 5  # Enclosing pour inner
    def inner():
        z = 3      # Local
        nonlocal y  # modifie y
        y += z
        print("inner:", x, y, z)
    inner()
    print("outer:", x, y)

outer()
# print(z)  # Erreur : z est local à inner
```


---

## Structures de données : Listes

* Ordonnées, modifiables, indexables

```python
lst = [1, 2, 3, 4]
lst.append(5)
lst[0] = 10
print(lst[1:4])
```

---

## Structures de données : Tuples

* Ordonnés, **immuables**

```python
t = (1, 2, 3)
# t[0] = 10  # Erreur
```

---

## Structures de données : Dictionnaires

* Clé → valeur

```python
d = {"a": 1, "b": 2}
d["c"] = 3
print(d.get("b"))  # 2
```

---

## Structures de données : Sets

* Ensemble non ordonné, unique

```python
s = {1, 2, 3}
s.add(2)   # pas d'effet
s.remove(1)
print(s)
```

---

## Expressions de liste

* Créer une liste **en une ligne**
* Boucle et condition possibles

```python
# Carrés
squares = [x**2 for x in range(10)]

# Nombres pairs
evens = [x for x in range(10) if x % 2 == 0]

# Majuscules
names = ["alice", "bob"]
upper_names = [name.upper() for name in names]
```

---

## Exercices 

1. Variable globale `count = 0`. Fonction qui ajoute 1 et affiche.
2. Liste `nums = [1,2,3,4,5]` : ajoute 6, supprime 2, affiche 3 premiers éléments
3. Tuple `t = (1, 2, 3)` : essaie de changer `t[0]`
4. Dictionnaire `d` avec 3 clés/valeurs : affiche valeur clé `"b"`
5. Set `s` avec 1,2,2,3,3,3 : affiche-le
6. List comprehension : carrés des nombres pairs 0-10
7. Liste `words = ["python","code"]` → mots en majuscules

