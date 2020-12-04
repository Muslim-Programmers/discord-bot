import asyncio
import random
from asyncio import queues
import discord
import youtube_dl
import json
import shutil
import os
from discord.ext import commands
from discord.utils import get
global mm





client = commands.Bot(command_prefix = '!')
client.remove_command('help')
client.fetch_offline_members = True


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('/help'))
    print('bot is ready')




extensions = ['Cogs.Music','Cogs.administrator', 'Cogs.events','Cogs.misc commands','Cogs.Activity','Cogs.Help','Cogs.random','Cogs.quran','Cogs.hadith','Cogs.hijricalendar','Cogs.mushaf','Cogs.dua','Cogs.tafsir','Cogs.tafsir-english','Cogs.prayertimes']

if __name__ == '__main__':
    for extension in extensions:
        client.load_extension(extension)


# 'Cogs.Music',





client.run('NjU0MjQ4MzAxNDY5ODkyNjIx.XfCyNg.aYKZFaD2AhvxoGhISPB50nnSrLw')
