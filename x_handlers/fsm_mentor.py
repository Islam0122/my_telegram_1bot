from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from aiogram import types, Dispatcher
from x_handlers.keyboards import start_markup, cancel_markup , submit_markup
from config import teacher_admin, tutor_admin , admins
from sql_tablet.x_mentors_dp import  sql_command_insert

class UserState(StatesGroup):
    name = State()
    age = State()
    group = State()
    direction = State()
    submit = State()


async def mentor_register(message: types.Message):
    if message.from_user.id not in teacher_admin and tutor_admin and admins:

        await message.answer("Ты не мой босс!")


    else:
        await message.answer(f"привет босс {message.from_user.full_name}")
        if message.chat.type == 'private':

            await UserState.name.set()
            await message.answer("имя ментора ", reply_markup=cancel_markup)
        else:
            await message.reply("Пиши в личке!")


async def get_name(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        await message.answer("пиши буквами !!")
    else:
        async with state.proxy() as data:

            data['name'] = message.text


            await message.answer("Отлично! Теперь введите  возраст ментора .", reply_markup = cancel_markup)
            await UserState.next()

async def get_age(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пиши числа!")
    else:
        async with state.proxy() as data:
            data['age'] = message.text

            await message.answer("Отлично! Теперь введите группа  ментора .", reply_markup= cancel_markup)
            await UserState.next()


async def get_group(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['group'] = message.text

    await message.answer("Отлично! Теперь Напрвление. ментора .", reply_markup= cancel_markup)
    await UserState.next()


async def get_dion(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['напрвление'] = message.text

    await message.answer(f"Имя: {data['name']}\n" 
                         f" возраст: {data['age']}\n"
                         f"группа: {data['group']}\n"
                         f"напрвление: {data['напрвление']}\n")

    await message.answer("Все верно?", reply_markup= submit_markup)
    await UserState.next()

async def submit(message: types.Message, state: FSMContext):
    if message.text.lower() == 'да':
        # Запись в БД
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Записал в БД!",reply_markup=start_markup)
    elif message.text.lower() == 'заново':
        await message.answer("пиши команду -> /reg")
        await state.finish()
    elif message.text.lower() == 'cancel':
        await state.finish()
        await message.answer('Отменено!')
    else:
        await message.answer("Используй кнопки!")


async def cancel_reg(message: types.Message, state: FSMContext):
    await state.get_state()
    await message.answer(" пока ", reply_markup=start_markup)

    await state.finish()



def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(cancel_reg, commands=['cancel'], state='*')
    dp.register_message_handler(cancel_reg, Text(equals='cancel', ignore_case=True), state='*')

    dp.register_message_handler(mentor_register, commands=['reg'])
    dp.register_message_handler(get_name, state=UserState.name)
    dp.register_message_handler(get_age, state=UserState.age)
    dp.register_message_handler(get_group, state=UserState.group)
    dp.register_message_handler(get_dion, state=UserState.direction)
    dp.register_message_handler(submit, state=UserState.submit)
