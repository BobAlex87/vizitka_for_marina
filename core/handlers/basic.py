from aiogram import Bot
from aiogram.types import FSInputFile
from aiogram.types import Message
from core.keyboards.inline import first_inline_keyboard
from core.database.database import db_start


async def get_start(message: Message, bot: Bot):
    await db_start(message, bot)
    photo = FSInputFile("core/images/LiveGoog.jpg")
    await message.answer_photo(photo)
    await message.answer(f'Привет {message.from_user.first_name}👋 '
                         f'\n<b>Рад тебя видеть!</b>\n***здесь будет приветственный текст***',
                         reply_markup=first_inline_keyboard)


# async def get_inline(message: Message, bot: Bot):
#     await message.answer(f'привет {message.from_user.username}, вот тебе клавиатура',
#                          reply_markup=my_inline_keyboard)


async def get_help(message: Message, bot: Bot):
    await message.answer("Я бот-помошник, и моя задача предоставить тебе всю необходимую информацию, "
                         "а также ответить на возникшие у тебя вопросы")


async def get_exit(message: Message, bot: Bot):
    await message.answer(f"Обращяйся еще {message.from_user.username}\nЯ всегда рад помочь!")


async def get_link(message: Message, bot: Bot):
    text = '<a href= "https://www.livegoodtour.com/Marynaantipova/">\u27a1\ufe0fЭто реферальная ссылка!!!</a>'
    await message.answer(text)


async def get_answer(message: Message, bot: Bot):
    await message.answer('Воспользуйся кнопкой "Menu"!')
