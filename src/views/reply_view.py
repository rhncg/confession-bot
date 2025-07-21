import discord

class ReplyView(discord.ui.View):
    def __init__(self, confession_num):
        super().__init__(timeout=None)
        self.confession_num = confession_num

    @discord.ui.button(label="Reply", style=discord.ButtonStyle.primary)
    async def reply_button_callback(self, button, interaction):
        from funcs.send_confession import send_confession

        await send_confession(interaction, reply_message=interaction.message, reply_number=self.confession_num)