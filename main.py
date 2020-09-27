# ---------------------------MODULES------------------------------------------->
import discord
from discord.ext import commands

# from on_cmds import nm_
from on_cmds import say_
from on_cmds import run_
from on_cmds import form_
from on_cmds import vote_
from on_cmds import help_
from on_cmds import forms_
from on_cmds import clear_

from on_init import init_
# from on_auth import join_
# ---------------------------MODULES------------------------------------------->

bot = commands.Bot(command_prefix='.') #define command decorator

# ---------------------------INTERFACES---------------------------------------->
@bot.command()
async def h(ctx):
	await help_(ctx)

"""
@bot.command()
async def nm(ctx, *args):
	await nm_(ctx, args)
"""

@bot.command()
async def say(ctx, *args):
	await say_(ctx, args)

@bot.command()
async def forms(ctx, *args):
	await forms_(ctx)

@bot.command()
async def form(ctx, type):
	await form_(ctx, type)

@bot.command()
async def run(ctx, *args):
	await run_(ctx, args)

@bot.command()
async def vote(ctx, *args):
	await vote_(ctx, args)

@bot.command()
async def clear(ctx, *args):
	await clear_(ctx, args)

@bot.event
async def on_ready():
	await init_(bot)

"""
@bot.event
async def on_member_join(member):
	await join_(member, bot)
"""
# ---------------------------INTERFACES---------------------------------------->

bot.run("")
