from discord.ext import commands

bot = commands.Bot(command_prefix='?')

@bot.event
async def on_ready():
    print(f'Logado em {bot.user.name}')

@bot.command
async def oi(mensagem):
    await mensagem.send('Olá!')