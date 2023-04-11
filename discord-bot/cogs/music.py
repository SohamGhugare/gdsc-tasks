import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
import youtube_dl

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    music = SlashCommandGroup(
        name="music",
        description="Music at your fingertips!"
    )

    @music.command()
    async def play(self, ctx: discord.ApplicationContext, url: str):
        """
            COMMAND play
            Plays the song from url
        """

def setup(bot):
    bot.add_cog(Music(bot))