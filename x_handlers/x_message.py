import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import admins, bot
from sql_tablet.x_mentors_dp import sql_command_all_ids
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger





async def heloo():
    photo = open(r"C:\Users\geeks\OneDrive\Изображения\Saved Pictures\avatar-telegramm-pixelbox.ru-58.jpg" ,"rb")
    for user in admins :
        await bot.send_photo(
            chat_id=user,
            photo = photo,
            caption=f"helooo!!!\n"
                    f"how are you ? "
        )


async def new_year():

        await bot.send_message(
           f"С Новым годом!"
        )


async def goodbye():
         await bot.send_message(f"goodbye!!!")



async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    scheduler.add_job(
          goodbye,
        CronTrigger(

                    hour=23,
                       minute=00,
                       start_date=datetime.datetime.now()
                    ),text = f"->")

    scheduler.add_job(
       heloo,
        IntervalTrigger(
            seconds=200,
            start_date=datetime.datetime.now()
        ))

    scheduler.add_job(
      new_year,
        DateTrigger(
          run_date=datetime.datetime(year=2024, month=1, day=1)    ),)
    scheduler.start()