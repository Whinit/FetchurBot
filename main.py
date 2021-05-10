import fandom
import discord

client = discord.Client()

async def get_fetchur(message):
    fandom.set_wiki("hypixel-skyblock")
    page = fandom.page(title = "Fetchur")
    sections = page.sections
    daily = page.section("Current Request")
    item = daily[daily.find(")")+1:]
    await message.channel.send(item)

@client.event
def on_message(message):

    if message.author == client.user:
            return

    if message.content.startswith("*fetchur"):
        await get_fetchur(message)

client.run("token")
