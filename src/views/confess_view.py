import discord
from funcs.db import add_confession

class ConfessModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Confess")
        self.add_item(discord.ui.InputText(label="Your Confession", style=discord.InputTextStyle.long, required=True))

    async def callback(self, interaction: discord.Interaction):
        confession = self.children[0].value

        confession_num = await add_confession(interaction.guild.id)
        
        embed = discord.Embed(
            title=f"Anonymous Confession (#{confession_num})",
            description=confession,
            color=discord.Color.dark_teal()
        )
        
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f"Your confession has been sent.", ephemeral=True)