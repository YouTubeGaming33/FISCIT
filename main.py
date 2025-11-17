# Required Imports
import discord
from discord.ext import commands

import os, asyncio

from core.config import BOT_TOKEN, GUILD_ID

# Discord Intents - Access to Everything.
intents = discord.Intents.all()

# Discord API Token
TOKEN = str(BOT_TOKEN)

# Class for FISCIT Bot
class FISCIT(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=intents)
    
    # Loads all Seperate Modules 
    async def setup_hook(self):
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")
                print(f"Successfully loaded Cog: {filename}")

        # Try, Except for Syncing Commands to Guild.
        try:
            guildCommands = await self.tree.sync(guild=GUILD_ID)
            print (f"[RUN TIME] {len(guildCommands)} Groups Synced")
        except Exception as e:
            print (f"[RUN TIME] Failed to Sync Groups: {e}")

# Passing FISCIT() Class to bot Variable
bot = FISCIT()

# Asyncrious Function for Updating Activity
async def update_activity():
    activity = discord.Activity(
        type=discord.ActivityType.playing,
        name=("Satisfactory")
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)

# Event Listener for Bot starting
@bot.event
async def on_ready():
    await update_activity()
    print (f"[RUN TIME] Bot Activity Set - Logged on as {bot.user}")

# Asyncrious Function for Running Bot.
async def main():
    async with bot:
        await bot.start(TOKEN)

# Asyncio run command for Main.
asyncio.run(main())