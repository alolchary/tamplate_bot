from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext


admin_start = Router()


@admin_start.message(Command('admin'))
async def admin_start_handler(message: types.Message, state: FSMContext):
   await state.clear()
   await message.answer("admin panel!")
