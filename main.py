import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from core.database.database import db_start, send_data
from core.handlers.basic import get_start, get_help, get_answer, get_link, get_exit
from core.handlers.callback import get_button_more_info, get_button_link, \
    get_button_call_manager, get_button_questions, get_questions_1, get_questions_2, get_questions_3, get_questions_4, \
    get_exit_inline, get_next_question
from core.commands.commands_menu import set_commands

from aiogram.client.session.aiohttp import AiohttpSession


async def start_bot(bot: Bot):
    await set_commands(bot)#Активируем кнопку Menu
    #await bot.send_message(config.admin_id.get_secret_value(), text='Бот запущен!')


#async def stop_bot(bot: Bot):
    #await bot.send_message(config.admin_id.get_secret_value(), text='Бот остановлен!')


async def main():
    #session = AiohttpSession(proxy="http://proxy.server:3128") # для подключения на pytonanywear

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    bot = Bot(
        token=config.bot_token.get_secret_value(),
        parse_mode="HTML",
        #session=session # для подключения на pytonanywear
    )
    dp = Dispatcher(storage=MemoryStorage())

#регистрируем хендлеры в диспетчере:
    dp.startup.register(start_bot)
    #dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_exit, Command(commands=['exit']))
    dp.message.register(get_link, Command(commands=['link']))
    dp.message.register(send_data, Command(commands=['data']))#у бота нет кнопки для этой команды!!!
    dp.callback_query.register(get_button_more_info, F.data == "more_info")
    dp.callback_query.register(get_button_link, F.data == "link")
    #dp.callback_query.register(get_button_google_doc, F.data == "doc")
    dp.callback_query.register(get_button_call_manager, F.data == "call_manager")
    dp.callback_query.register(get_button_questions, F.data == "questions")
    dp.callback_query.register(get_questions_1, F.data == "text_1")
    dp.callback_query.register(get_questions_2, F.data == "text_2")
    dp.callback_query.register(get_questions_3, F.data == "text_3")
    dp.callback_query.register(get_questions_4, F.data == "text_4")
    dp.callback_query.register(get_exit_inline, F.data == "exit_inline")
    dp.callback_query.register(get_next_question, F.data == "next_question")
    dp.message.register(get_answer)
    dp.message.register(db_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
