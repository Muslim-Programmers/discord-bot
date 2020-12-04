import discord
import random
import json
import asyncio
import os
import emoji
from discord.ext import commands
from discord.utils import get
#filter outdated & and new filter
class EventsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_member_join(self, member):
        for channel in member.guild.channels:
            if str(channel) == "welcome":
                embed = discord.Embed(color=0x4a3d9a)
                embed.add_field(name="Welcome", value=f"{member.name} has joined {member.guild.name}", inline=False)
                embed.set_image(url="https://cdn.discordapp.com/attachments/783714830560395304/784122149987287090/esselemualeykumverahmetullah-651.png")
                await channel.send(embed=embed)


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
