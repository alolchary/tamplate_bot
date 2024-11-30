from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from utils.db_api.commands.user_commands import UserDataBase

class UserBannedMessage(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ):
        db_user: UserDataBase = data['db_user']
        status = await db_user.get_ban(event.from_user.id)
        if status:
            await event.answer(text='🔥 Вы заблокированы!')
            return
        
        return await handler(event, data)



class UserBannedCallback(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any],
    ):
        db_user: UserDataBase = data['db_user']
        status = await db_user.get_ban(event.from_user.id)
        if status:
            await event.answer(show_alert=True, text='🔥 Вы заблокированы!')
            return

        return await handler(event, data)