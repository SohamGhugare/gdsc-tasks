import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    music = SlashCommandGroup(
        name="music",
        description="Music at your fingertips!"
    )

def setup(bot):
    bot.add_cog(Music(bot))