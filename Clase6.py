import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Habilita el contenido del mensaje

bot = commands.Bot(command_prefix='$', intents=intents, help_command=None)  # Deshabilitar el comando help por defecto

@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def ayuda(ctx):
    await ctx.send("Intenta los siguientes comandos:")
    await ctx.send("$reciclaje1")
    await ctx.send("$reciclaje2")
    await ctx.send("$general")

@bot.command()
async def reciclaje1(ctx):
    await ctx.send("Desenchufa los aparatos electrónicos que no estés usando.")
    await ctx.send("También, puedes hacer decoración con plástico y cartón.")
    await ctx.send("Y por último, evita botar la basura a la naturaleza.")

@bot.command()
async def reciclaje2(ctx):
    consejos = (
        "🗑️ **Consejos para Reciclar Correctamente** 🗑️\n"
        "1. **Limpia tus materiales**: Asegúrate de que los envases estén limpios y secos.\n"
        "2. **No mezcles materiales**: Separa plásticos, papel, vidrio y metales.\n"
        "3. **Infórmate sobre las normas locales**: Cada lugar tiene sus propias reglas de reciclaje.\n"
        "4. **Reduce y reutiliza**: Antes de reciclar, considera si puedes reducir el uso o reutilizar el material."
    )
    await ctx.send(consejos)

@bot.command()
async def general(ctx):
    """Proporciona información general sobre el reciclaje."""
    info = (
        "🌍 **Información sobre Reciclaje** 🌍\n"
        "El reciclaje es el proceso de convertir materiales usados en nuevos productos. "
        "Esto ayuda a reducir el consumo de materias primas, la energía utilizada en la producción "
        "y la contaminación. Aquí hay algunos materiales que se pueden reciclar:\n"
        "- **Plástico**: Botellas, envases, bolsas (verifica el símbolo de reciclaje).\n"
        "- **Papel**: Periódicos, cartón, papel de oficina.\n"
        "- **Vidrio**: Botellas y frascos.\n"
        "- **Metales**: Latas de aluminio y acero.\n"
        "Recuerda siempre limpiar y secar los materiales antes de reciclarlos."
    )
    await ctx.send(info)

bot.run("")
