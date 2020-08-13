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
    @commands.has_role('SS-Oberführer')
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
      for channel in ctx.guild.channels:
        print(f"Name: {channel.name} Id: {channel.id}")

    @commands.command()
    async def move(self, ctx: commands.Context, *, our_input: str):
        print(ctx.message.author.id)
        client = discord.Client()
        print(our_input)
        channel = client.get_channel(our_input)
        await ctx.message.author.move_to(channel)

def setup(bot):
    bot.add_cog(Basic(bot))
    logger.info(f'Loaded Basic')
