import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "*")



@client.event
async def on_ready():
    print("Bot is launched, ")




@client.event
async def on_message(message):
    if message.content.upper().startswith("**TRANSLATE"):
        s = message.content.split(" ", 1)[1]
        dict = str.maketrans("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM", "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ¹²³⁴⁵⁶⁷⁸⁹⁰Qᵂᴱᴿᵀʸᵁᴵᴼᴾᴬˢᴰᶠᴳᴴᴶᴷᴸᶻˣᶜⱽᴮᴺᴹ")
        
        value= s
        result = value.translate(dict)
        print(result)
        await client.send_message(message.channel, "%s" % (result))


client.run('NDQwNDU3NTMxNDg4NDY5MDEz.DigKrg.FoIcndz1wm462mcuFM2ii2Y2cJU')

