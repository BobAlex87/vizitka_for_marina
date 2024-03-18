from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#инлайн-клавиатура которая появляеться вместе с приветственным сообщением
first_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="Больше информации",
        callback_data="more_info"
    ),
        InlineKeyboardButton(
            text="Присоединиться",
            callback_data="link")]
])


#инлайн-клавиатура которая появляеться после нажатия кнопки "больше информации"
second_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="📚Прочесть информацию",
        url="https://drive.google.com/file/d/1HYhmVN8Ph3jQ5tIegCsrbFidpo8e0UPl/view?usp=sharing"
    )],
    [InlineKeyboardButton(
        text="📺Видео-презентация",
        url="https://www.youtube.com/watch?v=Wd_75X6BcQc"
    )],
    [InlineKeyboardButton(
        text="⁉️Частые вопросы",
        callback_data="questions"
    )],
    [InlineKeyboardButton(
        text="Связаться с менеджером",
        callback_data="call_manager"
    ),
        InlineKeyboardButton(
            text="Присоединиться",
            callback_data="link")]
])

#инлайн-клавиатура которая появляеться после нажатия кнопки "частые вопросы"
questions_inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="🤝Какие условия входа в команду?",
        callback_data="text_1"
    )],
    [InlineKeyboardButton(
        text="💎Что я получу от участия в клубе?",
        callback_data="text_2"
    )],
    [InlineKeyboardButton(
        text="💵Как выводятся средства?",
        callback_data="text_3"
    )],
    [InlineKeyboardButton(
        text="👛6 видов дохода",
        callback_data="text_4"
    )],
    [InlineKeyboardButton(
        text="реферальная ссылка",
        callback_data="link"
    ),
        InlineKeyboardButton(
            text="связь с менеджером",
            callback_data="call_manager"
    )],
    [InlineKeyboardButton(
        text="выход",
        callback_data="exit_inline"
    )]
])


#инлайн-клавиатура которая появляеться под ответом после нажатия на один из частых вопросов
questions_inline_keyboard_repiet = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text="еще вопрос",
        callback_data="next_question"
    )],
    [InlineKeyboardButton(
        text="выход",
        callback_data="exit_inline"
    )],
    [InlineKeyboardButton(
        text="реферальная ссылка",
        callback_data="link"
    ),
        InlineKeyboardButton(
            text="связь с менеджером",
            callback_data="call_manager"
    )]
])

