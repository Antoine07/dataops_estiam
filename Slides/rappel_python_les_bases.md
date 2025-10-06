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

Nous allons faire quelques exercices, mettez vous dans Jupyter ou un fichier *.py dans vscode ou votre éditeur.

---

### mississippi

Soit la chaîne de caractères suivante : "mississippi". Comptez le nombre d'occurence de chaque lettre(s).

---

### Entiers inversés

Nous souhaitons créer une fonction qui permet d'inverser des entiers signés ou non :

Par exemples :

-6523 donnerait -3256 

123 donnerait 321

Utilisez les notions du cours pour créer cette fonction. Notamment pensez à caster vos données afin de pouvoir les utiliser avec d'autre(s) fonction(s).

--- 

### Recherche d'un mot dans un texte

Un problème récurrent en analyse de données consiste à rechercher une séquence de valeur dans un tableau.

Ci-dessous on cherche la séquence  `123`

```python
l = [1,3,7,8,9,1,2,3,8, 1, 2, 3, 7, 8, 9, 1, 2, 3, 8, 10, 1, 2, 3]
```

1. Créez une fonction qui permette de rechercher un mot dans un texte ou une liste, notez que cette fonction sera identique pour un texte, un itérable... Il serait intéressant que cette fonction retourne le premier indice de la position de la séquence trouvée dans la liste. 

2. Retournez maintenant tous les indices de toutes les séquences trouvées dans la liste.
