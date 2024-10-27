# Bot discord avec rasa et action server

Ce projet combine un bot Discord, intégré avec un modèle Rasa, pour répondre aux utilisateurs sur un serveur Discord. Rasa est utilisé pour la gestion des intentions et des entités, ainsi que pour déclencher des actions personnalisées via un serveur d'actions.

# Equipe 
BENALIA Hamza
Eryan DELMON

## Fonctionnalités

- **Bot Discord** : Intégration avec Discord pour recevoir des messages et y répondre.
- **Modèle Rasa** : Analyse des intentions et des entités pour interpréter les messages des utilisateurs.
- **Action Server** : Exécution d'actions personnalisées pour gérer des processus spécifiques, comme `action_confirm_reservation`.

## Installation

### Prérequis

- Python 3.8+
- Rasa
- Bibliothèque Discord (`discord.py`)

### Étapes d'installation

1. **Cloner le dépôt**
   ```bash
   git clone https://github.com/HamzaBenalia/ChatBot
   ```
2. **Entraîner le modèle rasa avant d'utiliser le bot:**
   ```
   rasa train
   ```

3. **Une fois l'entraînement terminé, copiez le chemin d'accès au modèle généré, par exemple** : models/20241027-161421-animato-geyser.tar.gz.

Configurer le chemin du modèle dans rest.py Dans le fichier rest.py, remplacez le chemin du modèle par celui copié lors de l’étape précédente pour que le bot puisse se connecter au modèle.

4. **Configurer l'Action Server dans endpoints.yml Assurez-vous que l’URL de l’Action Server dans endpoints.yml est correcte** :

   ```bash
   action_endpoint:
   url: "http://localhost:5056/webhook"
   ```
5. **Ajouter votre token Discord Remplacez 'YOUR_TOKEN_HERE' dans rest.py avec le token de votre bot Discord**.

 ## Démarrage
 
**Lancer le serveur Rasa avec l'API activée**

```bash
rasa run --enable-api
```
```bash
Démarrer le serveur d'actions Dans un autre terminal, lancez le serveur d'actions pour gérer les actions personnalisées :
rasa run actions
```
```bash
Démarrer l'interface REST Dans un nouveau terminal, exécutez le fichier rest.py pour que le bot puisse se connecter au modèle Rasa :
python rest.py
```

# Tester le bot
Une fois que le bot est en cours d'exécution, vous pouvez envoyer des messages au bot dans Discord pour tester ses réponses. Le message sera traité par Rasa et le bot répondra en fonction des 
intentions détectées.


# Photos
![Description de l'image](https://github.com/HamzaBenalia/ChatBot/blob/master/Images/Discord.png)
![Description de l'image](https://github.com/HamzaBenalia/ChatBot/blob/master/Images/console.png)

# Remarque 
Il faut avoir un serveur et un token Discord au préalable pour pouvoir le connecter à Rasa. Il existe de nombreux tutoriels en ligne pour vous guider dans cette étape.

# Contribution
Les contributions sont les bienvenues ! Pour toute suggestion ou correction, merci de soumettre une pull request.
