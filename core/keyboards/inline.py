from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


first_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Больше информации",
        callback_data="more_info"
    ),
        InlineKeyboardButton(
            text="Присоединиться",
            callback_data="link")]
])

second_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="google_doc",
        callback_data="doc"
    )],
    [InlineKeyboardButton(
        text="video",
        url="https://www.youtube.com"
    )],
    [InlineKeyboardButton(
        text="pdf",
        callback_data="pdf"
    )]
])
