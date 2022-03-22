#Cog Events
import os
import random 
import re
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import praw

class Admin(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #Clear Command
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def clear(self, ctx, amount=100):
    '''Clears the last 100 Messages (only works for Messages of the last 14 Days)'''
    await ctx.channel.purge(limit=amount)

  #Kick Command
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def kick(self, ctx, member: discord.Member, *, reason=None):
    '''Kicks the Pinged Member (-kick @willi#6392)'''
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has kicked.')

  #Ban Command
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def ban(self, ctx, member: discord.Member, *, reason=None):
    '''Bans the Pinged Member (-Ban @willi#6392)'''
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has baned.')
          
  #Tictactoe End Commad
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def endTTT(self, ctx):
        '''Ends a Tictactoe Match'''
        # We need to declare them as global first
        global count
        global player1
        global player2
        global turn
        global gameOver
        
        # Assign their initial value
        count = 0
        player1 = ""
        player2 = ""
        turn = ""
        gameOver = True

        # Now print your message or whatever you want
        myEmbed = discord.Embed(title= "RESET GAME",description="TO START A NEW GAME, USE !tictactoe COMMAND",color=0xF85252)
        await ctx.send(embed=myEmbed)
  

def setup(bot):
  bot.add_cog(Admin(bot))

