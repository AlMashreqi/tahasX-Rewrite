import discord
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = 'rd', help = 'Simulates rolling of Dice')
    async def roll(self, ctx):
        dice = str(random.choice(range(1, 7)))
        await ctx.send(', '.join(dice))
        print('Dice rolled....')

    @commands.command(name = '8ball', help = 'Asks 8 Ball a Question', usage = '8ball <question>')
    async def _8ball(self, ctx, *, question):
        responses =['As I see it, yes.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Don’t count on it.',
                    'It is certain.',
                    'It is decidedly so.',
                    'Most likely.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Outlook good.',
                    'Reply hazy, try again.',
                    'Signs point to yes.',
                    'Very doubtful.',
                    'Without a doubt.',
                    'Yes.',
                    'Yes – definitely.',
                    'You may rely on it.']
        embed = discord.Embed(title = '8 Ball', description = f'**Question:** {question}\n**Answer:** {random.choice(responses)}')
        embed.set_footer(text=f'© {self.bot.user.name} | Owned by {self.ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please ask a Question!')

def setup(bot):
    bot.add_cog(Fun(bot))