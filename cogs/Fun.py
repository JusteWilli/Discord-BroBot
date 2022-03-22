#Cog Events
import os
import random 
import re
import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import praw
class Fun(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #Meme
  @commands.command(aliases=['Meme'])
  async def meme(self, ctx):
    '''Send a Random Meme from Reddit'''
    reddit = praw.Reddit(client_id='t50mR06A8btuxfmkcos7JA',
                        client_secret='5e5ZeNOSDEKhCz43D5aFiVJS5f-ang',
                        user_agent='Bro Discord Bot')
    submission = reddit.subreddit("memes").random()
    await ctx.send(submission.url)



  #Dog
  @commands.command(aliases=['Dog'])
  async def dog(self, ctx):
    '''Send a Random Dog pic from Reddit'''
    reddit = praw.Reddit(client_id='t50mR06A8btuxfmkcos7JA',
                        client_secret='5e5ZeNOSDEKhCz43D5aFiVJS5f-ang',
                        user_agent='Bro Discord Bot')
    submission = reddit.subreddit("Dog").random()
    await ctx.send(submission.url)

    
  #Sum Two Number
  @commands.command()
  async def sum(self, ctx, numOne: int, numTwo: int):
    '''Sum 2 nummbers (-sum Num1 Num2)'''
    embed = discord.Embed(title="Sum Number",
    description=(numOne + numTwo),
    color=(0xF85252))
    await ctx.send(embed=embed)


  #UWU
  @commands.command()
  async def uwu(self, ctx):
    '''lol idk'''
    embed = discord.Embed(title="uwu",
    description=("Du Junge, ich gib dir gleich uwu"),
    color=(0xF85252))
    await ctx.send(embed=embed)


  #Rock Paper Scissors
  @commands.command()
  async def rps(self, ctx, message):
    #Description
    '''Guess you opponent choice and take the opposite (-rps Rock/Paper/Scissors)'''
    answer = message.lower()
    #Choices
    choices = ["rock", "paper", "scissors"]
    #Random computer choice
    computers_answer = random.choice(choices)
    #Check if Choice is a valid option
    if answer not in choices:
      embed = discord.Embed(title=("Not a valid option!"),
                          description=("Please use one of these options: rock, paper, scissors"),
                          color=(0xF85252))
      await ctx.send(embed=embed)
      return
    #Else valid option
    else:
        if computers_answer == answer:
            await ctx.send(f"Tie! We both picked {answer} ")
        if computers_answer == "rock":
            if answer == "paper":
                embed = discord.Embed(title=("You win!"),
                          description=(f"You win! I picked {computers_answer} and you picked {answer}"),
                          color=(0xF85252))
                await ctx.send(embed=embed)
        if computers_answer == "paper":
            if answer == "rock":
                embed = discord.Embed(title=("You lose!"),
                          description=(f"I picked {computers_answer} and you picked {answer}"),
                          color=(0xF85252))
                await ctx.send(embed=embed)
        if computers_answer == "scissors":
            if answer == "rock":
                embed = discord.Embed(title=("You win!"),
                          description=(f"You win! I picked {computers_answer} and you picked {answer}"),
                          color=(0xF85252))
                await ctx.send(embed=embed)
        if computers_answer == "rock":
            if answer == "scissors":
                embed = discord.Embed(title=("You lose!"),
                          description=(f"I picked {computers_answer} and you picked {answer}"),
                          color=(0xF85252))
                await ctx.send(embed=embed)
        if computers_answer == "paper":
            if answer == "scissors":
              embed = discord.Embed(title=("You win!"),
                          description=(f"You win! I picked {computers_answer} and you picked {answer}"),
                          color=(0xF85252))
              await ctx.send(embed=embed)
        if computers_answer == "scissors":
            if answer == "paper":
              embed = discord.Embed(title=("You lose!"),
                          description=(f"I picked {computers_answer} and you picked {answer}"),
                          color=(0xF85252))
              await ctx.send(embed=embed)
  

  #Roll dice
  @commands.command(pass_context=True)
  async def rdice(self, ctx):
    #Description
    """Random Number between 1-6"""
    embed = discord.Embed(title="Roll dice 1 - 6",
                          #Choice a Random number between 1 and 6
                          description=(random.randint(1, 6)),
                          color=(0xF85252))
    await ctx.send(embed=embed)
  
  #Random Number
  @commands.command(pass_context=True)
  async def rnumber(self, ctx, numOne2: int, numTwo2: int):
    #Description
    """Random Number (-rnumber Num1 Num2)"""
    embed = discord.Embed(title=("Random Number between"),
                          #Choice a Random number between numOne2 and numTwo2
                          description=(random.randint(numOne2, numTwo2)),
                          color=(0xF85252))
    await ctx.send(embed=embed)

  #Guessnumber
  @commands.command()
  async def guessnumber(self, ctx, message):
      #Description
      '''Guess a random Nummber between 1 and 100 '''
      answer = message.lower()
      #Choices
      choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100"]
      #Random computer choice
      computers_answer = random.choice(choices)
      #Check if Choice is a valid option
      if answer not in choices:
        embed = discord.Embed(title=("Not a valid option!"),
                          description=("Please use one of these options: 1-100"),
                          color=(0xF85252))
        await ctx.send(embed=embed)
        return
      #Else valid option
      else:
        #Check if computer_aswer = answer
        if computers_answer == answer:
          embed = discord.Embed(title=("You win!"),
                          description=(f"The Nummber is {answer} "),
                          color=(0xF85252))
          await ctx.send(embed=embed)
        #Else Lose
        else:
          embed = discord.Embed(title=("You lose!"),
                          description=(f"You lose! The Nummber was {computers_answer} and you picked {answer}!"),
                          color=(0xF85252))
          await ctx.send(embed=embed)
          
  #Coinflip
  @commands.command()
  async def coinflip(self, ctx,  message):
    #Description
    '''Guess if the Coin land up or down (-coinflip up/down)'''
    answer = message.lower()
    #Choices
    choices = ["down", "up",]
    #Random computer choice
    computers_answer = random.choice(choices)
    #Check if Choice is a valid option
    if answer not in choices:
      embed = discord.Embed(title=("Not a valid option!"),
                          description=("Please use one of these options: up, down"),
                          color=(0xF85252))
      await ctx.send(embed=embed)
      return
    #Else valid option
    else:
        #Check if computer_aswer = answer
        if computers_answer == answer:
          embed = discord.Embed(title=("You win!"),
                          description=(f"The coin flipped {answer}!"),
                          color=(0xF85252))
          await ctx.send(embed=embed)
        #Else Lose
        else:
          embed = discord.Embed(title=("You lose!"),
                          description=(f"The coin Flipped {computers_answer} and you picked {answer}!"),
                          color=(0xF85252))
          await ctx.send(embed=embed)



  #Lotto
  @commands.command()
  async def dan(self, ctx, num1, num2, num3):
    #Description
    '''Guess 3 numbers between 1-99 (-dan 1 2 3)'''
    #Choices
    choices = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99"]
    #Makes the nums to answer
    answer1 = num1
    answer2 = num2
    answer3 = num3
    #Random computer choice
    computers_answer1 = random.choice(choices)
    computers_answer2 = random.choice(choices)
    computers_answer3 = random.choice(choices)
    #Check if Choice is a valid option
    if answer1 and answer2 and answer3 not in choices:
      embed = discord.Embed(title=("Not a valid option!"),
                          description=("Please use one of these options: 3 number between 1-99"),
                          color=(0xF85252))
      await ctx.send(embed=embed)
      return
    #Else valid option
    else:
        #Check if computer_aswer = answer
        if computers_answer1 == answer1 and computers_answer2 == answer2 and computers_answer3 == answer3:
          embed = discord.Embed(title=("You win,"),
                          description=(f" you took {answer1}, {answer2}, {answer3}"),
                          color=(0xF85252))
          await ctx.send(embed=embed)
        #Else Lose
        else:
          embed = discord.Embed(title=("You lose,"),
                          description=(f" you took {answer1}, {answer2}, {answer3}, the correct numbers were {computers_answer1}, {computers_answer2}, {computers_answer3}"),
                          color=(0xF85252))
          await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Fun(bot))