---
marp: true
theme: default
paginate: true
---

#  ETL et DataOps

---

## Qu’est-ce que l’ETL ?

**ETL** = **Extract, Transform, Load**

C’est le processus standard pour **préparer et centraliser des données** dans un système cible (base de données, entrepôt de données, etc.).

---

## Les 3 étapes de l’ETL

1. **Extract (Extraction)**  
   * Récupérer les données depuis CSV, API, SQL, logs…  
   * Exemple TP : dataset Kaggle `students-performance-dataset`.

2. **Transform (Transformation / Nettoyage)**  
   * Nettoyer : gérer valeurs manquantes, doublons, erreurs.  
   * Transformer : calculs, normalisation…  
   * Exemple TP : noms en minuscules, valeurs `abc` remplacées, lignes incomplètes supprimées.

3. **Load (Chargement)**  
   * Insérer les données dans la **base cible** : PostgreSQL, Data Warehouse…  
   * Exemple TP : données nettoyées insérées dans PostgreSQL.

> L’ETL assure que les données sont **propres, fiables et prêtes à l’analyse**.

---

## Pourquoi ETL dans le contexte DataOps ?

**DataOps** = méthodologie Agile appliquée aux pipelines de données.

**Objectifs :**  
* Automatiser **déploiement et exécution des pipelines ETL**  
* Garantir **qualité et fiabilité des données**  
* Livraison rapide et itérative pour analystes/BI  
* **Monitoring et feedback continu**

---

## Exemple DataOps dans notre TP

1. **Extraction automatisée** : GitHub Action télécharge dataset depuis Kaggle  
2. **Transformation testée** : tests unitaires vérifiant le nettoyage  
3. **Chargement automatisé** : push dans PostgreSQL si tests OK  
4. **Suivi et observabilité** : logs, Kanban, suivi Scrum

> Le pipeline ETL devient **fiable, répétable et intégré dans un workflow agile**.

---

## Exemple concret du TP

* **Source** : `students_raw.csv` avec erreurs et valeurs manquantes  
* **Pipeline ETL** :  
  1. Extraction du CSV  
  2. Transformation : correction noms, scores numériques, remplissage valeurs manquantes, suppression lignes incomplètes  
  3. Chargement dans PostgreSQL  

* **Automation DataOps** :  
  * GitHub Actions lance tests ETL  
  * Pipeline exécuté automatiquement si tests OK  
  * Issues fermées et backlog mis à jour

---

## Bonnes pratiques ETL/DataOps

1. Automatiser tout ce qui peut l’être (extraction, tests, chargement)  
2. Versionner les scripts ETL dans Git  
3. Tests unitaires et qualité des données à chaque étape  
4. Logs et monitoring pour détecter rapidement les erreurs  
5. Intégration avec workflow Scrum : user stories, tâches, Kanban

---

## Résumé visuel

**Pipeline ETL dans workflow DataOps/Scrum**

<img src="./diagramme_ETL.png" alt="diagramme d'activité" width="300"/>
