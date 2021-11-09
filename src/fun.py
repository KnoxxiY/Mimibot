import asyncio
import datetime
import json
import random
from datetime import datetime
from io import BytesIO
from random import random

import discord
import praw
from PIL import Image
from discord.ext import commands

reddit = praw.Reddit(client_id="s5Lhee4ESDUrZA",
                     client_secret="ktkza4xJ1jy1J0RMr4vek41RYVFY6w",
                     username="KnoxxiYY",
                     password="Maximilian1",
                     user_agent="Knox")

apikey = "L9ZEOOE55FNH"
lmt = 10


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
    async def meme(self, ctx, subred="meme"):
        subreddit = reddit.subreddit(subred)
        all_subs = []

        top = subreddit.top(limit=50)
        for submission in top:
            all_subs.append(submission)

        random_sub = random.choice(all_subs)
        name = random_sub.title
        url = random_sub.url
        upvotes = random_sub.score
        cmds = random_sub.num_comments
        au = random_sub.author
        embed = discord.Embed(description=f"**[{name}]({url})**", color=0xfcfcfc)
        embed.set_image(url=url)
        embed.set_footer(text=f"Reddit | 👍 {upvotes} | 💬 {cmds} | {au}")
        await ctx.send(embed=embed)

    @commands.command(
        name="hack",
        description="*Fake* Hacks a user",
        usage="hack <member>",
    )
    async def hack(self, ctx, member: discord.Member = None):
        if not member:
            return

        passwords = [
            "imnothackedlmao",
            "sendnudes63",
            "ilovenoodles",
            "1234",
            "betterasyou",
            "iloveroblox",
            "ilovefortnite",
            "hackedlmao",
            "987654321",
            "69420",
        ]

        fakeips = [
            "154.2345.24.743",
            "255.255.255.0",
            "356.653.56",
            "101.12.8.6053",
            "87.231.45.33",
            "91.55.43.8",
        ]

        sec = random.randint(1, 5)

        m = await ctx.send(f"Hacking: **{member.name}** {{0%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Searching for contacts... {{19%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Searching for any friends (if there is any) {{34%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Getting IP... {{55%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Got IP `{random.choice(fakeips)}` {{69%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Getting password... {{84%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Got password `{random.choice(passwords)}` {{99%}}")

        await asyncio.sleep(sec)

        await m.edit(content=f"Hacking: **{member.name}** {{100%}}")

        await asyncio.sleep(sec)

        embed = discord.Embed(
            title=f"{member} info ",
            description=f"*Email: `{member.name}@gmail.com`\nPassword: `{random.choice(passwords)}`\nIP: `{random.choice(fakeips)}`*",
            color=0xfcfcfc,
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677402079715348/fox6.png")
        embed.set_footer(text=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        embed.timestamp = datetime.utcnow()
        await m.edit(content=None, embed=embed)

    @commands.command()
    async def coinflip(self, ctx):
        coinsides = ['head', 'number']
        embed = discord.Embed(title="🪙 Coinflip",
            description=get_lang(ctx.guild, "coinflip").format(ctx.author.name, random.choice(coinsides)),
            color=0xfcfcfc)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/903382588289323008/903677340809318420/fox5.png")
        embed.set_footer(text=f'{ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command(aliases=['Reverse'])
    async def reverse(self, ctx, *, text: str):
        t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
        embed = discord.Embed(title="♻️ reverse than reverse",
            description=f"**{t_rev}**", color=0xfcfcfc)
        embed.set_footer(text=f'Reverse message from {ctx.author.name}',
                         icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ExtensionClass(client))
