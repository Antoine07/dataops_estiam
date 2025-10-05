# **TP : Organiser un Sprint DataOps avec Scrum – Contexte et données**

## **Contexte général**

Vous êtes une équipe Data dans une entreprise qui souhaite **suivre les performances scolaires des étudiants** pour alimenter un tableau de bord analytique.
L’objectif est de mettre en place un **pipeline de données automatisé** pour :

1. Télécharger le dataset depuis Kaggle,
2. Nettoyer et transformer les données,
3. Charger le dataset dans une base PostgreSQL.

> Les données à étudier proviennent du dataset Kaggle : [Students Performance Dataset](https://www.kaggle.com/datasets/rabieelkharoua/students-performance-dataset).
> Ce dataset contient des informations sur des étudiants (scores, sexe, origine, niveau parental, etc.) qui permettront d’explorer les performances et éventuellement d’identifier des patterns ou insights.

---

## **Composition de l’équipe**

* **1 Data Engineer** – Responsable de l’extraction et de la transformation des données.
* **1 Data Analyst** – Responsable de la compréhension du dataset et des indicateurs clés.
* **1 DataOps Engineer** – Responsable de l’automatisation et de l’orchestration du pipeline.
* **1 Scrum Master** – Facilite les réunions Scrum et le suivi du sprint.
* **(Optionnel) 1 Product Owner / Coach** – Pour guider et prioriser le backlog.

---

## **Étapes du TP**

### **Étape 1 — Lecture du Backlog**

Chaque équipe identifie les **User Stories** (US) pour ce sprint.
Exemple pour ce dataset :

| ID  | User Story                                                                                                                     | Priorité |
| --- | ------------------------------------------------------------------------------------------------------------------------------ | -------- |
| US1 | En tant que *Data Engineer*, je veux automatiser le téléchargement du dataset Kaggle pour standardiser la collecte de données. | Haute    |
...

---

### **Étape 2 — Détail des tâches**

Pour chaque User Story, définissez **les tâches techniques**. Exemple :

| Tâches                      | Description                                                                |
| --------------------------- | -------------------------------------------------------------------------- |
| Configurer la clé Kaggle    | Permettre l’accès à l’API Kaggle pour le téléchargement automatique.       |

...


---

### **Étape 3 — Estimation (Story Points)**

Chaque tâche est estimée en points Scrum :

| Valeur | Signification     |
| ------ | ----------------- |
| 1      | Très simple       |

...

---

### **Étape 4 — Planification du Sprint**

* Sélectionnez les tâches **réalisables en 1 sprint** selon votre vélocité.
* Répartissez-les entre les membres de l’équipe.
* Construisez le **Sprint Backlog** :

| Tâche                  | Responsable   | Estimation | Livrable attendu    |
| ---------------------- | ------------- | ---------- | ------------------- |
| Télécharger le dataset | Data Engineer | 3 pts      | CSV brut téléchargé |

...

---

### **Étape 5 — Événements Scrum à simuler**

| Événement            | Objectif                            | Durée indicative |
| -------------------- | ----------------------------------- | ---------------- |
| Sprint Planning      | Définir les priorités et les tâches | 1h               |

...

---

### **Étape 6 — Bilan**

À la fin du sprint, l'équipe répond à ces questions :

1. Qu'est-ce qui a bien fonctionné ?
2. Qu'est-ce qui aurait pu mieux se passer ?
3. Qu'allez-vous améliorer pour le prochain sprint ?

---