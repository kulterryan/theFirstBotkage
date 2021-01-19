#importing libraries

import discord
from discord.ext import commands
import os # for importing token

client = discord.Client() # defining Discord Bot

@client.event # When user logged in Discord Server
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Getting Started
@client.command() # When user send messages on Discord Server
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content # short substitution

    if msg.startswith('hello'):
        await message.channel.send("Hello! This is BotKage: The Ninja Bot.\nBuilt by github.com/kulterryan") # Sending msg as Reponse

client.run(os.getenv('TOKEN')) # accessing Discord Bot