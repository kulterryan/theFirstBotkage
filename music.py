#importing libraries

import discord
from discord.ext import commands
import os # for importing token

client = commands.bot(command_prefix="$") # setting prefix for bot

# creating play command
@create.command()
async def play(ctx, url:str): # for entering url
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General') # to access voice channel data
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild) # voice client
    await voiceChannel.connect()

client.run(os.getenv('TOKEN')) # accessing Discord Bot