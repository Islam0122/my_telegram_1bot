from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from decouple import config

storage = MemoryStorage()

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot,storage=storage)







admins = (5627082052,5845373079,)

teacher_admin = ( 5367214519,5627082052,5845373079)
tutor_admin = (1433704284 ,)