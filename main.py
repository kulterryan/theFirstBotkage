# FreeCodeCamp
# Source: https://www.youtube.com/watch?v=SPTfmiYiuok

# importing libraries

from operator import index
import discord # library of Discord.Py
import os # for importing token
import requests # for making HTTP Requests for API
import json # for JSON encoding
import random # for choosing random messages
from replit import db # using replit data & importing

client = discord.Client() # defining Discord Bot

# creating new key value pair in database
if "responding" not in db.keys():
    db["responding"] = True

# defining get_quote function for Quotes
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    print(json_data)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

# defining get_sad_words list function for Messages
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "Hey! You know what, You're great, cheer up and f**k the world."
]

# adding additional encouragements
def update_encouragements(encouraging_message): 
    if "encouragements" in db.keys(): # storing messages in database
        encouragements = db["encouragements"]
        encouragements.appen(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

# deleting an encouragement message
def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index :
        del encouragements[index] # deleting from index
    db["encouragements"] #saving back to database

@client.event # When user logged in Discord Server
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

###    
#@client.event # When user send messages on Discord Server
#async def on_message1(message):
#    if message.author == client.user:
#        return
###

# returning ZenQuotes.io API for Inspirational Quotes
@client.event # When user send messages on Discord Server
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content # short substitution

    if msg.startswith('$hello'):
        await message.channel.send('Hello!') # Sending msg as Reponse

    if msg.startswith('$inspire'): # inspiring msg
        quote=get_quote()
        await message.channel.send(quote) # Sending msg as Response

    if db["responding"]:
        options = starter_encouragements
        if "encouragements" in db.keys():
            options = options + db["encouragements"]

    if any(word in msg for word in sad_words):     # responding on user's msg with sad words
        await message.channel.send(random.choice(options))

    if msg.startswith("$new"): # adding new message by user
        encouraging_message = msg.split("$new", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added to database.")

    if msg.startswith("$del"): # deleting encouragements added by user
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement(index)
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$list"): # listing encouraging messages
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$responding"): # responding to user
        value = msg.split("$responding ", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("Responding is on.")
        else:
            db["responding"] = False
            await message.channel.send("Responding is on.")

client.run(os.getenv('TOKEN')) # accessing Discord Bot