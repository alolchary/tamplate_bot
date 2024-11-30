from aiogram.fsm.state import State, StatesGroup
# await state.set_state()
# await state.clear()
class State(StatesGroup):
    name = State()