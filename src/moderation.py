import asyncio
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

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self, ctx, user: discord.Member, *, reason: str = None):
        if reason is None:
            reason = "No reason"
        try:
            await ctx.guild.kick(user, reason=reason)
        except discord.errors.Forbidden:
            if user.top_role.position == ctx.me.top_role.position:
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Kick",
                                      description=get_lang(ctx.guild, "k1"),
                                      color=0xff0000)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            elif user.top_role.position > ctx.me.top_role.position:
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Kick",
                                      description=get_lang(ctx.guild, "k1"),
                                      color=0xff0000)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Kick",
                              description=get_lang(ctx.guild, "k2").format(ctx.author.mention, user.mention, reason),
                              color=0x46ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        embed2 = discord.Embed(title="<:win11_erro_icon:903679830300688455> Kick",
                               description=get_lang(ctx.guild, "k3").format(ctx.guild.name, ctx.guild.name,
                                                                            ctx.author.mention, ctx.author, reason),
                               color=0xff0000)
        embed2.set_thumbnail(url=ctx.author.guild.icon_url)
        embed2.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed2.timestamp = datetime.utcnow()
        try:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(embed=embed2);
        except discord.errors.Forbidden:
            print(" ")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self, ctx, user: discord.Member, *, reason: str = None):
        if reason is None:
            reason = "No reason"
        try:
            await ctx.guild.ban(user, delete_message_days=0, reason=reason)
        except discord.errors.Forbidden:
            if user.top_role.position == ctx.me.top_role.position:
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Ban",
                                      description=get_lang(ctx.guild, "b1"),
                                      color=0xff0000)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
            elif user.top_role.position > ctx.me.top_role.position:
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> Ban",
                                      description=get_lang(ctx.guild, "b1"),
                                      color=0xff0000)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                embed.timestamp = datetime.utcnow()
                await ctx.send(embed=embed)
        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Ban",
                              description=get_lang(ctx.guild, "b2").format(ctx.author.mention, user.mention,
                                                                           reason),
                              color=0x46ff00)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        embed2 = discord.Embed(title="<:win11_erro_icon:903679830300688455> Ban",
                               description=get_lang(ctx.guild, "b3").format(ctx.guild.name, ctx.guild.name,
                                                                            ctx.author.mention, ctx.author, reason),
                               color=0xff0000)
        embed2.set_thumbnail(url=ctx.author.guild.icon_url)
        embed2.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed2.timestamp = datetime.utcnow()
        try:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(embed=embed2);
        except discord.errors.Forbidden:
            print(" ")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.guild_only()
    async def unban(self, ctx, *, username: str):
        banlist = await ctx.guild.bans()
        user = None
        for ban in banlist:
            if ban.user.name == username:
                user = ban.user
        await ctx.guild.unban(user)
        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Unban",
                              description=get_lang(ctx.guild, "unb1").format(ctx.author.mention, username),
                              color=0x46ff00)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)
        embed2 = discord.Embed(title="<:win11_erro_icon:903679830300688455> Unban",
                               description=get_lang(ctx.guild, "unb2").format(ctx.guild.name, ctx.guild.name,
                                                                              ctx.author.mention, ctx.author),
                               color=0xff0000)
        embed2.set_thumbnail(url=ctx.author.guild.icon_url)
        embed2.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed2.timestamp = datetime.utcnow()
        try:
            await ctx.author.create_dm()
            await ctx.author.dm_channel.send(embed=embed2);
        except discord.errors.Forbidden:
            print(" ")

    @commands.command(aliases=['Clear', '_clear', 'purge'])
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def clear(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        e = discord.Embed(title="", description=get_lang(ctx.guild, "clear_value").format(len(deleted)), color=0x46ff00)
        e.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        e.timestamp = datetime.utcnow()
        await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def remove_reactions(self, ctx, messageid: int):
        message = await ctx.channel.fetch_message(messageid)
        await message.clear_reactions()


def setup(client):
    client.add_cog(ExtensionClass(client))
