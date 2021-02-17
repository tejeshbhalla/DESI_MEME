from reddit import req_memes
import discord
import os
from keepalive import keep_alive
import random


client=discord.Client()
available_subs=["IndianDankMemes","MemeEconomy","HindiMemes","wholesomememes","dankmemes"]
@client.event
async def on_ready():
  print(f"we have logged in as {client.user} ")


@client.event
async def on_message(message):
  if message.author==client.user:
    return 
  if message.content.startswith("$meme"):
    subreddit=message.content.split()
    if len(subreddit)==2:
      subreddit=subreddit[1]
    else:
      subreddit=random.choice(available_subs)

    path=req_memes(subreddit)
    await message.channel.send("if the memes are repeating plz change the subreddit ",file=discord.File(path))
  if message.content.startswith("$tell"):
    message_="some meme communites are"
    for i in available_subs:
      message_=message_+" "+i
    print(message_)
    await message.channel.send(message_)
  


keep_alive()
client.run(os.getenv("TOKEN_DISCORD"))