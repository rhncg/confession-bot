import discord
from funcs.db import add_confession
from views.confession_view import ConfessionView
from bot_instance import bot

async def send_confession_embed(self, interaction: discord.Interaction):
    confession = self.children[0].value
    image_url = self.children[1].value.strip()
    color_input = self.children[2].value.strip()
    if len(self.children) > 3:
        self.reply_message = self.children[3].value.strip()
        self.reply_message = self.reply_message.split("/")[-1] if self.reply_message else None
        self.reply_message = bot.get_message(self.reply_message)
        
    if image_url:
        try:
            image_url = image_url if image_url.startswith("http") else None
        except ValueError:
            image_url = None

    if color_input:
        try:
            color_input = int(color_input.lstrip("#"), 16)
        except ValueError:
            color_input = 0x11806A
    else:
        color_input = 0x11806A

    confession_num = await add_confession(interaction.guild.id)

    if self.reply_message:
        if self.reply_number:
            message_embed = discord.Embed(
                title=f"Anonymous Confession (#{confession_num})",
                color=color_input,
                image=image_url if image_url else None
            )
            message_embed.add_field(name=confession, value="", inline=False)
            message_embed.add_field(name="",
                                    value=f"(Reply to [Confession #{self.reply_number}]({self.reply_message.jump_url}))",
                                    inline=False)
        else:
            message_embed = discord.Embed(
                title=f"Anonymous Confession (#{confession_num})",
                color=color_input,
                image=image_url if image_url else None
            )
            message_embed.add_field(name=confession, value="", inline=False)
            message_embed.add_field(name="",
                                    value=f"(Reply to [this message]({self.reply_message.jump_url}))",
                                    inline=False)

    else:
        message_embed = discord.Embed(
            title=f"Anonymous Confession (#{confession_num})",
            color=color_input,
            image=image_url if image_url else None
        )
        message_embed.add_field(name=confession, value="", inline=False)

    if self.reply_message:
        await self.reply_message.reply(embed=message_embed, view=ConfessionView(confession_num))
        await interaction.response.send_message(f"Your reply has been sent.", ephemeral=True, delete_after=3)
    else:
        await interaction.channel.send(embed=message_embed, view=ConfessionView(confession_num))
        await interaction.response.send_message(f"Your confession has been sent.", ephemeral=True, delete_after=3)