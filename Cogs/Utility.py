import discord
from discord.ext import commands

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'introduce', help = 'Responds with Intoduction')
    async def introduce(self, ctx):
        embed = discord.Embed(title=f'I am {self.bot.user.name}!', description=f'Hello, I am {self.bot.user.name}, I was Created by Sauood#6924. I am a Multipurpose Bot having different Commands and Functionalities.\n I have Moderation, Utility and Fun Commands.\n\n**• Username: ** {self.bot.user}\n**• ID:** {self.bot.user.id}\n**• Programming Language: **Python', color=self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_thumbnail(url=f'{self.bot.user.avatar_url}')
        embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed = embed)
        print("Response sent....")

    @commands.command(name = 'ping', help = f'Gives the latency of the Bot')
    async def ping(self, ctx):
        embed = discord.Embed(description = f'Pong {round(self.bot.latency * 1000)}ms', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @commands.command(name = 'avatar', help = 'Shows the avatar of a User')
    async def avatar(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        embed = discord.Embed(color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_image(url = f'{member.avatar_url}')
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @avatar.error
    async def avatar_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please Specify a user!')

    @commands.command(name = 'userinfo', help = f'Gives the info of the user')
    async def userinfo(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.message.author
        roles = [role for role in member.roles]

        embed = discord.Embed(title = 'User Info', description = f'**{member.name}\'s Info**', color = self.bot.color_code, timestamp = ctx.message.created_at)
        embed.set_thumbnail(url = member.avatar_url)
        embed.add_field(name='Username', value=f'{member}', inline=True)
        embed.add_field(name='Guild Name', value=f'{member.guild}', inline=True)
        embed.add_field(name='Roles', value="".join([role.mention for role in roles]), inline=True)
        embed.add_field(name='Bot', value=f'{member.bot}',inline=True)
        embed.add_field(name='Joined Discord At:', value=f'{member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}', inline=False)
        embed.add_field(name='Joined Server At:', value=f'{member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC")}',inline=False)
        embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)

        await ctx.send(embed = embed)
    
    @commands.command(name = 'delsnipe', help = 'Shows last Deleted Message')
    @commands.has_permissions(manage_messages = True)
    async def delsnipe(self, ctx, num = 1):
        if ctx.channel.id not in self.bot.del_message:
            await ctx.send('Nothing to snipe')
            return
        message = self.bot.del_message[ctx.channel.id][-num]
        embed = discord.Embed(title = 'Last Deleted Message', description = f'Deleted Message:\n```{message.content}```\nAuthor: {message.author}', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @delsnipe.error
    async def delsnipe_error(self, ctx, error):
        if isinstance(error, Exception):
            await ctx.send('Nothing to Snipe')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps You don't have Permissions to That!")

    @commands.command(name = 'editsnipe', help = 'Shows last Edited Message')
    @commands.has_permissions(manage_messages = True)
    async def editsnipe(self, ctx, num = 1):
        if ctx.channel.id not in self.bot.ed_message:
            await ctx.send('Nothing to snipe')
            return
        message = self.bot.org_message[ctx.channel.id][-num]
        message2 = self.bot.ed_message[ctx.channel.id][-num]
        embed = discord.Embed(title = 'Last Edited Message', description = f'Orignal Message:\n```{message.content}```\nEdited Message:\n```{message2.content}```\nAuthor: {message.author}', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @editsnipe.error
    async def editsnipe_error(self, ctx, error):
        if isinstance(error, Exception):
            await ctx.send('Nothing to Snipe')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

def setup(bot):
    bot.add_cog(Utility(bot))
