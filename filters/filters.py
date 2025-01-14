from typing import Union
from data.config import Config
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: Message) -> bool: 
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type




class IsAdmin(BaseFilter):
    async def __call__(self, message: Message, config: Config) -> bool:
        return int(message.from_user.id) in config.ADMINS