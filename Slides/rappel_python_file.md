---
marp: true
theme: default
paginate: true
---

# Fichiers en Python  
## Lecture et écriture rapide

---

## Ouvrir un fichier

```python
# Ouvrir en lecture
f = open("exemple.txt", "r")
contenu = f.read()
print(contenu)
f.close()
````

* `"r"` : lecture
* `"w"` : écriture (écrase le fichier)
* `"a"` : ajout (append)
* Toujours **fermer** le fichier après utilisation avec `f.close()`

---

## Utiliser le contexte `with`

```python
with open("exemple.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

* Le fichier est **automatiquement fermé** à la fin du bloc
* Pratique et **plus sûr**

---

## Écriture dans un fichier

```python
with open("exemple.txt", "w") as f:
    f.write("Bonjour le monde!\n")
    f.write("Une deuxième ligne.")
```

* Chaque appel à `write()` ajoute du texte
* `"w"` écrase, `"a"` ajoute à la fin

---

## Lecture ligne par ligne

```python
with open("exemple.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())  # supprime \n
```

* Utile pour les fichiers volumineux
* Évite de charger tout le fichier en mémoire

---

## Exercices rapides

1. Crée un fichier `test.txt` et écris 3 lignes de texte dedans.
2. Lis le fichier et affiche chaque ligne.
3. Ajoute une 4ᵉ ligne à la fin du fichier.
4. Utilise le **contexte `with`** pour toutes les opérations.

```
