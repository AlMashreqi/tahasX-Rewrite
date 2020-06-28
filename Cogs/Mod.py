import discord
from discord.ext import commands

class Mod(commands.Cog, name = 'Moderation'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'warn', help = 'Warns the Specified User')
    @commands.has_permissions(kick_members = True)
    async def warn(self, ctx, member: discord.Member, *, reason = 'Unspecified'):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot Warn yourself!")
            return
        embed = discord.Embed(title = 'User Warned',description = f'{member} has been Warned\n**Reason:** {reason}', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Specify a User to Warn")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @commands.command(name = 'clear', help = 'Clears a certian amount')
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount = 5):
        await ctx.channel.purge(limit = amount + 1)
        embed = discord.Embed(title='Messages Cleared', description = f'Cleared {amount} Messages', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed = embed)
        print(f'{amount} messages Cleared')

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @commands.command(name='mute', help='Mutes a Member')
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx, member: discord.Member, *, reason='Unspecified'):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot Mute yourself!")
            return
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = False
        overwrite.read_messages = True

        for channel in ctx.guild.channels:
            await channel.set_permissions(member, overwrite=overwrite)
        await member.add_roles(role)
        embed = discord.Embed(title='User Muted', description=f'{member.mention} has been Muted.\n**Reason:** {reason}',
                              color=bot.color_code, timestamp=ctx.message.created_at)
        embed.set_footer(text=f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed=embed)

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Specify a User to Mute")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @command.command(name='unmute', help='unmutes a Member')
    @commands.has_permissions(kick_members=True)
    async def unmute(self, ctx, member: discord.Member):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot Mute yourself!")
            return
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        overwrite = discord.PermissionOverwrite()
        overwrite.send_messages = True
        overwrite.read_messages = True

        for channel in ctx.guild.channels:
            await channel.set_permissions(member, overwrite=overwrite)
        embed = discord.Embed(title='User Unmuted', description=f'{member.mention} has been Unmuted',
                              color=bot.color_code, timestamp=ctx.message.created_at)
        embed.set_footer(text=f'© {self..user.name} | Owned by {ctx.guild.owner}', icon_url=self..user.avatar_url)
        await ctx.send(embed=embed)

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Specify a User to Unmute")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")


    @commands.command(name = 'kick', help = 'kicks the user')
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *, reason = 'Unspecified'):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot kick yourself!")
            return
        await member.kick(reason=reason)
        channel = self.bot.get_channel(int(GCI))
        embed = discord.Embed(title = 'User Kicked',description = f'{member.mention} has been kicked from the Server\n**Reason:** {reason}', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)
        print(f'Kick message sent for {member}....')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Specify a User to kick")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @commands.command(name = 'ban' , help = 'bans a user')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason = 'Unspecified'):
        if member == None or member == ctx.message.author:
            await ctx.channel.send("You cannot ban yourself")
            return
        await member.ban(reason=reason)
        channel = self.bot.get_channel(int(GCI))
        embed = discord.Embed(title = 'User Banned',description = f'{member.mention} has been banned from the Server\n**Reason:** {reason}', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)
        print(f'Ban message sent for {member}......')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Specify a User to Ban")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @commands.command(name = 'unban', help = 'unbans a banned user')
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if(user.name, user.discriminator) == (member_name, member_discriminator):
                embed = discord.Embed(title = 'User Unbanned',description = f'{member_name}#{member_discriminator} has been Unbanned', color = self.bot.color_code,timestamp = ctx.message.created_at)
                embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
                await ctx.guild.unban(user)
                await ctx.send(embed = embed)
                print(f'Unbanned {user.mention}....')
                return
        await ctx.send(f'User was not found!')
        print('User was not Found....')

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please Specify a User to Unban!")
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @commands.command(name = 'lockdown', help = 'Puts a Channel Under lockdown')
    @commands.has_permissions(administrator = True)
    async def lockdown(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = False)
        embed = discord.Embed(title = ':lock: Channel Locked Down :lock:',description = f'{ctx.channel.mention} has been put under Lockdown', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @lockdown.error
    async def lockdown_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

    @commands.command(name = 'unlock', help = 'Puts a Channel Under lockdown')
    @commands.has_permissions(administrator = True)
    async def unlock(ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages = True)
        embed = discord.Embed(title = ':unlock: Channel Unlocked :unlock:',description = f'{ctx.channel.mention} has been Unlocked', color = self.bot.color_code,timestamp = ctx.message.created_at)
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {ctx.guild.owner}', icon_url = self.bot.user.avatar_url)
        await ctx.send(embed = embed)

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("OOps! You don't have Permissions to That!")

def setup(bot):
    bot.add_cog(Mod(bot))