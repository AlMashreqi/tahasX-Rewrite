import discord, asyncio
import sqlite3
from discord.ext import commands

class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # cursor = db.cursor()
        # cursor.execute('''
        # CREATE TABLE IF NOT EXISTS levels(
        #     AUTHOR_ID TEXT,
        #     USER_LEVEL TEXT,
        #     USER_EXP TEXT
        # )
        # ''')

    
    def lvl_up(self, author_id):
        db = sqlite3.connect('./Cogs/Database/levels_eco.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT USER_LEVEL, USER_EXP FROM levels WHERE AUTHOR_ID = '{author_id}'")
        lvl_up_result = cursor.fetchone()
        current_lvl = int(lvl_up_result[0])
        current_exp = int(lvl_up_result[1])
        

        if current_exp >= round((4 * (current_lvl ** 3))/5):
            update_sql = ("UPDATE levels SET USER_LEVEL = ? WHERE AUTHOR_ID = ?")
            values = (current_lvl + 1, str(author_id))
            cursor.execute(update_sql, values)
            db.commit()
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        db = sqlite3.connect('./Cogs/Database/levels_eco.sqlite')
        author_id = str(message.author.id)

        cursor = db.cursor()
        cursor.execute(f"SELECT AUTHOR_ID FROM levels WHERE AUTHOR_ID = '{author_id}'")
        result = cursor.fetchone()
        if result is None:
            user_sql = ("INSERT INTO levels(AUTHOR_ID, USER_LEVEL, USER_EXP) VALUES(?,?,?)")
            values = (author_id, 0, 0)
            cursor.execute(user_sql, values)
            db.commit()
        else:
            cursor.execute(f"SELECT USER_LEVEL, USER_EXP FROM levels WHERE AUTHOR_ID = '{author_id}'")
            user_result = cursor.fetchone()
            exp = int(user_result[1])
            update_sql = ("UPDATE levels SET USER_EXP = ? WHERE AUTHOR_ID = ?")
            values = (exp + 2, str(message.author.id))
            cursor.execute(update_sql, values)
            db.commit()
    
        if self.lvl_up(author_id):
            cursor.execute(f"SELECT USER_LEVEL, USER_EXP FROM levels WHERE AUTHOR_ID = '{author_id}'")
            user_result = cursor.fetchone()
            level = int(user_result[0])
            lvlup_embed = discord.Embed(title = f'Leveled Up!:up:', description = f'{message.author.mention}, You Have Leveled up to Level {level} :partying_face:', color = self.bot.color_code, timestamp = message.created_at)
            lvlup_embed.set_footer(text=f'© {self.bot.user.name} \nOwned by {message.guild.owner}', icon_url=self.bot.user.avatar_url)
            await message.channel.send(embed = lvlup_embed)
        db.close()
        
    @commands.command(name = 'level', help = 'Shows the Current Level Of User', usage = 'level [member]')
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        db = sqlite3.connect('./Cogs/Database/levels_eco.sqlite')
        cursor = db.cursor()

        cursor.execute(f"SELECT AUTHOR_ID FROM levels WHERE AUTHOR_ID = '{member_id}'")
        result = cursor.fetchone()

        if result is None:
            embed = discord.Embed(title = f'Level Error', description = f'User Not Found', color = self.bot.color_code, timestamp = ctx.message.created_at)
            embed.set_footer(text=f'© {self.bot.user.name} \nOwned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed = embed)
        else:
            cursor.execute(f"SELECT USER_LEVEL, USER_EXP FROM levels WHERE AUTHOR_ID = '{member_id}'")
            user_result = cursor.fetchone()
            level = int(user_result[0])
            exp = int(user_result[1])

            lvl_embed = discord.Embed(title = f'User Level', description = f'{member.mention}\'s Rankings:', color = self.bot.color_code, timestamp = ctx.message.created_at)
            lvl_embed.set_thumbnail(url = member.avatar_url)
            lvl_embed.add_field(name = '**Level**', value = f'{level}')
            lvl_embed.add_field(name = '**EXP**', value = f'{exp}')
            lvl_embed.set_footer(text=f'© {self.bot.user.name} \nOwned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed = lvl_embed)
        
    @commands.command(name = 'leaderboard', aliases=['lb'], help = 'Shows the Level Leaderboard', usage = 'leaderboard')
    async def leaderboard(self, ctx):
        db = sqlite3.connect('./Cogs/Database/levels_eco.sqlite')
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM levels ORDER BY USER_EXP DESC")
        serial = 1

        embed = discord.Embed(title = f'Leaderboard :partying_face:', description = f'**The Top Ten:**', color = self.bot.color_code, timestamp = ctx.message.created_at)
        for row in cursor:
            if serial == 10:
                break
            member = ctx.guild.get_member(int(row[0]))
            level = row[1]
            exp = row[2]
            embed.add_field(name = f'**{serial}.{member}**', value = f'`Level:` {level} `Exp:` {exp}', inline = False)
        embed.set_footer(text=f'© {self.bot.user.name} \nOwned by {ctx.guild.owner}', icon_url=self.bot.user.avatar_url)
        await ctx.send(embed = embed)
                
def setup(bot):
    bot.add_cog(Levels(bot))