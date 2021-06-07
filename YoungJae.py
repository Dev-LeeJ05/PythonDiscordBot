import discord, random
from discord.ext import commands
import json

with open('token.json') as json_file:
    json_data = json.load(json_file)
token = json_data["token"]

client = discord.Client()
bot = commands.Bot(command_prefix = 'm ', help_command = None)

@bot.event # Bot 온라인 접속 이벤트
async def on_ready() :
    print(f'부팅 성공 : {bot.user.name}!')
    game = discord.Game("Beta V.1")
    await bot.change_presence(status = discord.Status.online, activity = game)

@bot.command(name="영재운동해")
async def exercise(ctx):
    exers =  ["스쿼트","팔굽혀펴기","버피", "턱걸이", "사레레", "윗몸일으키기"]
    exer_cnt = random.randint(0,len(exers)/2)
    ex_cnt_set = ""
    for i in range(0,exer_cnt+1):
        exers_cnt = random.randint(0,len(exers))
        sets = random.randint(1, 5)
        count = random.randint(10,15)
        ex = exers[exers_cnt]
        exers.remove(ex)
        ex_cnt_set = ex_cnt_set+f"**{i+1}번**. ``{ex}``를 {count}개씩 {sets}세트 하면 되겠다!\n"  
    embed = discord.Embed(title=f"오늘은 {exer_cnt+1}개의 종류를 하면 되겠다!",description=ex_cnt_set,color=0xffffff)
    await ctx.send(embed=embed)

bot.run(token)