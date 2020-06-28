import os, random, datetime
import discord, corona_api

from configparser import ConfigParser
from discord.ext import commands

print('''
████████╗ █████╗ ██╗  ██╗ █████╗ ███████╗██╗  ██╗
╚══██╔══╝██╔══██╗██║  ██║██╔══██╗██╔════╝╚██╗██╔╝
   ██║   ███████║███████║███████║███████╗ ╚███╔╝ 
   ██║   ██╔══██║██╔══██║██╔══██║╚════██║ ██╔██╗ 
   ██║   ██║  ██║██║  ██║██║  ██║███████║██╔╝ ██╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
''')

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = os.environ['DISCORD_GUILD']
WCI = os.environ['WELCOME_CHANNEL_ID']
RCI = os.environ['RULES_CHANNEL_ID']
GCI = os.environ['GENERAL_CHANNEL_ID']
PREFIX = os.environ['COMMAND_PREFIX']

bot = commands.Bot(command_prefix = str(PREFIX))
bot.remove_command('help')

bot.color_code = 0x3333A2
bot.prefix = PREFIX
bot.del_message = {}
bot.org_message = {}
bot.ed_message = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(status = discord.Status.online, activity = discord.Game('w0help'))

# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("Woah! Command not Found!")
#     else:
#         await ctx.send(f'`{error}`')

for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
            try:
                bot.load_extension(f'Cogs.{filename[:-3]}')
            except Exception as e:
                print(f"{filename} can't be loaded")
                raise e

bot.run(TOKEN)
