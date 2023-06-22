import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("mentors.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name VARCHAR (100) NOT NULL,"
               "age INTEGER NOT NULL,"
               "groups VARCHAR (10),"
               "direction VARCHAR (144) NOT NULL)")
    db.commit()
async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO anketa "
            "(name,age,groups,direction) "
            "VALUES (?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_random():
    mentors= cursor.execute("SELECT * FROM anketa").fetchall()
    random_mentors = random.choice(mentors)
    return random_mentors


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_all_ids():
    return cursor.execute("SELECT id FROM anketa").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()

