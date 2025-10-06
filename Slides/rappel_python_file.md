---
marp: true
theme: default
paginate: true
---

# Fichiers en Python  
## Lecture et écriture rapide

---

## Ouvrir un fichier

```python
# Ouvrir en lecture
f = open("exemple.txt", "r")
contenu = f.read()
print(contenu)
f.close()
````

* `"r"` : lecture
* `"w"` : écriture (écrase le fichier)
* `"a"` : ajout (append)
* Toujours **fermer** le fichier après utilisation avec `f.close()`

---

## Utiliser le contexte `with`

```python
with open("exemple.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

* Le fichier est **automatiquement fermé** à la fin du bloc
* Pratique et **plus sûr**

---

## Écriture dans un fichier

```python
with open("exemple.txt", "w") as f:
    f.write("Bonjour le monde!\n")
    f.write("Une deuxième ligne.")
```

* Chaque appel à `write()` ajoute du texte
* `"w"` écrase, `"a"` ajoute à la fin

---

## Lecture ligne par ligne

```python
with open("exemple.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())  # supprime \n
```

* Utile pour les fichiers volumineux
* Évite de charger tout le fichier en mémoire

---

## TP 

## Contexte

Vous pouvez vous mettre dans votre équipe pour réaliser cet exercice.

Vous travaillez pour une librairie en ligne.  
Un fichier CSV de commandes vous est transmis : **incomplet, mal formaté et contenant des doublons**.

Votre mission :
- Nettoyer les données brutes
- Construire un modèle objet cohérent
- Hydrater ce modèle à partir des données nettoyées
- Produire une analyse et des exports finaux

---

### Fichier d'entrée

`raw_orders.csv`  
Contient les colonnes :  
`order_id, customer_name, customer_email, product, quantity, price, date`

---

# Étape 1 — Nettoyage & Structuration

### Nettoyage des données
1. Corrigez les formats incohérents :
   - Prix (`price`) : gérer virgules, symboles € ou $, chaînes  
   - Dates (`date`) : uniformiser tous les formats (`YYYY-MM-DD`)  
   - Emails : valider ou recréer un email temporaire si manquant  
   - Quantités (`quantity`) : convertir en entiers, supprimer les zéros ou négatifs  
2. Supprimez les doublons par `order_id` (gardez la première entrée valide).  
3. Logguez les erreurs et lignes rejetées dans un fichier `errors.log`.

### Questions
- Quelles fonctions de nettoyage allez-vous créer ?  
- Comment gérez-vous les champs manquants sans interrompre le script ?  
- Comment consignez-vous les erreurs pour les auditer ensuite ?

---

### Fichier d'entrée (extrait `raw_orders.csv`)

```
order_id,customer_name,customer_email,product,quantity,price,date
1,Alice,alice@mail.com,Book A,2,12,50,2024/06/10
2,Bob,bob@mail.com,Book B,1,15.0,10-06-2024
3,Charlie, ,book C,1,€20.00,2024.06.12
4,alice ,ALICE@MAIL.COM,Book A,2,12.50,2024/06/10
5,Denis,denis@mail,Book D,0,8.00,2024/06/15
6,Eve,eve@mail.com,Book E,1,"13,5",15/06/2024
2,Bob,bob@mail.com,Book B,1,15.0,10-06-2024
```

--- 

# Étape 2 — Hydratation, Analyse et Export

### Hydratation
1. Définissez des classes :  
   - `Customer`, `OrderItem`, `Order`  
   - Ajoutez une méthode de classe `from_dict()` pour créer un objet depuis un dictionnaire.  
2. Lisez les données nettoyées et **hydratez** vos objets.

### Analyse
- Calculez :
  - Le chiffre d'affaires total
  - Le nombre de clients uniques
  - Le top des produits les plus vendus  
- Exportez :
  - Les données nettoyées en `cleaned_orders.json`
  - Les analyses en `report.csv`
  - Les erreurs dans `errors.log`


### Questions

- Comment organiser le code pour séparer nettoyage, hydratation et analyse ?  
- Quels formats de sortie facilitent la réutilisation des données ?  
- Quelles limites rencontrez-vous avec cette approche objet ?
