---
marp: true
theme: default
paginate: true
size: 16:9
---

#  TP : Organiser un Sprint DataOps avec Scrum  
## Contexte et données

-  Durée du TP : 1h puis correction  
- Par équipe de **5 maximum**  
- Voir la composition des équipes dans **Teams > E3 Paris Lyon**

---

#  Objectif

Vous êtes une équipe **Data** dans une entreprise souhaitant **suivre les performances scolaires** des étudiants via un **tableau de bord analytique**.

Votre mission : concevoir **l'organisation Scrum** d'un pipeline automatisé pour :

1. Regardez le dataset depuis **Kaggle**,  

---

# 📊 Le dataset

> **Source :** [Students Performance Dataset](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)

Ce dataset contient des informations sur les étudiants :
- scores,  
- sexe,  
- origine ethnique,  
- niveau parental, etc.

🎯 Objectif analytique : identifier des **patterns** et **insights** sur la réussite scolaire.

---

#  Ce que vous devez faire

Aucun code n'est demandé dans ce TP.

L'objectif est de simuler l'organisation Scrum autour d'un projet DataOps.

---

## Étape 1 : Créez votre dépôt GitHub

1. Créez un **nouveau dépôt GitHub** pour votre équipe.(pensez à mettre le lien de ce dépôt dans le tableur dans Teams).
2. Ajoutez un fichier **`README.md`** décrivant :
   - Votre projet (contexte et objectifs),
   - L'organisation de votre équipe (Scrum),
   - Les rôles attribués à chacun.

 **Astuce :** utilisez le markdown [modèle de documentation](./tp_scum.md) pour vous guider.

 Des vidéos sont là pour vous aider à réaliser les issues et créer un projet.

---

## Étape 2 : Créez votre projet et vos issues

Tout se fait **dans GitHub**, en suivant les vidéos disponibles dans votre équipe **Teams**.

1. Ouvrez l'onglet **Projects** de votre dépôt.  
2. Créez un **nouveau projet** nommé `Sprint 1 - DataOps`.  
   - Type recommandé : **Board (Kanban)**  
   - Colonnes : `To do` → `In progress` → `Done`  

3. Créez des **issues** (une par User Story).  
   - Le **titre** = le nom de votre **User Story (US)**  
   - La **description** = le détail de la fonctionnalité, les critères d'acceptation, les tâches.

👉 Chaque issue sera automatiquement placée dans votre **backlog** (“To do”).

---

# 👥 Composition de l'équipe

| Rôle | Responsabilité principale |
| ---- | -------------------------- |
| **Product Owner** | Définit la vision et les priorités |
| **Scrum Master** | Facilite la méthode et les rituels |
| **Data Engineer(s)** | Préparent les données et pipelines |
| **Data Analyst** | Analyse les résultats |
| **Data Scientist (optionnel)** | Modélisation et prévisions |

---

# Étapes du TP

---

##  Étape 3 — Lecture du Product Backlog

Chaque équipe identifie les **User Stories (US)** du sprint.

| ID | User Story | Priorité |
|----|-------------|----------|
| US1 | En tant que *Data Engineer*, je veux **automatiser le téléchargement Kaggle** pour standardiser la collecte. | Haute |
| US2 | En tant que *Analyste*, je veux **nettoyer les données** pour éviter les valeurs manquantes. | Moyenne |
| US3 | En tant que *Data Engineer*, je veux **charger les données dans PostgreSQL** pour les centraliser. | Haute |

---

## Étape 4 — Détail des tâches

Pour chaque User Story, détaillez les **tâches techniques**.

| Tâches | Description |
|--------|--------------|
| Configurer la clé Kaggle | Permet d'accéder à l'API Kaggle. |
| Écrire `extract_from_kaggle()` | Télécharge le dataset brut. |
| Créer la table PostgreSQL | Structure la base pour accueillir les données. |

---

## Étape 5 — Estimation (Story Points)

Estimez la **complexité** de chaque tâche avec les **Story Points**.

| Points | Signification |
| ------- | -------------- |
| 1 | Très simple |
| 2 | Simple |
| 3 | Moyenne |
| 5 | Complexe |
| 8 | Très complexe |

> 📐 Basé sur la **suite de Fibonacci**  
> (1, 2, 3, 5, 8…)

---

## Étape 6 — Planification du Sprint

- Choisissez les tâches réalisables en **1 sprint (1 semaine)**.  
- Répartissez les responsabilités.  
- Construisez le **Sprint Backlog** dans votre projet GitHub.

---

### Exemple de Sprint Backlog

| Tâche | Responsable | Estimation | Livrable attendu |
|-------|--------------|-------------|------------------|
| Télécharger le dataset Kaggle | Data Engineer | 3 pts | CSV brut téléchargé |
| Nettoyer les données | Analyste | 2 pts | DataFrame propre |
| Charger dans PostgreSQL | Data Engineer | 5 pts | Table créée |

---

##  Étape 7 — Événements Scrum à simuler

| Événement | Objectif | Durée indicative |
|------------|-----------|------------------|
| **Sprint Planning** | Définir les priorités et tâches | 1h |
| **Daily Scrum** | Synchroniser les actions | 10 min |
| **Sprint Review** | Montrer les livrables | 30 min |
| **Sprint Retrospective** | Identifier les améliorations | 30 min |

---

##  Étape 8 — Bilan de Sprint

À la fin du sprint, répondez ensemble :

1. ✅ Qu'est-ce qui a bien fonctionné ?  
2. ⚠️ Qu'est-ce qui aurait pu mieux se passer ?  
3. 🚀 Que va-t-on améliorer pour le prochain sprint ?

🎯 Objectif : **amélioration continue** et **meilleure collaboration**.

---

#  Livrables attendus

1. Un **dépôt GitHub** par équipe contenant :
   - Un **README.md** clair et structuré  
   - Un **projet GitHub (Project)** avec backlog, sprint et issues  
2. Une **documentation Scrum** (markdown)
3. Une **présentation orale rapide** du fonctionnement de l'équipe  

---

#  Fin du TP

Vous aurez simulé **un sprint complet Scrum** appliqué à un **projet DataOps réel**.

> “Inspecter, adapter et livrer de la valeur — même dans la donnée.” 💡
