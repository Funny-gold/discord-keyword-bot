import discord
import requests
import os

TOKEN = os.getenv("DISCORD_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

KEYWORDS = [
    "announcement",
    "release",
    "song of the elves",
    "important",
    "update",
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
