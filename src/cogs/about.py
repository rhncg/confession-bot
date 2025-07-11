import discord

class About(discord.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @discord.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title="About",
            color=discord.Color.dark_teal()
        )
        embed.add_field(name="This is a completely anonymous confession bot. No logs are stored.", value="The code for this bot is open source. You can find it on [GitHub](https://github.com/rhncg/confession-bot).")
        
        embed.set_footer(text="Made by @rhncg")
        
        await ctx.respond(embed=embed)
        
def setup(bot):
    bot.add_cog(About(bot))