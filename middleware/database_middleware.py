from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery

from data.config import Config
from utils.db_api.commands.user_commands import UserDataBase

from typing import Union

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

class DataBaseMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Union[Message, CallbackQuery], Dict[str, Any]], Awaitable[Any]],
        event: Union[Message, CallbackQuery],
        data: Dict[str, Any],
    ):
        config: Config = data['config']
        
        engine = create_async_engine(url=config.session_url, echo=False)
        session = async_sessionmaker(engine, expire_on_commit=False)
        

        async with session() as cursor:
            data['db_user'] = UserDataBase(session=cursor)


        return await handler(event, data)


