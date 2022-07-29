import nextcord, aiohttp, tasksio
from nextcord.ext import commands

client = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

@client.event
async def on_ready():
  print(f"status=[online] | name=[{client.user.name}] | id=[{client.user.id}]")
  client.remove_command("help")
  async with tasksio.TaskPool(20) as pool:
    client.pool = pool
    client.session = aiohttp.ClientSession()
    client.headers = {"authorization": "Bot "}
    client.load_extension("antinuke")

client.run("")
