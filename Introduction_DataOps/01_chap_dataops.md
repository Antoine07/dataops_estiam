# DataOps

L'idée centrale de **DataOps** est de rendre le traitement des données **itératif, automatisé et collaboratif**, exactement comme l'agilité transforme le développement logiciel. Il s'agit d'une approche qui combine **pratiques DevOps**, **gestion des données** et **culture de collaboration**, afin de livrer des pipelines de données fiables, rapides et reproductibles.

## Le cycle des données en DataOps

Le **cycle de vie des données** dans DataOps peut être représenté par un ensemble d’étapes interconnectées, allant de la collecte des données jusqu’à leur exploitation pour la prise de décision. Chaque étape est **itérative et surveillée**, permettant d'améliorer en continu la qualité et la valeur des données.

1. **Collecte / Ingestion**
   Les données sont extraites depuis diverses sources : bases de données, APIs, fichiers plats, applications SaaS ou flux temps réel. Cette étape vise à centraliser les données brutes pour pouvoir les traiter de manière cohérente.

2. **Stockage**
   Les données sont organisées dans des **data lakes**, **data warehouses** ou bases relationnelles, selon leurs volumes, leur format et leur usage. Le stockage moderne privilégie la scalabilité, la sécurité et la gestion des métadonnées.

3. **Transformation / Nettoyage**
   Cette phase consiste à **nettoyer, enrichir et transformer** les données brutes pour les rendre exploitables. Les transformations peuvent être simples (normalisation de formats) ou complexes (agrégation, enrichissement par d’autres sources).

4. **Qualité et observabilité**
   Chaque pipeline est testé et surveillé afin de détecter des anomalies, des erreurs ou des écarts de qualité. Les outils de **data observability** et de tests automatisés garantissent la fiabilité des données.

5. **Orchestration et automatisation**
   L’ensemble des étapes est orchestré par des workflows automatisés, permettant d’exécuter les pipelines de manière répétable et fiable, et de gérer les dépendances entre tâches.

6. **Analyse et visualisation**
   Les données transformées et validées sont mises à disposition pour l’**analyse, le reporting et la visualisation**. Cette étape permet de créer de la valeur en facilitant la prise de décision basée sur les données.

7. **Feedback et amélioration continue**
   Les résultats des analyses et les métriques de qualité sont utilisés pour **ajuster les pipelines**, corriger les erreurs et améliorer les processus. Ce feedback loop est au cœur de la philosophie DataOps, garantissant une évolution constante et agile des pipelines.



### Introduction au Manifeste Agile

Le **Manifeste Agile** a été créé en 2001 pour le développement logiciel. Il repose sur **4 valeurs fondamentales** :

1. **Les individus et leurs interactions plus que les processus et les outils**
   Dans DataOps, ça se traduit par une collaboration étroite entre les data engineers, data analysts, data scientists et DevOps.

* **Data Engineer** construit et maintient les **pipelines** de données.
* **Data Analyst** analyse et visualise les données pour en tirer des **insights** (information exploitable tirée de l'analyse des données).
* **Data Scientist** crée des modèles prédictifs et fait de la modélisation avancée.
* **DevOps** automatise le déploiement et la gestion des systèmes et applications.


Voici une mini-carte simplifiée des rôles et interactions en **DataOps** :

```
                ┌───────────────┐
                │  Data Source  │
                └───────┬───────┘
                        │
                        ▼
               ┌────────────────┐
               │ Data Engineer  │
               │ (pipelines)    │
               └───────┬────────┘
                       │
                       ▼
         ┌───────────────────────────┐
         │       Data Lake / DB      │
         └─────────┬─────────────────┘
                   │
         ┌─────────┴─────────┐
         ▼                   ▼
 ┌─────────────┐       ┌───────────────┐
 │ Data Analyst│       │ Data Scientist│
 │ (reporting) │       │ (modèles & IA)│
 └──────┬──────┘       └───────┬───────┘
        │                      │
        └──────────────┬───────┘
                       ▼
                ┌───────────────┐
                │    DevOps      │
                │(déploiement & │
                │ automatisation)│
                └───────────────┘
```

**Interactions clés :**

* **Data Engineers** alimentent le **Data Lake** pour les Analysts et Scientists.
* **Data Analysts** transforment les données en insights business.
* **Data Scientists** créent des modèles qui peuvent être déployés grâce au **DevOps**.
* **DevOps** assure la **répétabilité, fiabilité et scalabilité** des pipelines et modèles.


Remarque sur les termes scalabilité c'est la capacité d’un système, d’une application ou d’une infrastructure à gérer une augmentation de charge (plus d’utilisateurs, plus de données) sans perte de performance.

2. **Des logiciels opérationnels plus qu'une documentation exhaustive**
   → Ici, on pense à des pipelines de données **fonctionnels et testés**, plutôt que des diagrammes longs et figés.

3. **La collaboration avec le client plus que la négociation contractuelle**
   → En DataOps, les "clients" peuvent être les équipes métier qui consomment les données. On cherche des **retours rapides** pour améliorer les pipelines.

4. **L'adaptation au changement plus que le suivi d'un plan**
   → Les données changent constamment. Les pipelines et les analyses doivent pouvoir évoluer rapidement.

---

### Comment ça se relie à DataOps

* **Livraison continue de données fiables** → comme le CI/CD pour le code.
* **Tests automatisés et qualité** → chaque pipeline est testé avant d'être mis en production.
* **Feedback rapide** → erreurs de données détectées et corrigées rapidement.
* **Itérations courtes** → petits lots de données, évolutions incrémentales.

##  Outils DataOps modernes en Python

###  Ingestion / Extraction

* `Pandas` – lecture CSV, Excel, Parquet, SQL.
* `SQLAlchemy` – connexion et extraction depuis bases relationnelles.
* `Requests` – récupération depuis APIs REST.
* `Kafka-python` – ingestion temps réel.

---

### Orchestration

* `Airflow` – planification et automatisation des pipelines.
* `Prefect` – orchestration moderne avec monitoring intégré.
* `Dagster` – pipelines Python avec observabilité.

---

### Transformation / ETL

* `Pandas` – nettoyage et transformation de DataFrames.
* `Polars` – alternative rapide à Pandas pour gros volumes.
* `dbt + Python` – transformations SQL avec possibilités Python.
* `PySpark` – transformations distribuées pour Big Data (optionnel si gros volumes).

---

### Qualité et Observabilité

* `Great Expectations` – tests et validations de données.
* `Pandera` – validation des DataFrames.

---

### Visualisation

* `Matplotlib / Seaborn` – visualisation de base.
* `Plotly` – visualisation interactive.
* `Streamlit / Dash` – dashboards interactifs en Python.

---
