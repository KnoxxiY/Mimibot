import asyncio
import json
import os
import sys

import discord
import datetime

import praw
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot

intents = discord.Intents.all()
membercache = discord.MemberCacheFlags.all()
intents.members = True
intents.presences = True

if not os.path.isfile("core/config.json"):
    sys.exit("'core/config.json' nicht gefunden!")
else:
    with open("core/config.json") as file:
        config = json.load(file)

if not os.path.isfile("core/color.json"):
    sys.exit("'core/color.json' nicht gefunden!")
else:
    with open("core/color.json") as file:
        color = json.load(file)

bot = commands.Bot(command_prefix=config["bot_prefix"], intents=intents)
bot.remove_command('help')
extensions = [
              "src.helpmenu", "src.verify", "src.Levelsystem", "src.reactionroles",
              "src.info", "src.fun", "src.tempchannel", "src.error", "src.welcome",
              "src.moderation"
              ]


@bot.event
async def on_ready():
    print(f'--------------------------------------')
    print(f'Bot ist Bereit')
    print(f'Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print(f'--------------------------------------')
    await status_task()


async def status_task():
    await bot.change_presence(activity=discord.Game('Cute Fox'), status=discord.Status.online)


# #####################################################################################################################

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


@bot.command()
@commands.has_permissions(manage_messages=True)
async def slang(ctx, lang):
    l = ["de", "en"]

    if lang in l:
        with open("json/lang.json", "r") as jsonFile:
            data = json.load(jsonFile)
        data[str(ctx.guild.id)] = lang
        with open("json/lang.json", "w") as jsonFile:
            json.dump(data, jsonFile)

        embed = Embed(title=get_lang(ctx.guild, "set_language_title",), description="`✅` " + get_lang(ctx.guild, "set_language_value").format(lang), color=0x00ffe8)
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903382625127890964/h.png")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
    else:
        return


# #####################################################################################################################


@bot.command()
@commands.is_owner()
async def evaluate(ctx, *, cmd=None):
    try:
        eval(cmd)
        await ctx.send(f'Your bot friend executed your command --> {cmd}')
    except:
        print(f'{cmd} is an invalid command')
        await ctx.send(f'Your bot friend could not execute an invalid command --> {cmd}')


@bot.command(hidden=True)
@commands.is_owner()
async def goodnight(ctx):
    await bot.logout()
    await ctx.channel.send("Sleep well")
    print('Sleep well')


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print('{} wurde geladen.'.format(extension))
        embed = discord.Embed(
            title='{} wurde geladen.'.format(extension),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print('{} wurde deaktiviert.'.format(extension))
        embed = discord.Embed(
            title='{} wurde deaktiviert.'.format(extension),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nich deaktiviert werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht deaktiviert werden. [{}]'.format(extension, error),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await ctx.channel.send('`{}` wurde neu geupdated.'.format(extension))
    except Exception as error:
        await ctx.channel.send('{} konnte nicht geladen werden. [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
            print("{} ist bereit".format(extension))
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))

reddit = praw.Reddit(client_id="s5Lhee4ESDUrZA",
                     client_secret="ktkza4xJ1jy1J0RMr4vek41RYVFY6w",
                     username="KnoxxiYY",
                     password="Maximilian1",
                     user_agent="Knox")

subreddit = reddit.subreddit("memes")

bot.run(config["token"])
