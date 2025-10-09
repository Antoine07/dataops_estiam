
###  Fichier source : `students_raw.csv`

```csv
first_name,last_name,gender,math_score,reading_score,writing_score
Alice,Smith,F,85,88,92
bob,johnson,M,78,82,79
Charlie,,M,90,,85
diana,Lee,F,abc,91,87
Evan,White,M,70,68,72
Fay,King,F,95,89,94
George,Brown,M,60,58,65
Hannah,Davis,F,88,90,93
ian,Clark,M,82,81,80
Julia,Miller,F,77,80,78
```

Problèmes présents dans ce fichier :

* Nom ou prénom manquant (`Charlie,,M,...`)
* Score non numérique (`diana,Lee,F,abc,91,87`)
* Minuscules pour les prénoms (`bob`, `ian`)
* Valeurs manquantes (`Charlie,,M,90,,85`)

---

### Script ETL : `etl_pipeline.py`

```python
import pandas as pd

# Créez le script ici vous permettant de faire l'ETL
```

---

###  Résultat attendu dans `students_cleaned.csv`

```csv
first_name,last_name,gender,math_score,reading_score,writing_score
Alice,Smith,F,85.0,88.0,92.0
Bob,Johnson,M,78.0,82.0,79.0
Diana,Lee,F,82.11,91.0,87.0
Evan,White,M,70.0,68.0,72.0
Fay,King,F,95.0,89.0,94.0
George,Brown,M,60.0,58.0,65.0
Hannah,Davis,F,88.0,90.0,93.0
Ian,Clark,M,82.0,81.0,80.0
Julia,Miller,F,77.0,80.0,78.0
```
