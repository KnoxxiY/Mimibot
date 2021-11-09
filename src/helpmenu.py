import datetime
import json

import discord
from discord.ext import commands
from discord import Embed
from discord_components import *


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

    @commands.Cog.listener()
    async def on_ready(self):
        DiscordComponents(self.client)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content in [f"<@!{self.client.user.id}>", f"<@{self.client.user.id}>"]:
            e = discord.Embed(title="<:FoxyyHaiHai:904183742933893120> Mimi's Prefix",
                              description=get_lang(message.guild, "prefixxx"), colour=0xfae895)
            e.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677938120138752/fox10.png")
            e.set_footer(text=f'Request: {message.author.name}',
                         icon_url=f"{message.author.avatar_url}")
            e.timestamp = datetime.datetime.utcnow()
            await message.channel.send(embed=e)
        else:
            return

    @commands.command()
    async def help(self, ctx):
        e = Embed(color=0xfae895)
        e.set_author(name="Mimi's HelpList",
                     icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
        e.add_field(
            name="<:FoxyyLurk:904183933602775051> Version: 0.1.4 | Python3.7 | Discord.py 1.7.3 | sql3 | pillow...",
            value=get_lang(ctx.guild, "help_title"), inline=False)
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
        await ctx.send(embed=e, components=[
            Select(
                placeholder='📢 Select a option',
                options=[
                    SelectOption(label="🔥 Levelsystem",
                                 value="a"),
                    SelectOption(label="✅ Captcha system",
                                 value="b"),
                    SelectOption(label="🎭 Reation roles",
                                 value="c"),
                    SelectOption(label="🔊 Tempchannel",
                                 value="d"),
                    SelectOption(label="🚨 Auto moderation",
                                 value="e"),
                    SelectOption(label="👋 Welcome (with usercard)",
                                 value="f"),
                    SelectOption(label="🔧 Moderation",
                                 value="g"),
                    SelectOption(label="🔎 Information",
                                 value="h"),
                    SelectOption(label="🎮 Fun",
                                 value="i")
                ])])

    @commands.Cog.listener()
    async def on_select_option(self, interaction):
        if interaction.values[0] == "a":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Levelsystem",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="View all settings: `?lsettings`", value=get_lang(interaction.guild, "help_levelsystem"),
                         inline=False)
            e1.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)

        elif interaction.values[0] == "b":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Captcha",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="View all settings: `?vsettings`", value=get_lang(interaction.guild, "help_captcha"),
                         inline=False)
            e1.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/905212532904583208/fvddfvdfdf.PNG")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "c":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's reaction roles",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="View reaction roles: `?rsettings`", value=get_lang(interaction.guild, "rrolesss"),
                         inline=False)
            e1.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/905212532904583208/fvddfvdfdf.PNG")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "d":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Tempchannel",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="You cane get only one tempchannel", value=get_lang(interaction.guild, "tcnel"),
                         inline=False)
            e1.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "e":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Auto moderation",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="Automod", value=get_lang(interaction.guild, "automoderrrr"),
                         inline=False)
            e1.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "f":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Welcome message",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="View all settings with: `?wmsettings`", value=get_lang(interaction.guild, "wmsg"),
                         inline=False)
            e1.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "g":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Moderation",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="Moderation", value=get_lang(interaction.guild, "moderationas"),
                         inline=False)
            e1.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "h":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Information's",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="All commands are in English!", value=get_lang(interaction.guild, "infossu"),
                         inline=False)
            e1.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)
        elif interaction.values[0] == "i":
            e1 = Embed(color=0xfae895)
            e1.set_author(name="Mimi's Fun",
                          icon_url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
            e1.add_field(name="Fun", value=get_lang(interaction.guild, "funiiis"),
                         inline=False)
            e1.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677567201054740/fox7.png")
            await interaction.edit_origin(embed=e1)

    # @commands.Cog.listener()
    # async def on_button_click(self, interaction):
    # if interaction.custom_id[0] == "CUSTOM_ID":
    # await ...

    @commands.command()
    async def invite(self, ctx):
        e = Embed(title="Invite Link", description=get_lang(ctx.guild, "invite"), color=0xfae895)
        e.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677938120138752/fox10.png")
        await ctx.send(embed=e)

    @commands.command()
    async def changelog(self, ctx):
        e = discord.Embed(title="<:FoxyyHaiHai:904183742933893120> Mimi's Changelog",
                          description="> **This changelog is only in English!**\n\n"
                                      "<:Uncheck:904396892354527232> No entries", colour=0xfae895)
        e.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
        e.set_footer(text=f'Request: {ctx.author.name}',
                     icon_url=f"{ctx.author.avatar_url}")
        e.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=e)



def setup(client):
    client.add_cog(ExtensionClass(client))
