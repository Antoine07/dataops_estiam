# TP – ETL : Analyse des écarts de salaires à Boston

## Objectif

Mettre en œuvre un pipeline ETL (Extract, Transform, Load) complet pour analyser les écarts de salaires des employés municipaux de la ville de Boston sur l'année 2018.

Vous devez complèter chacune des parties de ce TP.

---

## 1. Contexte

L'objectif est d'extraire des données publiques, de les transformer pour les rendre exploitables, puis de calculer des statistiques par département (écarts de salaire, médiane, min, max, etc.).

Source des données :
[Analyse Boston – City Payroll Data](https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1)

---

## 2. Environnement et dépendances

Installez les dépendances nécessaires dans votre envirement de travail.

```bash
pip install numpy pandas pytest
```

Imports de base :

```python
import json
import urllib.request
import pandas as pd
import numpy as np
```

Proposition d'organisation

```txt
project_data/
│
├── env_dataops/          ←  environnement virtuel
│
├── requirements.txt      ← liste des dépendances du projet
├── main.py               ← point d'entrée principal du programme
│
├── mon_projet/           ← dossier du code source (ton “package”)
│   ├── models/           ← tes classes ou structures de données
│   │   └── user.py
│   └── utils/            ← fonctions utilitaires
│       └── helpers.py
│
└── tests/                ← tes fichiers de test
    └── test_user.py
```

---

## 3. Étapes du pipeline ETL

### 3.1 Extract

Récupération des données à partir de l'API Boston Open Data.

```python
def extract_boston_salary(url: str) -> pd.DataFrame:
    """Extrait les données brutes depuis l'API Boston."""
    pass
 
```

---

### 3.2 Transform

Nettoyage et typage des données sur la colonne **TOTAL EARNINGS**.

```python
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie et transforme les données de salaires."""
    pass

---

### 3.3 Load

Enregistrement des données nettoyées dans un fichier CSV.

```python
def load(df: pd.DataFrame, filename: str = "boston_salaries_clean.csv") -> None:
    """Enregistre les données nettoyées dans un fichier CSV."""
    pass
```

---

## 4. Analyse statistique

```python
def analyse(df: pd.DataFrame):
    """Réalise des calculs statistiques sur les salaires."""
    pass
```

---

## 5. Organisation selon la méthode AGILE

### Vision produit

Créer un pipeline ETL automatisé, testé et réutilisable pour analyser les données publiques de la ville de Boston.

### Backlog produit

### Sprints

### Rôles et rituels

---

## 6. Tests unitaires (pytest)

Créez un fichier `test_etl.py` :

```python
import pandas as pd
from etl import extract_boston_salary, transform, analyse

URL = "https://data.boston.gov/api/3/action/datastore_search?resource_id=31358fd1-849a-48e0-8285-e813f6efbdf1"

def test_extract_returns_dataframe():
   pass

def test_transform_converts_total_earnings():
    pass

def test_analyse_returns_dict():
   pass
```

---

## 7. Automatisation CI/CD – GitHub Actions

Fichier `.github/workflows/python-app.yml` :

```yaml
name: Python ETL Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.13"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install pytest pandas numpy

      - name: Run tests
        run: pytest -v
```

---

## 8. Cycle de vie des données (DataOps)



---