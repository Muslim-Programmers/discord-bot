import discord
import random
import json
import asyncio
import os
import emoji
import requests
import shutil
from discord.ext import commands
from discord.utils import get
from PIL import Image,ImageFont,ImageDraw
#filter outdated & and new filter
class EventsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "welcome":

                avatar = member.avatar_url_as(static_format='jpg', size=1024)
                response = requests.get(avatar,stream=True)
                file = open("assets/user.jpg","wb")
                response.raw_decode_content = True
                shutil.copyfileobj(response.raw,file)
                del response
                bg = Image.open("assets/code.jpg")
                user = Image.open("assets/user.jpg")
                user = user.resize((300,300))
                mask_im = Image.new("L", user.size, 0)
                draw = ImageDraw.Draw(mask_im)
                draw.ellipse((0, 0, 300, 300), fill=255)
                mask_im.save('assets/mask_circle.jpg', quality=100)
                    #(140, 50, 260, 170) fucking circle
                bg.paste(user, (450, 100), mask_im)
                    #bg = Image.open("code.jpg")
                    #user = Image.open("user.jpg")
                font = ImageFont.truetype("assets/BebasNeue.ttf",120)
                text = "Welcome"
                draw = ImageDraw.Draw(bg)
                draw.text((10,80),text,(255,255,255),font=font)
                bg.save('assets/image.jpg')
                await channel.send(file = discord.File("assets/image.jpg"))

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('This command does not exist.')

    @commands.Cog.listener()
    async def filter_message(self, message, ctx):
        filter = ["Curse1", "Curse1", "Curse", "Curse Words/links"]

        for word in filter:
            if message.content.count(word) > 0:
                print("A bad word was said")
                await message.channel.purge(limit=1)
                await ctx.send(f'banned {member.mention}, do not swear')

            elif message.content.count(word) > 0:
                await member.kick
                await ctx.send(f'banned {member.mention}, we told you so')

    @commands.Cog.listener()
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        permission = argument.guild_permissions.manage_messages


    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload=None):
        msgID = 783797861190991893 #message id
        guild = discord.utils.get(self.bot.guilds, name="Muslim Programmers") #guild name here
        role = discord.utils.get(guild.roles, name='Brother') #group role name
        if payload is not None:
            if payload.message_id == msgID:
                if str(payload.emoji) == "✅": #add raw emoji
                    await payload.member.add_roles(role)

def setup(bot):
    bot.add_cog(EventsCog(bot))
