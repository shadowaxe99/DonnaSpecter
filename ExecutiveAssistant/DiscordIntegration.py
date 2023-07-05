```python
import discord
import os

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_SERVER_ID = os.getenv('DISCORD_SERVER_ID')

client = discord.Client()

async def send_message(channel_id, message):
    channel = client.get_channel(channel_id)
    await channel.send(message)

async def join_server(invite_link):
    await client.accept_invite(invite_link)

async def create_channel(server_id, channel_name, channel_type='Text'):
    server = client.get_server(server_id)
    if channel_type == 'Text':
        await server.create_text_channel(channel_name)
    elif channel_type == 'Voice':
        await server.create_voice_channel(channel_name)

async def invite_to_channel(channel_id, user_id):
    channel = client.get_channel(channel_id)
    user = client.get_user(user_id)
    await channel.create_invite(destination=channel)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

client.run(DISCORD_TOKEN)
```