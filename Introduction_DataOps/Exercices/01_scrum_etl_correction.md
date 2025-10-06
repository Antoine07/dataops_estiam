---
marp: true
theme: default
paginate: true
size: 16:9
---

#  TP : Organiser un Sprint DataOps avec Scrum  

---

## Contexte général

Vous faites partie de l'équipe **Data** d’une entreprise qui souhaite **suivre les performances scolaires des étudiants** afin d’alimenter un **tableau de bord analytique**.

L’objectif est de simuler un **Sprint Scrum complet** sans écrire de code, autour de la mise en place d’un **pipeline de données automatisé** pour :

1. Télécharger le dataset depuis **Kaggle**,  
2. Nettoyer et transformer les données,  
3. Charger les données dans **PostgreSQL**.

>  **Dataset :** [Students Performance Dataset](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)  
> Contient des informations sur : sexe, origine, niveau parental, et scores en mathématiques, lecture et écriture.

---

##  Organisation du travail sur GitHub

Tout le travail de ce TP se fait sur **GitHub** :  
vous allez simuler un vrai sprint Scrum avec backlog, issues et Kanban.

### Étapes :
1. Créez un **repository GitHub** pour votre équipe.  
2. Dans l’onglet **Projects**, créez un tableau *Kanban*.  
3. Créez une **issue par User Story**.  
4. Utilisez les **labels** (`To do`, `In progress`, `Done`) pour suivre l’avancement.  
5. Des **vidéos explicatives** sont disponibles dans **Teams → Fichiers / Vidéos**.

---

##  Composition de l’équipe

| Rôle | Responsabilité principale |
|------|----------------------------|
| **Data Engineer** | Extraction et transformation des données |
| **Data Analyst** | Analyse et compréhension des données |
| **DataOps Engineer** | Automatisation et orchestration du pipeline |
| **Scrum Master** | Suivi du cadre Scrum et facilitation |
| *(Optionnel)* **Product Owner / Coach** | Priorisation du backlog et suivi métier |

---

##  Étape 1 — Lecture du Backlog

Chaque équipe identifie les **User Stories (US)** du sprint :

| ID  | User Story | Priorité |
| --- | ----------- | -------- |
| US1 | En tant que *Data Engineer*, je veux **automatiser le téléchargement Kaggle** pour standardiser la collecte. | Haute |
| US2 | En tant que *Data Engineer*, je veux **nettoyer et standardiser les colonnes** pour garantir la qualité. | Haute |
| US3 | En tant que *DataOps Engineer*, je veux **charger automatiquement les données dans PostgreSQL**. | Haute |
| US4 | En tant que *Data Analyst*, je veux **vérifier les distributions et anomalies** des données. | Moyenne |
| US5 | En tant que *Scrum Master*, je veux **suivre la progression via GitHub Kanban**. | Moyenne |

---

##  Étape 2 — Détail des tâches

Pour chaque User Story, définissez les **tâches techniques** correspondantes :

| Tâches | Description |
| ------- | ------------ |
| Configurer la clé Kaggle | Permet l’accès à l’API Kaggle pour le téléchargement. |
| Télécharger le dataset | Script ou commande pour récupérer le CSV brut. |
| Nettoyage des données | Gérer valeurs manquantes, normaliser les colonnes. |
| Transformation des données | Créer de nouvelles colonnes (ex. moyenne des scores). |
| Chargement PostgreSQL | Insérer les données dans la base. |
| Tests pipeline | Vérifier la cohérence des étapes. |
| Documentation | Expliquer le fonctionnement du pipeline. |
| Reporting initial | Visualiser les distributions et anomalies. |
| Suivi Kanban / issues | Mettre à jour les statuts dans GitHub Project. |

---

##  Étape 3 — Estimation (Story Points)

Chaque tâche est estimée selon la **complexité**, à l’aide du **Planning Poker**.

| Valeur | Signification |
| ------- | -------------- |
| 1 | Très simple |
| 2 | Simple |
| 3 | Moyenne |
| 5 | Difficile |
| 8 | Très difficile |
| 13 | Complexe / Risqué |

> 🔢 Basé sur la **suite de Fibonacci** : permet d’estimer la charge sans entrer dans le temps précis.

---

##  Étape 4 — Planification du Sprint

* Sélectionnez les tâches **réalisables en un sprint (1 semaine)**.  
* Répartissez-les entre les membres.  
* Créez votre **Sprint Backlog** dans GitHub Project.

| Tâche | Responsable | Estimation | Livrable attendu |
|-------|--------------|-------------|------------------|
| Télécharger le dataset | Data Engineer | 3 pts | CSV brut téléchargé |
| Nettoyer les données | Data Engineer | 5 pts | CSV nettoyé |
| Transformation des données | Data Engineer | 5 pts | CSV transformé |
| Charger PostgreSQL | DataOps | 5 pts | Données dans la DB |
| Tests pipeline | DataOps | 3 pts | Rapport de tests |
| Analyse exploratoire | Data Analyst | 3 pts | Rapport initial |
| Documentation | Tous | 2 pts | README pipeline |
| Suivi Kanban / issues | Scrum Master | 2 pts | Board à jour |

---

##  Étape 5 — Événements Scrum à simuler

| Événement | Objectif | Durée indicative |
|------------|-----------|------------------|
| **Sprint Planning** | Définir les priorités et les tâches | 1h |
| **Daily Scrum** | Synchroniser l’équipe (stand-up) | 10 min |
| **Sprint Review** | Présenter les résultats du sprint | 30 min |
| **Sprint Retrospective** | Identifier les points à améliorer | 30 min |

> 💬 Simulez ces réunions à l’oral ou à l’écrit dans Teams ou GitHub Discussions.

---

## Étape 6 — Bilan du Sprint

À la fin du sprint, l’équipe répond à trois questions :

1. ✅ Qu’est-ce qui a bien fonctionné ?  
2. ⚠️ Qu’est-ce qui aurait pu mieux se passer ?  
3. 🚀 Que va-t-on améliorer pour le prochain sprint ?

🎯 Objectif : **amélioration continue** et esprit d’équipe.

---

##  Livrables attendus

1. Un **repository GitHub** par équipe contenant :
   - Un `README.md` documentant votre organisation Scrum.  
   - Un **tableau GitHub Project** avec backlog et sprint.  
   - Des **issues** correspondant aux User Stories.
2. Un **compte rendu de sprint** (Review + Rétrospective) ajouté au README.  
3. *(Optionnel)* Une **capture du Kanban final** à la fin du sprint.

---

## Fin du TP

Vous aurez simulé un **Sprint Scrum complet appliqué à un projet DataOps réel**.  

> “Inspecter, adapter et livrer de la valeur — même dans la donnée.”  
