import discord
from funcs.db import add_confession
from views.reply_view import ConfessionView

async def send_confession_embed(self, interaction: discord.Interaction):
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

    if self.reply_message:
        message_embed = discord.Embed(
            title=f"Anonymous Confession (#{confession_num})",
            color=color_input
        )
        message_embed.add_field(name=confession, value="", inline=False)
        message_embed.add_field(name="",
                                value=f"(Reply to [Confession #{self.reply_number}]({self.reply_message.jump_url}))",
                                inline=False)
    else:
        message_embed = discord.Embed(
            title=f"Anonymous Confession (#{confession_num})",
            color=color_input
        )

        message_embed.add_field(name=confession, value="", inline=False)

    if self.reply_message:
        await self.reply_message.reply(embed=message_embed, view=ConfessionView(confession_num))
        await interaction.response.send_message(f"Your reply has been sent.", ephemeral=True)
    else:
        await interaction.channel.send(embed=message_embed, view=ConfessionView(confession_num))
        await interaction.response.send_message(f"Your confession has been sent.", ephemeral=True)