
---
marp: true
theme: default
paginate: true
size: 16:9
---

#  TP : Organiser un Sprint DataOps avec Scrum  
## Contexte et données

- Durée du TP : 1h puis correction
- Par équipe de 5 max voir le fichier dans votre Equipe **E3 Paris Lyon** 

Vous êtes une équipe **Data** dans une entreprise souhaitant **suivre les performances scolaires** des étudiants via un **tableau de bord analytique**.

🎯 Objectif : mettre en place un **pipeline automatisé** pour :

1. Télécharger le dataset depuis Kaggle,  
2. Nettoyer et transformer les données,  
3. Charger le dataset dans PostgreSQL.

---

##  Le dataset

> **Source :** [Students Performance Dataset](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset)

Ce dataset contient des informations sur les étudiants :
- scores,  
- sexe,  
- origine ethnique,  
- niveau parental, etc.

👉 Permet d'analyser les performances et d'identifier des **patterns ou insights**.

---

## Ce que vous devez faire 

On ne vous demande pas de code dans ce TP.

1. Créez un dépôt avec un README.md pour documenter votre travail.

2. Créez un projet et les issues dans votre dépôt, aidez-vous des supports vidéos.

---

# 👥 Composition de l'équipe

| Rôle | Responsabilité principale |
| ---- | -------------------------- |

... 

---

#  Étapes du TP

---

##  Étape 1 — Lecture du Backlog

Chaque équipe identifie les **User Stories (US)** pour le sprint.

| ID | User Story | Priorité |
|----|-------------|----------|
| US1 | En tant que *Data Engineer*, je veux **automatiser le téléchargement Kaggle** pour standardiser la collecte. | Haute |

...

---

##  Étape 2 — Détail des tâches

Pour chaque User Story, identifiez les **tâches techniques**.

| Tâches | Description |
|--------|--------------|
| Configurer la clé Kaggle | Permet l'accès à l'API pour le téléchargement automatique. |
| Écrire `extract_from_kaggle()` | Télécharge le dataset brut. |

...

---

##  Étape 3 — Estimation (Story Points)

Chaque tâche est estimée selon sa **complexité**.

| Points | Signification |
| ------- | -------------- |
| 1 | Très simple |

...

> Basé sur la **suite de Fibonacci**

---

##  Étape 4 — Planification du Sprint

* Sélectionnez les tâches réalisables en **1 sprint (1 semaine)**.  
* Répartissez-les entre les membres.  
* Construisez le **Sprint Backlog**.

---

### Exemple de Sprint Backlog

| Tâche | Responsable | Estimation | Livrable attendu |
|-------|--------------|-------------|------------------|
| Télécharger le dataset Kaggle | Data Engineer | 3 pts | CSV brut téléchargé |

...

---

## Étape 5 — Événements Scrum à simuler

| Événement | Objectif | Durée indicative |
|------------|-----------|------------------|
| **Sprint Planning** | Définir les priorités et les tâches | 1h |

...

---

##  Étape 6 — Bilan de Sprint

À la fin du Sprint, l'équipe répond :

1.  Qu'est-ce qui a bien fonctionné ?  
2.  Qu'est-ce qui aurait pu mieux se passer ?  
3.  Que va-t-on améliorer pour le prochain Sprint ?

🎯 Objectif : **amélioration continue** et meilleure collaboration.

---

#  Livrables attendus

à complèter 

---

#  Fin du TP

Vous aurez simulé **un sprint complet Scrum** appliqué à un **projet DataOps réel**.

> "Inspecter, adapter et livrer de la valeur — même dans la donnée." 
```

---
