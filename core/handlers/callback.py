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
        '✅вот тебе информация в разных форматах🗂 \nвыбирай, что тебе удобнее:',
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


# async def get_button_video(call: CallbackQuery, bot: Bot):
#     video = FSInputFile("core/images/video_inf.mpeg")
#     await call.message.answer_video(video)
#     await call.answer()


async def get_button_call_manager(call: CallbackQuery, bot: Bot):
    """
    ответ на нажатие инлайн-кнопки 'связь с менеджером'
    :param call: CallbackQuery
    :param bot:
    :return: first_name="Марина", phone_number="+380955498778"
    """
    await call.message.answer('t.me/marynaantipova')
    #await call.message.answer_contact(first_name="Марина", phone_number="+380955498778")
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
        caption='✅пройти регистрацию по ссылке \n📌 https://livegoodtour.com/Marynaantipova 📌'
                '\n✅приобрести одноразовый клубный билет 40$ '
                '\n✅вносить ежемесячный членский взнос 9,95$ '
                '\nИЛИ❗️ \n✅Внести сразу на год 140$ (билет и членский взнос) - экономите 20$',
        reply_markup=questions_inline_keyboard_repiet
    )
    await call.answer()

async def get_questions_2(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard 'Что я получу от участия в клубе?'
    """
    photo = FSInputFile("core/images/get_money.jpg")
    await call.message.answer_photo(
        photo,
        caption='Что получаешь от участия в клубе:'
                '\n✅У каждого есть возможность начать <b>зарабатывать до 2047$</b> не пригласив ни одного человека.'
                '\n✅Есть и покупать продукт не обязательно - продукт не привязан к маркетингу'
                '\n✅Стоимость продукта ниже на 70-80% рыночной'
                '\n✅за год уже 1 000000 пользователей в 300 странах мира'
                '\n✅ лояльный минимальный вход 50$ единоразовый'
                '\n✅за каждого приглашенного вам выплачивают 25$ - 50% реферальный бонус (до 10 уровня)'
                '\n✅матчинг бонус - 50%  с каждого лично приглашенного до 5 уровня',
        reply_markup=questions_inline_keyboard_repiet
    )
    await call.answer()

async def get_questions_3(call: CallbackQuery, bot: Bot):
    """
    Ответ на нажатие инлайн-кнопки клавиатуры questions_inline_keyboard 'Как выводятся средства?'
    """
    photo = FSInputFile("core/images/kopilka.jpg")
    await call.message.answer_photo(
        photo,
        caption='🏦 Деньги копятся на внутреннем счету в личном кабинете.'
                '\n👍При этом их можно <b>снять (обналичить) в любой момент</b>.\nКак снять деньги?'
                '\n📍На карту Мастеркард'
                '\n📍Через внутренние деньги - прямо на карту'
                '\n📍Перевести в <b>криптовалюту</b>'
                '\n🔥 Просто супер! 🔥',
        reply_markup=questions_inline_keyboard_repiet,
    )
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
    photo = FSInputFile("core/images/logo.jpg")
    await call.message.answer_photo(
        photo,
        caption='Ну что, готов присоединиться к нашей команде?',
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
