from bs4 import BeautifulSoup
import discord, os, requests, json


client = discord.Client()
my_secret = os.environ['TOKEN']

def get_servant(servName):
  # URL request to the API
  response = requests.get("https://api.atlasacademy.io/nice/JP/servant/search", params=servName)
  print(response.url)
  json_data = json.loads(response.text)
  name = json_data[0]
  return(name)

def scrape_sprite(servName, sprite_lvl):
  response = requests.get("https://fategrandorder.fandom.com/wiki/" + str(servName))
  serv_webpage = response.text
  soup = BeautifulSoup(serv_webpage, "html.parser")

  sprite = soup.find(name="a", title="Stage " + str(sprite_lvl))
  link = sprite.get("href")

  return(link)

# Build the embed message to be sent in chat
def build_embed(servInfo):
  servName = servInfo['name']
  embed=discord.Embed(title=servInfo['name'], url="https://fategrandorder.fandom.com/wiki/", 
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
    payload = {'name': servant_name, 'lang': 'en'}
    servant = get_servant(payload)
    servEmbed = build_embed(servant)
    await message.channel.send(embed=servEmbed)

  if message.content.startswith('$asc'):
    servant_req = message.content[5:].split()
    servant_name = servant_req[0:-1]
    asc_level = servant_req[-1]
    payload = {'name': servant_name}
    servant = get_servant(payload)
    await message.channel.send(servant['extraAssets']['charaGraph']['ascension'][asc_level])

  if message.content.startswith('$spr'):
    servant_req = message.content[5:].split()
    servant_name = servant_req[0:-1]
    spr_level = servant_req[-1]
    #payload = {'name': servant_name}
    servant_sprite = scrape_sprite(servant_name, spr_level)
    await message.channel.send(servant_sprite)

client.run(my_secret)
