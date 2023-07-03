from aiogram import executor
import logging
from config import dp , bot  , admins
from x_handlers import commands, callback, extra, admin,dice,fsm_mentor,x_mentor_admin,x_message
from sql_tablet.x_mentors_dp import sql_create
from x_new_ import  x_comabds_cinema



commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
x_comabds_cinema.register_handlers_2commands(dp)
dice.register_handlers_1commands(dp)
x_mentor_admin.register_handlers_admin(dp)
admin.register_handlers_admin(dp)
fsm_mentor.register_handlers_commands(dp)
extra.register_handlers_extra(dp)



async def on_startup(dp):
    sql_create()

    await bot.send_message(admins[0], f"Я родился! boss ")
    await x_message.set_scheduler()


async def on_shutdown(dp):
    await bot.send_message(admins[0], "Пока пока!")





if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)
