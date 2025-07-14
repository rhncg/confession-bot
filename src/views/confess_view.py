import discord
from funcs.db import add_confession

class ConfessModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Confess")
        # noinspection PyTypeChecker
        self.add_item(discord.ui.InputText(label="Your Confession", style=discord.InputTextStyle.long, required=True))
        self.add_item(discord.ui.InputText(label="Color (optional)", placeholder="#11806A", style=discord.InputTextStyle.short, required=False))

    async def callback(self, interaction: discord.Interaction):
        confession = self.children[0].value
        color_input = self.children[1].value.strip()

        if color_input:
            try:
                color_input = int(color_input.lstrip("#"), 16)
            except ValueError:
                color_input = 0x11806A
        else:
            color_input = 0x11806A

        confession_num = await add_confession(interaction.guild.id)
        
        embed = discord.Embed(
            title=f"Anonymous Confession (#{confession_num})",
            description=confession,
            color=color_input
        )
        
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f"Your confession has been sent.", ephemeral=True)