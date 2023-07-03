import emoji
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from x_new_.new_file import  parse1
ites = parse1()
from aiogram.types import ParseMode
async def parsser(message: types.Message):
    await bot.send_message(message.from_user.id,
    f"привет {message.from_user.full_name}")
    for item in ites:
        await bot.send_message(
            message.from_user.id,

            f"{item['url']}" ,
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Смотреть", url=item['url'])
            ),
            parse_mode=ParseMode.HTML

            )

    await bot.send_message(message.from_user.id,
    f"приятного просмотра {message.from_user.full_name}")
def register_handlers_2commands(dp: Dispatcher):
    dp.register_message_handler(parsser, commands=["kino"])
