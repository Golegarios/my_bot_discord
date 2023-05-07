import discord
from discord.ext import commands

#Compreendo que foi falta de profissionalismo meu nos codigos ou versões anteriores de não verificar antes de enviar.
#Deixando claro que sou um desenvolvedor Brasileiro e que "kkkkk" independe da quantidade aqui significa risada.

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='?', intents=intents)
# Esse aqui apenas mostra informações no console
@bot.event
async def on_ready():
    print(f'Logado em {bot.user.name}')

# Daqui em diante é apenas comando, estou pensando em por um sistema de classes
@bot.command()
async def oi(msg):
    await msg.send('Olá!')
    
# Aqui é só o Token
bot.run('Digite aqui seu token')