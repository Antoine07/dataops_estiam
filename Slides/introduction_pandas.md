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

# TP Pandas

## Contexte

Vous recevez un fichier CSV `orders.csv` contenant les commandes d’une boutique en ligne.

Votre mission :
- Nettoyer et préparer les données
- Analyser les commandes
- Générer des statistiques et des filtres avancés

--- 

## Les données

```txt
# Jeu de données : `orders.csv`

order_id,customer_name,product,quantity,price,date
1,Alice,Book A,2,12.5,2024-06-10
2,Bob,Book B,1,15.0,2024-06-11
3,Charlie,Book C,3,20.0,2024-06-12
4,Alice,Book A,2,12.5,2024-06-10
5,Denis,Book D,0,8.0,2024-06-15
6,Eve,Book E,1,13.5,2024-06-15
7,Frank,Book F,4,25.0,2024-06-16
8,Gina,Book G,1,10.0,2024-06-16
```

--- 

# Consignes — Lecture et nettoyage

Lire le fichier CSV dans un DataFrame Pandas

Nettoyage des données :
- Supprimer les lignes où `quantity` <= 0
- Convertir `price` en float si nécessaire
- Uniformiser le format de `date` (`YYYY-MM-DD`)
- Supprimer les doublons

--- 

# Consignes — Hydratation & calculs

Calculs avec NumPy / Pandas :
- Créer une nouvelle colonne `total` = `quantity * price`
- Calculer le **chiffre d’affaires total**
- Trouver la commande la plus chère (`total` max)
- Filtrer les commandes supérieures à 50 €

--- 

# Consignes — Statistiques & reporting

Statistiques avancées :
- Moyenne, médiane et écart-type des montants (`total`)
- Nombre de commandes par client
- Top 3 des produits les plus vendus

Affichage :
- Résumer chaque commande avec `customer_name`, `product`, `quantity`, `total`
- Exporter le DataFrame nettoyé et enrichi en CSV `cleaned_orders.csv`
