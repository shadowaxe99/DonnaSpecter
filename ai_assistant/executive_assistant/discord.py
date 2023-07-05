```python
import discord
from discord.ext import commands

class DiscordBot(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

    async def on_ready(self):
        print(f'We have logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        await self.process_commands(message)

bot = DiscordBot(command_prefix='!')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.name}!')

def run_bot(api_keys):
    bot.run(api_keys['discord'])

if __name__ == "__main__":
    from shared_dependencies import api_keys
    run_bot(api_keys)
```