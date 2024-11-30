from aiogram import types


async def set_default_commands(bot):
    commands = [types.BotCommand(command='start', description='Запустить бота')]
    await bot.set_my_commands(commands=commands)