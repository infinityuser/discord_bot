# ---------------------------------LIBS---------------------------------------->
import os
import time
import random
import asyncio

import discord
from discord.utils import get
# ---------------------------------LIBS---------------------------------------->

# ---------------------------------DATA---------------------------------------->
class vote:
	mems = []
	votech = []
	conditions = []
	args = 0

	def __init__(self, auth, variants, conditions):
		self.mems = [ i.nick for i in auth.author.guild.members ]
		self.votech = [ 0 for i in range(len(self.mems)) ]
		self.args = variants
		self.conditions = conditions

	async def forv_(self, auth, member, condition):
		if condition <= self.args:
			if ind := self.mems.index(member):
				self.votech[ind] = condition
		else:
			await auth.send("`//:bad request` - Pick up correct properties...")

	async def close(self, auth):
		general = 1
		count = 0
		local = 1

		self.votech.sort()
		for i in range(lenght := len(self.votech)):
			if self.votech[i] != self.votech[i - 1]:
				if local > count and self.votech[i - 1] != 0:
					general = self.votech[i - 1]
					count = local
					local = 0
		if local > count and self.votech[len(self.votech) - 1] != 0:
			general = self.votech[len(self.votech) - 1]

		await auth.send("```Голосование завершено...\n{0}```".format(self.conditions[general - 1]))

# data massives
colors = [0x00dfff, 0x00ff59, 0x95ff00, 0xffb700, 0xff1700, 0xff00bd, 0x7000ff, 0x0021ff]

FoAble = ["cpp", "c", "py", "sh", "css", "html", "txt"]
ExAble = ["cpp", "c", "py", "sh"]

hashForm = { "cpp" : "c++", "c" : "c", "py" : "py", "css" : "css", "html" : "html", "txt" : "" }
hashExec = { "py" : "python3 ./tmp/tmpfile ",
			 "bash" : "bash ./tmp/tmpfile ",
			 "c" : "gcc -o ./tmp/tmpfile ./tmp/tmpfile | sleep 0.2 | ./tmp/debug_c ",
			 "cpp" : "g++ -o ./tmp/tmpfile ./tmp/tmpfile | sleep 0.2 |./tmp/debug_cpp ", }

# votes difinition
active_votes = {}

# roles definition
standr = "ranker" # init role
chperm = "ranker" # channel managing
admin = "moder" # administration role
# ----------------------------------DATA--------------------------------------->

# ----------------------------------FUNCTIONS---------------------------------->
async def say_(ctx, args):
	await ctx.message.delete()

	temp_mes = ""
	for i in args:
		temp_mes += i + " "
	await ctx.send(temp_mes)

async def help_(ctx):
	emb = discord.Embed(title = "Help", description = "запрашиваемые комманды : ", color = random.choice(colors))
	emb.add_field(name = ".h", value = "справка", inline = False)
	emb.add_field(name = ".say", value = "эхо функция", inline = False)
	emb.add_field(name = ".nm", value = "инициализация пользователя", inline = False)
	emb.add_field(name = ".forms", value = "поддерживаемые форматы", inline = False)
	emb.add_field(name = ".clear {count}", value = "удаление {count} сообщений из текущего канала", inline = False)
	emb.add_field(name = ".form {format} + doc", value = "форматирование текстового документа", inline = False)
	emb.add_field(name = ".run {format} {args*} + doc", value = "отладка текстового документа", inline = False)
	emb.add_field(name = ".vote help", value = "справка о проведениях голосований", inline = False)
	await ctx.send(embed = emb)

async def forms_(ctx):
	# supported formats printing
	out = "```...Форматирование кода...\n"
	for i in range(len(FoAble)):
		if i % 3 == 0 and i != 0: out += "\n"
		out += FoAble[i] + " "
	out += "\n"

	out += "...Отладка кода...\n"
	for i in range(len(ExAble)):
		if i % 4 == 0 and i != 0: out += "\n"
		out += ExAble[i] + " "
	out += "```"

	await ctx.send(out)

async def nm_(ctx, args):
	await ctx.message.delete()
	# add default roles
	if not get(ctx.author.guild.roles, name = standr) in ctx.author.roles:
		role = get(ctx.author.guild.roles, name = standr)

		await ctx.author.add_roles(role)

		temp_name = ""
		for i in args:
			temp_name += i + " "
		await ctx.author.edit(nick = temp_name)

async def clear_(ctx, coun):
	# deleting all coun part of channel's messages
	if get(ctx.author.guild.roles, name = chperm) in ctx.author.roles:
		try:
			coun = int(coun[0])
		except:
			coun = 100

		async for message in ctx.channel.history(limit = coun):
			await message.delete()

async def form_(ctx, type):
	# formating the sent data into discord
	if type in FoAble and len(ctx.message.attachments) > 0:
		await ctx.message.attachments[0].save("./tmp/tmpfile")

		await ctx.send("`{0.author}` AKA `{0.author.nick}` sent `{1} file` `".format(ctx, type) + ctx.message.attachments[0].filename + "`")
		
		out = "```" + type + "\n"
		handler = open("./tmp/tmpfile", "r")

		for line in handler:
			out += line;
			if len(out) > 1500:
				out += "```"
				await ctx.send(out)
				out = "```" + type + "\n"


		out += "```"

		await ctx.send(out)
	else:
		await ctx.send("`{0.author}` AKA `{0.author.nick}` sent `{1} file`".format(ctx, type) + ctx.message.attachments[0].filename + "`")
		await ctx.send("`//:bad request` - Pick the correct setup...")
	await ctx.message.delete()

async def run_(ctx, args):
	# executing the sent data into discord
	if len(args) > 0 and args[0] in ExAble and len(ctx.message.attachments) > 0:
		await ctx.message.attachments[0].save("./tmp/tmpfile")

		param = ""
		for pr in args[1::]:
			param += pr + " "

		try:
			os.system("rm ./tmp/debug* ")
		except:
			pass

		code = os.system(hashExec[args[0]] + param + " >./tmp/tmpout")

		handler = open("./tmp/tmpout", "r")
		out = "```css\n"

		for line in handler:
			 out += line;

		out += "```"
		handler.close()

		if out == "```css\n```": out = ""

		await ctx.send("`{0.author}` AKA `{0.author.nick}` sent request `".format(ctx) + ctx.message.attachments[0].filename + "`")
		await ctx.send("Process stopped with code `{0}`\n".format(code) + out)
	else:
		await ctx.send("`{0.author}` AKA `{0.author.nick}` sent request `".format(ctx) + ctx.message.attachments[0].filename + "`")
		await ctx.send("`//:bad request` - Pick the correct setup...")
	await ctx.message.delete()

async def vote_(ctx, args):
	# votes functions and properties
	try:
		if args[0] == "n":
			if ctx.author.nick in active_votes:
				await ctx.send("`//:overflow` - Close opened votes...")
			else:
				conditions = []
				for word in args[2::]:
					if word[0] == "|":
						conditions.append(word[1::])
					else:
						conditions[len(conditions) - 1] += word
				if len(conditions) >= int(args[1]):
					active_votes.update( { ctx.author.nick : vote(ctx, int(args[1]), conditions) } )
				else:
					await ctx.send("`//:bad request` - Pick up the correct properties...")
		elif args[0] == "d":
			if ctx.author.nick in active_votes:
				active_votes.pop(ctx.author.nick)
			else:
				await ctx.send("`//:not found` - Vote doesn't exist...")
			await ctx.message.delete()
		elif args[0] == "c":
			if ctx.author.nick in active_votes:
				await active_votes[ctx.author.nick].close(ctx)
				active_votes.pop(ctx.author.nick)
			else:
				await ctx.send("`//:not found` - Vote doesn't exist...")
			await ctx.message.delete()
		elif args[0] == "v":
			choser = ""
			for i in args[2:len(args) - 1]: choser += i + " "
			choser += args[len(args) - 1]

			if choser in active_votes:
				await active_votes[choser].forv_(ctx, ctx.author.nick, int(args[1]))
			else:
				await ctx.send("`//:not found` - Vote doesn't exist...")
		elif args[0] == "help":
			await ctx.send("""
```.vote {function} {properties}\n
...function list...\n
n {кол-во варинтов} - создать новое голосование
Ниже через "|" должны быть представленны варианты

v {вариант} {создатель голосования} - проголосовать
c								   - подвести итоги
d								   - закрыть голосование\n
Каждый участник может иметь по одному активному голосованию за раз.
Участник не может начать новое голосование не закончив прежнее.\n```""")
		else:
			await ctx.send("`//:not found` - Pick up the correct properties...")
	except:
		await ctx.send("`//:bad request` - Pick up the correct properties...")
# --------------------------------FUNCTIONS------------------------------------>
