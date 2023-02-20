# This example requires the 'message_content' intent.

import discord

class MyClient(discord.Client):
    async def on_ready(self): # this bot is ready to take new requests
        print(f'Logged on as {self.user}!')

    async def on_message(self, message): # this listents to the events sent by the server (discord server)
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('my token goes here')
