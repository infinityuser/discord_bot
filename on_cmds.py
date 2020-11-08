import os
import time
import random
import asyncio

import discord
from discord.utils import get

colour = 0xffb700

foAble = ["cpp", "c", "py", "sh", "css", "html", "txt"]
exAble = ["cpp", "c", "py", "sh"]

hashForm = { "cpp" : "c++", "c" : "c", "py" : "py", "css" : "css", "html" : "html", "txt" : "txt" }
hashExec = { "py" : "python3 ./tmp/tmpfile.py",
             "bash" : "bash ./tmp/tmpfile.sh",
             "c" : "gcc -o ./tmp/debug_c ./tmp/tmpfile.c; sleep 0.2; timeout 2s ./tmp/debug_c ",
             "cpp" : "g++ -o ./tmp/debug_cpp ./tmp/tmpfile.cpp; sleep 0.2; timeout 2s ./tmp/debug_cpp ", }

async def say_(ctx, args):
    temp_mes = ""
    for i in args:
        temp_mes += i + " "
    await ctx.send(temp_mes)

async def supp_(ctx, args):
    out = "To send!"
    out += "```+ " + "\n+ ".join(foAble) + "```"
    await ctx.send(out)
    
    out = "To execute!"
    out += "```+ " + "\n+ ".join(exAble) + "```"
    await ctx.send(out)

async def help_(ctx):
    emb = discord.Embed(title = "Help", description = "Here's commands: ", color = colour)
    emb.add_field(name = ".h", value = "Reference", inline = False)
    emb.add_field(name = ".say", value = "Echo something", inline = False)
    emb.add_field(name = ".supported", value = "Supported file formats", inline = False)
    emb.add_field(name = ".form {format} + doc", value = "Format file's source in message", inline = False)
    emb.add_field(name = ".run {format} {input arguments} + doc", value = "Debug the source", inline = False)
    await ctx.send(embed = emb)

async def form_(ctx, type):
    try:
        if type in foAble:
            try:
                await ctx.message.attachments[0].save("./tmp/tmpfile." + type)
                await ctx.send("`{0.author.nick}` sent `".format(ctx) + ctx.message.attachments[0].filename + "`")
            except:
                await ctx.send("`{0.author.nick}` sent `previous file`".format(ctx))
            
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
            await ctx.send("`//:bad request` - Whoa! Unsupported file format...")
    except:
        await ctx.send("`//:system fault` - Whoa! Something gets wrong...")
        

async def run_(ctx, args):
    try:
        if len(args) > 0 and args[0] in exAble:
            try:
                await ctx.message.attachments[0].save("./tmp/tmpfile." + args[0])
                await ctx.send("`{0.author.nick}` sent a request with `".format(ctx) + ctx.message.attachments[0].filename + "`")
            except:
                await ctx.send("`{0.author.nick}` sent a request with `previous file`".format(ctx))

            param = " ".join(args[1:]) if len(args) > 1 else " "

            try:
                os.system("rm ./tmp/debug* ")
            except:
                pass
            
            inHandle = open("./tmp/tmpin", "w")
            inHandle.write(param)
            inHandle.close()
          
            code = os.system(hashExec[args[0]] + " <./tmp/tmpin >./tmp/tmpout")
            await ctx.send("Process returned code `{0}`\n".format(code))
            await ctx.send("Output:")
            
            outHandler = open("./tmp/tmpout", "r")
            out = "```\n"

            for line in outHandler:
                out += line;
                if len(out) > 1500:
                    out += "```"
                    await ctx.send(out)
                    out = "```" + type + "\n"

            out += "```"
            await ctx.send(out)

            outHandler.close()
        else:
            await ctx.send("`//:bad request` - Whoa! Incorrect request...")
    except:
        await ctx.send("`//:system fault` - It stuck...")
