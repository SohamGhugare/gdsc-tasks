import discord
from discord.ext import commands
from os import getenv

class Core(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    

    

def setup(bot):
    bot.add_cog(Core(bot))