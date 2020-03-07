import discord

client = discord.Client()

f = open("tokenfile.txt", 'r')
token = f.read()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$react'):
        await message.add_reaction("😎")

    if message.content.startswith('$echo'):
        await message.channel.send(message.content.split(' ', 1)[1])

client.run(token)