# On Utilise l'image de base Python 3
FROM python:3

# On Définit le répertoire de travail dans le conteneur
WORKDIR /login

# La Copie les fichiers de notre application dans le conteneur
COPY . .

# On installe les dépendances Python à partir de requirements.txt
RUN apt install pkg-config
RUN pip3 install --no-cache-dir -r requirements.txt


# On Expose le port sur lequel notre application Flask écoute
EXPOSE 5001

# Commande pour démarrer l'application Flask lorsque le conteneur est exécuté
CMD ["python3", "login.py"]
