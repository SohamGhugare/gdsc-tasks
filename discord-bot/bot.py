import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('.env')

token = os.getenv('TOKEN')
owner_ids = [884026947699634197]

bot = discord.Bot(owner_ids=owner_ids)

cogs = ["core", "reminders", "music"]

for cog in list(cogs):
    try:
        bot.load_extension(f"cogs.{cog}")
        print(f"Successfully loaded {cog}")
    except Exception as e:
        print(e)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
@commands.is_owner()
async def load(ctx, ext):
    if ext in cogs:
        bot.load_extension(f"cogs.{ext}")
        await ctx.send(f"Successfully loaded `{ext}`")
    else:
        await ctx.send(f"Cog not found")

@bot.command()
@commands.is_owner()
async def reload(ctx, ext):
    if ext in cogs:
        bot.unload_extension(f"cogs.{ext}")
        bot.load_extension(f"cogs.{ext}")
        await ctx.respond(f"Successfully reloaded `{ext}`")
    else:
        await ctx.respond("Cog not found")

bot.run(token)