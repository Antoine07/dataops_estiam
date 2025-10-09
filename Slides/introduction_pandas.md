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
# df.loc[rows, columns]
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

## Quelques commandes pratiques

* `df.head()` → affiche les 5 premières lignes
* `df["Nom"]` → accès à une colonne
* `df.iloc[0]` → accès à la première ligne
* `df.loc[0, "Age"]` → accès à une cellule spécifique
* `df["Score"].mean()` → moyenne de la colonne Score

---

## Glossaire non exhaustif

```

| `pd.read_csv("file.csv")` | Lire un CSV dans un DataFrame |
| `df.head(n)`              | Afficher les n premières lignes |
| `df.info()`               | Infos sur le DataFrame (types, NaN) |
| `df.describe()`           | Statistiques descriptives |
| `df["col"]`               | Sélection d’une colonne |
| `df.loc[...]`             | Sélection de lignes/colonnes par étiquette ou condition |
| `df.iloc[...]`            | Sélection de lignes/colonnes par position |
| `df.drop_duplicates()`    | Supprimer les doublons |
| `df.dropna()`             | Supprimer les valeurs manquantes |
| `df.astype(type)`         | Conversion de type d’une colonne |
| `df.to_csv("file.csv")`   | Exporter le DataFrame en CSV |

```

---

## **1. Créer une petite DataFrame**

```python
import pandas as pd

data = {
    "nom": ["Alice", "Bob", "Clara"],
    "age": [25, 30, 22],
    "ville": ["Paris", "Lyon", "Marseille"]
}

df = pd.DataFrame(data)

print(df)
print(df["nom"])   # colonne spécifique
print(df[["nom", "ville"]])  # plusieurs colonnes
```

---

## **2. Filtrer les personnes de plus de 25 ans**

```python
filtre = df[df["age"] > 25]
print(filtre[["nom", "ville"]])
```

---

## **3. Ajouter une nouvelle colonne**

```python
df["score"] = [12, 15, 9]
print(df)

moyenne_score = df["score"].mean()
print("Moyenne des scores :", moyenne_score)
```

---

## **4. Filtrer selon plusieurs conditions**

```python
filtre = df[(df["age"] < 30) & (df["ville"].isin(["Paris", "Marseille"]))]
print(filtre)
```

---

## **5. Calculer des statistiques**

```python
data = {
    "produit": ["A", "B", "C", "D"],
    "prix": [10, 15, 7, 20],
    "quantité": [5, 3, 10, 2]
}
df = pd.DataFrame(data)

df["total"] = df["prix"] * df["quantité"]
print(df)

somme_totale = df["total"].sum()
print("Somme totale des ventes :", somme_totale)
```

---

## **6. Trier les données**

```python
tri = df.sort_values(by=["prix", "quantité"], ascending=[True, False])
print(tri)
```

---

## **7. Grouper les données**

```python
ventes = pd.DataFrame({
    "ville": ["Paris", "Lyon", "Paris", "Marseille", "Lyon"],
    "produit": ["A", "B", "A", "C", "C"],
    "montant": [100, 200, 150, 300, 250]
})

groupes = ventes.groupby("ville")["montant"].sum()
print(groupes)
```

---

## **8. Remplacer les valeurs manquantes**

```python
import numpy as np

notes = pd.DataFrame({
    "nom": ["Alice", "Bob", "Clara", "David"],
    "note": [12, np.nan, 15, np.nan]
})

moyenne = notes["note"].mean()
notes["note"].fillna(moyenne, inplace=True)
print(notes)
```

---

## **9. Mélanger les lignes**

```python
melange = notes.sample(frac=1, random_state=1)
print(melange)
```

---

## **10. Bonus : filtrage logique**

```python
animaux = pd.DataFrame({
    "animal": ["chat", "chien", "oiseau", "poisson", "lapin"],
    "poids": [4, 10, 0.2, 0.1, 2]
})

filtre = animaux[(animaux["poids"] < 5) & (animaux["animal"].str.contains("a"))]
print(filtre)
```
