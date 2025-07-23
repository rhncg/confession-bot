import discord

class ConfessionView(discord.ui.View):
    def __init__(self, confession_num):
        super().__init__(timeout=None)
        self.confession_num = confession_num

    @discord.ui.button(label="Reply", style=discord.ButtonStyle.primary)
    async def reply_button_callback(self, button, interaction):
        from funcs.send_confession import send_confession

        await send_confession(interaction, reply_message=interaction.message, reply_number=self.confession_num, author_id=interaction.user.id)
    
    @discord.ui.button(label="New Confession", style=discord.ButtonStyle.success)
    async def new_confession_button_callback(self, button, interaction):
        from funcs.send_confession import send_confession

        await send_confession(interaction, reply_message=None, reply_number=None, author_id=interaction.user.id)