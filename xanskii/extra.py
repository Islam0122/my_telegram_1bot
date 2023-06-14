

from aiogram import types, Dispatcher
from config import bot

async def echo(message: types.Message) -> None:

    if  message.text.isdigit():
        n = int (message.text)**2
        await bot.send_message(message.chat.id, f"-->{n }")

    else:
        await bot.send_message(message.chat.id,f"[{message.text}]"  )
# 🎲🎯🎰🎳🏀⚽️
def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo, content_types=['text'])