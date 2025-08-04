import discord
from funcs.send_confession_embed import send_confession_embed


class ConfessModal(discord.ui.Modal):
    def __init__(self, reply_message: discord.Message = None, reply_number: int = None, author_id: int = None):
        super().__init__(title="Confess")
        self.reply_message = reply_message
        self.reply_number = reply_number
        # noinspection PyTypeChecker
        self.add_item(discord.ui.InputText(label="Your Confession", style=discord.InputTextStyle.long, required=True))
        self.add_item(discord.ui.InputText(label="Image (optional, paste URL)", style=discord.InputTextStyle.short, required=False))
        if not reply_message or not reply_number:
            self.add_item(discord.ui.InputText(label="Reply to non-confession message (optional)", style=discord.InputTextStyle.short, required=False))
        self.add_item(discord.ui.InputText(label="Color (optional)", placeholder="#11806A", style=discord.InputTextStyle.short, required=False))

        if author_id == 1066616669843243048:
            self.add_item(discord.ui.InputText(label="Send as System Message", style=discord.InputTextStyle.short, required=False))

    async def callback(self, interaction: discord.Interaction):
        await send_confession_embed(self, interaction)