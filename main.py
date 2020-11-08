import discord
from discord.ext import commands

from on_cmds import say_
from on_cmds import run_
from on_cmds import form_
from on_cmds import supp_
from on_cmds import help_

from on_init import init_

bot = commands.Bot(command_prefix='.') 

@bot.command()
async def h(ctx):
    await help_(ctx)

@bot.command()
async def say(ctx, *args):
    await say_(ctx, args)

@bot.command()
async def supported(ctx, *args):
    await supp_(ctx, args)

@bot.command()
async def form(ctx, type):
    await form_(ctx, type)

@bot.command()
async def run(ctx, *args):
    await run_(ctx, args)

@bot.event
async def on_ready():
    await init_(bot)

bot.run("")
