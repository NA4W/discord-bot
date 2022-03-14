import discord

token = ""

intent = discord.Intents.default()
intent.members = True
intent.message_content = True
intent.guilds = True

client = discord.Client(intents=intent)

@client.event
async def on_ready():
    print("booted")

@client.event
async def on_message(message:discord.Message):
    if message.author.bot is True:
        return
    if message.content == "/neko":
        await message.reply(content="nyaa")

if __name__ == "__main__":
    client.run(token)