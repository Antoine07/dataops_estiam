---
marp: true
theme: default
paginate: true
size: 16:9
---

# Pytest — Introduction aux tests automatisés

- **Pytest** est un framework de test simple et puissant pour Python.
- Permet de :
  - Vérifier le bon fonctionnement du code
  - Éviter les régressions
  - Simplifier la maintenance
- Compatible avec les outils de CI/CD et les projets data ou API.

---

# Pourquoi tester son code ?

- **Garantir la fiabilité** du code
- **Automatiser les vérifications**
- **Documenter** les comportements attendus
- Faciliter le **refactoring**

> "Si ce n’est pas testé, ce n’est pas fiable."

---

# Installation et exécution

```bash
pip install pytest
````

Pour lancer les tests :

```bash
pytest
```

Avec plus de détails :

```bash
pytest -v
```

---

 # Configuration d'un setup

```txt
 project/
│
├── src/
│ ├── init.py
│ └── data_manager.py
│
├── tests/
│ ├── init.py
│ └── test_data_manager.py
│
└── pytest.ini
```

---

# Fichier de configuration

Fichier `pytest.ini` :

```ini
[pytest]
pythonpath = src
addopts = -v
```


---

# Règles de base

- Les fichiers de test doivent commencer par `test_`
- Les fonctions doivent commencer par `test_`
- Pas besoin de classe pour écrire des tests simples

```python
def test_addition():
    assert 2 + 2 == 4
```


---

# Exemple : tester une fonction

```python
# fichier calculator.py
def mean(values):
    return sum(values) / len(values)
````

```python
# fichier test_calculator.py
from calculator import mean

def test_mean_basic():
    assert mean([1, 2, 3]) == 2

def test_mean_zero_division():
    try:
        mean([])
    except ZeroDivisionError:
        assert True
```


---

# Fixtures

- Permettent d'**initialiser des données de test**
- Utiles pour charger un dataset, configurer un environnement ou une classe

```python
import pytest
from data_manager import DataManager

@pytest.fixture
def sample_data():
    return [10, 20, 30, 40, 50]

@pytest.fixture
def manager(sample_data):
    return DataManager(sample_data)
````


---

# Exercice — Gestion de données

Vous devez tester la classe suivante :

```python
class DataManager:
    def __init__(self, values: list[float]):
        self.values = [v for v in values if v >= 0]

    def total(self) -> float:
        return sum(self.values)

    def average(self) -> float:
        if not self.values:
            return 0.0
        return self.total() / len(self.values)

    def max_value(self) -> float:
        return max(self.values, default=0.0)
```


---

# Questions de l'exercice

1. Créez un fichier `test_data_manager.py`
2. Écrivez les tests suivants :
   - Vérifier que les valeurs négatives sont filtrées
   - Vérifier le total d’un ensemble de données
   - Vérifier la moyenne d’une liste vide (== 0.0)
   - Vérifier le maximum sur un dataset mixte
3. Utilisez `pytest` pour exécuter et valider les tests

---

# Exemple attendu (résumé)


============================= test session starts =============================
collected 4 items

test_data_manager.py ....                                              [100%]
============================== 4 passed in 0.02s =============================


- Tous les tests doivent **passer sans erreurs**
- Le code doit être **robuste et clair**

---

# À retenir

- `pytest` est léger et rapide
- Les tests guident la **qualité** et la **maintenance**
- Fixtures et asserts sont vos meilleurs alliés
- Tester = coder avec confiance
