import discord
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


# commands in a cog

    @commands.command(name='ping', description='ping command')
    async def ping(self, ctx):
        await ctx.send('pong!')

# listeners in a cog

    @commands.Cog.listener()
    async def on_message(self, message):
        if '!ping' in message.content:
            await message.channel.send('pong!')

 # in main.bot with exceptions
 
@bot.command(aliases=['latency'], description="show bot's pin")
async def ping(ctx):
    try:
        await ctx.send("Pong!")
    
    except Exception:
        await ctx.send("command wan not found, perhaps you meant ping?")
    
    # raise the error to our shell
    else:
        raise
       

# you must register the cogs to be used by typing this.

def setup(bot):
  bot.add_cog(ping(bot))
