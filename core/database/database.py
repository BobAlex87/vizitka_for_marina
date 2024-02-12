import sqlite3
from aiogram import types, Bot

#создаем подключение к БД
db = sqlite3.connect('core/database/marina_db')
cursor = db.cursor()

#создаем таблицу и необходимые нам поля
async def db_start(message: types.Message, bot: Bot):
    cursor.execute("CREATE TABLE IF NOT EXISTS users("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "name TEXT,"
                   "nik TEXT)")
    db.commit()

# вибираем необходимые нам данные
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = message.chat.id
        user_name = message.from_user.first_name
        user_nik = message.from_user.username

# вставляем данные в таблицу
        cursor.execute("INSERT INTO users (id, name, nik) VALUES (?,?,?)", (user_id, user_name, user_nik))
        db.commit()
    else:
        None
        #await bot.send_message(message.chat.id, 'Такой пользователь уже существует')
