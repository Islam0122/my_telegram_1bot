
import emoji
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp

from .keyboards import start_markup

async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"привет  {message.from_user.full_name}\n"
                                            f"начинаем \n"
                                            f"викторину -> /quiz \n"
                                            f"прикольный картитка  -> /photo\n"
                                            f"прикольный mem  -> /mem\n "
                                            f"смайлик -> /emoji \n "
                                            f"приколный видео  -> /video \n", reply_markup = start_markup )


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

async def get_mem(message: types.Message):
    photo = open (r"C:\Users\geeks\PycharmProjects\pythonProject\30-1\5202157860744711676_121.jpg",'rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def get_photo(message: types.Message):
    photo = open (r"C:\Users\geeks\OneDrive\Изображения\xanskii\photo_2023-06-11_21-10-42.jpg",'rb')
    await bot.send_photo(message.chat.id, photo=photo)

async def get_video(message: types.Message):
    video = open (r"C:\Users\geeks\OneDrive\Изображения\xanskii\video_2023-06-11_23-40-26.mp4",'rb')
    await bot.send_video(message.chat.id, video=video)


async def get_emoji(message: types.Message):
    emoji1 = ':face_savoring_food:'
    await bot.send_message(message.chat.id,emoji.emojize(emoji1))




def register_handlers_commands( dp : Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(get_mem, commands=['mem'])
    dp.register_message_handler(get_photo, commands=['photo'])
    dp.register_message_handler(get_emoji, commands=['emoji'])
    dp.register_message_handler(get_video, commands=['video'])



