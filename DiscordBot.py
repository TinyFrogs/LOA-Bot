import asyncio, discord
import math
import os

from exam import *
from discord.ext import commands

bot = commands.Bot(command_prefix=".")


@bot.event
async def on_ready():
    print("We have loggedd in as {0.user}".format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(".명령어(회랑, 회랑1)"))


@bot.command()
async def 시발(ctx):
    await ctx.send("욕하지마 시발 :thumbsup:")





#하드 + 헬
@bot.command()
async def 회랑1(ctx, num1, num2):
    jewel = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    jewels = list(map(int, jewel))

    jewels[0] = int(num2) + int(num2)
    jewels[1] = jewels[1] + int(num2) + int(num2)
    jewels[2] = jewels[2] + int(num2) + int(num2)

    jewels[1] = jewels[1] + int(num1)
    jewels[2] = jewels[2] + int(num1) + int(num1)

    jewels[1] = jewels[1] + math.trunc(jewels[0] / 3)
    jewels[0] = jewels[0] % 3

    jewels[2] = jewels[2] + math.trunc(jewels[1] / 3)
    jewels[1] = jewels[1] % 3

    for i in range(2, 8):
        jewels[i+1] = math.trunc(jewels[i] / 3)
        jewels[i] = math.trunc(jewels[i] % 3)

    embeded = discord.Embed(title="회랑 보석 계산기", description="노말 + 하드 + 헬", colour=0x008080)
    embeded.add_field(name="2레벨", value=jewels[0], inline=True)
    embeded.add_field(name="3레벨", value=jewels[1], inline=True)
    embeded.add_field(name="4레벨", value=jewels[2], inline=True)
    embeded.add_field(name="5레벨", value=jewels[3], inline=True)
    embeded.add_field(name="6레벨", value=jewels[4], inline=True)
    embeded.add_field(name="7레벨", value=jewels[5], inline=True)
    embeded.add_field(name="8레벨", value=jewels[6], inline=True)
    embeded.add_field(name="9레벨:ring:", value=jewels[7], inline=True)
    embeded.add_field(name="10레벨:ring:", value=jewels[8], inline=True)

    await ctx.send(embed=embeded)

#하드
@bot.command()
async def 회랑(ctx, num1):
    jewel = [0, 0, 0, 0, 0, 0, 0, 0]
    jewels = list(map(int, jewel))

    jewels[0] = int(num1)
    jewels[1] = int(num1) + int(num1)

    jewels[1] = jewels[1] + math.trunc(jewels[0] / 3)
    jewels[0] = jewels[0] % 3

    for i in range(1, 7):
        jewels[i+1] = math.trunc(jewels[i] / 3)
        jewels[i] = math.trunc(jewels[i] % 3)

    embeded = discord.Embed(title="회랑 보석 계산기", description="노말 + 하드", colour=0x008080)
    embeded.add_field(name="3레벨", value=jewels[0], inline=True)
    embeded.add_field(name="4레벨", value=jewels[1], inline=True)
    embeded.add_field(name="5레벨", value=jewels[2], inline=True)
    embeded.add_field(name="6레벨", value=jewels[3], inline=True)
    embeded.add_field(name="7레벨", value=jewels[4], inline=True)
    embeded.add_field(name="8레벨", value=jewels[5], inline=True)
    embeded.add_field(name="9레벨:ring:", value=jewels[6], inline=True)
    embeded.add_field(name="10레벨:ring:", value=jewels[7], inline=True)

    await ctx.send(embed=embeded)

@bot.command()
async def test123(ctx):
    print("테스트")
    # result, _color, bot1, user = dice()
    result = "틀렸습니다."
    _color = 0xFF0000
    bot1 = str(1)
    user = str(2)
    print("테스트1")
    embed = discord.Embed(title="테스트", description="test embed", colour=_color)
    print("테스트2")
    embed.add_field(name="자신의 숫자", value=":book:" + user, inline=True)
    print("테스트3")
    embed.add_field(name="Bot의 숫자", value=":book:" + bot1, inline=True)
    embed.add_field(name=None, value=":regional_indicator_s::regional_indicator_e::regional_indicator_x:", inline=True)
    print("테스트4")
    embed.set_footer(text="결과: " + result)
    print("테스트5")
    await ctx.send(embed=embed)
    print("test end")


@bot.command()
async def 쿠크(ctx):
    embed = discord.Embed(title="쿠크 파티", description="쿠크 파티", colour=0x008080)
    embed.add_field(name="각두", value="기상", inline=True)
    embed.add_field(name="워로", value="홀나", inline=True)
    embed.add_field(name="홀카", value="인파", inline=True)
    embed.add_field(name="카멜", value="워로", inline=True)

    await ctx.send(embed=embeded)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("명령어 몰?루")
        await ctx.send("https://tenor.com/view/%EB%AA%B0%EB%A3%A8-gif-23066933")

access_token = os.environ["BOT_TOKEN"]
bot.run('MTAwMzQ2MDM2NzM2NTcwMTY3Mw.Gc_p7O.Fwrx3sA9TS3e7oLaOlad9vIT7XjJlAkwWLeLMY')
