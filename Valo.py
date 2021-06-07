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
  
@bot.command(name='내전4')
async def team4(ctx,player1,player2,player3,player4,player5,player6,player7,player8) :
    team = []
    team.append(player1)
    team.append(player3)
    team.append(player3)
    team.append(player4)
    team.append(player5)
    team.append(player6)
    team.append(player7)
    team.append(player8)
    random.shuffle(team)
    embed = discord.Embed(title = "※ 4vs4 내전 팀 ※", description = f"**1팀**\n{team[0]}\t{team[1]}\t{team[2]}\t{team[3]}\n\n**2팀**\n{team[4]}\t{team[5]}\t{team[6]}\t{team[7]}\n", color = 0x00ff00)
    embed.set_footer(text = f"{ctx.message.author.name} | 절대 내전해", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command(name='내전5')
async def team4(ctx,player1,player2,player3,player4,player5,player6,player7,player8,player9,player10) :
    team = []
    team.append(player1)
    team.append(player2)
    team.append(player3)
    team.append(player4)
    team.append(player5)
    team.append(player6)
    team.append(player7)
    team.append(player8)
    team.append(player9)
    team.append(player10)
    random.shuffle(team)
    embed = discord.Embed(title = "※ 5vs5 내전 팀 ※", description = f"**1팀**\n{team[0]}\t{team[1]}\t{team[2]}\t{team[3]}\t{team[4]}\n\n**2팀**\n{team[5]}\t{team[6]}\t{team[7]}\t{team[8]}\t{team[9]}\n", color = 0x00ff00)
    embed.set_footer(text = f"{ctx.message.author.name} | 절대 내전해", icon_url = ctx.message.author.avatar_url)
    await ctx.send(embed = embed)

@bot.command(name='캐릭터')
async def vlc(ctx) :
    char = ["피닉스","제트","레이즈","레이나","요루","브림스톤","바이퍼","오멘","아스트라","킬조이","사이퍼","스카이","브리치","소바","세이지"]
    rnd = random.randint(1,15)
    await ctx.send(char[rnd])

@bot.command(name='맵')
async def vlm(ctx) :
    map = ["헤이븐","스플릿","바인드","아이스박스","어센트"]
    rnd = random.randint(1,5)
    await ctx.send(map[rnd])

bot.run(token)