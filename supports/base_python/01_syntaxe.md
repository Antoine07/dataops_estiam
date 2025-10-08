## 1. Principe général

L’**indentation** sert à définir les **blocs de code** (aucune accolade `{}` comme en C ou Java).
Python utilise des **espaces** ou des **tabulations**, mais **jamais un mélange des deux**.

Convention : **4 espaces** par niveau d’indentation.

---

## 2. Exemple

```python
if x > 0:
    print("Positif")
    print("Toujours dans le bloc if")
print("En dehors du if")
```

Ici :

* les deux premières lignes indentées appartiennent au `if`
* la dernière ligne n’est plus indentée → en dehors du bloc

---

## 3. Autres cas courants

### Boucle `for`

```python
for i in range(3):
    print(i)
print("Fin")
```

### Boucle `while`

```python
while n < 5:
    n += 1
    print(n)
```

### Fonction

```python
def bonjour(nom):
    print("Salut", nom)
```

### Condition imbriquée

```python
if a > 0:
    if b > 0:
        print("a et b positifs")
    else:
        print("a positif, b non")
```

---

## 4. Règle à retenir

* Chaque bloc (après `if`, `for`, `while`, `def`, `class`, etc.) se termine par `:`
* Le contenu de ce bloc doit être **indenté uniformément**
* Une erreur d’indentation provoque une **erreur de syntaxe**

Exemple d’erreur :

```python
if True:
print("Erreur")  # pas indenté
```

→ `IndentationError: expected an indented block`

---