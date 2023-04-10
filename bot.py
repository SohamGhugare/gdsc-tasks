import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv('.env')

token = os.getenv('TOKEN')
owner_ids = [884026947699634197]

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all(), owner_ids=owner_ids)

cogs = ["core"]

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
        await ctx.send(f"Successfully reloaded `{ext}`")
    else:
        await ctx.send("Cog not found")

bot.run(token)