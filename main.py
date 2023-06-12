

from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging
import emoji

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"привет  {message.from_user.full_name}\n"
                                            f"начинаем \n"
                                            f"викторину -> /quiz \n"
                                            f"прикольный картитка  -> /photo\n"
                                            f"прикольный mem  -> /mem\n "
                                            f"смайлик -> /emoji \n "
                                            f"приколный видео  -> /video \n")


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "какой национальный цветок Японии? "
    answers = ['роза',
               'самурай ',
               'сакура',
               'не знаю']


    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,

    )
@dp.message_handler(commands=['mem'])
async def get_mem(message: types.Message):
    photo = open (r"C:\Users\geeks\PycharmProjects\pythonProject\30-1\5202157860744711676_121.jpg",'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['photo'])
async def get_photo(message: types.Message):
    photo = open (r"C:\Users\geeks\OneDrive\Изображения\xanskii\photo_2023-06-11_21-10-42.jpg",'rb')
    await bot.send_photo(message.chat.id, photo=photo)

@dp.message_handler(commands=['video'])
async def get_video(message: types.Message):
    video = open (r"C:\Users\geeks\OneDrive\Изображения\xanskii\video_2023-06-11_23-40-26.mp4",'rb')
    await bot.send_video(message.chat.id, video=video)

@dp.message_handler(commands=['emoji'])
async def get_emoji(message: types.Message):
    emoji1 = ':face_savoring_food:'
    await bot.send_message(message.chat.id,emoji.emojize(emoji1))

@dp.message_handler(content_types=['text'])
async def echo(message: types.Message) -> None:
    if message.text.isdigit():
        n = int (message.text)**2
        await bot.send_message(message.chat.id, f"-->{n }")
    else:
        await bot.send_message(message.chat.id,f"[{message.text}]"  )
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)