# Utiliser une image de base Python officielle
FROM python:3.8-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY . /app

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port sur lequel l'application s'exécute
EXPOSE 5000

# Définir la commande pour démarrer l'application
CMD ["python", "app.py"]
