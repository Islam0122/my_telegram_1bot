from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")

photo_button = KeyboardButton("/photo")
video_button = KeyboardButton("/video")
emoji_button = KeyboardButton("/emoji")
dice_button = KeyboardButton("/dice")
start_markup.add(
    start_button,
    quiz_button,
    photo_button,
    video_button,
    emoji_button,
    dice_button
)


cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)
cancel_button = KeyboardButton("Отмена")
cancel_markup.add(cancel_button)

submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
    cancel_button
)

