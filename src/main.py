import discord
from bot_instance import bot

import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

@bot.event
async def on_ready(): 
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    
cogs = [
    'about',
    'confess'
]

for cog in cogs:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)