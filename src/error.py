import datetime
import json

import discord
import math
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
    async def on_command_error(self, ctx, error):
        try:
            if hasattr(ctx.command, 'on_error'):
                return
            error = getattr(error, 'original', error)
            if isinstance(error, commands.CommandNotFound):
                e = discord.Embed(title="<:FoxyyHaiHai:904183742933893120> Mimi's Prefix",
                                  description=get_lang(ctx.guild, "prefixxx"), colour=0xfae895)
                e.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677938120138752/fox10.png")
                e.set_footer(text=f'Request: {ctx.author.name}',
                             icon_url=f"{ctx.author.avatar_url}")
                e.timestamp = datetime.datetime.utcnow()
                await ctx.channel.send(embed=e)
                return
            if isinstance(error, commands.BotMissingPermissions):
                missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
                if len(missing) > 2:
                    fmt = '{}, und {}'.format("**, **".join(missing[:-1]), missing[-1])
                else:
                    fmt = ' und '.join(missing)
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> | Error", colour=0xff0000)
                embed.add_field(name=f"Command", value=f"```ini\n"
                                                       f"{ctx.command}"
                                                       f"\n```", inline=True)
                embed.add_field(name=f"Error", value='```css\n'
                                                     'I need the *{}* permission(s) to use this command!'
                                                     '\n```'.format(fmt), inline=False)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                await ctx.send(embed=embed, delete_after=300)
                return

            if isinstance(error, commands.CommandOnCooldown):
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> | Error", colour=0xff0000)
                embed.add_field(name=f"Command", value=f"```ini\n"
                                                       f"{ctx.command}"
                                                       f"\n```", inline=True)
                embed.add_field(name=f"Error", value='```css\n'
                                                     'Youre in cooldown, try again in *{}s*'
                                                     '\n```'.format(math.ceil(error.retry_after)), inline=False)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                await ctx.send(embed=embed, delete_after=300)
                return

            if isinstance(error, commands.MissingPermissions):
                missing = [perm.replace('_', ' ').replace('guild', 'server').title() for perm in error.missing_perms]
                if len(missing) > 2:
                    fmt = '{}, and {}'.format("**, **".join(missing[:-1]), missing[-1])
                else:
                    fmt = ' and '.join(missing)
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> | Error", colour=0xff0000)
                embed.add_field(name=f"Command", value=f"```ini\n"
                                                       f"{ctx.command}"
                                                       f"\n```", inline=True)
                embed.add_field(name=f"Error", value='```css\n'
                                                     'You need *{}* permission(s) to use this command!'
                                                     '\n```'.format(fmt), inline=False)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                await ctx.send(embed=embed, delete_after=300)
                return

            if isinstance(error, commands.UserInputError):
                await ctx.send("<:FoxyyTired:904183582136893471> **Invalid Input!**")
                return

            if isinstance(error, commands.CheckFailure):
                embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> | Error", colour=0xff0000)
                embed.add_field(name=f"Command", value=f"```ini\n"
                                                       f"{ctx.command}"
                                                       f"\n```", inline=True)
                embed.add_field(name=f"Error", value='```css\n'
                                                     'You miss any premission(s) to use this command'
                                                     '\n```', inline=False)
                embed.set_thumbnail(
                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
                await ctx.send(embed=embed, delete_after=300)
                return
        except:
            embed = discord.Embed(title="<:win11_erro_icon:903679830300688455> | Error", colour=0xff0000)
            embed.add_field(name=f"Command", value=f"```ini\n"
                                                   f"{ctx.command}"
                                                   f"\n```", inline=True)
            embed.add_field(name=f"Error", value='```css\n'
                                                 f'{ctx.command.qualified_name} {ctx.command.signature}\n \n-----------------------------------------------\n{error}\n'
                                                 '\n```', inline=False)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/903382588289323008/903677855752392704/fox9.png")
            await ctx.send(embed=embed, delete_after=300)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        ghost = self.client.get_channel(905106229376991292)
        embed = discord.Embed(title="Betreten",
                              description=(f"> Servername: `{guild.name}`\n"
                                           f"> ServerID: `{guild.id}`\n"
                                           f"\n"
                                           f"> Server Owner: `{guild.owner}`\n"
                                           f"> Membercounter: `{len(list(guild.members))}`\n"
                                           f"\n"),
                              color=0x3eff00)
        embed.set_thumbnail(
            url=f'{guild.icon_url}')
        await ghost.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        ghost = self.client.get_channel(905106229376991292)
        embed = discord.Embed(title="Verlassen",
                              description=(f"> Servername: `{guild.name}`\n"
                                           f"> ServerID: `{guild.id}`\n"
                                           f"\n"
                                           f"> Server Owner: `{guild.owner}`\n"
                                           f"> Membercounter: `{len(list(guild.members))}`\n"
                                           f"\n"),
                              color=0xff0000)
        embed.set_thumbnail(
            url=f'{guild.icon_url}')
        await ghost.send(embed=embed)


def setup(client):
    client.add_cog(ExtensionClass(client))
