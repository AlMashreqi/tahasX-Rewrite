import corona_api, discord
from discord.ext import commands

class Corona(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'covid', help = 'Shows the current COVID stats', usage = 'covid [country]')
    async def covid(self, ctx, *, country = 'default'):
        corona = corona_api.Client()
        if country == 'default':
            data = await corona.all()  # get global data
            embed = discord.Embed(title = 'COVID-19 Stats', description = '**Worldwide Stats:**', color = self.bot.color_code,timestamp = ctx.message.created_at)
            embed.add_field(name = '**Global Cases**', value = f'{data.cases}', inline = False)
            embed.add_field(name = '**Global Deaths**', value=f'{data.deaths}', inline=False)
            embed.add_field(name = '**Global Recoveries**', value=f'{data.recoveries}', inline=False)
            embed.add_field(name='**Active Cases**', value=f'{data.active}', inline=False)
            embed.add_field(name = '**Cases Today**', value=f'{data.today_cases}', inline=False)
            embed.add_field(name='**Deaths Today**', value=f'{data.today_deaths}', inline=False)
            embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)

            await ctx.send(embed = embed)
            await corona.request_client.close()  # close the ClientSession
        else:
            try:
                data = await corona.get_country_data(country)
            except:
                embed = discord.Embed(title = f'COVID-19 Stats', description = f'**Country Not Found!**', color = self.bot.color_code,timestamp = ctx.message.created_at)
                embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
                await corona.request_client.close()
                await ctx.send(embed = embed)
                return

            embed = discord.Embed(title = f'COVID-19 Stats', description = f'**{country.title()}\'s COVID-19 Stats:**', color = self.bot.color_code,timestamp = ctx.message.created_at)
            embed.add_field(name = '**Total Cases**', value = f'{data.cases}', inline = False)
            embed.add_field(name = '**Total Deaths**', value=f'{data.deaths}', inline=False)
            embed.add_field(name = '**Total Recoveries**', value=f'{data.recoveries}', inline=False)
            embed.add_field(name='**Active Cases**', value=f'{data.active}', inline=False)
            embed.add_field(name = '**Cases Today**', value=f'{data.today_cases}', inline=False)
            embed.add_field(name='**Deaths Today**', value=f'{data.today_deaths}', inline=False)
            embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)

            await ctx.send(embed = embed)
            await corona.request_client.close()  # close the ClientSession

def setup(bot):
    bot.add_cog(Corona(bot))