# -*- coding: utf-8 -*-
import random
from random import shuffle
from discord.ext import commands
from discord.ext.commands import Bot
from logger import logger
teamplayers = []
class Teams(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name='join_team',aliases=[''])
    async def _join_team(self, ctx: commands.Context):
        teamplayers.append(ctx.author.name)
        await ctx.send(ctx.author.mention+' Joined team selection')

    @commands.command(name='teams')
    async def _teams(self, ctx: commands.Context, number_of_teams: int):
        global teamplayers
        number_teamplayers = len(teamplayers)
        peapol_in_teams = round(len(teamplayers)/number_of_teams)
        shuffle(teamplayers)
        try:
            teams = [teamplayers[i:i+peapol_in_teams] for i in range(0, number_teamplayers, peapol_in_teams)]
        except ValueError:
            await ctx.send('Get more friends you cunt')
        teamplayers.clear()
        list2 = teams
        i=0
        while len(list2) > number_of_teams:
            teams[i].append(teams[-1][-1])
            i =+ 1
            del teams[-1][-1]
            list2 = [x for x in teams if x != []]
        del i
        del number_of_teams
        del teams
        del peapol_in_teams
        await ctx.send(list2)

def setup(bot):
    bot.add_cog(Teams(bot))
    logger.info(f'Loaded Teams')
