import discord
import requests
import shutil
from discord.ext import commands
from PIL import Image,ImageFont,ImageDraw

class event(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    

def setup(bot):
    bot.add_cog(event(bot))
