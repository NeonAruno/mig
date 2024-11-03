# Utilise une image Python légère
FROM python:3.9-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie le fichier requirements.txt et installe les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le reste du code du bot
COPY . .

# Expose le port 8080 pour le health check
EXPOSE 8080

# Lance le serveur Flask et le bot en mode polling
CMD ["python", "bot.py"]

