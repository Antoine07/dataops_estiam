## **Étape 1 : Créer le dépôt et les branches**

1. Crée ton dépôt sur GitHub (ex : `etl-pipeline`).
2. Clone-le en local :

```bash
git clone https://github.com/ton-utilisateur/etl-pipeline.git
cd etl-pipeline
```

3. Crée les branches :

```bash
git checkout -b raw-data   # pour stocker les fichiers bruts
git checkout -b main       # pour le code ETL
git checkout -b clean-data # pour les données validées
```

---

## **Étape 2 : Organiser la structure des fichiers**

Exemple minimal :

```
etl-pipeline/
├── data/
│   └── raw_students.csv       # fichiers bruts
├── src/
│   ├── etl/
│   │   ├── extract.py
│   │   ├── transform.py
│   │   └── load.py
│   └── tests/
│       ├── test_extract.py
│       └── test_transform.py
├── requirements.txt
├── pytest.ini
└── .github/workflows/
    └── etl-tests.yml
```

---

## **Étape 3 : Ajouter et committer les fichiers initiaux**

1. Sur la branche `raw-data` :

```bash
git checkout raw-data
git add data/raw_students.csv
git commit -m "Add raw data"
git push -u origin raw-data
```

2. Sur la branche `main` :

```bash
git checkout main
git add src/ requirements.txt pytest.ini
git commit -m "Add ETL code and tests"
git push -u origin main
```

---

## **Étape 4 : Créer le workflow GitHub Actions**

`.github/workflows/etl-tests.yml` :

```yaml
name: ETL Unit Tests

on:
  push:
    branches:
      - raw-data
  workflow_dispatch:

jobs:
  test-etl:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run ETL unit tests
        run: |
          pytest src/tests/ --maxfail=1 --disable-warnings -q

      - name: Push clean data if tests pass
        if: success()
        run: |
          git config --global user.name "github-actions"
          git config --global user.email "actions@github.com"
          git checkout -B clean-data
          python src/etl/run_pipeline.py   # script qui génère data/clean_students.csv
          git add data/clean_students.csv
          git commit -m "Update clean data"
          git push -u origin clean-data --force
```

---

## **Étape 5 : Créer un script `run_pipeline.py`**

Dans `src/etl/run_pipeline.py` :

```python
import pandas as pd
from extract import extract
from transform import clean_data
from load import load

# Exemple simple
df_raw = extract("data/raw_students.csv")
df_clean = clean_data(df_raw)
load(df_clean, "data/clean_students.csv")
```

---

## **Étape 6 : Tester localement avant de push**

```bash
pytest src/tests/ --maxfail=1 --disable-warnings -q
python src/etl/run_pipeline.py
```

* Si tout est OK, push tes fichiers bruts sur `raw-data`.
* GitHub Actions se chargera de générer et de pousser automatiquement la branche `clean-data` avec les fichiers validés.

---