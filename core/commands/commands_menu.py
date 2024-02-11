from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начало работы с ботом'
        ),
        BotCommand(
            command='help',
            description='Жми если запутался)'
        ),
        BotCommand(
            command='exit',
            description='Выход'
        ),
        BotCommand(
            command='link',
            description='реферальная ссылка')
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())
