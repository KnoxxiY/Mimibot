import datetime
import io
import json
import math
import random
import sqlite3
from datetime import datetime

import discord

from PIL import Image, ImageOps, ImageDraw, ImageFont
from discord.ext import commands
from discord.errors import Forbidden
from discord_components import DiscordComponents, Select, SelectOption, Button, ButtonStyle


def get_lang(guild, response):
    with open("json/lang.json", "r") as jsonFile:
        data = json.load(jsonFile)
        try:
            with open(f"language/{data[f'{guild.id}']}.json", "r") as jsonFile:
                language = json.load(jsonFile)
                return language[response]
        except:
            with open("language/en.json", "r") as jsonFile:
                language = json.load(jsonFile)
                return language[response]


class ExtensionClass(commands.Cog):
    def __init__(self, client):
        self.message = None
        self.client = client

    async def ranking(self, message):
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{message.guild.id}'")
        result = cursor.fetchall()
        cursor.execute(
            f"SELECT user_id, exp, level FROM glevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
        result1 = cursor.fetchone()
        lvl = int(result1[2])
        for result in result:
            role = message.guild.get_role(int(result[0]))
            try:
                if lvl >= int(result[1]):
                    await message.author.add_roles(role)
            except:
                return

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM glevel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM glevel WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM ranks')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM ranks WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM text')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM text WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM tlevel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM tlevel WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM vlevel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM vlevel WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM aktiv')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM aktiv WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM cblacklist')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM cblacklist WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM mxp')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM mxp WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rlevel(self, ctx):
        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Level System",
                              description=get_lang(ctx.guild, "rlevel"),
                              color=0x46ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM glevel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM glevel WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM vlevel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM vlevel WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM tlevel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM tlevel WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def rranks(self, ctx):
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM ranks')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM ranks WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Level System",
                                  description=get_lang(ctx.guild, "rranks"),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            return
        else:
            pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def aleveling(self, ctx):
        db = sqlite3.connect('sql/main.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT * FROM aktiv WHERE guild_id = {ctx.guild.id} AND owner = {ctx.author.id}")
        result = cursor1.fetchone()
        if result is None:
            owner = ctx.author.id
            sql = f"INSERT INTO aktiv(guild_id, owner) VALUES(?,?)"
            val = (ctx.guild.id, owner)
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Level System",
                                  description=get_lang(ctx.guild, "aleveling"),
                                  color=0x3eff00)
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            await ctx.send(embed=embed)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()
        else:
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Level System",
                                  description=get_lang(ctx.guild, "aleveling_error"),
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sleveling(self, ctx):
        db = sqlite3.connect('sql/main.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT * FROM aktiv WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is not None:
            sql = f"DELETE FROM aktiv WHERE guild_id = {ctx.guild.id}"
            embed = discord.Embed(title="<:RoleIconSupportTeam:903679903709417572> Level System",
                                  description=get_lang(ctx.guild, "sleveling"),
                                  color=0x3eff00)
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            await ctx.send(embed=embed)
            cursor1.execute(sql)
            db.commit()
            cursor1.close()
            db.close()
        else:
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Level System",
                                  description=get_lang(ctx.guild, "sleveling_error"),
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.type is discord.ChannelType.private:
            print(" ")
        else:
            db = sqlite3.connect('sql/main.db')
            cursor1 = db.cursor()
            cursor1.execute(f"SELECT guild_id FROM aktiv WHERE guild_id = {message.guild.id}")
            result = cursor1.fetchone()
            if not result:
                print(" ")
            else:
                print(" ")
                main = sqlite3.connect('sql/main.db')
                cursor = main.cursor()
                cursor.execute(f"SELECT enabled FROM glevel WHERE guild_id = '{message.guild.id}'")
                result = cursor.fetchone()
                if result is None:
                    sql = ("INSERT INTO glevel(guild_id, enabled) VALUES(?,?)")
                    val = (str(message.guild.id), 'enabled')
                    cursor.execute(sql, val)
                    main.commit()
                elif str(result[0]) == 'disabled':
                    sql = ("UPDATE glevel SET enabled = ? WHERE guild_id = ?")
                    val = ('enabled', str(message.guild.id))
                    cursor.execute(sql, val)
                    main.commit()
                cursor.close()
                main.close()
                main = sqlite3.connect('sql/main.db')
                cursor = main.cursor()
                cursor.execute(
                    f"SELECT * FROM cblacklist WHERE guild_id = '{message.guild.id}' AND channel_id = '{message.channel.id}'")
                result = cursor.fetchall()
                if result:
                    print("Blocked")
                    cursor.close()
                    main.close()
                else:
                    if message.author.bot:
                        return
                    else:
                        main2 = sqlite3.connect('sql/main.db')
                        cursor2 = main2.cursor()
                        cursor2.execute(
                            f"SELECT * FROM mxp WHERE guild_id = '{message.guild.id}' AND channel_id = '{message.channel.id}'")
                        results = cursor2.fetchone()
                        if results:
                            cursor2.close()
                            main2.close()
                            main = sqlite3.connect('sql/main.db')
                            cursor = main.cursor()
                            cursor.execute(f"SELECT enabled FROM glevel WHERE guild_id = '{message.guild.id}'")
                            result = cursor.fetchone()
                            if result is None:
                                return
                            elif str(result[0]) == 'enabled':
                                cursor.execute(
                                    f"SELECT user_id, exp, level FROM glevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                                result1 = cursor.fetchone()
                                if result1 is None:
                                    sql = ("INSERT INTO glevel(guild_id, user_id, exp, level) VALUES(?,?,?,?)")
                                    val = (str(message.guild.id), str(message.author.id), 0, 0)
                                    cursor.execute(sql, val)
                                    sql = ("INSERT INTO tlevel(guild_id, user_id, xp_time) VALUES(?,?,?)")
                                    val = (str(message.guild.id), str(message.author.id), datetime.utcnow())
                                    cursor.execute(sql, val)
                                    main.commit()
                                    await ExtensionClass(self).ranking(message)
                                else:
                                    cursor.execute(
                                        f"SELECT xp_time FROM tlevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                                    result2 = cursor.fetchone()
                                    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
                                    time_diff = datetime.strptime(str(datetime.utcnow()),
                                                                  datetimeFormat) - datetime.strptime(str(result2[0]),
                                                                                                      datetimeFormat)
                                    if time_diff.seconds >= 5:
                                        exp = int(result1[1])
                                        sql = ("UPDATE glevel SET exp = ? WHERE guild_id = ? and user_id = ?")
                                        val = (
                                            int(exp + random.randint(26, 40)), str(message.guild.id),
                                            str(message.author.id))
                                        cursor.execute(sql, val)
                                        sql = ("UPDATE tlevel SET xp_time = ? WHERE guild_id = ? and user_id = ?")
                                        val = (datetime.utcnow(), str(message.guild.id), str(message.author.id))
                                        cursor.execute(sql, val)
                                        main.commit()
                                        cursor.execute(
                                            f"SELECT user_id, exp, level FROM glevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                                        result2 = cursor.fetchone()
                                        xp_start = int(result2[1])
                                        lvl_start = int(result1[2])
                                        xp_end = math.floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 300)
                                        if xp_end < xp_start:
                                            cursor.execute(
                                                f"SELECT msg FROM text WHERE guild_id = {message.guild.id}")
                                            result22 = cursor.fetchone()
                                            if result22:
                                                level = lvl_start + 1
                                                mention = message.author.mention
                                                e = discord.Embed(
                                                    description=result22[0].format(level=level, mention=mention),
                                                    color=message.author.color)
                                                e.set_author(
                                                    name=get_lang(message.guild, "levelup_title") + f", {message.author}",
                                                    icon_url=message.author.avatar_url)
                                                e.set_thumbnail(url=message.author.avatar_url)
                                                e.set_footer(text=f'{message.guild.name}', icon_url=message.guild.icon_url)
                                                e.timestamp = datetime.utcnow()
                                                await message.channel.send(embed=e)
                                            else:
                                                e = discord.Embed(
                                                    description=get_lang(message.guild, "levelup_error"),
                                                    color=message.author.color)
                                                e.set_author(
                                                    name=get_lang(message.guild,
                                                                  "levelup_title") + f" {message.author.name}",
                                                    icon_url=message.author.avatar_url)
                                                e.set_thumbnail(url=message.author.avatar_url)
                                                e.set_footer(text=f'{message.author.guild.name}',
                                                             icon_url=message.guild.icon_url)
                                                e.timestamp = datetime.utcnow()
                                                await message.channel.send(embed=e)
                                            sql = ("UPDATE glevel SET level = ? WHERE guild_id = ? and user_id = ?")
                                            val = (int(lvl_start + 1), str(message.guild.id), str(message.author.id))
                                            cursor.execute(sql, val)
                                            main.commit()
                                            sql1 = ("UPDATE glevel SET exp = ? WHERE guild_id = ? and user_id = ?")
                                            val1 = (xp_start - xp_end, str(message.guild.id), str(message.author.id))
                                            cursor.execute(sql1, val1)
                                            main.commit()
                                            await ExtensionClass(self).ranking(message)
                                        else:
                                            await ExtensionClass(self).ranking(message)
                            else:
                                return
                        else:
                            main = sqlite3.connect('sql/main.db')
                            cursor = main.cursor()
                            cursor.execute(f"SELECT enabled FROM glevel WHERE guild_id = '{message.guild.id}'")
                            result = cursor.fetchone()
                            if result is None:
                                return
                            elif str(result[0]) == 'enabled':
                                cursor.execute(
                                    f"SELECT user_id, exp, level FROM glevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                                result1 = cursor.fetchone()
                                if result1 is None:
                                    sql = ("INSERT INTO glevel(guild_id, user_id, exp, level) VALUES(?,?,?,?)")
                                    val = (str(message.guild.id), str(message.author.id), 0, 0)
                                    cursor.execute(sql, val)
                                    sql = ("INSERT INTO tlevel(guild_id, user_id, xp_time) VALUES(?,?,?)")
                                    val = (str(message.guild.id), str(message.author.id), datetime.utcnow())
                                    cursor.execute(sql, val)
                                    main.commit()
                                    await ExtensionClass(self).ranking(message)
                                else:
                                    cursor.execute(
                                        f"SELECT xp_time FROM tlevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                                    result2 = cursor.fetchone()
                                    datetimeFormat = '%Y-%m-%d %H:%M:%S.%f'
                                    time_diff = datetime.strptime(str(datetime.utcnow()),
                                                                  datetimeFormat) - datetime.strptime(str(result2[0]),
                                                                                                      datetimeFormat)
                                    if time_diff.seconds >= 5:
                                        exp = int(result1[1])
                                        sql = ("UPDATE glevel SET exp = ? WHERE guild_id = ? and user_id = ?")
                                        val = (
                                        int(exp + random.randint(15, 26)), str(message.guild.id), str(message.author.id))
                                        cursor.execute(sql, val)
                                        sql = ("UPDATE tlevel SET xp_time = ? WHERE guild_id = ? and user_id = ?")
                                        val = (datetime.utcnow(), str(message.guild.id), str(message.author.id))
                                        cursor.execute(sql, val)
                                        main.commit()
                                        cursor.execute(
                                            f"SELECT user_id, exp, level FROM glevel WHERE guild_id = '{message.guild.id}' and user_id = '{message.author.id}'")
                                        result2 = cursor.fetchone()
                                        xp_start = int(result2[1])
                                        lvl_start = int(result1[2])
                                        xp_end = math.floor(5 * (lvl_start ^ 2) + 50 * lvl_start + 300)
                                        if xp_end < xp_start:
                                            main5 = sqlite3.connect('sql/main.db')
                                            cursor5 = main5.cursor()
                                            cursor5.execute(
                                                f"SELECT msg FROM text WHERE guild_id = {message.guild.id}")
                                            result22 = cursor5.fetchone()
                                            if result22:
                                                level = lvl_start + 1
                                                mention = message.author.mention
                                                e = discord.Embed(
                                                    description=result22[0].format(level=level, mention=mention),
                                                    color=message.author.color)
                                                e.set_author(
                                                    name=get_lang(message.guild, "levelup_title") + f", {message.author}",
                                                    icon_url=message.author.avatar_url)
                                                e.set_thumbnail(url=message.author.avatar_url)
                                                e.set_footer(text=f'{message.guild.name}', icon_url=message.guild.icon_url)
                                                e.timestamp = datetime.utcnow()
                                                await message.channel.send(embed=e)
                                            else:
                                                e = discord.Embed(
                                                    description=get_lang(message.guild, "levelup_error"),
                                                    color=message.author.color)
                                                e.set_author(
                                                    name=get_lang(message.guild,
                                                                  "levelup_title") + f" {message.author.name}",
                                                    icon_url=message.author.avatar_url)
                                                e.set_thumbnail(url=message.author.avatar_url)
                                                e.set_footer(text=f'{message.author.guild.name}',
                                                             icon_url=message.guild.icon_url)
                                                e.timestamp = datetime.utcnow()
                                                await message.channel.send(embed=e)
                                            sql = ("UPDATE glevel SET level = ? WHERE guild_id = ? and user_id = ?")
                                            val = (int(lvl_start + 1), str(message.guild.id), str(message.author.id))
                                            cursor.execute(sql, val)
                                            main.commit()
                                            sql1 = ("UPDATE glevel SET exp = ? WHERE guild_id = ? and user_id = ?")
                                            val1 = (xp_start - xp_end, str(message.guild.id), str(message.author.id))
                                            cursor.execute(sql1, val1)
                                            main.commit()
                                            await ExtensionClass(self).ranking(message)
                                        else:
                                            await ExtensionClass(self).ranking(message)
                            else:
                                return

        @commands.command()
        @commands.has_permissions(administrator=True)
        async def ltext(self, ctx, *, text):
            db = sqlite3.connect('sql/main.db')
            cursor1 = db.cursor()
            cursor1.execute(f"SELECT msg FROM text WHERE guild_id = {ctx.guild.id}")
            result = cursor1.fetchone()
            if result is None:
                sql = f"INSERT INTO text(guild_id, msg) VALUES(?,?)"
                val = (ctx.guild.id, text)
                embed = discord.Embed(title="<:blurple_plus:903980365394362418> Leveling System",
                                      description=get_lang(ctx.guild, "ltext").format(text),
                                      color=0x00ffe8)
                embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
                cursor1.execute(sql, val)
                db.commit()
                cursor1.close()
                db.close()
            elif result is not None:
                sql = f"UPDATE text SET msg = ? WHERE guild_id = ?"
                val = (text, ctx.guild.id)
                embed = discord.Embed(title="Leveling System",
                                      description=get_lang(ctx.guild, "ltext2").format(text),
                                      color=0x46ff00)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
                embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
                cursor1.execute(sql, val)
                db.commit()
                cursor1.close()
                db.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lrole_add(self, ctx):
        embed = discord.Embed(title="<:blurple_plus:903980365394362418> Leveling System",
                              description=get_lang(ctx.guild, "lrole_add"),
                              color=0x00ffe8)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677648037875712/fox8.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

        def check(m):
            return m.id and m.id == m.author.id

        rolename = await self.client.wait_for('message', check=check)
        embed = discord.Embed(title="<:blurple_plus:903980365394362418> Leveling System",
                              description=get_lang(ctx.guild, "lrole_add2"),
                              color=0x00ffe8)
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677648037875712/fox8.png")
        await ctx.send(embed=embed)
        level = await self.client.wait_for('message', check=check)
        role = discord.utils.get(ctx.guild.roles, name=rolename.content)
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}' and role_id = '{role.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO ranks(guild_id, role_id, level) VALUES(?,?,?)")
            val = (str(ctx.guild.id), str(role.id), level.content)
            cursor.execute(sql, val)
            main.commit()
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Leveling System",
                                  description=get_lang(ctx.guild, "lrole_add3"),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Leveling System",
                                  description=get_lang(ctx.guild, "lrole_add4"),
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            embed.set_footer(text=f'{ctx.author.name}')
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
        cursor.close()
        main.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lrole_remove(self, ctx):
        embed = discord.Embed(title="<:dnd:903980779565113384> Leveling System",
                              description=get_lang(ctx.guild, "lrole_remove"),
                              color=ctx.author.color)
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel

        rolename = await self.client.wait_for('message', check=check)
        role = discord.utils.get(ctx.guild.roles, name=rolename.content)
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}' and role_id = '{role.id}'")
        result = cursor.fetchone()
        if result is not None:
            cursor.execute("DELETE FROM ranks WHERE guild_id = '{}' and role_id = '{}'".format(ctx.guild.id, role.id))
            main.commit()
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Leveling System",
                                  description=get_lang(ctx.guild, "lrole_remove2"),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Leveling System",
                                  description=get_lang(ctx.guild, "lrole_remove3"),
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            embed.set_footer(text=f'{ctx.author.name}')
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
        cursor.close()
        main.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_2xp(self, ctx, channel: discord.TextChannel):
        ch = channel
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(
            f"SELECT channel_id FROM mxp WHERE guild_id = '{ctx.guild.id}' and channel_id = '{ch.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO mxp(guild_id, channel_id) VALUES(?,?)")
            val = (str(ctx.guild.id), str(ch.id))
            cursor.execute(sql, val)
            main.commit()
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Leveling System",
                              description=get_lang(ctx.guild, "2xp").format(channel.mention),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Leveling System",
                              description=get_lang(ctx.guild, "2xp2").format(channel.mention),
                              color=0xff0000)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        cursor.close()
        main.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_2xp(self, ctx, channel: discord.TextChannel):
        ch = channel
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(
            f"SELECT channel_id = '{ch.id}' AND guild_id = '{ctx.guild.id}' FROM mxp WHERE guild_id = '{ctx.guild.id}'")
        result = cursor.fetchone()
        if result:
            sql = f"DELETE FROM mxp WHERE channel_id = '{ch.id}' AND guild_id = '{ctx.guild.id}'"
            cursor.execute(sql)
            main.commit()
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Leveling System",
                              description=get_lang(ctx.guild, "2xpr").format(channel.mention),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Leveling System",
                              description=get_lang(ctx.guild, "2xpr2").format(channel.mention),
                              color=0xff0000)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        cursor.close()
        main.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_lblacklist(self, ctx, channel: discord.TextChannel):
        ch = channel
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(
            f"SELECT channel_id FROM cblacklist WHERE guild_id = '{ctx.guild.id}' and channel_id = '{ch.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO cblacklist(guild_id, channel_id) VALUES(?,?)")
            val = (str(ctx.guild.id), str(ch.id))
            cursor.execute(sql, val)
            main.commit()
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Leveling System",
                              description=get_lang(ctx.guild, "add_lblacklist").format(channel.mention),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Leveling System",
                              description=get_lang(ctx.guild, "add_lblacklist2").format(channel.mention),
                              color=0xff0000)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        cursor.close()
        main.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_lblacklist(self, ctx, channel: discord.TextChannel):
        ch = channel
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(
            f"SELECT channel_id = '{ch.id}' AND guild_id = '{ctx.guild.id}' FROM cblacklist WHERE guild_id = '{ctx.guild.id}'")
        result = cursor.fetchone()
        if result:
            sql = f"DELETE FROM cblacklist WHERE channel_id = '{ch.id}' AND guild_id = '{ctx.guild.id}'"
            cursor.execute(sql)
            main.commit()
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Leveling System",
                              description=get_lang(ctx.guild, "remove_lblacklist").format(channel.mention),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        else:
            e = discord.Embed(title="<:win11_erro_icon:903679830300688455> Leveling System",
                              description=get_lang(ctx.guild, "remove_lblacklist2").format(channel.mention),
                              color=0xff0000)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            e.set_footer(text=f'{ctx.author.name}')
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
        cursor.close()
        main.close()

    @commands.command()
    async def rlist(self, ctx):
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}'")
        result = cursor.fetchall()
        ranks = ''
        for result in result:
            role = ctx.guild.get_role(int(result[0]))
            ranks += f'`Level: {str(result[1])}` -> {role.mention}\n'
        embed = discord.Embed(title="📈 Leveling system",
                              description=get_lang(ctx.guild, "rlist").format(ctx.author.guild.name, ranks),
                              color=0x00ffe8)
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_footer(text=f'{ctx.author.name}')
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def list_2xp(self, ctx):
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT channel_id FROM mxp WHERE guild_id = '{ctx.guild.id}'")
        result = cursor.fetchall()
        channel = ''
        for result in result:
            ch = await self.client.fetch_channel(result[0])
            channel += f'{ch.mention}\n'
        embed = discord.Embed(title="📈 Leveling system",
                              description=get_lang(ctx.guild, "list_xp").format(channel),
                              color=0x00ffe8)
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_footer(text=f'{ctx.author.name}')
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def lc_blacklist(self, ctx):
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT channel_id FROM cblacklist WHERE guild_id = '{ctx.guild.id}'")
        result = cursor.fetchall()
        channel = ''
        for result in result:
            ch = await self.client.fetch_channel(result[0])
            channel += f'{ch.mention}\n'
        embed = discord.Embed(title="📈 Leveling system",
                              description=get_lang(ctx.guild, "lc_blacklist").format(ctx.author.guild.name, channel),
                              color=0x00ffe8)
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_footer(text=f'{ctx.author.name}')
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def lsettings(self, ctx):
        main = sqlite3.connect('sql/main.db')
        cursor1 = main.cursor()
        cursor2 = main.cursor()
        cursor3 = main.cursor()
        cursor4 = main.cursor()
        cursor5 = main.cursor()
        cursor1.execute(f"SELECT * FROM aktiv WHERE guild_id = '{ctx.guild.id}'")
        cursor2.execute(f"SELECT channel_id FROM cblacklist WHERE guild_id = '{ctx.guild.id}'")
        cursor3.execute(f"SELECT channel_id FROM mxp WHERE guild_id = '{ctx.guild.id}'")
        cursor4.execute(f"SELECT role_id, level FROM ranks WHERE guild_id = '{ctx.guild.id}'")
        cursor5.execute(f"SELECT msg FROM text WHERE guild_id = {ctx.guild.id}")
        aktiv = cursor1.fetchall()
        blacklist = cursor2.fetchall()
        mxp = cursor3.fetchall()
        rewards = cursor4.fetchall()
        text = cursor5.fetchall()
        e = discord.Embed(title="<:RoleIconSupportTeam:903679903709417572> Level system Settings", color=0xfae895)
        if aktiv:
            e.add_field(name="__Leveling__", value="<:check:904396843528646676> enabled", inline=False)
        else:
            e.add_field(name="__Leveling__", value="<:Uncheck:904396892354527232> disabled", inline=False)

        if mxp:
            e.add_field(name="__2XP channel__",
                        value=" ".join([f"<:check:904396843528646676> <#{mxp[0]}>\n" for mxp[0] in mxp[0]]),
                        inline=False)
        else:
            e.add_field(name="__2XP channel__", value="<:Uncheck:904396892354527232> no entries", inline=False)
        if blacklist:
            e.add_field(name="__Blacklist channel__", value="".join(f"\n<:check:904396843528646676> <#{blacklist[0]}>" for blacklist[0] in blacklist[0]), inline=False)
        else:
            e.add_field(name="__Blacklist channel__", value="<:Uncheck:904396892354527232> no entries", inline=False)
        if rewards:
            e.add_field(name="__Role rewards__", value="".join(
                f"\n<:check:904396843528646676> lvl:`{rewards[1]}` -> <@&{rewards[0]}>" for rewards in rewards),
                        inline=False)
        else:
            e.add_field(name="__Role rewards__", value="<:Uncheck:904396892354527232> no entries", inline=False)
        if text:
            e.add_field(name="__Levelup message__", value=f"<:check:904396843528646676> enabled\n{text[0]}",
                        inline=False)
        else:
            e.add_field(name="__Levelup message__", value=f"<:Uncheck:904396892354527232> disabled", inline=False)
        e.set_thumbnail(url=ctx.author.guild.icon_url)
        e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT enabled FROM glevel WHERE guild_id = '{member.guild.id}'")
        result = cursor.fetchone()
        if result is None:
            return
        elif str(result[0]) == 'enabled':
            cursor.execute(
                f"SELECT user_id, exp, level FROM glevel WHERE guild_id = '{member.guild.id}' and user_id = '{member.id}'")
            result1 = cursor.fetchone()
            if result1 is None:
                sql = ("INSERT INTO glevel(guild_id, user_id, exp, level) VALUES(?,?,?,?)")
                val = (str(member.guild.id), str(member.id), 0, 0)
                cursor.execute(sql, val)
                sql = ("INSERT INTO tlevel(guild_id, user_id, xp_time) VALUES(?,?,?)")
                val = (str(member.guild.id), str(member.id), datetime.datetime.utcnow())
                cursor.execute(sql, val)
                main.commit()
            if result1 is not None:
                return
        else:
            return
        cursor.close()
        main.close()

    @commands.command(aliases=['r'])
    async def rank(self, ctx, user: discord.Member = None):
        if user is None:
            main = sqlite3.connect('sql/main.db')
            cursor = main.cursor()
            cursor.execute(
                f"SELECT exp, level FROM glevel WHERE guild_id = '{ctx.guild.id}' and user_id = '{ctx.message.author.id}'")
            result = cursor.fetchone()
            if result is not None:
                avatar = ctx.author.avatar_url_as(format="png")
                data = io.BytesIO(await avatar.read())

                im = Image.open(data)
                im = im.resize((153, 153))
                bigsize = (im.size[0] * 3, im.size[1] * 3)
                mask = Image.new('L', bigsize, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + bigsize, fill=9000)
                mask = mask.resize(im.size, Image.ANTIALIAS)
                im.putalpha(mask)

                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                output.save('out.png')

                background1 = Image.open('rank1.png')
                background1.paste(im, (40, 45), im)
                background1.save('over.png')
                i = Image.open('over.png')
                font = ImageFont.truetype("CarterOne-Regular.ttf", size=30)
                fontt = ImageFont.truetype("CarterOne-Regular.ttf", size=40)
                draw = ImageDraw.Draw(i)

                text = ctx.author.name
                if len(text) > 12:
                    te = text[:12] + '...'
                    draw.text((670, 95), f"{str(result[1])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((670, 215), f"{str(result[0])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((340, 140), f"{te}", (250, 250, 250), font=fontt, anchor="ms")
                    draw.text((340, 190), f"#{ctx.author.discriminator}", (250, 250, 250), font=fontt, anchor="ms")
                    i.save("Fin.png")
                    await ctx.send(file=discord.File("Fin.png"))
                else:
                    draw.text((670, 95), f"{str(result[1])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((670, 215), f"{str(result[0])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((340, 120), f"{ctx.author.name}", (250, 250, 250), font=fontt, anchor="ms")
                    draw.text((340, 170), f"#{ctx.author.discriminator}", (250, 250, 250), font=fontt, anchor="ms")
                    i.save("Fin.png")
                    await ctx.send(file=discord.File("Fin.png"))
        else:
            main = sqlite3.connect('sql/main.db')
            cursor = main.cursor()
            cursor.execute(f"SELECT exp, level FROM glevel WHERE guild_id = '{ctx.guild.id}' and user_id = '{user.id}'")
            result = cursor.fetchone()
            if result is None:
                avatar = ctx.author.avatar_url_as(format="png")
                data = io.BytesIO(await avatar.read())

                im = Image.open(data)
                im = im.resize((153, 153))
                bigsize = (im.size[0] * 3, im.size[1] * 3)
                mask = Image.new('L', bigsize, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + bigsize, fill=9000)
                mask = mask.resize(im.size, Image.ANTIALIAS)
                im.putalpha(mask)

                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                output.save('out.png')

                background1 = Image.open('rank1.png')
                background1.paste(im, (40, 45), im)
                background1.save('over.png')
                i = Image.open('over.png')
                font = ImageFont.truetype("CarterOne-Regular.ttf", size=30)
                fontt = ImageFont.truetype("CarterOne-Regular.ttf", size=40)
                draw = ImageDraw.Draw(i)

                text = ctx.author.name
                if len(text) > 12:
                    te = text[:12] + '...'
                    draw.text((670, 95), f"0", (250, 250, 250), font=font, anchor="ms")
                    draw.text((670, 215), f"0", (250, 250, 250), font=font, anchor="ms")
                    draw.text((340, 120), f"{te}", (250, 250, 250), font=fontt, anchor="ms")
                    draw.text((340, 170), f"#{user.discriminator}", (250, 250, 250), font=fontt, anchor="ms")
                    i.save("Fin.png")
                    await ctx.send(file=discord.File("Fin.png"))
                else:
                    draw.text((670, 95), f"0", (250, 250, 250), font=font, anchor="ms")
                    draw.text((670, 215), f"0", (250, 250, 250), font=font, anchor="ms")
                    draw.text((340, 120), f"{ctx.author.name}", (250, 250, 250), font=fontt, anchor="ms")
                    draw.text((340, 170), f"#{ctx.author.discriminator}", (250, 250, 250), font=fontt, anchor="ms")
                    i.save("Fin.png")
                    await ctx.send(file=discord.File("Fin.png"))
            elif result is not None:
                avatar = user.avatar_url_as(format="png")
                data = io.BytesIO(await avatar.read())

                im = Image.open(data)
                im = im.resize((153, 153))
                bigsize = (im.size[0] * 3, im.size[1] * 3)
                mask = Image.new('L', bigsize, 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0) + bigsize, fill=9000)
                mask = mask.resize(im.size, Image.ANTIALIAS)
                im.putalpha(mask)

                output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
                output.putalpha(mask)
                output.save('out.png')

                background1 = Image.open('rank1.png')
                background1.paste(im, (40, 45), im)
                background1.save('over.png')
                i = Image.open('over.png')
                font = ImageFont.truetype("CarterOne-Regular.ttf", size=30)
                fontt = ImageFont.truetype("CarterOne-Regular.ttf", size=40)
                draw = ImageDraw.Draw(i)

                text = user.name
                if len(text) > 12:
                    te = text[:12] + '...'
                    draw.text((670, 95), f"{str(result[1])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((670, 215), f"{str(result[0])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((340, 120), f"{te}", (250, 250, 250), font=fontt, anchor="ms")
                    draw.text((340, 170), f"#{user.discriminator}", (250, 250, 250), font=fontt, anchor="ms")
                    i.save("Fin.png")
                    await ctx.send(file=discord.File("Fin.png"))
                else:
                    draw.text((670, 95), f"{str(result[1])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((670, 215), f"{str(result[0])}", (250, 250, 250), font=font, anchor="ms")
                    draw.text((340, 120), f"{user.name}", (250, 250, 250), font=fontt, anchor="ms")
                    draw.text((340, 170), f"#{user.discriminator}", (250, 250, 250), font=fontt, anchor="ms")
                    i.save("Fin.png")
                    await ctx.send(file=discord.File("Fin.png"))
            cursor.close()
            main.close()

    @commands.command()
    async def lb(self, ctx):
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(
            f"SELECT user_id, level, exp FROM glevel WHERE guild_id = '{ctx.guild.id}' ORDER BY level + 0 DESC LIMIT 10")
        result = cursor.fetchall()
        embed = discord.Embed(title=f"📈 Leaderboard {ctx.author.guild.name}", description=get_lang(ctx.guild, "llb"),
                              colour=discord.Colour(0xfae895))
        for i, x in enumerate(result, 1):
            emoji = ["<:FoxyyEhhky:904183870738554880>", "<:FoxyyHaiHai:904183742933893120>",
                     "<:FoxyyHeart:904183989026324491>", "<:FoxyyLove:904184172158025738>",
                     "<:FoxyyLurk:904183933602775051>", "<:FoxyyShockWakingUp:904184046542790667>",
                     "<:FoxyySleeping:904184109096648714>", "<:FoxyyThink:904183485911158825>",
                     "<:FoxyyTired:904183582136893471>", "<:chibifox:904184474093371412>"]
            re = random.choice(emoji)
            embed.add_field(name=f"#{i}. Level `{str(x[1])}` | `{str(x[2])}`XP", value=f"{re} <@{str(x[0])}>  ",
                            inline=False)
        embed.set_thumbnail(url=ctx.author.guild.icon_url)
        embed.set_footer(text="Je nach größe des Servers kann -glb einige sekunden dauern!")
        await ctx.send(embed=embed)

    @commands.command()
    async def glb(self, ctx):
        db = sqlite3.connect('sql/main.db')
        cursor = db.cursor()
        cursor.execute(
            f"SELECT user_id, level, exp FROM glevel WHERE guild_id = '{ctx.guild.id}' ORDER BY level + 0 DESC")
        result = cursor.fetchall()
        with open("txt/leaderboard.md", "w", encoding="utf-8") as file:

            for i, x in enumerate(result, 1):
                try:
                    emoji = ["😀", "😁", "😂", "😅", "😉", "😎", "🥰", "🥶", "🤑", "🥳", "😛", "🔥", "⭐️", "🌟", "✨",
                             "⚡️", "💥", "🍀", "☘️",
                             "🍂", "🌷", "🌺", "🌈", "👤", "🧠", "🦴", "🎩", "🎓"]
                    re = random.choice(emoji)
                    user = await self.client.fetch_user(x[0])
                    file.write(f'{re} {i}. Level{str(x[1])} | {str(x[2])}XP | {user}\n')
                except:
                    break
        with open("txt/leaderboard.md", "rb") as file:
            await ctx.send(f"{ctx.author.guild.name} Leaderboard:", file=discord.File(file, "leaderboard.md"))
        cursor.close()
        db.close()

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        main = sqlite3.connect('sql/main.db')
        cursor = main.cursor()
        cursor.execute(f"SELECT enabled FROM glevel WHERE guild_id = '{guild.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO glevel(guild_id, enabled) VALUES(?,?)")
            val = (str(guild.id), 'enabled')
            cursor.execute(sql, val)
            main.commit()
        elif str(result[0]) == 'disabled':
            sql = ("UPDATE glevel SET enabled = ? WHERE guild_id = ?")
            val = ('enabled', str(guild.id))
            cursor.execute(sql, val)
            main.commit()
        cursor.close()
        main.close()


def setup(client):
    client.add_cog(ExtensionClass(client))
