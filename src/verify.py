import asyncio
import datetime
import json
import random
import sqlite3
from datetime import datetime
import discord
from discord import Embed
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
        db = sqlite3.connect('sql/verify.db')
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
        db = sqlite3.connect('sql/verify.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM channel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM channel WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/verify.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM role')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM role WHERE guild_id = {guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def vdelete(self, ctx):
        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Captcha",
                              description=get_lang(ctx.guild, "vdelete"),
                              color=0x46ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        db = sqlite3.connect('sql/verify.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM aktiv')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM aktiv WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/verify.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM channel')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM channel WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass
        db = sqlite3.connect('sql/verify.db')
        cursor = db.cursor()
        cursor.execute(f'SELECT * FROM role')
        result = cursor.fetchall()
        print(result)
        if result is not None:
            sql = f"DELETE FROM role WHERE guild_id = {ctx.guild.id}"
            cursor.execute(sql)
            db.commit()
            cursor.close()
            db.close()
            return
        else:
            pass


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_vchannel(self, ctx, channel: discord.TextChannel):
        db = sqlite3.connect('sql/verify.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT channel_id FROM channel WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is None:
            sql = f"INSERT INTO channel(guild_id, channel_id) VALUES(?,?)"
            val = (ctx.guild.id, channel.id)
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Verify",
                              description=get_lang(ctx.guild, "vchannel").format(channel.id),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()
        elif result is not None:
            sql = f"UPDATE channel SET channel_id = ? WHERE guild_id = ?"
            val = (channel.id, ctx.guild.id)
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Verify",
                              description=get_lang(ctx.guild, "vchannel2").format(channel.id),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def add_vrole(self, ctx, role: discord.Role):
        db = sqlite3.connect('sql/verify.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT role_id FROM role WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is None:
            sql = f"INSERT INTO role(guild_id, role_id) VALUES(?,?)"
            val = (ctx.guild.id, role.id)
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Verify",
                              description=get_lang(ctx.guild, "vrole").format(role.id),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()
        elif result is not None:
            sql = f"UPDATE role SET role_id = ? WHERE guild_id = ?"
            val = (role.id, ctx.guild.id)
            e = discord.Embed(title="<:win11_check_icon:903680159293538386> Verify",
                              description=get_lang(ctx.guild, "vrole2").format(role),
                              color=0x46ff00)
            e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
            e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            e.timestamp = datetime.utcnow()
            await ctx.send(embed=e)
            cursor1.execute(sql, val)
            db.commit()
            cursor1.close()
            db.close()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def averify(self, ctx):
        db = sqlite3.connect('sql/verify.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT * FROM enabled WHERE guild_id = {ctx.guild.id} AND owner = {ctx.author.id}")
        result = cursor1.fetchone()
        if result is None:
            owner = ctx.author.id
            sql = f"INSERT INTO enabled(guild_id, owner) VALUES(?,?)"
            val = (ctx.guild.id, owner)
            embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Level System",
                                  description=get_lang(ctx.guild, "averify"),
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
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Verify",
                                  description=get_lang(ctx.guild, "averify_error"),
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def sverify(self, ctx):
        db = sqlite3.connect('sql/verify.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT * FROM enabled WHERE guild_id = {ctx.guild.id}")
        result = cursor1.fetchone()
        if result is not None:
            sql = f"DELETE FROM enabled WHERE guild_id = {ctx.guild.id}"
            embed = discord.Embed(title="<:RoleIconSupportTeam:903679903709417572> Verify",
                                  description=get_lang(ctx.guild, "saverify"),
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
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Verify",
                                  description=get_lang(ctx.guild, "saverify_error"),
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
            db = sqlite3.connect('sql/verify.db')
            cursor2 = db.cursor()
            cursor2.execute(f"SELECT channel_id FROM channel WHERE guild_id = '{message.guild.id}'")
            resultc = cursor2.fetchone()
            if resultc:
                if message.channel.id == resultc[0]:
                    await asyncio.sleep(60)
                    await message.delete()
                else:
                    print(" ")
            else:
                print(" ")

    @commands.command()
    async def verify(self, ctx):
        db = sqlite3.connect('sql/verify.db')
        cursor1 = db.cursor()
        cursor1.execute(f"SELECT guild_id FROM enabled WHERE guild_id = '{ctx.guild.id}'")
        aktiv = cursor1.fetchone()
        if aktiv:
            db = sqlite3.connect('sql/verify.db')
            cursor2 = db.cursor()
            cursor2.execute(f"SELECT channel_id FROM channel WHERE guild_id = '{ctx.guild.id}'")
            resultc = cursor2.fetchone()
            if resultc:
                if ctx.message.channel.id == resultc[0]:

                    captcha = [
                        "https://cdn.discordapp.com/attachments/904720803151634462/905608288727597087/vfdvdfdfvfdv.png",
                        "https://cdn.discordapp.com/attachments/904720803151634462/905609433063768064/dcadcssd.png",
                        "https://cdn.discordapp.com/attachments/904720803151634462/905609803651502080/dfbbfgdbdfbfdfbd.png",
                        "https://cdn.discordapp.com/attachments/904720803151634462/905610002524414022/bgfbgtfgfghdfrgfg.png",
                        "https://cdn.discordapp.com/attachments/904720803151634462/905610301368586270/dfghfgdhfgdfghdgsds.png",
                        "https://cdn.discordapp.com/attachments/904720803151634462/905610559167283220/tfghhtfhtfghfhfthfhf.png"
                    ]
                    cr = random.choice(captcha)

                    def check(m):
                        return m.author == ctx.author and m.guild is None


                    db55 = sqlite3.connect('sql/verify.db')
                    cursor55 = db55.cursor()
                    cursor55.execute(f"SELECT role_id FROM role WHERE guild_id = '{ctx.guild.id}'")
                    result22 = cursor55.fetchone()

                    if result22 is not None:

                        crid = result22[0]
                        print(result22[0])
                        checkr = discord.utils.get(ctx.author.guild.roles, id=crid)
                        ce = discord.Embed(description=get_lang(ctx.guild, "ce").format(ctx.author.guild.name), color=0x3eff00)
                        cf = discord.Embed(description=get_lang(ctx.guild, "cf"), color=0xff0000)
                        edchm = Embed(description=get_lang(ctx.guild, "edchm").format(ctx.author.mention), color=0xff0000)

                        if checkr in ctx.author.roles:

                            ertt = Embed(title=f"<:win11_erro_icon:903679830300688455> Error | {ctx.guild.name}",
                                         description=get_lang(ctx.guild, "rae"), color=0xff0000)
                            ertt.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                            ertt.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677340809318420/fox5.png")
                            ertt.timestamp = datetime.utcnow()
                            await ctx.send(embed=ertt)

                        else:

                            dm = Embed(title=f"<:Recaptcha:904721981298057266> Captcha | {ctx.guild.name}",
                                       description=get_lang(ctx.guild, "verify1"), color=0xffffff)
                            dm.set_image(url=cr)
                            dm.set_thumbnail(url=ctx.author.guild.icon_url)
                            try:
                                await ctx.author.create_dm()
                                await ctx.author.dm_channel.send(embed=dm);
                            except discord.errors.Forbidden:
                                print(" ")

                            if cr == "https://cdn.discordapp.com/attachments/904720803151634462/905608288727597087/vfdvdfdfvfdv.png":
                                c1 = await self.client.wait_for('message', check=check)
                                l1 = ["5MF4", "5mf4"]

                                if l1 in c1.content:
                                    role = discord.utils.get(ctx.author.guild.roles, id=crid)
                                    await ctx.author.add_roles(role)
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=ce);
                                    except discord.errors.Forbidden:
                                        print(" ")
                                    await ctx.send(embed=edchm)

                                else:
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=cf);
                                    except discord.errors.Forbidden:
                                        print(" ")

                            elif cr == "https://cdn.discordapp.com/attachments/904720803151634462/905609433063768064/dcadcssd.png":
                                c2 = await self.client.wait_for('message', check=check)
                                l2 = ["3STF", "3stf"]

                                if l2 in c2.content:
                                    role = discord.utils.get(ctx.author.guild.roles, id=crid)
                                    await ctx.author.add_roles(role)
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=ce);
                                    except discord.errors.Forbidden:
                                        print("error")
                                    await ctx.send(embed=edchm)

                                else:
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=cf);
                                    except discord.errors.Forbidden:
                                        print("error")

                            elif cr == "https://cdn.discordapp.com/attachments/904720803151634462/905609803651502080/dfbbfgdbdfbfdfbd.png":
                                c3 = await self.client.wait_for('message', check=check)
                                l3 = ["9YVS", "9yvs"]

                                if l3 in c3.content:
                                    role = discord.utils.get(ctx.author.guild.roles, id=crid)
                                    await ctx.author.add_roles(role)
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=ce);
                                    except discord.errors.Forbidden:
                                        print("error")
                                    await ctx.send(embed=edchm)

                                else:
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=cf);
                                    except discord.errors.Forbidden:
                                        print("error")

                            elif cr == "https://cdn.discordapp.com/attachments/904720803151634462/905610002524414022/bgfbgtfgfghdfrgfg.png":
                                c4 = await self.client.wait_for('message', check=check)
                                l4 = ["45ZA", "45za"]

                                if l4 in c4.content:
                                    role = discord.utils.get(ctx.author.guild.roles, id=crid)
                                    await ctx.author.add_roles(role)
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=ce);
                                    except discord.errors.Forbidden:
                                        print("error")
                                    await ctx.send(embed=edchm)

                                else:
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=cf);
                                    except discord.errors.Forbidden:
                                        print("error")

                            elif cr == "https://cdn.discordapp.com/attachments/904720803151634462/905610301368586270/dfghfgdhfgdfghdgsds.png":
                                c5 = await self.client.wait_for('message', check=check)
                                l5 = ["87F5", "87f5"]

                                if l5 in c5.content:
                                    role = discord.utils.get(ctx.author.guild.roles, id=crid)
                                    await ctx.author.add_roles(role)
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=ce);
                                    except discord.errors.Forbidden:
                                        print("error")
                                    await ctx.send(embed=edchm)

                                else:
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=cf);
                                    except discord.errors.Forbidden:
                                        print("error")

                            elif cr == "https://cdn.discordapp.com/attachments/904720803151634462/905610559167283220/tfghhtfhtfghfhfthfhf.png":
                                c6 = await self.client.wait_for('message', check=check)
                                l6 = ["W46P", "w46p", "W46p"]

                                if l6 in c6.content:
                                    role = discord.utils.get(ctx.author.guild.roles, id=crid)
                                    await ctx.author.add_roles(role)
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=ce);
                                    except discord.errors.Forbidden:
                                        print("error")
                                    await ctx.send(embed=edchm)

                                else:
                                    try:
                                        await ctx.author.create_dm()
                                        await ctx.author.dm_channel.send(embed=cf);
                                    except discord.errors.Forbidden:
                                        print("error")
                    else:
                        er = Embed(title=f"<:win11_erro_icon:903679830300688455> Error | {ctx.guild.name}",
                                   description=get_lang(ctx.guild, "roleerror"), color=0xff0000)
                        er.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                        er.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                        er.timestamp = datetime.utcnow()
                        await ctx.send(embed=er)
                else:
                        er2 = Embed(title=f"<:win11_erro_icon:903679830300688455> Error | {ctx.guild.name}",
                                   description=get_lang(ctx.guild, "fchan").format(int(resultc[0])), color=0xff0000)
                        er2.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                        er2.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                        er2.timestamp = datetime.utcnow()
                        await ctx.send(embed=er2)
        else:
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Verify",
                                  description=get_lang(ctx.guild, "saverify_error2"),
                                  color=0xff0000)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command()
    async def vsettings(self, ctx):
        main = sqlite3.connect('sql/verify.db')
        cursor1 = main.cursor()
        cursor2 = main.cursor()
        cursor3 = main.cursor()
        cursor1.execute(f"SELECT guild_id FROM enabled WHERE guild_id = '{ctx.guild.id}'")
        cursor2.execute(f"SELECT channel_id FROM channel WHERE guild_id = '{ctx.guild.id}'")
        cursor3.execute(f"SELECT role_id FROM role WHERE guild_id = '{ctx.guild.id}'")
        aktiv = cursor1.fetchall()
        channel = cursor2.fetchall()
        role = cursor3.fetchall()
        e = discord.Embed(title="<:RoleIconSupportTeam:903679903709417572> Captcha system Settings", color=0xfae895)
        if aktiv:
            e.add_field(name="__Captcha system__", value="<:check:904396843528646676> enabled", inline=False)
        else:
            e.add_field(name="__Captcha system__", value="<:Uncheck:904396892354527232> disabled", inline=False)

        if channel:
            e.add_field(name="__Captcha channel__",
                        value=f"".join(f"\n<:check:904396843528646676> <#{channel[0]}>" for channel[0] in channel[0]),
                        inline=False)
        else:
            e.add_field(name="__Captcha channel__", value="<:Uncheck:904396892354527232> no entry", inline=False)

        if role:
            e.add_field(name="__Captcha role__",
                        value=f"".join(f"\n<:check:904396843528646676> <@&{role[0]}>" for role[0] in role[0]),
                        inline=False)
        else:
            e.add_field(name="__Captcha role__", value="<:Uncheck:904396892354527232> no entry", inline=False)
        e.set_thumbnail(url=ctx.author.guild.icon_url)
        e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(ExtensionClass(client))
