import discord
from discord.ext import commands

token = "OTAzMjcxNTY0MTEwMzY0NzY0.YXqjMg.JYgQsZrA-F6HAEmVkp_VMe62Ad4"

client = discord.Client()
bot = commands.Bot(command_prefix = '검색아 ', help_command = None)

@bot.event # Bot 온라인 접속 이벤트
async def on_ready() :
    print(f'부팅 성공 : {bot.user.name}!')
    game = discord.Game("\"검색아 도움\"을 쳐보세요")
    await bot.change_presence(status = discord.Status.online, activity = game)
 
@bot.command(name='도움')
async def Help(ctx):
    embed = discord.Embed(title=f"{bot.user.name}의 도움말", description=f"**검색아 유니티 [검색 단어]**\n유니티 문서에서 [검색 단어]를 검색합니다.\n\n**검색아 네이버 [검색단어]**\n네이버에서 [검색 단어]를 검색합니다.\n\n**검색아 구글 [검색 단어]**\n구글에서 [검색 단어]를 검색합니다.", color=0xffffff)
    await ctx.send(embed=embed)

@bot.command(name='유니티')
async def UnitySearch(ctx, search : str):
    domain = "https://docs.unity3d.com/Manual/30_search.html?q="
    embed = discord.Embed(title=f"유니티 문서 내에서 다음 내용을 검색합니다. [{search}]", description=f"{domain}{search}", color=0xffffff)
    await ctx.send(embed=embed)

@bot.command(name="네이버")
async def NaverSearch(ctx, search : str):
    domain = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
    embed = discord.Embed(title=f"네이버에서 다음 내용을 검색합니다. [{search}]", description=f"{domain}{search}", color=0xffffff)
    await ctx.send(embed=embed)

@bot.command(name="구글")
async def GoogleSearch(ctx, search : str):
    domain = "https://www.google.com/search?q="
    embed = discord.Embed(title=f"구글에서 다음 내용을 검색합니다. [{search}]", description=f"{domain}{search}", color=0xffffff)
    await ctx.send(embed=embed)

bot.run(token)