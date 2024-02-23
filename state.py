from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup,State

class Tiflo(StatesGroup):
    choose_literature_type=State()
    

class Video(StatesGroup):
    choose_video_type=State()
    choose_economics=State()
    choose_video=State()


