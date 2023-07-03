from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
)

start_button = KeyboardButton("/start")
quiz_button = KeyboardButton("/quiz")

photo_button = KeyboardButton("/photo")
video_button = KeyboardButton("/video")

dice_button = KeyboardButton("/dice")
reg_button = KeyboardButton("/reg")
kino_button = KeyboardButton("/kino")

start_markup.add(
    start_button,
    quiz_button,
    photo_button,
    video_button,

    dice_button,
    reg_button,
    kino_button
    # cancel_button
)


cancel_button = KeyboardButton("cancel")
cancel_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    cancel_button
)




submit_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
).add(
    KeyboardButton("ДА"),
    KeyboardButton("ЗАНОВО"),
    cancel_button
)

