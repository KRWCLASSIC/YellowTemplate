# External Imports
from urllib.parse import urlparse, urlunparse
from datetime import datetime
import subprocess
import discord
import asyncio
import random
import shutil
import json
import sys
import os
import re

# Internal Imports
from imports.functions import *
from imports.global_setup import bot, config

# Some variables
telemetry_file_path = config['telemetry']['file_path']
telemetry_enabled = config['telemetry']['enabled']
admin_ids = config['settings']['admin_ids']

# Async Functions
async def send_help(message):
    embed = discord.Embed(title="Bot Help", description="Here are the commands you can use:", color=0x00ff00)
    embed.add_field(name="@Bot example", value="example line of help.", inline=False)
    await message.channel.send(embed=embed)

# Functions
def restart():
    try:
        print("Bot is restarting...")
        os.execv(sys.executable, ['python'] + sys.argv)
        
    except Exception as e:
        print(f"Error during bot restart: {e}")

def remove_pycache():
    for root, dirs, files in os.walk('.'):
        for dir in dirs:
            if dir == '__pycache__':
                shutil.rmtree(os.path.join(root, dir))

def check_files(config, base_path=''):
    missing_files = []

    def scan_config(d, path_prefix=''):
        for key, value in d.items():
            if isinstance(value, dict):
                # Recursively scan nested dictionaries
                scan_config(value, path_prefix)
            elif isinstance(value, str) and ('.' in value or '/' in value or '\\' in value):
                # Check if the value looks like a file path
                file_path = os.path.join(base_path, value)
                if not os.path.exists(file_path):
                    missing_files.append(file_path)

    scan_config(config)

    if missing_files:
        print("\nMissing files:")

        for file in missing_files:
            print(f"  {file}")

        exit()
    else:
        print("\nAll required files are present.")

def log_telemetry(message):
    if telemetry_enabled:
        timestamp = datetime.now().isoformat()
        log_entry = {timestamp: message}
        
        if os.path.exists(telemetry_file_path):
            with open(telemetry_file_path, 'r', encoding='utf-8') as file:
                telemetry_data = json.load(file)
        else:
            telemetry_data = {"telemetry": {}}
        
        telemetry_data["telemetry"].update(log_entry)
        
        with open(telemetry_file_path, 'w', encoding='utf-8') as file:
            json.dump(telemetry_data, file, indent=4, ensure_ascii=False)

def print_and_log(message):
    print(message)
    log_telemetry(message)