## 1. Ouvrir un fichier

Pour ouvrir un fichier, on utilise la fonction intégrée `open()`.

```python
# présent dans le dossier 
f = open("exemple.txt", "r")
contenu = f.read()
f.close()
```

Mais la méthode recommandée est d’utiliser le mot-clé `with`, qui ferme le fichier automatiquement :

```python
with open("exemple.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

---

## 2. Modes d’ouverture

| Mode  | Signification | Action                                          |
| ----- | ------------- | ----------------------------------------------- |
| `"r"` | read          | lecture (erreur si le fichier n’existe pas)     |
| `"w"` | write         | écriture (écrase le fichier s’il existe)        |
| `"a"` | append        | ajout à la fin du fichier                       |
| `"x"` | create        | création, erreur si le fichier existe déjà      |
| `"b"` | binary        | lecture/écriture en mode binaire (images, etc.) |

On peut combiner les modes, par exemple :
`"rb"` = lecture binaire, `"wb"` = écriture binaire.

---

## 3. Lire un fichier

### Lire tout le contenu :

```python
with open("exemple.txt", "r") as f:
    texte = f.read()
```

### Lire ligne par ligne :

```python
with open("exemple.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
```

### Lire toutes les lignes dans une liste :

```python
with open("exemple.txt", "r") as f:
    lignes = f.readlines()
```

---

## 4. Écrire dans un fichier

### Écraser le contenu :

```python
with open("exemple.txt", "w") as f:
    f.write("Première ligne\n")
    f.write("Deuxième ligne\n")
```

### Ajouter à la fin :

```python
with open("exemple.txt", "a") as f:
    f.write("Nouvelle ligne ajoutée\n")
```

---

## 5. Lire et écrire dans le même fichier

```python
with open("exemple.txt", "r+") as f:
    contenu = f.read()
    f.write("\nTexte ajouté à la fin")
```

---

## 6. Fichiers CSV (texte tabulaire)

Python fournit un module dédié : `csv`.

### Lecture :

```python
import csv

with open("data.csv", "r") as f:
    lecteur = csv.reader(f)
    for ligne in lecteur:
        print(ligne)
```

### Écriture :

```python
import csv

with open("data.csv", "w", newline="") as f:
    ecrivain = csv.writer(f)
    ecrivain.writerow(["nom", "age"])
    ecrivain.writerow(["Alice", 25])
```

---

## 7. Fichiers JSON (données structurées)

Le module `json` permet de lire et écrire du JSON.

### Écriture :

```python
import json

data = {"nom": "Alice", "age": 25}

with open("data.json", "w") as f:
    json.dump(data, f)
```

### Lecture :

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)
    print(data["nom"])
```

---