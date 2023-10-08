from aiogram.dispatcher.filters.state import State, StatesGroup



class Registration(StatesGroup):
    getting_name_state = State()
    getting_phone_number = State()
    getting_location = State()
    getting_gender = State()

