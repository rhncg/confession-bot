import discord

class ConfessModal(discord.ui.Modal):
    def __init__(self, channel):
        super().__init__(title="Confess")
        self.add_item(discord.ui.InputText(label="Your Confession", style=discord.InputTextStyle.long, required=True))

    async def callback(self, interaction: discord.Interaction):
        confession = self.children[0].value
        
        embed = discord.Embed(
            title="Anonymous Confession",
            description=confession,
            color=discord.Color.purple()
        )
        
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f"Your confession has been sent.", ephemeral=True)