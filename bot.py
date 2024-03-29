import asyncio
import math

import discord
from discord.ext import commands
from discord.utils import get
from discord.ui import button, View

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)


@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("$기능/11월 28일 종료"))


# 하드 + 헬
@bot.command()
async def 회랑헬(ctx, num1, num2):
    icon_hell_url = str("https://media.discordapp.net/attachments/1010932575403003974/1010934804818174022/unknown.png")
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
        jewels[i + 1] = math.trunc(jewels[i] / 3)
        jewels[i] = math.trunc(jewels[i] % 3)

    embeded = discord.Embed(title="회랑 보석 계산기", description="노말 + 하드 + 헬", colour=0x008080)
    embeded.set_thumbnail(url=icon_hell_url)
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

# 하드
@bot.command()
async def 회랑(ctx, num1):
    icon_nomal_url = str("https://cdn.discordapp.com/attachments/1010932575403003974/1010934821276618825/unknown.png")
    jewel = [0, 0, 0, 0, 0, 0, 0, 0]
    jewels = list(map(int, jewel))

    jewels[0] = int(num1)
    jewels[1] = int(num1) + int(num1)

    jewels[1] = jewels[1] + math.trunc(jewels[0] / 3)
    jewels[0] = jewels[0] % 3

    for i in range(1, 7):
        jewels[i + 1] = math.trunc(jewels[i] / 3)
        jewels[i] = math.trunc(jewels[i] % 3)

    embeded = discord.Embed(title="회랑 보석 계산기", description="노말 + 하드", colour=0x008080)
    embeded.set_thumbnail(url=icon_nomal_url)
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
async def 배위(ctx):
    await ctx.send(
        "https://media.discordapp.net/attachments/865698548723744769/970330313257537566/802f117f8d9278ac.gif")


@bot.command()
async def 누가울어(ctx):
    await ctx.send("https://coinpan.com/files/attach/images/198/700/600/175/7a21079132edda8c7575550e5d7fbf01.gif")

@bot.command()
async def 경매(ctx, num1):
    icon_gold_url = str("https://cdn.discordapp.com/attachments/1010932575403003974/1010932610173780028/unknown.png")
    party_gold_4 = int(num1) * 0.95 * 3 / 4
    gold_4 = party_gold_4 - party_gold_4 * 0.1

    party_gold_8 = int(num1) * 0.95 * 7 / 8
    gold_8 = party_gold_8 - party_gold_8 * 0.1

    embed = discord.Embed(title="경매 계산기", description="가격 약간 다름", colour=0x008080)
    embed.set_thumbnail(url=icon_gold_url)
    embed.add_field(name="인원수", value=4, inline=True)
    embed.add_field(name="선점 입찰가", value=int(gold_4), inline=True)
    embed.add_field(name="N빵 입찰가", value=int(party_gold_4), inline=True)
    embed.add_field(name="인원수", value=8, inline=True)
    embed.add_field(name="선점 입찰가", value=int(gold_8), inline=True)
    embed.add_field(name="N빵 입찰가", value=int(party_gold_8), inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def 쿠크(ctx):
    icon_satan_url = str("https://cdn.discordapp.com/attachments/1010932575403003974/1010933002521563238/unknown.png")

    embed = discord.Embed(title="쿠크 파티", description="쿠크 파티", colour=0x008080)
    embed.set_thumbnail(url=icon_satan_url)
    embed.add_field(name="각각두", value="기상 | 알카 | 소서 | 아가", inline=True)
    embed.add_field(name="워로드", value="홀나 | 기상 | 건슬 | 워로", inline=False)
    embed.add_field(name="홀홀카", value="인파 | 아가 | 블레 | 리퍼", inline=False)
    embed.add_field(name="카카멜", value="워로 | 충동 | 아가 | 배마", inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def 기능(ctx):
    view = MyView(ctx)
    await ctx.send(view=view)

class MyView(View):

    def __init__(self, ctx):
        super().__init__(timeout=None)
        self.ctx = ctx

    @discord.ui.button(label="쿠크 파티", style=discord.ButtonStyle.danger)
    async def Satan_button_callback(self, button, interaction):
        icon_satan_url = str("https://cdn.discordapp.com/attachments/1010932575403003974/1010933002521563238/unknown.png")

        embed = discord.Embed(title="쿠크 파티", description="쿠크 파티", colour=0x008080)
        embed.set_thumbnail(url=icon_satan_url)
        embed.add_field(name="각각두", value="기상 | 알카 | 소서 | 아가", inline=True)
        embed.add_field(name="워로드", value="홀나 | 기상 | 건슬 | 워로", inline=False)
        embed.add_field(name="홀홀카", value="인파 | 아가 | 블레 | 리퍼", inline=False)
        embed.add_field(name="카카멜", value="워로 | 충동 | 아가 | 배마", inline=False)

        await self.ctx.send(embed=embed)
        await interaction.response.edit_message(embed=embed)
        self.clear_items()


    @discord.ui.button(label="명령어", style=discord.ButtonStyle.green, custom_id="two")
    async def order_button_callback(self, button, interaction):
        icon_Star_url = str(
            "https://cdn.discordapp.com/attachments/1010932575403003974/1010933888287264839/ee78cd98e3010b26.png")
        embed = discord.Embed(title="명령어", description=None, colour=0x008080)
        embed.set_thumbnail(url=icon_Star_url)
        embed.add_field(name="회랑 [노말/하드]", value="회랑 개수에 대한 보석 나옴", inline=True)
        embed.add_field(name="회랑헬 [노말/하드] [헬]", value="노말 + 하드 + 헬 보석 개수 나옴", inline=False)
        embed.add_field(name="경매 [골드]", value="4, 8인 기준 선점·N빵 입찰가 나옴", inline=False)
        embed.add_field(name="배위", value="멋진 제리콘", inline=False)
        embed.add_field(name="누가울어", value="임춘식", inline=False)
        dm_channel = await self.ctx.message.author.create_dm()
        await dm_channel.send(embed=embed)
        await dm_channel.send(
            "https://media.discordapp.net/attachments/865698548723744769/970330313257537566/802f117f8d9278ac.gif")
        self.clear_items()
        await interaction.response.edit_message(view=self)

    @discord.ui.button(label="서버 상세", style=discord.ButtonStyle.secondary)
    async def hos_button_callback(self, button, interaction):
        name = str(self.ctx.guild.name)
        description = str(self.ctx.guild.description)
        owner = str(self.ctx.guild.owner)
        id = str(self.ctx.guild.id)
        memberCount = str(self.ctx.guild.member_count)
        icon = str("https://cdn.discordapp.com/attachments/867400582392971295/984722367072837642/image0.jpg")
        embed = discord.Embed(
            title=name + " 서버 정보",
            description=description,
            colour=discord.Color.green()
        )
        embed.set_thumbnail(url=icon)
        embed.add_field(name="주인장", value=owner, inline=True)
        embed.add_field(name="서버 ID", value=id, inline=True)
        embed.add_field(name="멤버 수", value=memberCount, inline=True)

        await self.ctx.send(embed=embed)
        self.clear_items()
        await interaction.response.edit_message(embed=embed)

    async def interaction_check(self, interaction) -> bool:
        if interaction.user != self.ctx.author:
            await interaction.response.send_message("명령어를 실행한 사람이 아닙니다. ", ephemeral=True)
            return False
        else:
            return True

    # async def on_timeout(self):
    #     await self.ctx.send("시간 초과")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"{ctx.message.author.mention}명령어 몰?루")
        await ctx.send("https://tenor.com/view/%EB%AA%B0%EB%A3%A8-gif-23066933")


bot.run('MTAwMzQ2MDM2NzM2NTcwMTY3Mw.Gc_p7O.Fwrx3sA9TS3e7oLaOlad9vIT7XjJlAkwWLeLMY')
