import discord
import requests
from discord.ext import commands
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=config.settings["prefix"], intents=intents)


@bot.event
async def on_ready():
    # Status
    statusText = discord.Game("Consultando el clima 🌤️")
    await bot.change_presence(status=discord.Status.idle,
                              activity=statusText)
    print("✅ Status establecido correctamente.")
    print(f"✅ {bot.user} está conectado. ¡Listo para recibir comandos!")


@bot.event
async def on_message(message):
    # Ignora mensajes del propio bot
    if message.author == bot.user:
        return

    if message.content.strip() == config.settings["prefix"]:
        await message.channel.send(
            "❌ Escribe un comando después del prefijo.\n"
            "Usa `!helpop` para ver los comandos disponibles."
        )
        return

    # Permite que los comandos funcionen normalmente
    await bot.process_commands(message)


@bot.command()
async def helpop(ctx):
    message_description = (
        "`!temperatura <ciudad>` — Muestra la temperatura y clima actual.\n"
        "`!tempmax <ciudad>` — Muestra la temperatura máxima registrada.\n"
        "`!tempmin <ciudad>` — Muestra la temperatura mínima registrada.\n"
    )
    embed = discord.Embed(
        title="📖 Comandos:",
        description=message_description,
        color=discord.Color.red()
    )
    embed.set_footer(text="Comandos disponibles")
    await ctx.send(embed=embed)


@bot.command()
async def temperatura(ctx, *, ciudad: str = None):
    if not ciudad:
        await ctx.send(
            "🌍 Escribe el nombre de una ciudad para ver la temperatura.\n"
            "Ejemplo: `!temperatura Bogotá`"
        )
        return

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={ciudad}&appid={config.settings['API_KEY']}"
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
                f"🌡️ Temperatura en **{ciudad_nombre}**: **{temp}°C** "
                f"({descripcion})"
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


@bot.command()
async def tempmax(ctx, *, ciudad: str = None):
    if not ciudad:
        await ctx.send(
            "🌍 Escribe el nombre de una ciudad"
            "para ver la temperatura máxima.\n"
            "Ejemplo: `!tempmax Bogotá`"
        )
        return

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={ciudad}&appid={config.settings['API_KEY']}"
        "&units=metric&lang=es"
    )

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            datos = response.json()
            temp_max = datos["main"]["temp_max"]
            ciudad_nombre = datos["name"]

            await ctx.send(
                f"🌡️ Temperatura máxima en **{ciudad_nombre}"
                f"**: **{temp_max}°C**"
            )
        else:
            await ctx.send(
                "⚠️ No se pudo obtener la temperatura máxima. "
                "Verifica el nombre de la ciudad e intenta de nuevo."
            )
    except requests.RequestException:
        await ctx.send(
            "❌ Hubo un problema al consultar la temperatura máxima. "
            "Por favor, intenta más tarde."
        )


@bot.command()
async def tempmin(ctx, *, ciudad: str = None):
    if not ciudad:
        await ctx.send(
            "🌍 Escribe el nombre de una ciudad "
            "para ver la temperatura mínima.\n"
            "Ejemplo: `!tempmin Bogotá`"
        )
        return

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={ciudad}&appid={config.settings['API_KEY']}"
        "&units=metric&lang=es"
    )

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            datos = response.json()
            temp_min = datos["main"]["temp_min"]
            ciudad_nombre = datos["name"]

            await ctx.send(
                f"🌡️ Temperatura mínima en **{ciudad_nombre}"
                f"**: **{temp_min}°C**"
            )
        else:
            await ctx.send(
                "⚠️ No se pudo obtener la temperatura mínima. "
                "Verifica el nombre de la ciudad e intenta de nuevo."
            )
    except requests.RequestException:
        await ctx.send(
            "❌ Hubo un problema al consultar la temperatura mínima. "
            "Por favor, intenta más tarde."
        )


# Pronostico
@bot.command()
async def pronostico(ctx, *, ciudad: str = None):
    if not ciudad:
        await ctx.send(
            "🌍 Escribe el nombre de una ciudad "
            "para ver el pronóstico del clima.\n"
            "Ejemplo: `!pronostico Bogotá`"
        )
        return
    url = ("https://api.openweathermap.org/data/2.5/forecast")
    params = {
        "q": ciudad,
        "appid": config.settings["API_KEY"],
        "units": "metric",
        "lang": "es"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            datos = response.json()
            ciudad_nombre = datos["city"]["name"]
            pronosticos = datos["list"][:5]

            mensaje = f"🌤️ Pronóstico del clima para **{ciudad_nombre}**:\n"
            for pronosticar in pronosticos:
                hora = pronosticar["dt_txt"]
                temp = pronosticar["main"]["temp"]
                descripcion = pronosticar["weather"][0]["description"]
                mensaje += f"- {hora}: **{temp}°C** ({descripcion})\n"

            await ctx.send(mensaje)
        else:
            await ctx.send(
                "⚠️ No se pudo obtener el pronóstico. "
                "Verifica el nombre de la ciudad e intenta de nuevo."
            )
    except requests.RequestException:
        await ctx.send(
            "❌ Hubo un problema al consultar el pronóstico. "
            "Por favor, intenta más tarde."
        )

bot.run(config.settings["token"])
