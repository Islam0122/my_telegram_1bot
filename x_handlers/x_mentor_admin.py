from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, admins , tutor_admin , teacher_admin
from sql_tablet.x_mentors_dp import sql_command_all, sql_command_delete, sql_command_all_ids

async def delete_data(message: types.Message):
    if message.from_user.id not in admins and tutor_admin  and teacher_admin :
        await message.answer("Ты не мой босс!")
    else:
        mentors = await sql_command_all()
        for i in mentors:
            await message.answer(

                f" {i[2]} "
                        f"{i[3]} {i[4]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"Удалить {i[1]}",
                                         callback_data=f"delete {i[0]}")
                ))


async def complete_delete(callback: types.CallbackQuery):
    await sql_command_delete(callback.data.replace("delete ", ""))
    await callback.answer("Удалено с БД!", show_alert=True)
    await callback.message.delete()


async def rassylka(message: types.Message):
    if message.from_user.id not in admins:
        await message.answer("Ты не мой босс!")
    else:
        mentors = await sql_command_all_ids()
        for i in mentors:
            await bot.send_message(i[0], message.text[3:])



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(rassylka, commands=['R'])
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda callback: callback.data and callback.data.startswith("delete ")
    )
