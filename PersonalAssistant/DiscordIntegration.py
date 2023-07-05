```python
import discord
from discord.ext import commands

DISCORD_TOKEN = 'your-token-here'
DISCORD_SERVER_ID = 'your-server-id-here'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def send_message(ctx, channel_id: int, *, message: str):
    channel = bot.get_channel(channel_id)
    await channel.send(message)

@bot.command()
async def join_server(ctx, invite_link: str):
    try:
        await bot.accept_invite(invite_link)
        print(f"Joined server with invite link: {invite_link}")
    except Exception as e:
        print(f"Failed to join server with invite link: {invite_link}. Error: {e}")

@bot.command()
async def create_channel(ctx, channel_name: str):
    guild = discord.utils.get(bot.guilds, id=DISCORD_SERVER_ID)
    await guild.create_text_channel(channel_name)

@bot.command()
async def invite_to_channel(ctx, channel_id: int, user_id: int):
    channel = bot.get_channel(channel_id)
    user = bot.get_user(user_id)
    await channel.set_permissions(user, read_messages=True)

bot.run(DISCORD_TOKEN)
```