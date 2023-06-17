from aiogram import executor
import logging
from config import dp
from x_handlers import commands, callback, extra, admin,dice,fsm_mentor




commands.register_handlers_commands(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
dice.register_handlers_1commands(dp)

fsm_mentor.register_handlers_commands(dp)
extra.register_handlers_extra(dp)







if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=False)