import asyncio
import types

from aiogram import Dispatcher, executor, Bot, types
from states import Registration
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import buttons as btns
import database
import states
import os
from dotenv import load_dotenv, find_dotenv
import logging

from datetime import datetime

load_dotenv(find_dotenv())

bot = Bot(os.getenv('TOKEN'))

logging.basicConfig(filename='spam.log', level=logging.INFO)


dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start_message(message):
    # ---Получить user_id пользователя
    user_id = message.from_user.id
    # ---Происходит проверка в базе
    checker = database.check_user(user_id)
    if checker:
        await message.answer('Приветствуем вас в нашем PsychoFemme Vebinar🐝\n\nВыберите раздел🔽',
                             reply_markup=btns.main_menu())
    else:
        await message.answer(
            'Приветствую, Пройдите простую регистрацию чтобы в дальнейшем не было проблем!\n\nОтправьте Имя для регистрации!',
            reply_markup=btns.ReplyKeyboardMarkup())
        await Registration.getting_name_state.set()


@dp.message_handler(state=Registration.getting_name_state)
async def get_name(message, state=Registration.getting_name_state):
    user_answer = message.text

    await state.update_data(name=user_answer)
    await message.answer('Имя сохранил!\n\nОтправьте номер телефона!', reply_markup=btns.phone_number_kb())

    await Registration.getting_phone_number.set()


@dp.message_handler(state=Registration.getting_phone_number, content_types=['text', 'contact'])
async def get_number(message: types.Message, state=Registration.getting_phone_number):
    user_answer = message.text

    if message.content_type == 'text':
        user_answer = message.text

        if not user_answer.replace('+', '').isdigit():
            await message.answer('Отправьте номер телефона')
            return

    elif message.content_type == 'contact':
        user_answer = message.contact.phone_number

    await state.update_data(number=user_answer)
    await message.answer('Номер сохранил!', reply_markup=btns.main_menu())

    await message.answer('Успешно зарегистрирован📝!\n\nВыберите раздел🔽', reply_markup=btns.main_menu())

    all_info = await state.get_data()
    name = all_info.get('name')
    phone_number = all_info.get('number')
    user_id = message.from_user.id
    database.add_user(user_id, name, phone_number)
    # ---Остановка
    await state.finish()



# ---Независимый обработчик текста для основного меню
@dp.message_handler(content_types=['text'])
async def main_menu(message):
    user_answer = message.text


    if user_answer == '📄Vebinar':
        await message.answer("Vebinarda ishtirok etish uchun kichik anketamizni to`ldiring va '✅Tasdiqlash' tugmasini bosing\n\n https://docs.google.com/forms/d/e/1FAIpQLSdftrN5zTDfbmgRIjAVqInzVnjTkviiQgOwLAdelNUriuV9vg/viewform?usp=sf_link", reply_markup=btns.access_kb())

    elif user_answer == '✅Tasdiqlash':
        await message.answer(btns.veb)
        await message.answer('...')
        await asyncio.sleep(2)
        await message.answer(btns.veb1, reply_markup=btns.back_main_menu_kb())

    elif user_answer == 'Назад🔙':
        await message.answer('❗️Вы вернулись в Главное меню❗️\n\nВыберите раздел🔽', reply_markup=btns.main_menu())



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

