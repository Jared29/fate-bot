import discord, os, requests, json

client = discord.Client()
my_secret = os.environ['TOKEN']

def get_servant(servName):
  # URL request to the API
  response = requests.get("https://api.atlasacademy.io/nice/NA/servant/search", params=servName)
  json_data = json.loads(response.text)
  name = json_data[0]
  return(name)

# Build the embed message to be sent in chat
def build_embed(servInfo):
  embed=discord.Embed(title=servInfo['name'], url="https://fategrandorder.fandom.com/wiki/" + servInfo['name'], 
                        description="Class: " + servInfo['className'].capitalize(), 
                        color=0xFF5733)
  embed.set_thumbnail(url=servInfo['extraAssets']['faces']['ascension']['1'])

  # Rarity / Cost
  embed.add_field(name="Rarity", value=servInfo['rarity'], inline=True)
  embed.add_field(name="Cost", value=servInfo['cost'], inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)

  # Servants stats
  embed.add_field(name="Max Atk", value=servInfo['atkMax'], inline=True)
  embed.add_field(name="Max Hp", value=servInfo['hpMax'], inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)
  embed.add_field(name="Grail Atk", value=servInfo['atkGrowth'][-1], inline=True)
  embed.add_field(name="Grail Hp", value=servInfo['hpGrowth'][-1], inline=True)
  embed.add_field(name="\u200B", value="\u200B", inline=True)

  # Servant command cards
  embed.add_field(name="Command Cards", value=' '.join(servInfo['cards']).title(), inline=False)

  return(embed)


# Confirm bot has logged in
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

# Chat commands
@client.event
async def on_message(message):
  if message.author == client:
    return

  if message.content.startswith('$servant'):
    servant_name = message.content[9:]
    payload = {'name': servant_name}
    servant = get_servant(payload)
    servEmbed = build_embed(servant)
    await message.channel.send(embed=servEmbed)

client.run(my_secret)
