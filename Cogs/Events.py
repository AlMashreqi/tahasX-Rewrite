import discord
from discord.ext import commands
from datetime import datetime

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(WCI))
        embed = discord.Embed(title = f'Welcome {member.name}', description = f'{member.mention}, Be sure read the {self.bot.get_channel(int(RCI)).mention} and enjoy your stay.\n\n**• Username: ** {member}\n**• ID:** {member.id}\n**• Server Members: ** {len(guild.members)}', color = self.bot.color_code, timestamp = member.joined_at)
        embed.set_thumbnail(url = f'{member.avatar_url}')
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {member.guild.owner}', icon_url = self.bot.user.avatar_url)
        await channel.send(embed = embed)
        print(f'Public Welcome message sent for {member}....')
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(GCI))
        embed = discord.Embed(title = f'Thanks for being Here', description = f'{member.mention} has Left the Server.\nIt was good having you here.\n\n**• Username: ** {member}\n**• ID:** {member.id}\n**• Server Members: ** {len(guild.members)}', color = self.bot.color_code, timestamp = datetime.datetime.now())
        embed.set_thumbnail(url = f'{member.avatar_url}')
        embed.set_footer(text = f'© {self.bot.user.name} | Owned by {member.guild.owner}', icon_url = self.bot.user.avatar_url)
        await channel.send(embed = embed)
        print(f'Leave message sent for {member}.....')

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot:
            return

        message_id = message.channel.id

        self.bot.del_message.setdefault(message.channel.id, [])

        if len(self.bot.del_message[message_id]) > 40:
            del self.bot.del_message[message_id][0]

        self.bot.del_message[message_id].append(message)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        if before.author == self.bot:
            return

        message_id = before.channel.id
        message2_id = after.channel.id

        if before.content != after.content:
            self.bot.org_message.setdefault(before.channel.id, [])
            self.bot.ed_message.setdefault(after.channel.id, [])

            if len(self.bot.org_message[message_id]) > 40 and len(self.bot.ed_message[message2_id]) > 40:
                del self.bot.org_message[message_id][0]
                del self.bot.ed_message[message2_id][0]

            self.bot.org_message[message_id].append(before)
            self.bot.ed_message[message2_id].append(after)

def setup(bot):
    bot.add_cog(Events(bot))