from aiogram import Bot
from aiogram.types import FSInputFile
from aiogram.types import Message
from core.keyboards.inline import first_inline_keyboard
from core.database.database import db_start


async def get_start(message: Message, bot: Bot):
    """
    Приветственное сообщение, ответ на команду /start
    :param message: Message
    :param bot: Bot
    :return: приветственный текст и две инлайн-кнопки:"больше информации"(открывает следующий блок кнопок) и
    "присоединиться" (переадресовывает на реферальную ссылку)
    """
    await db_start(message, bot)
    photo = FSInputFile("core/images/LiveGoog.jpg")
    await message.answer_photo(photo)
    await message.answer(f'Привет {message.from_user.first_name}👋 рад тебя видеть!'
                         f'\nСейчас я тебя познакомлю с новым проектом <b>LiveGood</b>'
                         f'\nв котором можно зарабатывать при минимальных вложениях'
                         f'\nи расскажу как построить пассивный доход до <b>2000 грн/месяц</b>',
                         reply_markup=first_inline_keyboard)


async def get_help(message: Message, bot: Bot):
    """
    Даный хэндлер отвечает на команду '/help' при нажатии боковой кнопки 'menu'
    """
    await message.answer("Я бот-помошник, и моя задача предоставить тебе всю необходимую информацию, "
                         "а также ответить на возникшие у тебя вопросы")


async def get_exit(message: Message, bot: Bot):
    """
    Даный хэндлер отвечает на команду '/exit' при нажатии боковой кнопки 'menu'
    """
    await message.answer(f"Обращяйся еще {message.from_user.first_name}\nЯ всегда рад помочь!")


async def get_link(message: Message, bot: Bot):
    """
    Даный хэндлер отвечает на команду '/link' при нажатии боковой кнопки 'menu'
    """
    text = '<a href= "https://www.livegoodtour.com/Marynaantipova/">\u27a1\ufe0fЭто реферальная ссылка!!!</a>'
    await message.answer(text)


async def get_answer(message: Message, bot: Bot):
    """
    Даный хэндлер отвечает 'Воспользуйся кнопкой "Menu"!' на любой случайный текст отправленный пользователем,
    при условии, что текст не являеться запрограмированной командой для бота
    """
    await message.answer('Воспользуйся кнопкой "Menu"!')
