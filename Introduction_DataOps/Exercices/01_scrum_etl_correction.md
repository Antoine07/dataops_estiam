# **TP : Organiser un Sprint DataOps avec Scrum – Contexte et Données**

## **Contexte général**

Vous faites partie de l'équipe Data d’une entreprise qui souhaite **suivre les performances scolaires des étudiants** afin d’alimenter un futur tableau de bord analytique.

L'objectif est de mettre en place un **pipeline de données automatisé** pour :

1. Télécharger le dataset depuis Kaggle,
2. Nettoyer et transformer les données,
3. Charger les données dans une base PostgreSQL.

> Les données proviennent du dataset Kaggle : [Students Performance Dataset](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset).
> Ce dataset contient des informations sur les étudiants : sexe, origine, niveau parental, scores en mathématiques, lecture et écriture, etc.

---

## **Composition de l’équipe**

* **1 Data Engineer** – Extraction et transformation des données.
* **1 Data Analyst** – Analyse et compréhension des données, création de premiers indicateurs.
* **1 DataOps Engineer** – Automatisation et orchestration du pipeline.
* **1 Scrum Master** – Facilitation, suivi et respect du processus Scrum.
* **(Optionnel) 1 Product Owner / Coach** – Priorisation du backlog et suivi des objectifs.

---

## **Étape 1 — Lecture du Backlog**

Chaque équipe identifie les **User Stories** (US) pour ce sprint.

| ID  | User Story                                                                                                                     | Priorité |
| --- | ------------------------------------------------------------------------------------------------------------------------------ | -------- |
| US1 | En tant que *Data Engineer*, je veux automatiser le téléchargement du dataset Kaggle pour standardiser la collecte de données. | Haute    |
| US2 | En tant que *Data Engineer*, je veux nettoyer et standardiser les colonnes du dataset pour garantir la qualité des données.    | Haute    |
| US3 | En tant que *DataOps Engineer*, je veux automatiser l’insertion des données dans PostgreSQL pour garantir la disponibilité.    | Haute    |
| US4 | En tant que *Data Analyst*, je veux vérifier les distributions et anomalies des données pour produire un rapport initial.      | Moyenne  |
| US5 | En tant que *Scrum Master*, je veux suivre la progression via le Kanban et les issues pour assurer le respect des deadlines.   | Moyenne  |

---

## **Étape 2 — Détail des tâches**

Pour chaque User Story, définissez **les tâches techniques et annexes**.

| Tâches                      | Description                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| Configurer la clé Kaggle    | Permettre l’accès à l’API Kaggle pour le téléchargement automatique.       |
| Télécharger le dataset      | Script Python pour récupérer le CSV depuis Kaggle.                         |
| Nettoyage des données       | Gérer les valeurs manquantes, normaliser les colonnes, convertir types.    |
| Transformation des données  | Calculer de nouvelles colonnes si nécessaire (ex. moyenne des scores).     |
| Tests unitaires du pipeline | Vérifier que chaque étape produit le résultat attendu.                     |
| Documentation               | Expliquer le fonctionnement du pipeline et les transformations effectuées. |
| Chargement PostgreSQL       | Insérer les données nettoyées dans la base, avec script SQL ou ORM.        |
| Reporting initial           | Créer un mini rapport pour visualiser les distributions et anomalies.      |
| Gestion Kanban / issues     | Suivi des tâches et des issues sur GitHub Project.                         |

---

## **Étape 3 — Estimation (Story Points)**

Chaque tâche est estimée en points Scrum selon la méthode **Planning Poker** :

| Valeur | Signification     |
| ------ | ----------------- |
| 1      | Très simple       |
| 2      | Simple            |
| 3      | Moyenne           |
| 5      | Difficile         |
| 8      | Très difficile    |
| 13     | Complexe / Risqué |

---

## **Étape 4 — Planification du Sprint**

* Sélectionnez les tâches **réalisables en un sprint** selon votre vélocité.
* Répartissez-les entre les membres de l’équipe.
* Construisez le **Sprint Backlog** :

| Tâche                      | Responsable   | Estimation | Livrable attendu    |
| -------------------------- | ------------- | ---------- | ------------------- |
| Télécharger le dataset     | Data Engineer | 3 pts      | CSV brut téléchargé |
| Nettoyer les données       | Data Engineer | 5 pts      | CSV nettoyé         |
| Transformation des données | Data Engineer | 5 pts      | CSV transformé      |
| Charger PostgreSQL         | DataOps       | 5 pts      | Données dans la DB  |
| Tests pipeline             | DataOps       | 3 pts      | Rapport de tests    |
| Analyse exploratoire       | Data Analyst  | 3 pts      | Rapport initial     |
| Documentation              | Tous          | 2 pts      | README pipeline     |
| Suivi Kanban / issues      | Scrum Master  | 2 pts      | Board mis à jour    |

---

## **Étape 5 — Événements Scrum à simuler**

| Événement            | Objectif                            | Durée indicative |
| -------------------- | ----------------------------------- | ---------------- |
| Sprint Planning      | Définir les priorités et les tâches | 1h               |
| Daily Scrum          | Synchroniser l’équipe               | 10 min           |
| Sprint Review        | Présenter les résultats             | 30 min           |
| Sprint Retrospective | Identifier les axes d’amélioration  | 30 min           |

---

## **Étape 6 — Bilan du Sprint**

À la fin du sprint, l’équipe répond à ces questions :

1. Qu'est-ce qui a bien fonctionné ?
2. Qu'est-ce qui aurait pu mieux se passer ?
3. Qu'allez-vous améliorer pour le prochain sprint ?

---