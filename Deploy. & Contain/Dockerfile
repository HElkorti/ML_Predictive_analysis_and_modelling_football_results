# Utiliser une image Python officielle en tant que base
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les dépendances et installer les packages requis
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code du projet dans le conteneur
COPY . /app/

# Exposer le port sur lequel le serveur Django fonctionne (par défaut 8000)
EXPOSE 8000

# Commande pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
