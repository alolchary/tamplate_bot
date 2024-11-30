from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from utils.db_api.commands.user_commands import UserDataBase
import keyboards.inline.user.keyboard as default_user


start_router = Router()


@start_router.message(Command('start'))
async def start_handler(message: types.Message, state: FSMContext, db_user: UserDataBase):
    
    await state.clear()
    await message.answer(f'Приветствую тебя, {message.from_user.first_name}', reply_markup=default_user.get_keyboard())
    await db_user.add_user(message.from_user.id, message.from_user.username)

    
