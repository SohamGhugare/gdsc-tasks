import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from os import getenv
from typing import Optional
from utils import Utils


class Reminder(commands.Cog):
    """
        REMINDER COG
        Contains all the commands and listeners related to the Reminder feature.
    """
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.utils = Utils()
    
    # Creating a subclass group
    reminder = SlashCommandGroup(
        name="reminder",
        description="Follow up with work!"
    )
    
    @reminder.command()
    async def add(self, ctx: discord.ApplicationContext, title: str, time: str, description: Optional[str]=None, date: str = None):
        """
            COMMAND: add
            ARGUMENTS: 
                - title (str)
                - description (OPTIONAL str)
            Takes in a title and description and creates a model 
        """
        rem_time = self.utils.parse_time(time, date)
        await ctx.respond(f"Successfully added {title} for {rem_time.time()} {rem_time.date()}")
    

def setup(bot):
    bot.add_cog(Reminder(bot))