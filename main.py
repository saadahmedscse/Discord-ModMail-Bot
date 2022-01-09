import discord
import os
from webserver import keep_alive

client = discord.Client()

@client.event
async def on_ready():
  print('Blazed Enigma is logged in')
  await client.change_presence(activity=discord.Game(name="DM to contact staff!"))

@client.event
async def on_message(message):

  empty_array = []
  mod_channel = discord.utils.get(client.get_all_channels(), name="『📧』mod-mail")

  if message.author == client.user:
    return

  if str(message.channel.type) =="private":

    if message.attachments != empty_array:
      files = message.attachments
      await mod_channel.send("**User: **" + message.author.mention + "\n"
      + "**Copy to mention: **" + "<@!" + str(message.author.id) + " >\n" + "  ​ ‍ ")
      for file in files:
        await mod_channel.send(file.url)

    else:
      await mod_channel.send("**User: **" + message.author.mention + "\n"
      + "**Copy to mention: **" + "<@!" + str(message.author.id) + " >\n"
      + "**Message: **" + "`" + str(message.content)+ "`\n" + "  ​ ‍ ")

  elif str(message.channel) == "『📧』mod-mail" and message.content.startswith("<"):
    member_object = message.mentions[0]

    if message.attachments != empty_array:
      files = message.attachments
      for file in files:
        await member_object.send(file.url)

    else:
      index = message.content.index(" ")
      string = message.content
      mod_msg = string[index:]

      await member_object.send(mod_msg)

keep_alive()
client.run(os.getenv('TOKEN'))
