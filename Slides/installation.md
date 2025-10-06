---
marp: true
theme: default
paginate: true
size: 16:9
---

# DataOps — Installation des outils

Cours complet :  
[https://antoine07.github.io/dataops_estiam/](https://antoine07.github.io/dataops_estiam/)

---

# Installer Python

Téléchargez la dernière version :  
👉 [python.org/downloads](https://www.python.org/downloads/)

![w:600](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)

---

#  Créer un environnement virtuel

```bash
python -m venv env_dataops
````

Activez-le selon votre système :

**Windows**

```bash
env_dataops\Scripts\activate
```

**Mac / Linux**

```bash
source env_dataops/bin/activate
```

---

# Installer Jupyter et JupyterLab

![w:100](https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg)

```bash
pip install --upgrade pip
pip install notebook jupyterlab
```

Lancez JupyterLab :

```bash
jupyter lab
```

Pour sortir :

```bash
deactivate
```



---

#  En cas de problème d'installation 

![w:200](https://colab.research.google.com/img/colab_favicon_256px.png)

Alternative en ligne sans installation Colab :

[Google Colab](https://colab.research.google.com)



---

#  Approche Docker 

Pour aller plus loin, vous pouvez installer Docker Compose afin de faciliter le déploiement et la scalabilité.

Téléchargez et installez Docker Desktop :

👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Assurez-vous qu’il fonctionne avant de continuer.

![w:300](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)

---

#  Docker Compose

**Docker Compose** permet de lancer plusieurs services ensemble.
Nous allons déployer :

* Jupyter Notebook
* PostgreSQL

Les deux seront connectés automatiquement.

![w:300](https://docs.docker.com/assets/images/compose-diagram.webp)

---

# docker-compose.yml

Récupérez le fichier source [docker compose](./docker-compose.yaml)

- Créez les dossiers suivants 

    - project
    - pgdata

---

# ▶️ Lancer les conteneurs

```bash
docker compose up -d
```

Ouvrez ensuite Jupyter sur [http://localhost:8880](http://localhost:8880)

---

# 🔍 Vérifier les conteneurs

```bash
docker ps
```

Vous devriez voir :

* `jupyter` → running ✅
* `postgres` → healthy 🟢

---

# 📚 Outils utilisés

| Catégorie      | Outils                                     | Images                                                                                    |
| -------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Ingestion      | Pandas, SQLAlchemy, Requests, Kafka-python | ![w:120](https://pandas.pydata.org/static/img/pandas_mark.svg)                            |
| Orchestration  | Airflow, Prefect, Dagster                  | ![w:120](https://airflow.apache.org/images/airflow_logo.png)                              |
| Transformation | Pandas, Polars, dbt, PySpark               | ![w:120](https://www.getdbt.com/ui/img/logos/dbt-logo.svg)                                |
| Qualité        | Great Expectations, Pandera                | ![w:120](https://great-expectations-web-assets.s3.us-east-2.amazonaws.com/logo-long.png)  |
| Visualisation  | Matplotlib, Plotly, Streamlit, Dash        | ![w:120](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png) |

---

# Résumé

Vous avez maintenant :
✅ Python + Jupyter
✅ Docker + PostgreSQL
✅ Les outils pour pratiquer le DataOps

Suivez le cours ici :
👉 [https://antoine07.github.io/dataops_estiam/](https://antoine07.github.io/dataops_estiam/)

```

---
