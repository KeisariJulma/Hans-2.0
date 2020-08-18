import discord
import asyncio
import random
from logger import logger
from discord.ext import commands
players=[]
class russian_roulette(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='Join russian ruolette', aliases=['roulette'])
    async def _join_russian_roulette(self, ctx: commands.Context):
        players.append(ctx.author.id)
        await ctx.send(ctx.author.mention+' Joined to Russian roulette')

    @commands.command(name='Game of Russian ruolette', aliases=['roll'])
    async def russian_roulette(self, ctx: commands.Context):
        winner = random.choice(players)
        true = True
        while true:
            for player in players:
                bang = random.randint(1,6)
                if bang == 2:
                    winner = ctx.guild.get_member(player)
                    await ctx.send(f'{winner.mention} :gun: BANG!!!')
                    true = False
                    break
                else:
                    player = ctx.guild.get_member(player)
                    await ctx.send(f'{player.mention} :gun:')
        await winner.move_to(None)
        players.clear()
def setup(bot):
    bot.add_cog(russian_roulette(bot))
    logger.info(f'Loaded russian roulette')
