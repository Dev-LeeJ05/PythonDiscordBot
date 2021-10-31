import discord, random,datetime
from discord.ext import commands
import asyncio,json

token = "NTIwOTQ5MDkxNDAwOTQxNTg4.XAvBpg.C4Ia38nlOJJpkRgbwLMvh3XvUtY"
client = discord.Client()
bot = commands.Bot(command_prefix = 'm ', help_command = None)

@bot.event # Bot 온라인 접속 이벤트
async def on_ready() :
    print(f'부팅 성공 : {bot.user.name}!')
    game = discord.Game("Beta V.1")
    await bot.change_presence(status = discord.Status.online, activity = game)
  
@bot.event #bad word
async def on_message(message):
    if message.content.startswith("!시간"):
        await message.channel.send(embed=discord.Embed(title="Time", timestamp=datetime.datetime.utcnow()))
    if message.content.startswith("안녕"):
        await message.channel.send("반가워!")
    if message.content.startswith("영재는?"):
        await message.channel.send("꾸익꾸익!")
    
    message_content = message.content
    bad = []
    bad.append(message_content.find("시팔"))
    bad.append(message_content.find("씨발"))
    bad.append(message_content.find("시발"))
    bad.append(message_content.find("ㅅ@발"))
    bad.append(message_content.find("ㅅㅍ"))
    bad.append(message_content.find("씨팔"))
    bad.append(message_content.find("싸발"))
    bad.append(message_content.find("찌발"))
    bad.append(message_content.find("ㅈㄲ"))
    bad.append(message_content.find("ㅗ"))
    bad.append(message_content.find("찌"))
    bad.append(message_content.find("씨"))

    for index in range(0,len(bad)):
        print(bad[index])
        if bad[index] >= 0:
            print(message)
            await message.delete()
            await message.channel.send("No KKap")
    await bot.process_commands(message)

@bot.command(name='주사위')
async def roll(ctx) :
    rnd = random.randint(1,6)
    await ctx.send(rnd)

@bot.command(name='홀짝')
async def single_multi(ctx) :
    rnd = random.randint(0,99)
    rnd = rnd % 2
    print(rnd)
    if rnd == 0:
        await ctx.send("짝")
    else:
        await ctx.send("홀")

@bot.command(name="청소")
async def clear(ctx,count : int):
    await ctx.channel.purge(limit=count)
    await ctx.send(str(count)+"개의 채팅이 청소 되었습니다!")
    print("청소 완료!")

@bot.command(name='잭팟')
async def rollet(ctx) :

    for j in range(0,1):
        rolling = '돌리는 중'
        msg = await ctx.send(rolling)
        for i in range(0,3):
            rolling = rolling + '.'
            await asyncio.sleep(0.1)
            await msg.edit(content=rolling)
        await ctx.channel.purge(limit=1) 


    rnd_1 = random.randint(1,9)
    rnd_2 = random.randint(1,9)
    rnd_3 = random.randint(1,9)

    print(rnd_1,rnd_2,rnd_3)
    if rnd_1 == rnd_2 :
        if rnd_1 == rnd_3 :
            embed = discord.Embed(title="잭팟", description = "**"+str(rnd_1)+" " + str(rnd_2) + " "+ str(rnd_3)+"**"+"\n당첨!\n축하합니다.", color = 0xFAFAD2)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="잭팟", description = "**"+str(rnd_1) + " " + str(rnd_2) +" " + str(rnd_3)+"**"+"\n아쉽네요.\n다시 도전하세요!", color = 0xFAFAD2)
        await ctx.send(embed=embed)

@bot.command(name='랜덤')
async def Rand(ctx, num1,num2) :
    await ctx.send(f'{random.randint(int(num1),int(num2))}')

@bot.command(name='가위바위보')
async def rsp(ctx, user : str) :
    rsp_table = ['가위','바위','보']
    bot = random.choice(rsp_table)
    result = rsp_table.index(user) - rsp_table.index(bot)
    if result ==0:
        embed = discord.Embed(title = "가위바위보", description=f"**당신**   **봇**\n{user}   {bot}\n비겼습니다.",color=0x000000)
        await ctx.send(embed=embed)
    elif result == -2 or result == 1 :
        embed = discord.Embed(title = "가위바위보", description=f"**당신**   **봇**\n{user}   {bot}\n당신이 이겼습니다.",color=0x000000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title = "가위바위보", description=f"**당신**   **봇**\n{user}   {bot}\n봇이 이겼습니다.",color=0x000000)
        await ctx.send(embed=embed)

bot.run(token)