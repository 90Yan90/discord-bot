import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

# Загружаем переменные окружения из файла .env
load_dotenv()

# Получаем токен из переменной окружения
token = os.getenv("DISCORD_TOKEN")

# Создаём бота с нужными интентами
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Пример скриптов
light_scripts = {
    "1 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 18\nжди 5",
    "2 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 19\nжди 5",
    "3 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 20\nжди 5",
    "4 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 21\nжди 5",
    "5 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 22\nжди 5",
    "6 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 23\nжди 5",
    "7 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 24\nжди 5",
    "8 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 25\nжди 5",
    "9 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 26\nжди 5",
    "10 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 27\nжди 5",
    "11 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 28\nжди 5",
    "12 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 29\nжди 5",
    "13 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 30\nжди 5",
    "14 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 0\nжди 5\nслот 31\nжди 5",
    "15 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 18\nжди 5",
    "16 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 19\nжди 5",
    "17 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 20\nжди 5",
    "18 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 21\nжди 5",
    "19 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 22\nжди 5",
    "20 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 23\nжди 5",
    "21 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 24\nжди 5",
    "22 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 25\nжди 5",
    "23 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 26\nжди 5",
    "24 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 27\nжди 5",
    "25 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 28\nжди 5",
    "26 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 29\nжди 5",
    "27 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 30\nжди 5",
    "28 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 31\nжди 5",
    "29 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 32\nжди 5",
    "30 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 33\nжди 5",
    "31 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 1\nжди 5\nслот 34\nжди 5",
    "32 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 18\nжди 5",
    "33 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 19\nжди 5",
    "34 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 20\nжди 5",
    "35 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 21\nжди 5",
    "36 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 22\nжди 5",
    "37 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 23\nжди 5",
    "38 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 24\nжди 5",
    "39 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 25\nжди 5",
    "40 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 26\nжди 5",
    "41 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 27\nжди 5",
    "42 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 28\nжди 5",
    "43 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 29\nжди 5",
    "44 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 30\nжди 5",
    "45 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 31\nжди 5",
    "46 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 18\nжди 5",
    "47 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 19\nжди 5",
    "48 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 2\nжди 5\nслот 20\nжди 5",
    "49 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 21\nжди 5",
    "50 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 22\nжди 5",
    "51 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 23\nжди 5",
    "52 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 24\nжди 5",
    "53 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 25\nжди 5",
    "54 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 26\nжди 5",
    "55 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 27\nжди 5",
    "56 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 28\nжди 5",
    "57 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 29\nжди 5",
    "58 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 30\nжди 5",
    "59 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 31\nжди 5",
    "60 лайт": "жди 30\nпкм\nжди 5\nслот 12\nжди 5\nслот 3\nжди 5\nслот 32\nжди 5",
}

classic_scripts = {
    "1 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 1\nжди 5",
    "2 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 3\nжди 5",
    "3 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 5\nжди 5",
    "4 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 7\nжди 5",
    "5 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 11\nжди 5",
    "6 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 13\nжди 5",
    "7 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 15\nжди 5",
    "8 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 19\nжди 5",
    "9 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 21\nжди 5",
    "10 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 23\nжди 5",
    "11 классик": "жди 30\nпкм\nжди 5\nслот 15\nжди 5\nслот 25\nжди 5",
}

# Дополнительные команды
extra_commands = {
    "копание": "копание старт",
    "фармить": "кликер включить",
    "рыбачить": "рыбалка включить",
    "установка": "установка включить",
    "ягоды": "сбор включить",
    "нарост": "жатва старт",
    "афк": "ожидание"
}

@bot.command()
async def скрипт(ctx, *, args):
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        print("Нет прав на удаление сообщения.")

    parts = args.lower().split()
    if len(parts) < 2:
        await ctx.author.send("Укажи название анархии или классики, например: `15 лайт` или `3 классика`.")
        return

    base_key = " ".join(parts[:2])
    modes = parts[2:]

    script = light_scripts.get(base_key) or classic_scripts.get(base_key)
    if not script:
        try:
            await ctx.author.send("Скрипт не найден.")
        except discord.Forbidden:
            await ctx.send(f"{ctx.author.mention}, открой ЛС, чтобы получить скрипт.")
        return

    for mode in modes:
        if mode in extra_commands:
            script += f"\n{extra_commands[mode]}"

    try:
        await ctx.author.send(f"Вот твой скрипт для `{base_key}`:\n```{script}```")
    except discord.Forbidden:
        await ctx.send(f"{ctx.author.mention}, не удалось отправить скрипт — включи ЛС от участников сервера.")

# Запуск бота с токеном из переменной окружения
bot.run(token)
