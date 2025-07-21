import discord
from funcs.send_confession import send_confession

class Confess(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.command()
    async def confess(self, ctx):
        await send_confession(ctx)

def setup(bot):
    bot.add_cog(Confess(bot))