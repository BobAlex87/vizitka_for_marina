import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage

from config_reader import config
from core.database.database import db_start
from core.handlers.basic import get_start, get_help, get_answer, get_link, get_exit
from core.handlers.callback import get_button_more_info, get_button_link, get_button_google_doc, get_button_pdf
from core.commands.commands_menu import set_commands


async def start_bot(bot: Bot):
    await set_commands(bot)#Активируем кнопку Menu
    #await bot.send_message(config.admin_id.get_secret_value(), text='Бот запущен!')


#async def stop_bot(bot: Bot):
    #await bot.send_message(config.admin_id.get_secret_value(), text='Бот остановлен!')


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    bot = Bot(
        token=config.bot_token.get_secret_value(),
        parse_mode="HTML"
    )
    dp = Dispatcher(storage=MemoryStorage())

#регистрируем хендлеры в диспетчере:
    dp.startup.register(start_bot)
    #dp.shutdown.register(stop_bot)

    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, Command(commands=['help']))
    dp.message.register(get_exit, Command(commands=['exit']))
    dp.message.register(get_link, Command(commands=['link']))
    dp.callback_query.register(get_button_more_info, F.data == "more_info")
    dp.callback_query.register(get_button_link, F.data == "link")
    dp.callback_query.register(get_button_google_doc, F.data == "doc")
    dp.callback_query.register(get_button_pdf, F.data == "pdf")
    dp.message.register(get_answer)
    dp.message.register(db_start)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
