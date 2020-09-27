# ---------------------------------LIBS---------------------------------------->
import asyncio
import discord
import time
# ---------------------------------LIBS---------------------------------------->

# ---------------------------------FUNCTIONS----------------------------------->
async def init_(bot):
	print("Logged in as")
	print(bot.user.name)
	print(bot.user.id)
	print("------------")
	await bot.change_presence(status = discord.Status.online, activity = discord.Game(".h -> cmds"))
# ---------------------------------FUNCTIONS----------------------------------->
