import emoji
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp

from .keyboards import start_markup
from sql_tablet.x_mentors_dp import sql_command_random
from x_parser.x_parser1 import parser
from aiogram.types import ParseMode


async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"привет  {message.from_user.full_name}\n"
                                            f"начинаем \n", reply_markup=start_markup)


async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "Сколько полос на флаге США?"
    answers = [
        "12",
        "13",
        "40",
        "14",
        "19",

    ]

    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        reply_markup=markup
    )


async def get_photo(message: types.Message):
    photo = open(r"C:\Users\geeks\pythonProject\venv\x_media\x_photo\Internet_20230616_200026_1.jpeg", 'rb')
    await bot.send_photo(message.chat.id, photo=photo)


async def get_video(message: types.Message):
    video = open(r"C:\Users\geeks\pythonProject\venv\x_media\x_photo\Internet_20230616_200026_1.jpeg", 'rb')
    await bot.send_video(message.chat.id, video=video)


async def get_emoji(message: types.Message):
    emoji1 = ':face_savoring_food:'
    await bot.send_message(message.chat.id, emoji.emojize(emoji1))


async def get_random_mentor(message: types.Message) -> None:
    random_mentor = await sql_command_random()
    await message.answer(
        f" name -> {random_mentor[1]} \n"
        f"  age -> {random_mentor[2]} \n "
        f" group -> {random_mentor[3]} \n "
        f" direction ->  {random_mentor[4]}"
    )



async def parsser_wheels(message: types.Message):
    items = parser()
    for item in items:
        await bot.send_message(
            message.from_user.id,

            f"{item['url']}"
            f"{item['title']}\n"
            f"цена - {item['price']}\n",  reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton("Смотреть", url=item['url'])
            ),
            parse_mode=ParseMode.HTML

            )
def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_photo, commands=['photo'])
    dp.register_message_handler(get_emoji, commands=['emoji'])
    dp.register_message_handler(get_video, commands=['video'])
    dp.register_message_handler(get_random_mentor, commands=['get'])
    dp.register_message_handler(parsser_wheels, commands=['news'])
