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

config = ConfigParser()
config.read('config.ini')
TOKEN = config.get('bot_config', 'TOKEN')
GUILD = config.get('server_config', 'GUILD_ID')
WCI = config.get('server_config', 'WELCOME_CHANNEL_ID')
RCI = config.get('server_config', 'RULES_CHANNEL_ID')
GCI = config.get('server_config', 'GENERAL_CHANNEL_ID')
PREFIX = config.get('bot_config', 'COMMANDS_PREFIX')

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