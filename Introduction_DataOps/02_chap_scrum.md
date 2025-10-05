## **Agilité – le cadre général**

L'**Agilité** repose sur le **Manifeste Agile (2001)**, qui défend :

* **Les individus** et **leurs interactions**> les processus et outils
* Le logiciel fonctionnel > la documentation exhaustive
* La collaboration avec le client > la négociation contractuelle
* L’adaptation au changement > le suivi d’un plan

L'idée : livrer **vite, souvent et mieux**, en restant **flexible** face au changement.

---

## **Scrum — la méthode agile la plus utilisée**

**Scrum** n'est pas une méthode mais un **cadre (framework)**.
Il est léger, basé sur **la transparence**, l'inspection et l'adaptation.

### Les **rôles**

* **Product Owner (PO)** : définit les priorités (le 'quoi').
* **Scrum Master** : garantit la méthode (le 'comment').
* **Dev Team** : réalise le produit (le 'faire').

### Les **artefacts**

* **Product Backlog** : liste des besoins.
* **Sprint Backlog** : sélection des tâches pour le sprint.
* **Incrément** : version potentiellement livrable du produit.

### Les **événements (rituels)**

1. **Sprint** → période fixe (1 à 4 semaines).
2. **Sprint Planning** → définir ce qu’on va faire.
3. **Daily Scrum** → 15 min chaque jour (synchronisation).
4. **Sprint Review** → présentation du travail fini.
5. **Sprint Retrospective** → amélioration continue.

### Exemple concret : projet "Pipeline Data ETL pour analyser les performances d’étudiants"

#### **User Stories**

1. **En tant que data engineer**, je veux **collecter les données depuis Kaggle**, afin de **disposer d'une source de données brute à traiter.**
2. **En tant qu'analyste**, je veux **nettoyer et structurer les données**, afin de **pouvoir générer des statistiques fiables.**
3. **En tant que data scientist**, je veux **entraîner un modèle prédictif**, afin de **prédire la réussite des étudiants.**
4. **En tant que responsable**, je veux **voir un tableau de bord clair**, afin de **suivre la performance globale.**

---

#### **Tâches associées (exemple pour la story 1)**

| User Story | Tâche                                           | Rôle          |
| ---------- | ----------------------------------------------- | ------------- |
| 1          | Configurer les credentials Kaggle (kaggle.json) | Data Engineer |
| 1          | Écrire la fonction `extract_from_kaggle()`      | Data Engineer |
| 1          | Tester le téléchargement avec pytest            | Data Engineer |
| 1          | Stocker le dataset brut dans `/data/raw/`       | Data Engineer |

Et ainsi de suite pour les autres stories (cleaning, transformation, dashboard...).

---

## Exemple de Sprints

###  **Sprint 1 — Objectif : Obtenir un dataset propre prêt pour analyse**

#### Durée : 1 semaine

#### 👥 Équipe :

* Antoine (Data Engineer)
* Chloé (Data Analyst)

---

### **Sprint Backlog**

| **User Story**                                                                                                                     | **Tâches techniques**                                                                                                                | **Responsable** | **Statut**  |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ----------- |
| **US1** — En tant que data engineer, je veux extraire le dataset depuis Kaggle pour commencer le pipeline.                         | - Créer la fonction `extract_from_kaggle()`  <br> - Configurer la clé API dans Docker <br> - Écrire un test `test_extract_kaggle.py` | Antoine         | ✅ Terminé   |
| **US2** — En tant que data analyst, je veux nettoyer les données pour supprimer les valeurs manquantes et normaliser les colonnes. | - Implémenter `clean_data()` dans `transform.py` <br> - Ajouter des tests unitaires <br> - Générer le fichier `clean_students.csv`   | Chloé           | 🟡 En cours |
| **US3** — En tant qu’analyste, je veux sauvegarder les données propres dans un dossier versionné.                                  | - Créer fonction `load(df, path)` <br> - Ajouter étape `run_pipeline.py` <br> - Commit auto via GitHub Actions                       | Antoine         | 🔴 À faire  |

---

### **Colonnes Scrum simplifiées (tableau de bord)**

* 🟥 **To Do** → à planifier ou non commencées
* 🟨 **In Progress** → en développement/test
* 🟩 **Done** → validées en revue de code + testées

Exemple visuel en texte :

```
To Do         | In Progress       | Done
--------------|-------------------|-------------------
US3 - Load    | US2 - Clean data  | US1 - Extract Kaggle
```

---

###  **Livrables attendus du Sprint**

* `data/clean_students.csv`
* Tests unitaires verts (`pytest`)
* Workflow GitHub Actions fonctionnel

---

**Bilan du Sprint :**

* Extraction maîtrisée
* Nettoyage à stabiliser (valeurs nulles dans certaines colonnes)
* Étape de chargement et automatisation CI/CD à venir dans le Sprint 2

---

## Gestion des problèmes 

### Réaction Agile

1. On en discute lors de la **rétrospective de sprint** :

   * Qu'est-ce qui a bloqué ?
   * Qu'est-ce qu’on aurait pu faire mieux ?
   * Que change-t-on au prochain sprint ?
2. On ajuste le backlog et le planning (plus court, plus réaliste).

> 🎯 Objectif : **amélioration continue**, pas sanction.
> On apprend à chaque sprint.

---

## La rétrospective juste après la review

### Concrètement dans Scrum :

Un **sprint** dure généralement **1 à 4 semaines** (souvent 2).
L'ordre des événements à la fin du sprint est :

1. **Sprint Review** (revue de sprint)

> L'équipe montre ce qu'elle a réalisé au Product Owner et aux parties prenantes.
> → Objectif : recueillir du feedback sur le produit.

2. **Sprint Retrospective** (rétrospective de sprint)

> L'équipe (Scrum Master + devs + data engineers, etc.) se réunit **entre eux**, sans le client.
> → Objectif : réfléchir **sur la façon de travailler**, pas sur le produit.

---

###  But de la rétrospective

Répondre à trois questions simples :

1. Qu’est-ce qui a bien marché ?
2. Qu’est-ce qui a posé problème ?
3. Que peut-on améliorer pour le prochain sprint ?

Le Scrum Master anime cette réunion pour qu'elle reste constructive et orientée amélioration continue.

---

### Durée recommandée :

| Durée du sprint | Durée de la rétrospective |
| --------------- | ------------------------- |
| 1 semaine       | ~45 minutes à 1 heure     |
| 2 semaines      | ~1h30                     |
| 4 semaines      | ~3 heures                 |

---

### Exemple DataOps :

À la fin d'un sprint :

* **Ce qui a bien marché :** les tests automatiques du pipeline ont détecté une erreur tôt.
* **Ce qui a posé problème :** la connexion Kaggle a souvent échoué.
* **À améliorer :** ajouter un *retry automatique* dans l’étape `extract_from_kaggle`.

> La conclusion devient une **tâche d’amélioration** pour le sprint suivant.


## Estimation des difficultées de chaque useer story ou tâche à réaliser 

En Scrum (et plus largement dans l'agilité), la difficulté des tâches est **estimée par l’équipe**, pas par le chef de projet.

##  1. Le but

Attribuer une **valeur de complexité** (ou d'effort) à chaque **user story** ou **tâche**, pour :

* anticiper la charge de travail,
* équilibrer le sprint,
* et suivre la *vélocité* (la capacité moyenne de l’équipe par sprint).

---

## 2. L'unité : les *Story Points*

Les tâches ne sont pas estimées en heures mais en **points d’effort** (Story Points), qui mesurent la **complexité globale** :

> effort ⟶ temps ⟶ incertitude ⟶ risque technique

Par exemple (suite de Fibonacci)

| Story Points | Signification                                 |
| ------------ | --------------------------------------------- |
| 1            | Très simple (changement mineur, script court) |
| 2            | Simple (une fonction à écrire)                |
| 3            | Moyenne complexité                            |
| 5            | Difficile, plusieurs étapes                   |
| 8            | Très complexe                                 |
| 13+          | Trop gros → à découper                        |

On utilise souvent la **suite de Fibonacci** : 1, 2, 3, 5, 8, 13, 21…
→ car les grands nombres reflètent une incertitude croissante.

---

## 3. Méthode : *Planning Poker*

C'est la méthode la plus utilisée 

### Déroulement :

1. Le Product Owner présente la user story.
2. Chaque membre estime individuellement la difficulté, sans montrer son estimation aux autres (avec des cartes ou outils numériques : 1, 2, 3, 5, 8…).
3. Tout le monde révèle sa carte **en même temps**.
4. Si les estimations diffèrent, on discute pour comprendre pourquoi.
5. L'équipe converge vers une estimation commune.

> Ce n'est **pas un vote**, c'est un **consensus collectif**.

---

## 4. Exemple concret DataOps

User story :

> “En tant que Data Engineer, je veux automatiser le téléchargement des datasets Kaggle pour simplifier l'intégration.”

Équipe :

* Alice (backend) → 3 points
* Bob (infra) → 5 points
* Chloé (analyste) → 3 points

Discussion → Bob explique les difficultés réseau possibles et la gestion d'erreurs → on s'aligne sur **5 points**.

---

## 5. Pourquoi c’est important

* Favorise la **communication technique** et la **vision partagée**.
* Permet d'évaluer la **vélocité moyenne** (ex. : “on livre ~20 points par sprint”).
* Aide à **planifier le prochain sprint** de manière réaliste.

