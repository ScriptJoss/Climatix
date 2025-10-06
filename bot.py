import discord
import requests
from discord.ext import commands
import config  # Importación explícita

# Privilegios o permisos
intents = discord.Intents.default()
intents.message_content = True

# Transferimos los privilegios al bot
bot = commands.Bot(command_prefix=config.settings["prefix"], intents=intents)


# Evento on_ready
@bot.event
async def on_ready():
    print(f"✅ {bot.user} está conectado. ¡Listo para recibir comandos!")


@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! El bot está funcionando correctamente.")


@bot.command()
async def clima(ctx, *, ciudad: str = None):
    if not ciudad:
        await ctx.send(
            "🌍 Escribe el nombre de una ciudad para ver la temperatura.\n"
            "Ejemplo: `!clima Bogotá`"
        )
        return

    url = ("https://api.openweathermap.org/data/2.5/"
           f"weather?q={ciudad}&appid={config.settings["API_KEY"]}"
           "&units=metric&lang=es"
           )

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            datos = response.json()
            temp = datos["main"]["temp"]
            descripcion = datos["weather"][0]["description"]
            ciudad_nombre = datos["name"]

            await ctx.send(
                f"🌡️ La temperatura actual en **{ciudad_nombre}** "
                f"es de **{temp}°C**"
                f"con un clima **{descripcion}.**"
            )
        else:
            await ctx.send(
                "⚠️ No se pudo obtener la temperatura. "
                "Verifica el nombre de la ciudad e intenta de nuevo."
            )
    except requests.RequestException:
        await ctx.send(
            "❌ Hubo un problema al consultar la temperatura. "
            "Por favor, intenta más tarde."
        )

bot.run(config.settings["token"])
