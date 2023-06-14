from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)
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
        reply_markup=markup
    )
async def quiz_3(callback: types.CallbackQuery):

        markup = InlineKeyboardMarkup()
        next_button = InlineKeyboardButton("NEXT", callback_data="next_button_3")
        markup.add(next_button)
        quiestion = "Сколько дней  нужно ,чтобы земля совершила  оборот  вокруг Солнца ? "
        answers = ['345',
                   '366',
                   '365',
                   '367']

        await callback.message.answer_poll(
            question=quiestion,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=2,

        )
def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")


