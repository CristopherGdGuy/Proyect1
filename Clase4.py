import discord
from discord.ext import commands

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.event
async def hello(ctx):
    await ctx.send('hi')

@bot.event
async def bye(ctx):
    await ctx.send('\\U0001f642')

@bot.event
async def calculadora(ctx):
    await ctx.send("Que quieres hacer")
    await ctx.send("Escribe sumar")
    await ctx.send("Escribe restar")
    await ctx.send("Escribe multiplicar")
    await ctx.send("Escribe dividir")

#Bot en desarrollo aun estoy investigando de como sumar y restar

bot.run("")
