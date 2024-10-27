import discord

import asyncio

from rasa.core.agent import Agent
 
# Charger le modèle Rasa

agent = Agent.load("C:/Users/hamza benzy/Desktop/ChatBot/models/20241027-175435-free-jaguar.tar.gz")
 
# Initialisation du client Discord avec les intents pour lire les messages

intents = discord.Intents.default()

intents.message_content = True  # Activer la lecture des messages pour que le bot puisse les traiter

client = discord.Client(intents=intents)
 
@client.event

async def on_ready():

    print(f'Bot connecté en tant que {client.user}')
 
@client.event

async def on_message(message):

    # Affiche le message reçu dans la console pour confirmer la réception

    print(f"Message reçu de {message.author}: {message.content}")

    # Éviter de traiter les messages envoyés par le bot lui-même

    if message.author == client.user:

        return
 
    # Envoi du message utilisateur à Rasa pour obtenir une réponse

    response = await agent.handle_text(message.content)

    # Si une réponse est reçue de Rasa, elle est renvoyée sur Discord

    if response:

        print(f"Réponse de Rasa : {response[0].get('text')}")

        await message.channel.send(response[0].get("text"))
 
# Démarrer le bot avec le token

client.run("MTI5OTAzNDIxMDU5NzYwMTMyMA.GR8bQA.2KBexZCtndNviFk2ITDz_z9JDb-OGSsCnawl0g")

 