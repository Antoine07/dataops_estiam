---
marp: true
theme: default
paginate: true
---

#  GitHub Actions  
## Automatisation CI/CD et workflows

---

## Qu’est-ce que GitHub Actions ?

- GitHub Actions est un service intégré à GitHub pour **automatiser les workflows**.  
- Permet de **lancer des scripts ou pipelines** lors d’événements GitHub : push, pull request, issue…  
- Utilisé pour **CI/CD**, tests automatiques, déploiement, ETL, DataOps, etc.

---

## Concepts clés

- **Workflow** : fichier YAML définissant une suite d’actions (`.github/workflows/*.yml`)  
- **Job** : ensemble de steps qui s’exécutent sur une machine virtuelle  
- **Step** : action individuelle ou commande à exécuter  
- **Runner** : machine qui exécute les jobs (Linux, Windows, macOS)  
- **Event** : déclencheur du workflow (push, PR, schedule…)

---

## Exemple simple de workflow

```yaml
name: CI

on:
  push:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
````

* Déclenché sur **push** vers `main`
* Installe Python, dépendances, puis lance les tests

---

## Utilisations courantes

* **CI/CD** : tests, linting, déploiement automatique
* **Automation DataOps** : pipelines ETL, vérification de datasets
* **Déploiement cloud** : AWS, Azure, GCP
* **Notifications** : Slack, email, Jira
* **Monitoring & observabilité** : logs des workflows, reporting

---

## Bonnes pratiques GitHub Actions

1. **Modulariser les workflows** en plusieurs jobs
2. **Tester localement** les scripts avant automation
3. **Utiliser des secrets** pour mots de passe, tokens
4. **Versionner les actions** avec tags (`@v3`)
5. **Logs clairs et précis** pour debugging rapide

---

## Exemple concret pour notre TP ETL/DataOps

* **Pipeline ETL automatisé** :

  * Workflow déclenché par push ou planification
  * Extraction dataset Kaggle
  * Tests unitaires pour nettoyage
  * Chargement dans PostgreSQL uniquement si tests OK
  * Notifications dans Slack ou GitHub Issues

> Résultat : un workflow **fiable, répétable et observable**, intégré dans notre méthodologie DataOps

Parfait ! Voici un **exercice pratique GitHub Actions** que tu peux proposer aux étudiants :

---

## **Exercice pratique : Pipeline CI simple**

**Objectif :** Créer un workflow GitHub Actions qui teste automatiquement un projet Python à chaque push sur la branche `main`.

### **Étapes**

1. **Préparer le projet Python**

   * Crée un fichier `calculator.py` avec une fonction `add(a, b)` qui renvoie la somme.
   * Crée un fichier `test_calculator.py` avec un test utilisant `pytest` pour vérifier que `add(2,3) == 5`.

2. **Créer le workflow GitHub Actions**

   * Crée un dossier `.github/workflows/`
   * Ajoute un fichier `ci.yml` avec le workflow suivant :

     * Déclenché sur `push` sur `main`
     * Installer Python
     * Installer `pytest`
     * Lancer les tests

3. **Valider le pipeline**

   * Pousse les fichiers sur GitHub
   * Vérifie que le workflow s’exécute et que le test passe

---

### **Bonus (optionnel)**

* Ajouter une étape pour **installer des dépendances** depuis un `requirements.txt`.
* Ajouter un **linter** (ex : `pylint`) avant les tests.
* Ajouter un workflow pour **les Pull Requests** afin de tester avant fusion.

[rappel sur les linter](./rappel_linter.html)
