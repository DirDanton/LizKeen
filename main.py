import discord
import json
import random
from log import *
from settings import *

welcomeMsgs = []

with open('welcome.json', 'r+') as f:
    welcomeMsgs = json.loads(f.read())

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # random chat msgs
        for k,v in settings()['reaction_channels'].items():
            if message.channel.id == int(k):
                for value in range(len(v)):
                    print(v[value])
                    await message.add_reaction(v[value])
                return
        if message.channel.id == settings()['general_chat']:
            if random.randint(1,100) <= 10:
                await message.channel.send(settings()['random_chats'][random.randint(0,len(settings()['random_chats'])-1)])
    async def on_member_join(self, member):
        log('serverjoin.log', f'member <@{member.id}>')
        channel = self.get_channel(1180901512222875728)
        await channel.send(welcomeMsgs[random.randint(0,len(welcomeMsgs)-1)].replace("member", f"<@{member.id}>"))

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run('MTE4MDc5NDQ1NzY1OTAyMzM4MA.GcqvnB.AAhPLOZ_y-bUIf8Oome967pAdtJ5bCPFPnjjRQ')