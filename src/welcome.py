import datetime
import io
import json
import sqlite3
from datetime import datetime

import discord
from PIL import Image, ImageOps, ImageDraw, ImageFont
from discord.ext import commands


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
        db = sqlite3.connect('sql/welcome.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM join_message')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM join_message WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass

    @commands.command()
    async def wmsettings(self, ctx):
        main = sqlite3.connect('sql/welcome.db')
        cursor1 = main.cursor()
        cursor2 = main.cursor()
        cursor1.execute(f"SELECT channel_id FROM join_message WHERE guild_id = {ctx.guild.id}")
        cursor2.execute(f"SELECT msg FROM join_message WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchall()
        result2 = cursor1.fetchall()
        e = discord.Embed(title="<:RoleIconSupportTeam:903679903709417572> Welcome message Settings", color=0xfae895)

        if result and result2:

            e.add_field(name="__Welcome message__", value="<:check:904396843528646676> enabled", inline=False)

        else:

            e.add_field(name="__Welcome message__", value="<:Uncheck:904396892354527232> disabled", inline=False)

        if result:

            e.add_field(name="__Welcome channel__", value=f"<:check:904396843528646676> Channel: <#{result[0]}>",
                        inline=False)

        else:
            e.add_field(name="__Welcome channel__", value="<:Uncheck:904396892354527232> no entry", inline=False)

        if result2:

            e.add_field(name="__Welcome text__", value=f"<:check:904396843528646676> Text:\n\n{result[0]}",
                        inline=False)

        else:

            e.add_field(name="__Welcome text__", value="<:Uncheck:904396892354527232> no entry", inline=False)

        e.set_thumbnail(url=ctx.author.guild.icon_url)
        e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def remove_wchannel(self, ctx):
        db = sqlite3.connect('sql/welcome.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT channel_id FROM join_message WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is not None:
            sql = f"DELETE FROM join_message WHERE guild_id = {ctx.guild.id}"
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Welcome message",
                                  description=get_lang(ctx.guild, "remove_wchannel"),
                                  color=0x46ff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            cursor1.execute(sql)
            db.commit()
            cursor1.close()
            db.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_wchannel(self, ctx, channel: discord.TextChannel):
        db = sqlite3.connect('sql/welcome.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT channel_id FROM join_message WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is None:
            sql = f"INSERT INTO join_message(guild_id, channel_id) VALUES(?,?)"
            val = (ctx.guild.id, channel.id)
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Welcome message",
                                  description=get_lang(ctx.guild, "add_wchannel2").format(channel.id),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()
        elif result is not None:
            sql = f"UPDATE join_message SET channel_id = ? WHERE guild_id = ?"
            val = (channel.id, ctx.guild.id)
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Welcome message",
                                  description=get_lang(ctx.guild, "add_wchannel").format(channel.id),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_wtext(self, ctx, *, text):
        db = sqlite3.connect('sql/welcome.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT msg FROM join_message WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is None:
            sql = f"INSERT INTO join_message(guild_id, msg) VALUES(?,?)"
            val = (ctx.guild.id, text)
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Welcome message",
                                  description=get_lang(ctx.guild, "add_wtext").format(text),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()
        elif result is not None:
            sql = f"UPDATE join_message SET msg = ? WHERE guild_id = ?"
            val = (text, ctx.guild.id)
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Welcome message",
                                  description=get_lang(ctx.guild, "add_wtext2").format(text),
                                  color=0x46ff00)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        db = sqlite3.connect('sql/welcome.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT msg FROM join_message WHERE guild_id = {member.guild.id}")
        result = cursor1.fetchone()
        if result is None:
            return
        else:
            cursor1.execute(f"SELECT channel_id FROM join_message WHERE guild_id = {member.guild.id}")
            result1 = cursor1.fetchone()
            usercount = len(list(member.guild.members))
            mention = member.mention
            user = member.name
            guild = member.guild
            embed = discord.Embed(description=str(result[0]).format(membercount=usercount, mention=mention, user=user,
                                                                    guild=guild), colour=0xffffff)

            avatar = member.avatar_url_as(format="png")
            data = io.BytesIO(await avatar.read())

            im = Image.open(data)
            im = im.resize((550, 550))
            bigsize = (im.size[0] * 3, im.size[1] * 3)
            mask = Image.new('L', bigsize, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + bigsize, fill=255)
            mask = mask.resize(im.size, Image.ANTIALIAS)
            im.putalpha(mask)

            output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)

            background1 = Image.open('mimibot_welcome.png')
            background1.paste(im, (220, 100), im)
            font = ImageFont.truetype("CarterOne-Regular.ttf", size=100)
            draw = ImageDraw.Draw(im)
            text = member.name
            m = member.discriminator
            membe = " Member" + " #" + str(member.guild.member_count)
            mm = text + " #" + m
            draw.text((810, 215), membe, (250, 250, 250), font=font, anchor="ms")
            draw.text((810, 115), mm, (250, 250, 250), font=font, anchor="ms")
            output.save("FinishImage1.png")

            image = "FinishImage1.png"

            file = discord.File(f"{image}")
            embed.set_image(url=f"attachment://{image}")

        channel = self.client.get_channel(id=int(result1[0]))
        await channel.send(embed=embed, file=file)


def setup(client):
    client.add_cog(ExtensionClass(client))
