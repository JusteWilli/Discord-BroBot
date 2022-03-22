#Cog Events
import os
import random 
import re
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import praw
import time

class Tools(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(pass_context=True)
  async def verify(self, ctx):
    role = ctx.guild.roles, name="Regeln"
    if ctx.channel.id == 939245820048441364:
        await ctx.message.delete()
        await ctx.send(f"{ctx.author.mention} has been verified.")

        await ctx.channel.purge(limit = 1)
        await ctx.author.add_roles(role)
    else:
        await ctx.message.delete()
        await ctx.send("You can not verify here.")


def setup(bot):
  bot.add_cog(Tools(bot))