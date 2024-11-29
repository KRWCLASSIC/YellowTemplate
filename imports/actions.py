# External Imports
import discord
import re

# Internal Imports
from imports.functions import *
from imports.global_setup import bot, ver, config

# Some variables and arrays
admin_ids = config['settings']['admin_ids']

async def on_ready():
    await bot.tree.sync()

    print('')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('   ASCII ART WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOO OOOO OOO OO O  O   O')
    print('')

    print(f'Bot is online! Logged in as {bot.user}')
    print(f'Yellow Template ver. {ver}')
    for guild in bot.guilds:
        print(f'- {guild.name}')

async def on_member_join(member):
    return

async def on_reaction_add(reaction, user):
    return

async def on_member_update(before: discord.Member, after: discord.Member):
    return

async def on_message(message):
    if bot.user in message.mentions and message.author != bot.user:
        content = message.content.lower()
        if re.search(r'\bexample_command\b', content):
            #await function_name(message)
            return # remove that
        elif re.search(r'\bsecond\b', content):
            #await second_function(message)
            return # remove that
        return  # Exit early if the bot is mentioned with its own commands
