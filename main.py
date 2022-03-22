from http import client
import os
import random 
import re
from tokenize import Token
import discord
from discord.ext import commands

from urllib import parse, request
from discord.ext.commands.bot import Bot
import praw
from discord_slash import SlashCommand





bot = commands.Bot(command_prefix='B/', description="Need Help? Contact @willi#6392")
slash = SlashCommand(bot, sync_commands=True)

#Help Command
class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=discord.Color.red(), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = MyHelpCommand()

#Main 
cogs =['cogs.Admin','cogs.Fun','cogs.Tools']

for cog in cogs:
  try:
    bot.load_extension(cog)
  except Exception as e:
    print(f'Could not load cog{cog}: {str(e)}')
#
#
#
# 

#
#
@slash.slash()
async def hi(ctx):
    if ctx.author.id == 697757488455483453:
        await ctx.send('Hey, Willi Alexander')
    elif ctx.author.id == 844445600770031658:
        await ctx.send('Hi, Max Werner!')
    elif ctx.author.id == 884886198353555456:
        await ctx.send('Hallo, Willis 2. Account')


@slash.slash()
async def ping(ctx):
    await ctx.send("pong")

@slash.slash()
async def Hänchen(ctx):
    if ctx.channel.id == 935541414761205893:
        """       embed = discord.Embed(title=("Hänchen"),
                          description=(ctx.message.author + "hat ein Hänchen bekommen"),
                          color=(0xF85252))
        await ctx.send(embed=embed)
        """
        await ctx.send("Hier ein Hänchen")
    elif ctx.channel.id == 935537915398881333:
        await ctx.send("Das ist kein Meme")
    elif ctx.channel.id == 935536919960489984:
        await ctx.send("Das ist keine Musik")
    else:
        await ctx.send("Du bekommst keins")
my_secret = os.environ['Client_Secret']

#
#
#helper


#Tictactoe
player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@bot.command()
async def tictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2

        # print the board
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]

        # determine who goes first
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@bot.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1

                # print the board
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")

                # switch turns
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 (inclusive) and an unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the !tictactoe command.")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")

#Tictactoe End Commad
@slash.slash()
@commands.has_permissions(administrator=True)
async def endttt(ctx):
    '''(Ends a Tictactoe Match)'''
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


#Bod Boddy
@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="B/Help"))
  print(f'{bot.user.name} is online. ID: {bot.user.id} ')



@bot.event
async def on_ready():
  await bot.get_channel(935552190557339668).send("I'm online")
  print("Hi")

bot.run(os.environ['Token'])