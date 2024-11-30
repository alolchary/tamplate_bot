import asyncio
from utils.set_bot_commands import set_default_commands
import logging
import data
import filters
from data.config import Config
from aiogram import Bot, Dispatcher
from handlers import main_router
from aiogram.client.default import DefaultBotProperties

async def on_startup():
    
    config = Config('settings.ini')
    config.load_config()


    bot = Bot(token=config.BOT_TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
    dp = Dispatcher()



    await bot.delete_webhook(drop_pending_updates=True)
    await set_default_commands(bot)
    dp.include_router(router=main_router)
    await dp.start_polling(bot, config=config)


    


if __name__ == '__main__':
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(on_startup())
    except Exception as err:
        logging.exception(err)

