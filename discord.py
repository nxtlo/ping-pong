import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# commands

    @commands.command(name='ping', description='ping command')
    async def ping(self, ctx):
        await ctx.send('pong!')

# listeners

    @commands.Cog.listener()
    async def on_message(self, message):
        if '!ping' in message.content:
            await message.channel.send('pong!')


# you must register the cogs to be used by typing this.

def setup(bot):
  bot.add_cog(ping(bot))
