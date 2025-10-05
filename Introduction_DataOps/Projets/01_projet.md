# Installation

https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset


## Permet d'installer les dépendances
```bash
docker compose exec jupyter bash -c "pip install -r /home/jovyan/work/requirements.txt"
```

## Commande pour créer le projet


```bash
mkdir -p src/{etl,tests,.github/workflows} && \
touch src/{requirements.txt,Dockerfile} && \
touch src/etl/{extract.py,transform.py,load.py} && \
touch src/tests/{test_extract.py,test_transform.py,test_load.py} && \
touch src/.github/workflows/ci.yml
```

## Structure du projet pour nettoyer les données

```txt
├── .github
│   └── workflows
│       └── ci.yml
├── data
│   └── raw_students.csv
├── docker-compose.yaml
└── src
    ├── etl
    │   ├── extract.py
    │   ├── load.py
    │   └── transform.py
    └── tests
        ├── test_extract.py
        ├── test_load.py
        └── test_transform.py
```

## Jeu de données d'exemple à nettoyer (format CSV)

```txt


```

## Lancer les tests

```bash
pytest src/tests/ --maxfail=1 -q
```