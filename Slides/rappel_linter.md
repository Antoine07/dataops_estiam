---
marp: true
theme: default
paginate: true
---

# Linters Python dans VSCode  
## Avec Pylint

---

## 1. Installer l’extension Python

1. Ouvre VSCode  
2. Allez dans **Extensions** (`Ctrl+Shift+X`)  
3. Recherchez **Python** (Microsoft)  
4. Installez l’extension officielle  

---

## 2. Installer Pylint

- Ouvrez le terminal intégré dans VSCode  
- Installez Pylint dans votre environnement Python :

```bash
pip install pylint
````

* Vérifie l’installation :

```bash
pylint --version
```

---

## 3. Configurer VSCode pour Pylint

1. Ouvrez **Settings** 
2. Cherchez `Python Linting`
3. Activez **Python: Linting Enabled**
4. Dans **Python: Linting Pylint Enabled**, coche **true**

> VSCode utilisera maintenant Pylint pour analyser ton code à la volée.

---

## 4. Comment ça fonctionne

* Les erreurs et warnings sont **soulignés dans l’éditeur**
* Le panneau **Problems** (`Ctrl+Shift+M`) liste tous les problèmes détectés
* Exemple de messages Pylint :

```
C0114: Missing module docstring
W0611: Unused import os
E1101: Instance of 'int' has no 'append' member
```

* `C` → convention
* `W` → warning
* `E` → erreur

---

## 5. Configurer Pylint pour ton projet

* Crée un fichier `.pylintrc` à la racine du projet :

```ini
[MESSAGES CONTROL]
disable=C0114, C0115  # ignore les docstrings

[FORMAT]
max-line-length=100
```

* Permet d’adapter les règles à ton projet et ton équipe

---

## 6. Bonus : Intégration CI/CD

* Pylint peut être exécuté dans GitHub Actions pour **bloquer le code non conforme** :

```yaml
- name: Run Pylint
  run: |
    pip install pylint
    pylint my_project/
```

> Résultat : code propre, uniforme et analysé automatiquement
