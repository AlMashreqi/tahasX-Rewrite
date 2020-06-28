import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'help', help = 'Shows the help command')
    async def help(self, ctx, *cog:str):
        if not cog:
            help_embed = discord.Embed(title = 'Help Command', description = '**Categories**\n', color = self.bot.color_code,timestamp = ctx.message.created_at)
            help_embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
            for cog in self.bot.cogs:
                if not (cog == 'Events' or cog == 'Help'):
                    help_embed.add_field(name = f'**{cog}**', value = f'`{self.bot.prefix}help {cog}`')
            await ctx.send(embed = help_embed)
        else:
            found = False
            for x in self.bot.cogs:
                for y in cog:
                    if x == y:
                        halp=discord.Embed(title=cog[0]+' Commands',description=self.bot.cogs[cog[0]].__doc__, color = self.bot.color_code, timestamp = ctx.message.created_at)
                        halp.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
                        for c in self.bot.get_cog(y).get_commands():
                            if not c.hidden:
                                halp.add_field(name=c.name,value=f'{c.help}\nUsage: `{self.bot.prefix}{c.usage}`',inline=False)
                        found = True
            if not found:
                halp = discord.Embed(title='Error!',description='How do you even use "'+cog[0]+'"?',color=self.bot.color_code)
            await ctx.send(embed = halp)
        
def setup(bot):
    bot.add_cog(Help(bot))