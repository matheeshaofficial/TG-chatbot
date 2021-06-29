from lycia import LYCIA
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

LYCIA_START = """
😃 Hello, I am TG-chatbot , An Intelligent ChatBot. You can Always Come to me and Chat With Me! join with us - @slbotzone 
"""


@LYCIA.on_message(filters.command(["start"], prefixes = "/") & ~filters.edited)
async def info(client, message):
    buttons = [
                [InlineKeyboardButton("🔥TG- chatbot 🔥", switch_inline_query_current_chat="🔥TG- chatbot 🔥 "), InlineKeyboardButton(" 📦 my socure code 📦", url = "https://github.com/youtubeslgeekshow/TG-chatbot")]
              ]
    await LYCIA.send_message(chat_id = message.chat.id, text = LYCIA_START, reply_markup = InlineKeyboardMarkup(buttons))
