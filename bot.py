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
    if message.content.startswith("**translate"):
        s = message.content.split("**translate", 1)[1]
        dict = str.maketrans("qwertyuiopasdfghjklzxcvbnm1234567890", "qʷᵉʳᵗʸᵘⁱᵒᵖᵃˢᵈᶠᵍʰʲᵏˡᶻˣᶜᵛᵇⁿᵐ¹²³⁴⁵⁶⁷⁸⁹⁰")
        
        value= s
        result = value.translate(dict)
        print(result)
        await client.send_message(message.channel, "%s" % (result))


bot.run('NDQwNDU3NTMxNDg4NDY5MDEz.DcjupA.ymYfiUoOh35--aI-oIUfZBN9U-E')

