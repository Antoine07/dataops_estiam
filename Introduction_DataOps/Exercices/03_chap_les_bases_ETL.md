
###  Fichier source : `students_raw.csv`

```csv
first_name,last_name,gender,math_score,reading_score,writing_score
Alice,Smith,F,85,88,92
bob,johnson,M,78,82,79
Charlie,,M,90,,85
diana,Lee,F,abc,91,87
Evan,White,M,70,68,72
Fay,King,F,95,89,94
George,Brown,M,60,58,65
Hannah,Davis,F,88,90,93
ian,Clark,M,82,81,80
Julia,Miller,F,77,80,78
```

Problèmes présents dans ce fichier :

* Nom ou prénom manquant (`Charlie,,M,...`)
* Score non numérique (`diana,Lee,F,abc,91,87`)
* Minuscules pour les prénoms (`bob`, `ian`)
* Valeurs manquantes (`Charlie,,M,90,,85`)

---

### Script ETL : `etl_pipeline.py`

```python
import pandas as pd

# --- Extraction ---
df = pd.read_csv("students_raw.csv")
print("=== Données brutes ===")
print(df)

# --- Transformation / Nettoyage ---

# 1️⃣ Capitaliser les noms et prénoms
df['first_name'] = df['first_name'].str.capitalize()
df['last_name'] = df['last_name'].str.capitalize()

# 2️⃣ Remplacer les scores non numériques par NaN
score_cols = ['math_score', 'reading_score', 'writing_score']
for col in score_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3️⃣ Remplir les valeurs manquantes par la moyenne de la colonne
for col in score_cols:
    df[col] = df[col].fillna(df[col].mean())

# 4️⃣ Supprimer les lignes sans prénom ou nom
df = df.dropna(subset=['first_name', 'last_name'])

# --- Chargement ---
df.to_csv("students_cleaned.csv", index=False)

print("\n=== Données nettoyées ===")
print(df)
```

---

### 3️⃣ Résultat attendu dans `students_cleaned.csv`

```csv
first_name,last_name,gender,math_score,reading_score,writing_score
Alice,Smith,F,85.0,88.0,92.0
Bob,Johnson,M,78.0,82.0,79.0
Diana,Lee,F,82.11,91.0,87.0
Evan,White,M,70.0,68.0,72.0
Fay,King,F,95.0,89.0,94.0
George,Brown,M,60.0,58.0,65.0
Hannah,Davis,F,88.0,90.0,93.0
Ian,Clark,M,82.0,81.0,80.0
Julia,Miller,F,77.0,80.0,78.0
```

> Remarques :
>
> * Les valeurs `abc` ont été remplacées par la moyenne des scores valides de la colonne.
> * Les prénoms et noms sont correctement capitalisés.
> * Les lignes sans prénom ou nom ont été supprimées.

---