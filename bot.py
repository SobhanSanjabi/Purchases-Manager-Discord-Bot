import discord
import api
from db import config
# from db import mycursor, mydb


client = discord.Client(intents=discord.Intents.all())


#test_ch_id = 908493426411069495
LEGIT_CH_ID = list(dict(config["CHANNELS"]).values())


# 1 ahangari , 2 gun shop

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    # await txt_ch.send("Fuck The World I'm In!!!")



# MSG = !sxs! money hex -> Money of the hex
# MSG = !sxs! remoney hex -> hex, money
# MSG = !sxs! allmoney -> all money hex
@client.event
async def on_message(message):
    if str(message.channel.id) in LEGIT_CH_ID and str(message.author.id) != config["BOTS"]["BOT"]:
        msg = str(message.content).split()
        content = ""
        if config["COMMAND"] in msg:
            match msg[1]:
                case "help":
                    f = open("help.txt", "rt")
                    await message.reply(f.read())
                case "money":
                    res = api.get_money(msg[2])
                    if res != 404:
                        content = f"```Hex: {msg[2]}\nMoney: ${str(res[0])} ```"
                        await message.reply(content)
                    else:
                        await message.reply("Hex Not Found")
                case "remoney":
                        if api.reset_money(msg[2]) == 200:
                            content = f"Money Got Reset!\n```Account: {msg[2]}\nMoney: $0 ```"
                            await message.reply(content)
                        elif api.reset_money(msg[2]) == 404:
                            await message.reply("Hex Not Found")
                case "allmoney":
                    content = "```"
                    for res in api.get_all():
                        content += f"Hex: {res[0]}, Money: ${str(res[1])}"
                        content += "\n"
                    content += "```"
                    if content == "``````":
                        message.reply("No Hex Found")
                    else:
                        await message.reply(content)
        else:
            hex = ""
            if len(msg) == 28:
                money = int(msg[-2][:-3])
            elif len(msg) == 30:
                money = int(msg[-3])

            for word in msg:
                if "steam" in word:
                    hex = word[6:]
            if api.set_money(hex, money) == 200:
                await message.reply(f"Info Saved\n```Hex: {hex}\nMoney: {money} ```")
            # THIS IS FOR LEGIT USING
            # if str(message.channel.id) in LEGIT_CH_ID and str(message.author.id) in LEGIT_BOT_ID:
                

client.run(config["TOKEN"])


