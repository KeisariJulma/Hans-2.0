# -*- coding: utf-8 -*-
import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from logger import logger
from datetime import datetime as d
from configobj import ConfigObj
config = ConfigObj('conf.ini')

# New - The Cog class must extend the commands.Cog class
class Basic(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command(
        name='ping',
        description='The ping command'
    )
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
        msg = await ctx.send(content='Pinging')
        await msg.edit(content=f'Pong!\nOne message round-trip took {( d.timestamp( d.now() ) - start ) * 1000 }ms.')
        return

    @commands.guild_only()
    @commands.command(
        name='setmusic',
        description='Sets music channel'
    )
    async def setmusic(self, ctx):
        try:
            config[str(ctx.guild.id)]['music_channel'] = ctx.channel.id
        except KeyError:
            config[str(ctx.guild.id)] = {}
            config[str(ctx.guild.id)]['music_channel'] = ctx.channel.id
        config.write()
        await ctx.send("Music channel set!")

    @commands.command()
    async def channels(self, ctx):
        if ctx.author.id == 302174001113989132:
            for channel in ctx.guild.channels:
                print(f'Type: {channel.type} | Name: {channel.name} | Id: {channel.id}')

    @commands.command()
    async def move(self, ctx: commands.Context, id: int):
        channel = self.bot.get_channel(id)
        await ctx.message.author.move_to(channel)
        ctx.message.delete()

    @commands.command()
    async def moveall(self, ctx: commands.Context, id: int):
        if ctx.author.id == 302174001113989132:
            voicechannel = ctx.guild.get_channel(ctx.author.voice.channel.id)
            #finds the members
            members = voicechannel.members
            channel = self.bot.get_channel(id)
            for member in members:
                await member.move_to(channel)

    @commands.command()
    async def connected(self, ctx: commands.Context):
        if ctx.author.id == 302174001113989132:
            for channel in ctx.guild.voice_channels:
                voicechannel = ctx.guild.get_channel(channel.id)
                members = voicechannel.members
                print(f'Name: {channel.name} members: {members}')
def setup(bot):
    bot.add_cog(Basic(bot))
    logger.info(f'Loaded Basic')
