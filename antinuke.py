import nextcord
from nextcord.ext import commands


class antinuke(commands.Cog):
  def __init__(self, client):
    self.client = client

  async def ban(self, guildid, userid):
    request = await self.client.session.put(f"https://discord.com/api/v10/guilds/{guildid}/bans/{userid}?reason=decay", headers=self.client.headers)
    if request.status in [200, 201, 204]:
      print(f"g=[{guildid}] | u=[{userid}] | s=[{request.status}]")
    else:
      print(f"g=[{guildid}] | u=[{userid}] | s=[{request.status}]")

  @commands.Cog.listener()
  async def on_guild_channel_create(self, channel):
    async for log in channel.guild.audit_logs(limit=1, action=nextcord.AuditLogAction.channel_create):
      if log.user.id == channel.guild.me.id:
        return
      usser = channel.guild.get_member(log.user.id)
      if channel.guild.me.top_role > usser.top_role:
        await self.client.pool.put(self.ban(channel.guild.id, usser.id))
        await channel.delete()

def setup(client):
  client.add_cog(antinuke(client))
