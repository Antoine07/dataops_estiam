---
marp: true
theme: default
paginate: true
size: 16:9
---

# Stacks

*Lisez bien tout pour choisir une méthode d'installation*

1. **Télécharger Python**
2. **Environnement virtuel**
3. **Jupyter & JupyterLab**
4. **Alternative : Google Colab**
5. **Approche Docker & Docker Compose**
6. **Lancement des conteneurs**
7. **Vérification du setup**
8. **Panorama des outils DataOps**
9. **Résumé & lien vers le cours**

---

# DataOps — Cours

Cours complet :  
[https://antoine07.github.io/dataops_estiam/](https://antoine07.github.io/dataops_estiam/)

---

# Télécharger Python

Téléchargez la dernière version :  
[python.org/downloads](https://www.python.org/downloads/)

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


#  Approche Docker 

Pour aller plus loin, vous pouvez installer Docker Compose afin de faciliter le déploiement et la scalabilité.

Téléchargez et installez Docker Desktop :

👉 [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)

Assurez-vous qu’il fonctionne avant de continuer.

![w:150](https://www.docker.com/wp-content/uploads/2022/03/Moby-logo.png)

---

#  Docker Compose

**Docker Compose** permet de lancer plusieurs services ensemble.
Nous allons déployer :

- Jupyter Notebook
- PostgreSQL

Les deux seront connectés automatiquement, voir le docker compose

---

# Fichier d'exemple docker compose

Récupérez le fichier source [docker compose](./docker-compose.yaml)

- Créez les dossiers suivants : **project** et **pgdata**

---

# ▶️ Lancer les conteneurs

```bash
docker compose up -d
```

Ouvrez ensuite Jupyter sur [http://localhost:8880](http://localhost:8880)

---

# Vérifier les conteneurs

```bash
docker ps
```

Vous devriez voir :

* `jupyter` → running ✅
* `postgres` → healthy 🟢

---


#  En cas de problème d'installation 

![w:100](https://colab.research.google.com/img/colab_favicon_256px.png)

Alternative en ligne sans installation Colab :

[Google Colab](https://colab.research.google.com)


