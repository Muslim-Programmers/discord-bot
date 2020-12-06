import random

import discord

from discord.ext import commands


class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slots(self, ctx):
        """!slots - Play fruit emojis slot machine."""
        icon_url = 'https://i.imgur.com/8oGuoyq.png'
        slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        slot_spin = f'|\t:{slot1}:\t|\t:{slot2}:\t|\t:{slot3}:\t|\t:{slot4}:\t|'
        jackpot = '$$$ !!! JACKPOT !!! $$$'

        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_author(name='Slot Machine', icon_url=icon_url)
        embed.add_field(
            name=f'*{ctx.author.name} pulls the slot machine handle...*',
            value='\u200b',
            inline=False,
            
        )


        if (
            slot1 == slot2 and slot3 == slot4 or
            slot1 == slot3 and slot2 == slot4 or
            slot1 == slot4 and slot2 == slot3
        ):
            embed.add_field(name=slot_spin, value='\u200b')
            embed.set_footer(text=jackpot)
        else:
            embed.add_field(name=slot_spin, value='\u200b')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Slots(bot))

