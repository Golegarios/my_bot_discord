import discord
from discord.ext import commands

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='?', intents=intents)

@bot.event
async def on_ready():
    print(f'Logado em {bot.user.name}')

@bot.command()
async def oi(mensagem):
    await mensagem.send('Olá!')

#Acontece que na primeira versão eu esqueci de por a função token kkkkkkk
bot.run('Digite aqui seu token')