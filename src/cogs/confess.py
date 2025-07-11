import discord
from views.confess_view import ConfessModal

class Confess(discord.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.command()
    async def confess(self, ctx):
        await ctx.send_modal(ConfessModal(ctx.channel))
        
def setup(bot):
    bot.add_cog(Confess(bot))