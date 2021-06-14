import discord, json
from discord.ext import commands

with open('token.json') as json_file:
    json_data = json.load(json_file)
token = json_data["token"]

client = discord.Client()
bot = commands.Bot(command_prefix = 'm ', help_command = None)

bot.run(token)