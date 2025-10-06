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

![w:600](https://upload.wikimedia.org/wikipedia/commons/3/38/Jupyter_logo.svg)

---

#  cas de problème

Alternative en ligne sans installation :

[Google Colab](https://colab.research.google.com)

![w:600](https://colab.research.google.com/img/colab_favicon_256px.png)

---

#  Installer Docker Desktop

Téléchargez et installez Docker Desktop :

👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Assurez-vous qu’il fonctionne avant de continuer.

![w:600](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)

---

# ⚙️ Docker Compose

**Docker Compose** permet de lancer plusieurs services ensemble.
Nous allons déployer :

* Jupyter Notebook
* PostgreSQL

Les deux seront connectés automatiquement.

![w:700](https://docs.docker.com/assets/images/compose-diagram.webp)

---

# docker-compose.yml

```yaml
services:
  jupyter:
    image: jupyter/base-notebook:latest
    environment:
      JUPYTER_ENABLE_LAB: "yes"
      GRANT_SUDO: "yes"
      PYTHONPATH: "/home/jovyan/work/src"
    user: root
    ports:
      - "8880:8888"
    volumes:
      - ./project:/home/jovyan/work
      - ./project/kaggle.json:/home/jovyan/.config/kaggle/kaggle.json
    command: >
      bash -c "
      chown jovyan /home/jovyan/.config/kaggle/kaggle.json &&
      chmod 600 /home/jovyan/.config/kaggle/kaggle.json &&
      pip install -r /home/jovyan/work/config/requirements.txt &&
      start-notebook.sh --NotebookApp.token='' --NotebookApp.password=''"
    restart: always
    depends_on:
      postgres:
        condition: service_healthy

  postgres:
    image: postgres:latest
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: students
    ports:
      - "5432:5432"
    volumes:
      - ./pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user"]
      interval: 10s
      timeout: 5s
      retries: 5
    restart: always
```

---

# ▶️ Lancer les conteneurs

```bash
docker compose up -d
```

👉 Ouvrez ensuite Jupyter sur [http://localhost:8880](http://localhost:8880)

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
