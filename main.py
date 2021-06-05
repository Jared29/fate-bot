import discord, os

client = discord.Client()
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello')

client.run(my_secret)
