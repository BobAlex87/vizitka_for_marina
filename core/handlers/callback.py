from aiogram import Bot
from aiogram.types import CallbackQuery, FSInputFile, message, Message
from core.keyboards.inline import first_inline_keyboard, second_inline_keyboard, questions_inline_keyboard, \
    questions_inline_keyboard_repiet


async def get_button_more_info(call: CallbackQuery, bot: Bot):
    """
    ответ на нажатие инлайн-кнопки 'больше информации'
    :param call: CallbackQuery
    :param bot: Bot
    :return: '✅вот тебе информация в разных форматах🗂 \nвыбирай что тебе удобнее:',
        reply_markup=second_inline_keyboard,
    """
    await call.message.answer(
        '✅вот тебе информация в разных форматах🗂 \nвыбирай что тебе удобнее:',
        reply_markup=second_inline_keyboard,
    )
    await call.answer() #для того чтобы кнопка не мигала


async def get_button_link(call: CallbackQuery, bot: Bot):
    """
    ответ на нажатие инлайн-кнопки 'присоедитится' и 'реферальная ссылка'
    :param call: CallbackQuery
    :param bot: Bot
    :return: "https://www.livegoodtour.com/Marynaantipova/"
    """
    text = '<a href= "https://www.livegoodtour.com/Marynaantipova/">\u27a1\ufe0fЭто реферальная ссылка!!!</a>'
    await call.message.answer(text)
    await call.answer()


async def get_button_google_doc(call: CallbackQuery, bot: Bot):
    await call.message.answer("https://docs.google.com/document/d/11QnMhYrAeLnRQ7mPZGWdfn0aXeg_OtOhhLuNDIALM8I/edit")
    await call.answer() #для того чтобы кнопка не мигала


async def get_button_video(call: CallbackQuery, bot: Bot):
    video = FSInputFile("core/images/video_inf.mpeg")
    await call.message.answer_video(video)
    await call.answer()


async def get_button_call_manager(call: CallbackQuery, bot: Bot):
    """
    ответ на нажатие инлайн-кнопки 'связь с менеджером'
    :param call: CallbackQuery
    :param bot:
    :return: first_name="Марина", phone_number="+380955498778"
    """
    await call.message.answer_contact(first_name="Марина", phone_number="+380955498778")
    await call.answer()


async def get_button_questions(call: CallbackQuery, bot: Bot):
    """
    ответ на нажатие инлайн-кнопки 'частые вопросы'
    :param call: CallbackQuery
    :param bot: Bot
    :return: 'эти вопросы звучат чаще всего:',
        reply_markup=questions_inline_keyboard,
    """
    photo = FSInputFile("core/images/question.jpg")
    await call.message.answer_photo(
        photo,
        caption='Это самые часто-задаваемые вопросы:',
        reply_markup=questions_inline_keyboard
    )
    await call.answer()


async def get_questions_1(call: CallbackQuery, bot: Bot):
    """
     Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard 'условия входа'
    """
    photo = FSInputFile("core/images/deal.jpg")
    await call.message.answer_photo(
        photo,
        caption='🎯Эксклюзивные цены на все виды товаров и услуг со скидкой до 75% Продукты премиум класса.\n'
        '🎯Без обязательных закупок.\n'
        '🎯Бессрочная Клубная карта 40$, приобретается единожды.\n'
        '🎯 Работа онлайн из любой точки мира.\n'
        '🎯Бесплатная международная доставка.\n'
        '🎯Бизнес передаётся по наследству.\n'
        '🎯Выплаты в сеть до 82.5%‼\n17.5% - идут на развитие компании,\n'
        'оплата налогов, открытие складов, поощрение членов клуба.',
        reply_markup=questions_inline_keyboard_repiet
    )
    await call.answer()

async def get_questions_2(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard '6 видов дохода'
    """
    photo = FSInputFile("core/images/get_money.jpg")
    await call.message.answer_photo(
        photo,
        caption='ответ на: 6 видов дохода'
        '1-й вид дохода\n'
        '2-й вид дохода\n'
        '3-й вид дохода\n'
        '4-й вид дохода\n'
        '5-й вид дохода\n'
        '6-й вид дохода',
        reply_markup=questions_inline_keyboard_repiet
    )
    await call.answer()

async def get_questions_3(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard 'вывод средств'
    """
    photo = FSInputFile("core/images/money.jpg")
    await call.message.answer_photo(
        photo,
        caption='🏦 Гроші накопичуються на внутрішньому рахунку в особистому кабінеті.\n'
        '👍При цього їх можна знімати в будь-який момент.\n'
        'Як зняти гроші?\n📍На карту Мастеркард\n📍Через внутрішні кошти - прямо на вашу карту\n📍'
        'Провести в криптовалюту\nПросто супер!🔥',
        reply_markup=questions_inline_keyboard_repiet,)
    await call.answer()

async def get_questions_4(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard 'пассивный доход'
    """
    photo = FSInputFile("core/images/add_money.jpg")
    await call.message.answer_photo(
        photo,
        caption="✅У кожного є можливість почати заробляти до 2047$, не запросивши жодної людини\n"
        "✅Є продукт, але обов'язкових закупівель немає!\n"
        "✅Продукт не прив'язаний до маркетингу\n"
        "✅ Вартість продукту нижче за риночну на 75-80%\n"
        "✅ За 5 місяців – понад 300 000 партнерів у 200-х країнах світу\n"
        "✅ Лояльний вхід - 50$\n"
        "✅ За кожного особисто  запрошеного отримуєте  25$\n"
        "✅ З запрошеного 50% – реферальний бонус (до 10-го рівня)",
        reply_markup=questions_inline_keyboard_repiet,
    )
    await call.answer()


async def get_exit_inline(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard 'выход',
    возвращает пользователя к стартовому меню выбора кнопок
    """
    photo = FSInputFile("core/images/LiveGoog.jpg")
    await call.message.answer_photo(
        photo,
        caption='Ну что готов присоединиться к нашей команде?',
        reply_markup=first_inline_keyboard,
    )
    await call.answer()


async def get_next_question(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard_repiet 'еще вопрос'
    """
    photo = FSInputFile("core/images/вопрос.jpg")
    await call.message.answer_photo(
        photo,
        caption='выбери еще вопрос который тебя интересует',
        reply_markup=questions_inline_keyboard,
    )
    await call.answer()
