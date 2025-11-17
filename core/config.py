# Required Imports
import discord
import os

from dotenv import load_dotenv

# Load .env File
load_dotenv()

# Pull Bot Token from .env and Define Guild ID
BOT_TOKEN = os.getenv("BOT_TOKEN")
GUILD_ID = discord.Object(id=1439444974096748616)