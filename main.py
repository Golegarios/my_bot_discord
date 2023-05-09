import discord
from discord.ext import commands

#Compreendo que foi falta de profissionalismo meu nos codigos ou versões anteriores de não verificar antes de enviar.
#Deixando claro que sou um desenvolvedor Brasileiro e que "kkkkk" independe da quantidade aqui significa risada.

prefix = '?'
intents = discord.Intents().all()
bot = commands.Bot(command_prefix=prefix, intents=intents)

# Funções Passivas
@bot.event
async def on_ready():
    guild = bot.guilds[0]
    nick_name = bot.user.name
    member = guild.get_member(bot.user.id)
    print(f'Logado em {nick_name}') # Diz que está logado no console
    await bot.change_presence(activity=discord.Game("exemplo de jogo")) # Aqui diz oq ele esta jogando
    await member.edit(nick=f'[{prefix}]{nick_name}') # Nome fixo do bot com prefixo desde o inicio

# Daqui em diante é apenas comando, estou pensando em por um sistema de classes
@bot.command()
async def oi(msg):
    await msg.send('Olá!')
    
# Aqui é só o Token
bot.run('Digite seu token')