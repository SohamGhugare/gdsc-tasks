import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup
from os import getenv
from typing import Optional

from utils import Utils
from models import Reminder
from db import Database
from exceptions import InvalidDateTimeFormat

class ReminderCog(commands.Cog):
    """
        REMINDER COG
        Contains all the commands and listeners related to the Reminder feature.
    """
    def __init__(self, bot):
        self.bot: commands.Bot = bot
        self.utils = Utils()
        self.db = Database()
    
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
        try:
            rem_time = self.utils.parse_time(time, date)
        except InvalidDateTimeFormat as e:
            return await ctx.respond(e.message)

        rem = Reminder(
            title=title,
            description=description,
            author_id=ctx.author.id,
            time=rem_time
        )
        idx = self.db.add_reminder(rem)
        await ctx.respond(f":white_check_mark: Successfully added Reminder #{idx}")

    @reminder.command()
    async def list(self, ctx: discord.ApplicationContext):
        """
            COMMAND list
            Lists all the reminders of the user
        """
        rems = ""
        for rem in self.db.fetch_user_reminders(ctx.author.id):
            rems+=f"**ID:** {rem.id} \n**Title:** {rem.title} \n**Description:** {rem.description} \n**Time:** {rem.time.time().strftime('%H:%M')} {rem.time.date()}\n\n"
        await ctx.respond(rems)

def setup(bot):
    bot.add_cog(ReminderCog(bot))