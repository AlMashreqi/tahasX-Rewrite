import discord
from discord.ext import commands
import re

def setup(bot):
    @bot.event
    async def on_message(message):
        bad_words = [word.strip('\n') for word in open("./Cogs/Database/swear.txt", 'r').readlines()]
        if any(bad_word in message.content.lower() for bad_word in bad_words):
            await message.delete()
            embed = discord.Embed(title = 'User Warned',description = f'{message.author.mention} has been Warned\n**Reason:** Swearing', color = bot.color_code,timestamp = message.created_at)
            embed.set_footer(text = f'© {bot.user.name} | Owned by {message.guild.owner}\n', icon_url = bot.user.avatar_url)
            await message.channel.send(embed = embed)
        else:
            await bot.process_commands(message)        
     
        
