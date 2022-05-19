import nextcord
import random
import time
import asyncio

start = 0.0
end = 0.0
bot = nextcord.Client()
game_on = 0
on_asd = 0
game_num = 1
result_set = [0, 0, 0]
@bot.event
async def on_ready():
    print("On")
    print(bot.user.name)
    print(str(bot.user.id))
    game = nextcord.Game("test")
    await bot.change_presence(status=nextcord.Status.online, activity=game)

@bot.event
async def on_message(message: nextcord.Message):
    global game_on, game_num, result_set,start,end,on_asd
    if message.author == bot.user:
        return
    if message.content == "test":
        await message.channel.send("test")
    if message.content == "!순발력 시작":
        if game_on == 1:
            await message.channel.send("이미 게임을 시작중입니다.")
            return
        await message.channel.send("게임을 시작합니다.")
        game_on = 1
        await asyncio.sleep(3)
        await message.channel.send(". 을 보내세요.")
        on_asd = 1
        start = time.time()
    #순발력 게임 코드
    if message.content == ".":
        if game_on == 1:
            if on_asd == 0:
                    await message.channel.send("메시지가 나오면 입력해주십시오.")
                    return
            if game_num == 1:
                end = time.time()
                await message.channel.send(str(game_num) + "번째 테스트 : " + str(round(end-start, 3)) + "초")
                on_asd = 0
                sleep_time = random.randint(3, 6)
                await asyncio.sleep(sleep_time)
                result_set[game_num - 1] = round(end-start, 3)
                game_num += 1
                await message.channel.send(". 을 보내세요.")
                on_asd = 1

                start = time.time()
                return
            end = time.time()
            await message.channel.send(str(game_num) + "번째 테스트 : " + str(round(end-start, 3)) + "초")
            on_asd = 0
            #게임 끝
            if game_num == 3:
                result = (result_set[0] + result_set[1] + result_set[2]) / 3
                await message.channel.send("당신의 순발력은" + str(round(result,3)) + "초 입니다.")
                game_on = 0
                game_num = 1
                return
            sleep_time = random.randint(3, 6)
            await asyncio.sleep(sleep_time)
            result_set[game_num - 1] = round(end-start, 3)
            game_num += 1
            await message.channel.send(". 을 보내세요.")
            on_asd = 1
            start = time.time()
        else:
            return
token = "토큰 입력"
bot.run(token)
