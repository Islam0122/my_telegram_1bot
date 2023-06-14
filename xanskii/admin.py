import random

from aiogram import types, Dispatcher
from config import admins

a = "\U0001F3AF " # 🎯
b = "\U0001F3B2"                # 🎲
c = "\U0001F3B0"            # 🎰
h = "\U000026BD"                   # ⚽️
o = "\U0001F3C0"  # 🏀
k = "\U0001F3B3"
emoji_game = [a,b,c,h,o,k]




async def game (message: types.Message):

    if message.from_user.id not in  admins:

        await message.answer("Ты не мой босс!")


    else:

        await message.answer_dice(random.choices(emoji_game))
        await message.answer(f"привет босс {message.from_user.full_name}")







async def pin(message: types.Message):
    if  not message.reply_to_message:
        await message.answer("Команда должна быть ответом на сообщение!")
    else :
        await message.reply_to_message.pin()


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(game, text =['game'])