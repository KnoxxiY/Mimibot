import sqlite3
import datetime
import json
import sqlite3
from datetime import datetime

import discord
import re
from discord.ext import commands


def ctx(args):
    pass


def get_lang(guild, response):
    with open("json/lang.json", "r") as jsonFile:
        data = json.load(jsonFile)
        try:
            with open(f"language/{data[f'{guild.id}']}.json", "r") as jsonFile:
                language = json.load(jsonFile)
                return language[response].replace('ae', 'ä').replace('ue', 'ü').replace('oe', 'ö')
        except:
            with open("language/en.json", "r") as jsonFile:
                language = json.load(jsonFile)
                return language[response].replace('ae', 'ä').replace('ue', 'ü').replace('oe', 'ö')


class ExtensionClass(commands.Cog):
    def __init__(self, client):
        self.message = None
        self.client = client

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        db = sqlite3.connect('sql/reactroles.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM reaction')
        result = cursor.fetchall()
        if result is not None:
            sql = f"DELETE FROM reaction WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rreset(self, ctx):
        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Captcha",
                              description=get_lang(ctx.guild, "rreset"),
                              color=0x46ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, reaction):
        main = sqlite3.connect('sql/reactroles.db')
        cursor = main.cursor()
        result = ""
        cursor.execute(
            f"SELECT emoji, role, message_id, channel_id FROM reaction WHERE guild_id = '{reaction.guild_id}' and message_id = '{reaction.message_id}' and emoji = '<a:{reaction.emoji.name}:{reaction.emoji.id}>'")
        result = cursor.fetchone()

        if result is None:
            cursor.execute(
                f"SELECT emoji, role, message_id, channel_id FROM reaction WHERE guild_id = '{reaction.guild_id}' and message_id = '{reaction.message_id}' and emoji = '<:{reaction.emoji.name}:{reaction.emoji.id}>'")
            result = cursor.fetchone()

        if result is None:
            cursor.execute(
                f"SELECT emoji, role, message_id, channel_id FROM reaction WHERE guild_id = '{reaction.guild_id}' and message_id = '{reaction.message_id}' and emoji = '{reaction.emoji.id}'")
            result = cursor.fetchone()

        if result is None:
            cursor.execute(
                f"SELECT emoji, role, message_id, channel_id FROM reaction WHERE guild_id = '{reaction.guild_id}' and message_id = '{reaction.message_id}' and emoji = '{reaction.emoji}'")
            result = cursor.fetchone()

        if result is None:
            return

        guild = self.client.get_guild(reaction.guild_id)
        on = discord.utils.get(guild.roles, id=int(result[1]))
        user = guild.get_member(reaction.user_id)
        await user.remove_roles(on)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, reaction):
        if reaction.member != self.client.user:
            main = sqlite3.connect('sql/reactroles.db')
            cursor = main.cursor()
            if '<:' in str(reaction.emoji):
                cursor.execute(
                    f"SELECT emoji, role, message_id, channel_id FROM reaction WHERE guild_id = '{reaction.guild_id}' and message_id = '{reaction.message_id}' and emoji = '{reaction.emoji.id}'")
                result = cursor.fetchone()
                guild = self.client.get_guild(reaction.guild_id)
                if result is None:
                    return
                elif str(reaction.emoji.id) in str(result[0]):
                    on = discord.utils.get(guild.roles, id=int(result[1]))
                    user = guild.get_member(reaction.user_id)
                    await user.add_roles(on)
                else:
                    return
            elif '<:' not in str(reaction.emoji):
                cursor.execute(
                    f"SELECT emoji, role, message_id, channel_id FROM reaction WHERE guild_id = '{reaction.guild_id}' and message_id = '{reaction.message_id}' and emoji = '{reaction.emoji}'")
                result = cursor.fetchone()
                guild = self.client.get_guild(reaction.guild_id)
                if result is None:
                    return
                elif result is not None:
                    on = discord.utils.get(guild.roles, id=int(result[1]))
                    user = guild.get_member(reaction.user_id)
                    await user.add_roles(on)
                else:
                    return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def radd(self, ctx, channel: discord.TextChannel, messageid, emoji, role: discord.Role):
        main = sqlite3.connect('sql/reactroles.db')
        cursor = main.cursor()
        cursor.execute(
            f"SELECT emoji, role, message_id, channel_id, emojiname From reaction WHERE guild_id = '{ctx.message.guild.id}' and message_id = '{messageid}'")
        result = cursor.fetchone()
        if '<:' in emoji:
            emm = re.sub(':.*?:', '', emoji).strip('<>')
            if result is None:
                sql = 'INSERT INTO reaction(emoji, role, message_id, channel_id, guild_id, emojiname) VALUES(?,?,?,?,?,?)'
                VAL = (emm, role.id, messageid, channel.id, ctx.guild.id, emoji)
                msg = await channel.fetch_message(messageid)
                en = self.client.get_emoji(int(emm))
                await msg.add_reaction(en)
                e = discord.Embed(title="<:win11_check_icon:903680159293538386> Reaction roles",
                                  description=get_lang(ctx.guild, "radd").format(channel.id, ctx.guild.id, channel.id,
                                                                                 messageid, emoji, role.id),
                                  color=0x46ff00)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677202493739058/fox3.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            elif str(messageid) not in str(result[3]):
                sql = 'INSERT INTO reaction(emoji, role, message_id, channel_id, guild_id, emojiname) VALUES(?,?,?,?,?,?)'
                VAL = (emm, role.id, messageid, channel.id, ctx.guild.id, emoji)
                msg = await channel.fetch_message(messageid)
                en = self.client.get_emoji(int(emm))
                await msg.add_reaction(en)
                e = discord.Embed(title="<:win11_check_icon:903680159293538386> Reaction roles",
                                  description=get_lang(ctx.guild, "radd").format(channel, ctx.guild.id, channel.id,
                                                                                 messageid, emoji, role),
                                  color=0x46ff00)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677202493739058/fox3.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
        elif '<:' not in emoji:
            if result is None:
                sql = 'INSERT INTO reaction(emoji, role, message_id, channel_id, guild_id, emojiname) VALUES(?,?,?,?,?,?)'
                VAL = (emoji, role.id, messageid, channel.id, ctx.guild.id, emoji)
                msg = await channel.fetch_message(messageid)
                await msg.add_reaction(emoji)
                e = discord.Embed(title="<:win11_check_icon:903680159293538386> Reaction roles",
                                  description=get_lang(ctx.guild, "radd").format(channel, ctx.guild.id, channel.id,
                                                                                 messageid, emoji, role),
                                  color=0x46ff00)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677202493739058/fox3.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            elif str(messageid) not in str(result[3]):
                sql = 'INSERT INTO reaction(emoji, role, message_id, channel_id, guild_id, emojiname) VALUES(?,?,?,?,?,?)'
                VAL = (emoji, role.id, messageid, channel.id, ctx.guild.id, emoji)
                msg = await channel.fetch_message(messageid)
                await msg.add_reaction(emoji)
                e = discord.Embed(title="<:win11_check_icon:903680159293538386> Reaction roles",
                                  description=get_lang(ctx.guild, "radd").format(channel, ctx.guild.id, channel.id,
                                                                                 messageid, emoji, role),
                                  color=0x46ff00)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677202493739058/fox3.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
        cursor.execute(sql, VAL)
        main.commit()
        cursor.close()
        main.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rremove(self, ctx, messageid=None, emoji=None):
        main = sqlite3.connect('sql/reactroles.db')
        cursor = main.cursor()
        cursor.execute(
            f"SELECT emoji, role, message_id, channel_id, emojiname From reaction WHERE guild_id = '{ctx.guild.id}' and message_id = '{messageid}'")
        result = cursor.fetchone()
        if '<:' in emoji:
            emm = re.sub(':.*?:', '', emoji).strip('<>')
            if result is None:
                e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Reaction roles",
                                  description=get_lang(ctx.guild, "rremove_error"), color=0xff0000)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            elif str(messageid) in str(result[2]):
                cursor.execute(
                    f"DELETE FROM reaction WHERE guild_id = '{ctx.guild.id}' and message_id = '{messageid}' and emoji = {emm}")
                e = discord.Embed(title="<:win11_check_icon:903680159293538386> Reaction roles",
                                  description=get_lang(ctx.guild, "rremove").format(ctx.guild.id, ctx.channel.id,
                                                                                    messageid, emoji), color=0x46ff00)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677202493739058/fox3.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            else:
                e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Reaction roles",
                                  description=get_lang(ctx.guild, "rremove_error"), color=0xff0000)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
        elif '<:' not in emoji:
            if result is None:
                e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Reaction roles",
                                  description=get_lang(ctx.guild, "rremove_error"), color=0xff0000)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            elif str(messageid) in str(result[2]):
                cursor.execute(
                    f"DELETE FROM reaction WHERE guild_id = '{ctx.guild.id}' and message_id = '{messageid}' and emoji = '{emoji}'")
                e = discord.Embed(title="<:win11_check_icon:903680159293538386> Reaction roles",
                                  description=get_lang(ctx.guild, "rremove").format(ctx.guild.id, ctx.channel.id,
                                                                                    messageid, emoji), color=0x46ff00)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677202493739058/fox3.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
            else:
                e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Reaction roles",
                                  description=get_lang(ctx.guild, "rremove_error"), color=0xff0000)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.utcnow()
                await ctx.send(embed=e)
        main.commit()
        cursor.close()
        main.close()

    @commands.command()
    async def rsettings(self, ctx):
        main = sqlite3.connect('sql/reactroles.db')
        cursor1 = main.cursor()
        cursor1.execute(
            f"SELECT emoji, role, message_id, channel_id, emojiname From reaction WHERE guild_id = '{ctx.guild.id}'")
        result = cursor1.fetchall()
        e = discord.Embed(title="<:RoleIconSupportTeam:903679903709417572> Reaction role Settings",
                          description=get_lang(ctx.guild, "rsettings"), color=0xfae895)
        if result:

            e.add_field(name="__Reaction roles__", value="".join(
                f"\n<:check:904396843528646676> | <#{result[3]}> [message](https://discord.com/channels/{ctx.guild.id}/{result[3]}/{result[2]}) {result[4]} <@&{result[1]}>"
                for result in result), inline=False)

        else:

            e.add_field(name="__Reaction roles__", value="<:Uncheck:904396892354527232> no entries", inline=False)

        e.set_thumbnail(url=ctx.author.guild.icon_url)
        e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(ExtensionClass(client))
