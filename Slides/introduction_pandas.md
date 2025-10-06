---
marp: true
theme: default
paginate: true
---

# Introduction à Pandas
## Bibliothèque Python pour la manipulation de données

---

## 1. Qu’est-ce que Pandas ?

- Bibliothèque Python pour **analyser et manipuler des données tabulaires**  
- Structures principales :
  - **Series** : vecteur 1D (comme une colonne)
  - **DataFrame** : tableau 2D (lignes × colonnes)

- Très utilisée pour **ETL, data analysis, data science, DataOps**  

Documentation : [doc](https://pandas.pydata.org/docs/)

---

## 2. Importer Pandas

```python
import pandas as pd
````

* Convention standard : `pd`

---

## 3. Créer une Series

```python
s = pd.Series([10, 20, 30, 40])
print(s)
```

**Résultat :**

```
0    10
1    20
2    30
3    40
dtype: int64
```

---

## 4. Créer un DataFrame

```python
data = {
    "Nom": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85, 90, 95]
}
df = pd.DataFrame(data)
print(df)
```

**Résultat :**

```
      Nom  Age  Score
0    Alice   25     85
1      Bob   30     90
2  Charlie   35     95
```

---

## 5. Lire un fichier CSV

```python
df = pd.read_csv("students.csv")
print(df.head())  # affiche les 5 premières lignes
```

* `read_csv` : lecture rapide de fichiers CSV
* `head(n)` : affiche les n premières lignes (par défaut 5)

---

## 6. Accéder aux colonnes / lignes

```python
print(df["Nom"])       # colonne Nom
print(df.iloc[0])      # première ligne
print(df.loc[0, "Age"]) # valeur ligne 0, colonne Age
```

---

## 7. Opérations rapides

```python
df["Age"] + 1                # incrémente chaque âge sans modifier le df
df["Score"].mean()           # moyenne des scores
df[df["Score"] > 90]         # filtrer les lignes
df.sort_values("Age")        # trier par âge
```

---

Parfait ! Je vais te refaire l’exercice **guidé pour débutants** en ajoutant **le filtrage et la sauvegarde** directement dans les étapes, avec indications pas à pas.


# Exercice guidé Pandas

## Étape 1 : Créer un DataFrame

**Instructions :**  

1. Crée un dictionnaire Python avec :  
   - `"Nom"` : liste des noms des étudiants  
   - `"Age"` : liste de leurs âges  
   - `"Score"` : liste de leurs notes  

2. Transforme ce dictionnaire en **DataFrame Pandas** avec `pd.DataFrame()`  
3. Affiche le DataFrame pour vérifier  

**Indice :**

```python
import pandas as pd

data = {
   
}

df = pd.DataFrame(data)
print(df)
```

---


## Étape 2 : Ajouter une colonne

**Instructions :**

* Crée une colonne `"Bonus"` égale à **10% du Score** (`Score * 0.1`)
* Affiche le DataFrame pour vérifier

**Indice :**

```python
# créez la colonne en plus
df["Bonus"] = ...
print(df)
```

---

## Étape 3 : Filtrer les étudiants

**Instructions :**

* Garde uniquement les étudiants ayant un `Score > 85`
* Utilise la notation `df[condition]`

**Indice :**

```python
df_filtered = ... # appliquer le filtre ici 
print(df_filtered)
```

---

## Étape 4 : Trier les résultats

**Instructions :**

* Trie le DataFrame filtré par la colonne `"Bonus"` en **ordre décroissant**
* Utilise `sort_values()` avec `ascending=False`

**Indice :**

```python
...
print(df_sorted)
```

---

## Étape 5 : Sauvegarder dans un CSV

**Instructions :**

* Sauvegarde le DataFrame final dans un fichier `students_clean.csv`
* N’inclue pas les index du DataFrame (`index=False`)

**Indice :**

```python
df_sorted.to_csv("students_clean.csv", index=False)
```

---

## Quelques commandes pratiques

* `df.head()` → affiche les 5 premières lignes
* `df["Nom"]` → accès à une colonne
* `df.iloc[0]` → accès à la première ligne
* `df.loc[0, "Age"]` → accès à une cellule spécifique
* `df["Score"].mean()` → moyenne de la colonne Score
