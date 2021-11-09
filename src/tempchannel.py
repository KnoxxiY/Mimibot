import datetime
import json
import os
from datetime import datetime

import discord
from discord.ext import commands

tempchannels = []
botcolor = 0xffffff
tempchannels = []


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


if os.path.isfile("json/channels.json"):
    with open('json/channels.json', encoding='utf-8') as f:
        channels = json.load(f)
else:
    channels = {}
    with open('json/channels.json', 'w') as f:
        json.dump(channels, f, indent=4)


async def getChannel(guild, name):
    for channel in guild.voice_channels:
        if name in channel.name:
            return channel
    return None


def isJoinHub(channel):
    if channels[str(channel.guild.id)]:
        if channel.id in channels[str(channel.guild.id)]:
            return True
    return False


def isTempChannel(channel):
    if channel.id in tempchannels:
        return True
    else:
        return False


class ExtensionClass(commands.Cog):
    def __init__(self, client):
        self.message = None
        self.client = client

    @commands.command(pass_context=True)
    async def add_tchannel(self, ctx, channelid):
        if ctx.author.bot:
            return
        if ctx.author.guild_permissions.administrator:
            if channelid:
                for vc in ctx.guild.voice_channels:
                    if vc.id == int(channelid):
                        if str(ctx.channel.guild.id) not in channels:
                            channels[str(ctx.channel.guild.id)] = []
                        channels[str(ctx.channel.guild.id)].append(int(channelid))
                        with open('json/channels.json', 'w') as f:
                            json.dump(channels, f, indent=4)
                        embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Tempchannel",
                                              description=get_lang(ctx.guild, "add_tc").format(vc.name),
                                              colour=0x3eff00)
                        embed.set_thumbnail(
                            url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
                        embed.set_footer(text=f'Request: {ctx.author.name}', icon_url=f"{ctx.author.avatar_url}")
                        embed.timestamp = datetime.utcnow()
                        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def remove_tchannel(self, ctx, channelid):
        if ctx.author.bot:
            return
        if ctx.author.guild_permissions.administrator:
            if channelid:
                guildS = str(ctx.channel.guild.id)
                channelidI = int(channelid)
                for vc in ctx.guild.voice_channels:
                    if vc.id == int(channelid):
                        if channels[guildS]:
                            if channelidI in channels[guildS]:
                                channels[guildS].remove(channelidI)
                                with open('json/channels.json', 'w') as f:
                                    json.dump(channels, f, indent=4)
                                    embed = discord.Embed(title="<:win11_check_icon:903680159293538386> Tempchannel",
                                                          description=get_lang(ctx.guild,
                                                                               "delete_tc").format(
                                                              vc.name),
                                                          colour=0x3eff00)
                                    embed.set_thumbnail(
                                        url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
                                    embed.set_footer(text=f'Request: {ctx.author.name}',
                                                     icon_url=f"{ctx.author.avatar_url}")
                                    embed.timestamp = datetime.utcnow()
                                    await ctx.send(embed=embed)
                                    return
                            else:
                                embed5 = discord.Embed(title="<:win11_erro_icon:903679830300688455> Tempchannel",
                                                       description=get_lang(ctx.guild, "delete_tc_error"),
                                                       colour=0xf0ff00)
                                embed5.set_thumbnail(
                                    url="https://cdn.discordapp.com/attachments/903382588289323008/903677340809318420/fox5.png")
                                embed5.set_footer(text=f'Request: {ctx.author.name}',
                                                  icon_url=f"{ctx.author.avatar_url}")
                                embed5.timestamp = datetime.utcnow()
                                await ctx.send(embed=embed5)

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if before.channel:
            if isTempChannel(before.channel):
                bchan = before.channel
                if len(bchan.members) == 0:
                    await bchan.delete(reason="Keiner hat diesen Voice mehr verwendet")
        if after.channel:
            if isJoinHub(after.channel):
                overwrite = discord.PermissionOverwrite()
                overwrite.manage_channels = True
                overwrite.move_members = True
                name = "│⏳ {}".format(member.name)
                output = await after.channel.clone(name=name, reason="ist in einen Joingub beigetreten")
                if output:
                    tempchannels.append(output.id)
                    await output.set_permissions(member, overwrite=overwrite)
                    await member.move_to(output, reason="Tempvoice wurde erstellt")
                    e = discord.Embed(title="🔊 Tempchannel",
                                      description=get_lang(member.guild, "tccreated").format(output.id,
                                                                                             member.guild.name),
                                      colour=0x46ff00)
                    e.set_thumbnail(
                        url="https://cdn.discordapp.com/attachments/903382588289323008/903677281300516894/fox4.png")
                    e.set_footer(text=f'Request: {member.name}', icon_url=f"{member.avatar_url}")
                    e.timestamp = datetime.utcnow()
                    try:
                        await member.create_dm()
                        await member.dm_channel.send(embed=e);
                    except discord.errors.Forbidden:
                        print(" ")


def setup(client):
    client.add_cog(ExtensionClass(client))
