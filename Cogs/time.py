import discord
from discord.ext import commands
import datetime, time

start_time = datetime.datetime.now()

class Time(commands.Cog):
	@commands.command()
	async def time(self, ctx):
		current_time = datetime.datetime.now().strftime('%H:%M:%S')
		embed = discord.Embed(color=0xB2272D)
		embed.add_field(name=':alarm_clock: Time:', value=(f'Current time is: {current_time}'), inline=True)
		await ctx.send(embed=embed)

	@commands.command()
	async def uptime(self, ctx):
		current_time = datetime.datetime.now()
		difference = current_time - start_time
		text = difference.total_seconds() / 3600
		await ctx.send('Current uptime: {:.2f} hours'.format(text))


def setup(bot):
	bot.add_cog(Time())
