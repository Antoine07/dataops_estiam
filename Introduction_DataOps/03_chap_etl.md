# **Cours : ETL et DataOps**

## Qu’est-ce que l’ETL ?

**ETL** = **Extract, Transform, Load**

C’est le processus standard pour **préparer et centraliser des données** dans un système cible (base de données, entrepôt de données, etc.).

### Les 3 étapes :

1. **Extract (Extraction)**

   * Récupérer les données depuis une ou plusieurs sources : CSV, API, base SQL, fichiers logs…
   * Exemple dans notre TP : télécharger le **dataset Kaggle** `students-performance-dataset`.

2. **Transform (Transformation / Nettoyage)**

   * Nettoyer les données : gérer les valeurs manquantes, erreurs de format, doublons…
   * Transformer les colonnes si nécessaire : calcul de moyennes, normalisation, standardisation…
   * Exemple dans notre TP : corriger les noms en minuscules, remplacer `abc` par une valeur numérique moyenne, supprimer les lignes incomplètes.

3. **Load (Chargement)**

   * Insérer les données dans le **système cible** : base PostgreSQL, Data Warehouse, ou autre outil analytique.
   * Exemple : insérer les données nettoyées dans PostgreSQL pour alimenter un tableau de bord.

> L’ETL assure que les données sont **propres, fiables et prêtes à l’analyse**.

---

## Pourquoi ETL dans le contexte DataOps ?

**DataOps** = méthodologie Agile pour la gestion des pipelines de données.
Elle reprend les principes DevOps (automatisation, CI/CD, tests) et les applique à la **donnée**.

### Objectifs de DataOps :

* Automatiser le **déploiement et l’exécution des pipelines ETL**
* Garantir **la qualité et la fiabilité des données**
* Assurer **une livraison rapide et itérative** pour les analystes et les outils BI
* Permettre le **monitoring et le feedback continu**

### Exemple avec notre TP

1. **Extraction automatisée** : GitHub Action qui télécharge automatiquement le dataset depuis Kaggle.
2. **Transformation testée** : tests unitaires pour vérifier que le nettoyage est correct avant tout chargement.
3. **Chargement automatisé** : GitHub Action ou script ETL qui pousse les données dans PostgreSQL uniquement si les tests passent.
4. **Suivi et observabilité** : chaque étape est tracée dans GitHub (issues, Kanban, logs), permettant au Scrum Master et à l’équipe de suivre l’avancement.

> Le pipeline ETL devient ainsi **une chaîne fiable et répétable**, qui s’intègre dans un workflow DataOps agile.

---

## Exemple concret du TP

* **Source** : `students_raw.csv` avec des erreurs et valeurs manquantes.
* **Pipeline ETL** :

  1. Extraction du fichier CSV (ou depuis Kaggle via API).
  2. Transformation : correction des noms, conversion des scores en numériques, remplissage des valeurs manquantes, suppression des lignes incomplètes.
  3. Chargement dans PostgreSQL.
* **Automation DataOps** :

  * GitHub Actions lance les tests ETL
  * Pipeline exécuté automatiquement si les tests passent
  * Fermeture des issues dans le Kanban et mise à jour du backlog

---

## Bonnes pratiques ETL/DataOps

1. **Automatiser tout ce qui peut l’être** : extraction, tests, chargement.
2. **Versionner les scripts ETL** dans Git pour suivi et collaboration.
3. **Tests unitaires et de qualité des données** à chaque étape.
4. **Log et monitoring** pour détecter les erreurs rapidement.
5. **Intégration avec le workflow Scrum** : user stories, tâches et Kanban pour visualiser l’avancement.

---

 **Résumé visuel du pipeline ETL DataOps :**

 Diagramme UML d'activité - Pipeline ETL dans un workflow DataOps/Scrum

<img src="./images/diagramme_ETL.png" alt="diagramme d'activité" width="300"/>



