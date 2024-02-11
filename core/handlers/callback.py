from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile
from core.keyboards.inline import second_inline_keyboard


async def get_button_more_info(call: CallbackQuery, bot: Bot):
    await call.message.answer(
        '✅вот тебе информация в разных форматах🗂 \nвыбирай что тебе удобнее:',
        reply_markup=second_inline_keyboard,
    )
    await call.answer() #для того чтобы кнопка не мигала


async def get_button_link(call: CallbackQuery, bot: Bot):
    text = '<a href= "https://www.livegoodtour.com/Marynaantipova/">\u27a1\ufe0fЭто реферальная ссылка!!!</a>'
    await call.message.answer(text)
    await call.answer()


async def get_button_google_doc(call: CallbackQuery, bot: Bot):
    await call.message.answer("https://docs.google.com/document/d/1NiqW2SHKBD4FyTsZ1d0SshIs7Eaq8F0j/edit")
    await call.answer() #для того чтобы кнопка не мигала


async def get_button_pdf(call: CallbackQuery, bot: Bot):
    doc = FSInputFile("core/images/pdf.pdf")
    await call.message.answer_document(doc)
    await call.answer()
