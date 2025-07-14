import discord
from bot_instance import bot
from funcs.db import create_db

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

@bot.event
async def on_ready():
    await create_db()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    
cogs = [
    'about',
    'confess'
]

for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)