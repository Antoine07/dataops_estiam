---
marp: true
theme: default
paginate: true
headingDivider: 2
---

##  Objectif de l’exercice

Créer un petit projet Python avec :

* une **fonction à tester**
* un **test unitaire**
* un **workflow GitHub Actions** qui s’exécute automatiquement
  👉 à chaque push sur la branche `feature_test_calculator`


##  Arborescence du projet

```
simple-python-ci/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements.txt
└── README.md
```

##  Étape 1 : le code Python

**`src/calculator.py`**

```python
def add(a: int, b: int) -> int:
    """Additionne deux entiers."""
    return a + b
```

## 🧪 Étape 2 : le test unitaire

**`tests/test_calculator.py`**

```python
from src.calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
```

##  Étape 3 : fichier de dépendances

**`requirements.txt`**

```
pytest
```

##  Workflow  **`.github/workflows/test.yml`**

```yaml
name: Run Python Tests
on:
  push:
    branches:
      - 'feature_test_calculator'
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

##  Étape 5 : tester le déclencheur

1. Crée une nouvelle branche :

   ```bash
   git checkout -b feature_test_ci
   ```

2. Committe et pousse ton code :

   ```bash
   git add .
   git commit -m "add simple calculator and test"
   git push origin feature_test_ci
   ```

3. Ssur **GitHub → Actions** → Le workflow se lancer automatiquement 
