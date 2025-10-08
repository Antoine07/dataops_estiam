## 1. Qu’est-ce que Python

Python est un langage de programmation simple à lire et à écrire.
Il est utilisé pour l’automatisation, le web, la data, l’intelligence artificielle, etc.

Exécution d’un fichier :

```bash
python fichier.py
```

---

## 2. Afficher du texte

```python
print("Bonjour le monde")
```

---

## 3. Variables

```python
nom = "Alice"
age = 20
print("Je m'appelle", nom, "et j'ai", age, "ans.")
```

---

## 4. Types principaux

| Type  | Exemple      | Description          |
| ----- | ------------ | -------------------- |
| int   | 3            | entier               |
| float | 3.14         | nombre décimal       |
| str   | "texte"      | chaîne de caractères |
| bool  | True / False | booléen              |

---

## 5. Opérations

```python
a = 5 + 2
b = 5 - 2
c = 5 * 2
d = 5 / 2
e = 5 // 2
f = 5 % 2
```

---

## 6. Conditions

```python
age = 18
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

---

## 7. Boucles

```python
for i in range(5):
    print(i)

n = 0
while n < 3:
    print(n)
    n += 1
```

---

## 8. Listes

```python
fruits = ["pomme", "banane", "cerise"]
print(fruits[0])
fruits.append("orange")

for fruit in fruits:
    print(fruit)
```

---

## 9. Fonctions

```python
def bonjour(nom):
    print("Salut", nom)

bonjour("Alice")
```