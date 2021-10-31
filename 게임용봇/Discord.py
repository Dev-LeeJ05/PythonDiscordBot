#region import
import discord, json
from discord.ext import commands
#endregion

#region bot init
with open('token.json') as json_file:
    json_data = json.load(json_file)
token = json_data["token"]

client = discord.Client()
bot = commands.Bot(command_prefix = 'm ', help_command = None)
#endregion

#region bot event
@bot.event
async def on_ready() :
    print(f'부팅 성공 : {bot.user.name}!')
    game = discord.Game("Beta V.1")
    await bot.change_presence(status = discord.Status.online, activity = game)
#endregion

#region bot command

#endregion
bot.run(token)