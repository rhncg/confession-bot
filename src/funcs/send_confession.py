import discord
from views.confess_modal import ConfessModal

async def send_confession(ctx, reply_message: discord.Message=None, reply_number: int=None):
    await ctx.response.send_modal(ConfessModal(reply_message=reply_message, reply_number=reply_number))
