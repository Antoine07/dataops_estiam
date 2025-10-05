---
marp: true
theme: default
paginate: true
---

# Introduction DataOps

L'idée centrale de **DataOps** est de rendre le traitement des données **itératif, automatisé et collaboratif**, exactement comme **l'agilité transforme le développement logiciel** que nous verrons dans ce cours.

**Concept clé :** Combiner **pratiques DevOps**, **gestion des données** et **culture collaborative** pour des pipelines fiables, rapides et reproductibles.

---

# Le cycle des données en DataOps

Le **cycle de vie des données** dans DataOps peut être représenté par un ensemble d’étapes interconnectées, allant de la collecte jusqu’à l’exploitation pour la prise de décision.

Chaque étape est **itérative et surveillée**, permettant d'améliorer en continu la qualité et la valeur des données.

---

## 1. Collecte / Ingestion

* Extraction depuis diverses sources :
  * Bases de données
  * APIs
  * Fichiers plats
  * Applications SaaS
  * Flux temps réel
* Objectif : centraliser les données brutes pour traitement cohérent

---

## 2. Stockage

* Organisation dans :
  * **Data lakes**
  * **Data warehouses**
  * Bases relationnelles
* Priorités :
  * Scalabilité
  * Sécurité
  * Gestion des métadonnées

---

## 3. Transformation / Nettoyage

* Nettoyer, enrichir et transformer les données brutes
* Types de transformations :
  * Simples : normalisation de formats
  * Complexes : agrégation, enrichissement par d’autres sources

---

## 4. Qualité et observabilité

* Tests et surveillance des pipelines
* Détection des anomalies et erreurs
* Outils :
  * **Data observability**
  * Tests automatisés pour garantir la fiabilité

---

## 5. Orchestration et automatisation

* Workflows automatisés
* Exécution répétable et fiable
* Gestion des dépendances entre tâches

---

## 6. Analyse et visualisation

* Mise à disposition des données transformées pour :
  * Analyse
  * Reporting
  * Visualisation
* Objectif : faciliter la **prise de décision basée sur les données**

---

## 7. Feedback et amélioration continue

* Utilisation des résultats et métriques pour :
  * Ajuster les pipelines
  * Corriger les erreurs
  * Améliorer les processus
* La **boucle de feedback** est au cœur de DataOps

---

# Introduction aux méthodes collaboratives

Les méthodologies collaboratives ou le client est au centre des décisions est essentiel en DevOps, mais également en DataOps.

Nous allons rappeler ce que c'est que l'Agilité et surtout la méthode Agile Scrum dans ce cours.

---

# Manifeste Agile

Le **Manifeste Agile** a été créé en 2001 pour le développement logiciel.

**4 valeurs fondamentales** appliquées à DataOps :

1. **Individus et interactions > processus et outils**  
2. **Logiciels opérationnels > documentation exhaustive**  
3. **Collaboration avec le client > négociation contractuelle**  
4. **Adaptation au changement > suivi d’un plan**
---

## Valeur 1 : Individus et interactions

Dans DataOps, cela se traduit par une collaboration étroite entre :

* **Data Engineer** : construit et maintient les **pipelines** de données  
* **Data Analyst** : analyse et visualise les données pour en tirer des **insights**  
* **Data Scientist** : crée des modèles prédictifs et fait de la modélisation avancée  
* **DevOps** : automatise le déploiement et la gestion des systèmes

---

# Interactions clés

* **Data Engineers** → alimentent le **Data Lake**  
* **Data Analysts** → transforment les données en **insights business**  
* **Data Scientists** → créent des modèles déployables  
* **DevOps** → assure la **répétabilité, fiabilité et scalabilité**  

**Note :** Scalabilité = capacité à gérer plus de données/utilisateurs sans perte de performance

---

## Valeurs 2 à 4

* **Logiciels opérationnels > documentation exhaustive**  
  → Pipelines **fonctionnels et testés** plutôt que diagrammes figés  

* **Collaboration avec le client > négociation contractuelle**  
  → Retours rapides des équipes métier  

* **Adaptation au changement > suivi d’un plan**  
  → Pipelines et analyses évoluent avec les données

---

## Comment ça se relie à DataOps

* **Livraison continue de données fiables** → comme CI/CD pour le code  
* **Tests automatisés et qualité** → chaque pipeline testé avant production  
* **Feedback rapide** → erreurs détectées et corrigées rapidement  
* **Itérations courtes** → petits lots de données, évolutions incrémentales

---

# Documentation des données en DataOps

La **documentation des données** est cruciale pour garantir la **compréhension, la qualité et la réutilisabilité** des données.

En DataOps, elle est **itérative, collaborative et automatisée**.

---

# Pourquoi documenter les données ?

* Assurer la **compréhension des datasets** par toutes les équipes  
* Faciliter la **maintenance et l’évolution des pipelines**  
* Améliorer la **qualité et la conformité** (RGPD, audits)  
* Permettre la **réutilisation des données** et éviter la duplication  
* Fournir un **contexte pour l’analyse** et la prise de décision

---

## Contenu typique de la documentation

1. **Catalogue de données**
   * Liste des datasets disponibles, origine, fréquence, propriétaire  
2. **Schémas et dictionnaires**
   * Structure des tables/fichiers, description des champs et unités  
3. **Flux et pipelines**
   * Comment les données circulent, transformations appliquées  
4. **Qualité et métriques**
   * Validations, tests et anomalies fréquentes  
5. **Historique et versions**
   * Changements et versioning des datasets
---

## Bonnes pratiques

* **Automatiser la documentation** dès que possible  
  * Ex : générer des dictionnaires à partir des pipelines  
* **Mettre à jour en continu**  
  * Toute modification dans le pipeline doit être reflétée  
* **Centraliser l’information**  
  * Un **catalogue central** pour toutes les équipes  
* **Inclure des exemples et cas d’usage**  
  * Facilite la compréhension et l’exploitation par les métiers
---

## Outils modernes pour la documentation

* **Data Catalogs** : `Apache Atlas`, `Amundsen`, `DataHub`  
* **Automatisation dans les pipelines** : `Great Expectations`, `dbt`  
* **Notebooks et dashboards** : `Jupyter`, `Streamlit`, `Confluence`, `Markdown`

Nous verrons le `Markdown`

---

# Docstrings vs Documentation DataOps

Comparer l’utilité des docstrings Python et la documentation complète des données.

---

## Docstrings Python

* Chaîne de caractères au début d’un module, classe ou fonction
* Explique **la logique du code**, les entrées/sorties
* Générable automatiquement avec **Sphinx, pdoc, MkDocs**
* Utile pour :
  * Comprendre et maintenir les pipelines
  * Réutiliser le code
  * Aider les développeurs

---

## Limites des Docstrings en DataOps

* Ne documente pas la **provenance des données** (sources, fréquence, propriétaire)  
* Ne fournit pas de **catalogue global de datasets**  
* Ne trace pas les **flux et dépendances** des données  
* Ne remplace pas les **tests de qualité et métriques**

---

## Exemple de code bien documenté


```python

import pandas as pd

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Charge un fichier CSV dans un DataFrame Pandas.

    Args:
        file_path (str): Chemin vers le fichier CSV à charger.

    Returns:
        pd.DataFrame: DataFrame contenant les données du CSV.

    Example:
        >>> df = load_csv("data/users.csv")
        >>> df.head()
           id   name    age
        0   1   Alice   30
        1   2   Bob     25
    """
    return pd.read_csv(file_path)


```