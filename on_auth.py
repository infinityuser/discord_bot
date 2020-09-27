# ------------------------------LIBS------------------------------------------->
import time
import asyncio
import discord
import random
# ------------------------------LIBS------------------------------------------->

# ------------------------------DATA------------------------------------------->
colors = [0x00dfff, 0x00ff59, 0x95ff00, 0xffb700, 0xff1700, 0xff00bd, 0x7000ff, 0x0021ff]

# main channel
front = "welcome"
# ------------------------------DATA------------------------------------------->

# ------------------------------FUNCTIONS-------------------------------------->
async def join_(member, bot):
	time.sleep(0.9)

	# add ambed in wellcome
	for channel in member.guild.channels:
		if channel.name == front:
			emb = discord.Embed(title = "Добро пожаловать, {0}!".format(member.name),
								description = "{0} присоединился к нам\n Введите .nm <имя>".format(member.name),
								color = random.choice(colors))
			emb.set_thumbnail(url = member.avatar_url)
			await channel.send(embed = emb)
# ------------------------------FUNCTIONS-------------------------------------->
