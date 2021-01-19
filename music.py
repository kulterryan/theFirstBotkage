#importing libraries

import discord
from discord.ext import commands
import os # for importing token

# source: https://www.youtube.com/watch?v=ml-5tXRmmFk

client = commands.Bot(command_prefix="!")

# Getting Started
@client.command() # When user send messages on Discord Server

# Playing
async def play(ctx, url : str):
    # Accessing Voice Channel
    voiceChannel = discord.utils.get(ctx.guild.voice_channel, name="General")
    # setup voice client
    voice = discord.utils.get(client.voice_clients, guilds = ctx.guild)
    # join voice channel
    if not voice.is_connected():
        await voiceChannel.connect()

client.run(os.getenv('TOKEN')) # accessing Discord Bot