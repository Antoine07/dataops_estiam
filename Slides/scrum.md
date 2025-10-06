---
marp: true
theme: default
paginate: true
size: 16:9
---

#  Agilité — Le cadre général

L'**Agilité** repose sur le **Manifeste Agile (2001)**, qui défend :

* **Les individus** et **leurs interactions** > les processus et outils  
* Le **logiciel fonctionnel** > la documentation exhaustive  
* La **collaboration avec le client** > la négociation contractuelle  
* L’**adaptation au changement** > le suivi d’un plan  

🎯 Livrer **vite, souvent et mieux**, en restant **flexible** face au changement.

---

#  Scrum — Le cadre agile le plus utilisé

**Scrum** est un **cadre (framework)**, pas une méthode.  
Il repose sur la **transparence**, l’**inspection** et l’**adaptation**.

---

## 👥 Les rôles Scrum

* **Product Owner (PO)** — définit les priorités (*le quoi*)  
* **Scrum Master** — garantit la méthode (*le comment*)  
* **Dev Team** — réalise le produit (*le faire*)

---

##  Les artefacts

* **Product Backlog** — liste des besoins  
* **Sprint Backlog** — sélection des tâches pour le sprint  
* **Incrément** — version livrable du produit

---

## Les événements (rituels)

1. **Sprint** → période fixe (1 à 4 semaines)  
2. **Sprint Planning** → définir ce qu’on va faire  
3. **Daily Scrum** → 15 min chaque jour (synchronisation)  
4. **Sprint Review** → présentation du travail fini  
5. **Sprint Retrospective** → amélioration continue

---

#  Exemple concret : projet DataOps

> **Projet : Pipeline Data ETL pour analyser les performances d’étudiants**

---

## 🧩 User Stories

1.  En tant que **data engineer**, je veux **collecter les données depuis Kaggle** pour avoir une source brute.  
2. En tant qu’**analyste**, je veux **nettoyer et structurer les données** pour générer des statistiques fiables.  
3. En tant que **data scientist**, je veux **entraîner un modèle prédictif** pour estimer la réussite.  
4.  En tant que **responsable**, je veux **voir un tableau de bord clair** pour suivre la performance.

---

##  Tâches associées (exemple)

| User Story | Tâche | Rôle |
| ----------- | ----- | ---- |
| 1 | Configurer les credentials Kaggle (`kaggle.json`) | Data Engineer |
| 1 | Écrire la fonction `extract_from_kaggle()` | Data Engineer |
| 1 | Tester le téléchargement avec pytest | Data Engineer |
| 1 | Stocker le dataset brut dans `/data/raw/` | Data Engineer |

---

#  Exemple de Sprint

### **Sprint 1 — Objectif : Dataset propre prêt pour analyse**
Durée : 1 semaine  
Équipe : Antoine (DE) & Chloé (DA)

---

##  Sprint Backlog

| **User Story** | **Tâches techniques** | **Responsable** | **Statut** |
| --------------- | --------------------- | ---------------- | ----------- |
| US1 | Extraction Kaggle + tests | Antoine | ✅ Terminé |
| US2 | Nettoyage des données | Chloé | 🟡 En cours |
| US3 | Chargement des données propres | Antoine | 🔴 À faire |

---

##  Tableau Scrum simplifié

```

| To Do      | In Progress      | Done                 |
| ---------- | ---------------- | -------------------- |
| US3 - Load | US2 - Clean data | US1 - Extract Kaggle |

```

---

##  Livrables du Sprint

* `data/clean_students.csv`  
* Tests unitaires ✅  
* Workflow GitHub Actions  

**Bilan :**
* Extraction maîtrisée  
* Nettoyage à stabiliser  
* CI/CD à mettre en place prochainement  

---

# ⚠️ Gestion des problèmes

Lors de la **rétrospective** :
1. Identifier les blocages  
2. Discuter des améliorations  
3. Adapter le prochain sprint  

🎯 Objectif : **amélioration continue**, pas sanction.

---

#  Fin de Sprint : Review & Rétrospective

1. **Sprint Review** → montrer le produit au PO  
2. **Sprint Retrospective** → discuter entre l’équipe  

> Objectif : améliorer **la manière de travailler**, pas le produit.

---

##  But de la rétrospective

1. Qu’est-ce qui a bien marché ?  
2. Qu’est-ce qui a posé problème ?  
3. Que peut-on améliorer ?  

Le **Scrum Master** anime la discussion pour la garder constructive.

---

## ⏱️ Durée recommandée

| Durée du sprint | Durée rétro |
| ---------------- | ------------ |
| 1 semaine | 45 min – 1h |
| 2 semaines | 1h30 |
| 4 semaines | 3h |

---

##  Exemple DataOps

* ✅ Ce qui a bien marché : détection précoce d’erreurs via tests automatiques  
* ⚠️ Problème : échecs fréquents de connexion Kaggle  
* 🔁 Amélioration : ajouter un *retry automatique*  

---

#  Estimation des difficultés

L’équipe estime collectivement la **complexité** de chaque tâche pour :
- équilibrer le sprint,  
- anticiper la charge,  
- suivre la **vélocité**.

---

##  Les Story Points

| Points | Signification |
| ------- | -------------- |
| 1 | Très simple |
| 2 | Simple |
| 3 | Moyenne complexité |
| 5 | Difficile |
| 8 | Très complexe |
| 13+ | Trop gros → à découper |

> Basé sur la **suite de Fibonacci** (1, 2, 3, 5, 8, 13...)

---

#  Planning Poker

Méthode d’estimation collective :  
1. Le PO présente la story  
2. Chacun choisit une carte (1, 2, 3, 5, 8…)  
3. Révélation simultanée  
4. Discussion et consensus  
🎯 Pas un vote — une **décision d’équipe**

---

# 💻 Exemple concret DataOps

> “Automatiser le téléchargement des datasets Kaggle”

| Membre | Estimation |
| ------- | ----------- |
| Alice | 3 pts |
| Bob | 5 pts |
| Chloé | 3 pts |

💬 Discussion → alignement à **5 points** (prise en compte des risques réseau).

---

# 🧭 Pourquoi estimer ?

* Favorise la **communication technique**  
* Donne une **vélocité moyenne** (ex : 20 pts/sprint)  
* Permet de **planifier le prochain sprint** de façon réaliste

---

# ✅ Conclusion

L’agilité, c’est :
- Collaborer efficacement  
- Livrer souvent  
- S’améliorer continuellement  

> “Inspecter, adapter, et livrer de la valeur à chaque sprint.” 🚀

---