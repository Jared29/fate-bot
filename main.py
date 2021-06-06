from webbrowser import get
import discord, os, requests, json

client = discord.Client()
my_secret = os.environ['TOKEN']

def get_servant(servName):
    # URL request to the API
    response = requests.get("https://api.atlasacademy.io/basic/NA/servant/search", params=servName)
    json_data = json.loads(response.text)
    name = json_data[0]
    return(name)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello')

  if message.content.startswith('$servant'):
      servant_name = message.content[9:]
      payload = {'name': servant_name}
      servant = get_servant(payload)
      await message.channel.send(servant['name'])
  
  if message.content.startswith('$embed'):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", 
                        description="This is an embed that will show how to build an embed and the different components", 
                        color=0xFF5733)
    await message.channel.send(embed=embed)
    

client.run(my_secret)
