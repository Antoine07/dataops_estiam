---
marp: true
theme: default
paginate: true
size: 16:9
---

# NumPy — Introduction

- Bibliothèque principale pour le **calcul scientifique en Python**
- Structures de données efficaces pour **tableaux multidimensionnels (`ndarray`)**
- Fonctions mathématiques **vectorisées**
- Souvent utilisée avec **Pandas**, **scikit-learn**, **Matplotlib**


---


# Installation

```bash
pip install numpy
````

---

# Création de tableaux

### À partir de listes Python
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
````

### Tableaux multidimensionnels

```python
matrix = np.array([[1, 2], [3, 4]])
```

### Tableaux spéciaux

```python
np.zeros((2,3))
np.ones((3,3))
np.arange(0,10,2)
np.linspace(0,1,5)
```

---

# Propriétés d’un tableau

```python
arr.shape    # Dimensions
arr.ndim     # Nombre de dimensions
arr.size     # Nombre total d’éléments
arr.dtype    # Type des éléments

```

---

# Opérations vectorisées

```python
a = np.array([1,2,3])
b = np.array([4,5,6])

a + b  # [5,7,9]
a * b  # [4,10,18]
a ** 2 # [1,4,9]
```

* Très rapide pour **grandes séries de données**

---

# Statistiques de base

```python
np.mean(arr)
np.median(arr)
np.std(arr)
np.max(arr)
np.min(arr)
```

---

# Indexation et slicing

```python
arr = np.array([10,20,30,40,50])
arr[0]      # premier élément
arr[-1]     # dernier élément
arr[1:4]    # éléments 1 à 3
arr[arr > 20] # filtrage conditionnel
```

---

# Intégration avec Pandas

```python
import pandas as pd
df = pd.DataFrame({
    "quantity": [2,3,1],
    "price": [10.0,15.0,20.0]
})

df["total"] = df["quantity"].values * df["price"].values
```

* Les **opérations vectorisées** NumPy sont plus rapides que les boucles Python


---

# Fonctions utiles

| Fonction        | Utilité |
|-----------------|---------|
| np.sum(arr)     | Somme des éléments |
| np.cumsum(arr)  | Somme cumulative |
| np.prod(arr)    | Produit des éléments |
| np.sort(arr)    | Trier le tableau |
| np.unique(arr)  | Valeurs uniques |

---

# Résumé

- NumPy = moteur mathématique derrière Pandas
- Permet de **calculer, filtrer et générer des statistiques** efficacement
- Idéal pour manipuler de **grandes quantités de données**

---

# Exercice 

Températures au mois de janvier 

```python
january = np.array([-2,  5, -5,  6, -2,  0,  6,  2,  8,  0,  6, -1,  3,  3,  7,  0, -5,
        7,  4,  7,  8, -1,  5, -2,  3, -3, -2,  7,  8,  4,  2], dtype='float64')
```

1. Donnez toutes les températures qui sont supérieures à 0.
2. Comparez les températures supérieures et inférieures à 0.
3. Donnez le pourcentage des températures positives sur le mois
4. Créez un tableau days pour les jours du mois et donnez les jours pour lesquels la température était supérieure à 0.

--- 

# Deux questions pour finir 

5. Donnez toutes les températures supérieures à 0 
à partir du dixième jour du mois.

6. Remplacez maintenant les températures négatives par 
la moyenne ou la médiane des températures positives.

---

## **1. Remplace les nombres négatifs**

**Consigne :**

```python
import numpy as np
a = np.array([-3, 5, -1, 7, -9, 2])
```

Remplace toutes les valeurs négatives par 0, et affiche le nouveau tableau.

---

## **2. Trouve les indices des nombres pairs**

**Consigne :**

```python
b = np.array([4, 9, 12, 7, 6, 3, 10])
```

Trouve les indices (positions) des nombres pairs dans le tableau.
Indice : utilise `np.where(condition)`.

---

## **3. Crée un damier (échiquier) de 0 et 1**

**Consigne :**
Crée un tableau 8×8 avec des 0 et 1 alternés comme ceci :

```
[[0 1 0 1 0 1 0 1]
 [1 0 1 0 1 0 1 0]
 [0 1 0 1 0 1 0 1]
 ...]
```

Indice : tu peux utiliser `np.zeros((8,8))` et modifier avec du slicing.

---

## **4. Double les valeurs impaires**

**Consigne :**

```python
c = np.array([1, 2, 3, 4, 5, 6])
```

Multiplie par 2 uniquement les valeurs impaires. Le reste reste inchangé.

---

## **5. Moyenne des températures supérieures à 20°C**

**Consigne :**

```python
temperatures = np.array([18, 22, 25, 19, 30, 15, 24])
```

Calcule la moyenne des températures strictement supérieures à 20°C.

---

## **6. Crée un tableau de 0 à 100, puis filtre**

Crée un tableau de tous les nombres de 0 à 100.

* Garde seulement les multiples de 5.
* Calcule la somme de ces multiples.

---

## **7. Mélange et retrouve la valeur maximale**

**Consigne :**
Crée un tableau de 10 nombres aléatoires entre 0 et 100.

* Mélange l’ordre des éléments.
* Trouve la valeur maximale et son indice.

Indice : `np.random.randint()`, `np.random.shuffle()`, `np.argmax()`.

---

## **8. Normalise un tableau**

**Consigne :**

```python
data = np.array([10, 20, 30, 40, 50])
```

Transforme ce tableau pour que les valeurs soient comprises entre 0 et 1 selon la formule :

$$
x_{norm} = \frac{x - \min(x)}{\max(x) - \min(x)}
$$
