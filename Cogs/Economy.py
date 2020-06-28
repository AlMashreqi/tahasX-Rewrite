import discord, asyncio
import sqlite3
from discord.ext import commands

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # db = sqlite3.connect('./Cogs/Database/levels_eco.sqlite')
        # cursor = db.cursor()
        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS economy(
        #     AUTHOR_ID TEXT,
        #     USER_CREDITS TEXT
        # )
        # ''')

    

def setup(bot):
    bot.add_cog(Economy(bot))