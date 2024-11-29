# External Imports
from discord.ext import commands
import discord
import toml

# Internal Imports
from imports.update import *

# Version Variable
ver = '1.0'

# Enable some permissions
intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.messages = True
intents.members = True
intents.guilds = True

# Register the bot variable
bot = commands.Bot(command_prefix="", intents=intents, sync_commands=True)

# Load the config file
config = toml.load('files/installation/config.toml')