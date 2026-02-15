import discord
import requests
import os

TOKEN = os.getenv("DISCORD_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

KEYWORDS = [
    "song of the elves",
    "lunar diplomacy",
    "monkey madness ii",
    "fairytale part ii",
    "while guthix sleeps",
    "heroes quest",
    "recipe for disaster",
    "the curse of arrav",
    "the final dawn",
    "roving elves",
    "dragon slayer ii",
    "secrets of the north",
    "making friends with my arm",
    "perilous moons",
    "mourning's end part ii",
    "a kingdom divided",
    "king's ransom",
    "the fremennik exiles",
    "desert treasure i",
    "desert treasure ii",
    "defender of varrock",
    "sins of the father",
    "dream mentor",
    "beneath cursed sands",
]

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()

    if any(k in content for k in KEYWORDS):
        requests.post(WEBHOOK_URL, json={
            "user": str(message.author),
            "message": message.content,
            "channel": message.channel.name
        })

bot.run(TOKEN)
