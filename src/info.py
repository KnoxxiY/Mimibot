
import datetime
from datetime import datetime

import discord
import os
import platform
import psutil
import requests
from cpuinfo import get_cpu_info
from discord.ext import commands

api_key = "d0f189dc9a35d070d51fa321174efb0c"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

start_time = datetime.utcnow()


class ExtensionClass(commands.Cog):
    def __init__(self, client):
        self.message = None
        self.client = client
        self.process = psutil.Process(os.getpid())

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def serverinfo(self, ctx):
        if not ctx.message.author.bot:
            server = ctx.guild
            server_info1 = (datetime.utcnow() - server.created_at).days
            rl = list(role.mention for role in server.roles if not role.name == "@everyone")
            Bot = list(member.bot for member in server.members if member.bot is True)
            user = list(member.bot for member in server.members if member.bot is False)
            channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
            voice_count = len([x for x in server.channels if type(x) == discord.channel.VoiceChannel])
            emoji_count = len(server.emojis)
            embed = discord.Embed(color=0xfcfcfc)
            embed.set_author(name=f"| Serverinfo",
                             icon_url=f"https://cdn.discordapp.com/emojis/790008676576264192.png?v=1")
            embed.add_field(name='🔧 Server ID:', value='{}'.format(server.id),
                            inline=True)
            embed.add_field(name=' ⚙️ name:', value='{}'.format(server.name),
                            inline=True)

            embed.add_field(name='server size:',
                            value='{} (250+ member)'.format(server.large), inline=False)

            embed.add_field(name='membercount:',
                            value='👥 {} members'.format(server.member_count), inline=True)
            embed.add_field(name='botcount:',
                            value='🤖 {} Bots'.format(str(len(Bot))),
                            inline=True)
            embed.add_field(name='emojis:', value=f"<:arrowwhite:904178288220581929> {str(emoji_count)}",
                            inline=True)

            embed.add_field(name='text Channels', value=f"<:YellowSmallDot:904488252722008125> {str(channel_count)}",
                            inline=False)
            embed.add_field(name='voice Channels', value=f"<:YellowSmallDot:904488252722008125> {str(voice_count)}",
                            inline=True)

            embed.add_field(name='serverowner:', value='{}'.format(server.owner.mention),
                            inline=False)

            embed.add_field(name='region:', value='{}'.format(server.region),
                            inline=True)
            embed.add_field(name='verifylevel:',
                            value='{}'.format(server.verification_level), inline=True)
            embed.add_field(name='serverroles:', value=str(len(rl)), inline=True)

            embed.add_field(name='AFK Channel:',
                            value='🔕 {0} ({1} seconds)'.format(server.afk_channel, server.afk_timeout), inline=True)

            embed.add_field(name='Created at:', value='{}'.format(
                "{} ({} days ago)".format(server.created_at.strftime("%A, %d. %B %Y | %H:%M:%S"), server_info1)),
                            inline=False)
            embed.set_thumbnail(url="{0}".format(server.icon_url))
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command(
        name="userinfo",
        description="Displays information about the server.",
        aliases=["user", "ui"],
        usage="userinfo",
    )
    async def userinfo(self, ctx, member: discord.Member = None, *, msg=None):
        member = member if member else self.client.fetch_user(msg) if member else ctx.author
        embed = discord.Embed(
            title="<:RoleIconSupportTeam:903679903709417572> User Information",
            color=0xfae895,
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(
            name="👤 User ❯",
            value=f"> **<:blob_minecraft_totem_of_undying:904848096951939073> Username: `{member}`**\n"
            f"> **\\📇 User ID: `{ctx.guild.id}`**\n"
            f"> **\\👦 Avatar: {f'[`Click here!`]({member.avatar_url})'}**\n"
            f"> **\\📅 Created: `{member.created_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - member.created_at).days}` day(s) ago**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="<:Player:903682117832151040> Member ❯",
            value=f"> **📘 Display Name: `{member.display_name}`**\n"
            f"> **\\🥇 Highest Role: {member.top_role.mention if member.top_role else '`None`'}**\n"
            f"> **\\🏅 Roles count: `{len(member.roles) - 1}`**\n"
            f"> **\\📥 Joined: `{member.joined_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - member.joined_at).days}` day(s) ago**\n",
            inline=False,
        )
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member:
            embed = discord.Embed(color=ctx.author.color, title=f'{ctx.author.name}')
            embed.set_image(url=member.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(color=ctx.author.color, title=f'{ctx.author.name}')
            embed.set_image(url=ctx.author.avatar_url)
            embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
            embed.timestamp = datetime.utcnow()
            await ctx.send(embed=embed)

    @commands.command()
    async def servericon(self, ctx):
        embed = discord.Embed(
            color=ctx.author.color)
        embed.set_image(url=ctx.guild.icon_url_as(size=1024, format=None, static_format="png"))
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)

    @commands.command()
    async def weather(self, ctx, *, city: str):

        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":

            y = x["main"]
            o = x["wind"]
            h = x["clouds"]
            current_temperature = y["temp"]
            mt = y["temp_max"]
            nt = y["temp_min"]
            fl = y["feels_like"]
            clo = h["all"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_temperature_celsiuis2 = str(round(mt - 273.15))
            current_temperature_celsiuis3 = str(round(nt - 273.15))
            current_temperature_celsiuis4 = str(round(fl - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            ws = o["speed"]
            gggg = o["deg"]

            embed = discord.Embed(title=f"⛅ The weather from {city_name}", color=0x00d8ff)
            embed.add_field(
                name="📈 The weather",
                value=f"**•** {weather_description}",
                inline=True)
            embed.add_field(
                name="☁️ Cloud cover",
                value=f"**•** {clo}%",
                inline=True)
            embed.add_field(
                name="🌡️ temperature",
                value=f"**•** {current_temperature_celsiuis}°C",
                inline=True)
            embed.add_field(
                name="⬆️ Highest temperature",
                value=f"**•** {current_temperature_celsiuis2}°C",
                inline=True)
            embed.add_field(
                name="⬇️ Lowest temperature",
                value=f"**•** {current_temperature_celsiuis3}°C",
                inline=True)
            embed.add_field(
                name="💥 Temperature Feels like",
                value=f"**•** {current_temperature_celsiuis4}°C",
                inline=True)
            embed.add_field(
                name="💧 humidity",
                value=f"**•** {current_humidity}%",
                inline=True)
            embed.add_field(
                name="💨 Air pressure",
                value=f"**•** {current_pressure} hPa",
                inline=True)
            embed.add_field(
                name="🥏 speed",
                value=f"**•** {ws} m/s | {gggg}°",
                inline=True)
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/775669943772643348/808164271833219153/forecastsunweathericon-1320184881471073011.png")
            embed.set_footer(text=f'{ctx.author.name}')
            embed.timestamp = datetime.utcnow()
            await channel.send(embed=embed)
        else:
            embed = discord.Embed(colour=0x00d8ff)
            embed.add_field(
                name="⛅ Weather",
                value=f"There were no results about this place!",
                inline=False)
            embed.set_footer(text=f'{ctx.author.name}')
            embed.timestamp = datetime.utcnow()
            await channel.send(embed=embed)

    @commands.command(
        name="botinfo",
        description="Displays indept information about the bot.",
        aliases=["bot", "bi"],
        usage="botinfo",
    )
    async def botinfo(self, ctx):
        channels = []
        for channel in self.client.get_all_channels():
            channels.append(channel.name)
        embed = discord.Embed(
            title="<:RoleIconSupportTeam:903679903709417572> Bot Information",
            color=0xfae895,
            timestamp=datetime.utcnow(),
        )
        embed.set_thumbnail(url=self.client.user.avatar_url)
        embed.add_field(
            name="<:ModeradorDiscord:904457795691233301> General ❯",
            value=f"> **<:FoxyyThink:904183485911158825> Bot Name: `MimiBot`**\n"
            f"> **\\📇 Bot ID: `{self.client.user.id}`**\n"
            f"> **\\👑 Owner: `KnoxxiY#1274` | <@443789116484878336>**\n"
            f"> **\\🌐 Servers: `{len(self.client.guilds)}` Servers**\n"
            f"> **\\👥 Users: `{len(self.client.users)}` Users**\n"
            f"> **\\📺 Channels: `{len(channels)}` Channels**\n"
            f"> **\\💬 Commands: `{len([x.name for x in self.client.commands])}` Commands**\n"
            f"> **\\📅 Created: `{self.client.user.created_at.strftime('%B %d %Y, %X')}` | `{(datetime.utcnow() - self.client.user.created_at).days}` day(s) ago**\n"
            "\u200b",
            inline=False,
        )
        embed.add_field(
            name="💾 System ❯",
            value=
            f"> **<:python:905144731628081222> Python: `v{platform.python_version()}`**\n"
            f"> **<:discordpy:905144834652766208> Discord.py: `v{discord.__version__}`**\n"
            f"> **\\🖥 Platform: `{platform.system()}`**\n"
            f"> **\\📊 Memory: `{self.process.memory_full_info().rss / 1024**2:.2f} MB Used`**\n"
            f"> **\\💻 CPU: `{get_cpu_info()['brand_raw']}`**\n",
            inline=False,
        )
        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
        embed.timestamp = datetime.utcnow()
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ExtensionClass(client))
