import sqlite3
from aiogram import types, Bot

#создаем подключение к БД
db = sqlite3.connect('core/database/marina_db')
cursor = db.cursor()

#создаем таблицу и необходимые нам поля
async def db_start(message: types.Message, bot: Bot):
    cursor.execute("CREATE TABLE IF NOT EXISTS users("
                   "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                   "first_name TEXT,"
                   "last_name TEXT,"
                   "nik TEXT)")
    db.commit()

# вибираем необходимые нам данные
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM users WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = message.chat.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        user_nik = message.from_user.username

# вставляем данные в таблицу
        cursor.execute("INSERT INTO users (id, first_name,last_name, nik) VALUES (?,?,?,?)", (user_id, first_name,
                                                                                              last_name, user_nik))
        db.commit()
    else:
        None
        #await bot.send_message(message.chat.id, 'Такой пользователь уже существует')


def get_data_from_database():
    conn = db
    cursor = conn.cursor()
    # Пример выполнения запроса
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    #conn.close()
    return data


async def send_data(message: types.Message):
    if message.from_user.id == 469308650 or 574923539:
        # Получаем данные из базы данных
        data = get_data_from_database()

        # Формируем сообщение с данными из базы данных
        response = "Данные из базы данных:\n"
        for index, item in enumerate(data, start=1):
            response += f"{index}. {item}\n"

        # Отправляем сообщение пользователю
        await message.answer(response)
    else:
        await message.answer('у тебя нет доступа к базе данных')


