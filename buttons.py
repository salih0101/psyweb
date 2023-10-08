from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import database


def phone_number_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton('Отправить номер телефона', request_contact=True)
    kb.add(button)

    return kb


def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    button = KeyboardButton('📄Vebinar')
    order = KeyboardButton('Список заказов')
    cart = KeyboardButton('Корзина🗑')
    about = KeyboardButton('О нас')
    callback = KeyboardButton('Контакты☎️')

    kb.add(button)

    return kb


def access_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    access = KeyboardButton('✅Tasdiqlash')
    back = KeyboardButton('Ortga qaytish🔙')
    kb.add(access, back)

    return kb

def back_main_menu_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    back = KeyboardButton('Ortga qaytish🔙')
    kb.add(back)

    return kb

veb = 'Qabul qilindi✅🌹Oxirgi shartimiz ushbu webinar haqidagi postni 3 dugonangiz/tanishingizga yuboring👇\n\n'

veb1 = ('📣📣📣📣📣📣📣📣\n\n'
        'Sizlarga faqat eng kerakli bilimlarni beraman❗️\n'
        'Oilada Ayol Rivoji butun Oilaga ta’sir qiladi.\n'
        '❗️Agarda Rivojlanishni xohlasangiz\n'
        'ERTAGA SOAT 20:00da\n'
        '❗️Unda bu Vebinar Aynan Siz uchun❗️\n'
        'Bu Vebinarga⬇️:\n'
        '♦️Muvaffaqiyatga olib keladigan odatlarni shakllantirmoqchi boʻlganlarni;\n'
        '♦️Xayotda va jamiyatda oʻz oʻrnini topmoqchi boʻlganlarni;\n'
        '♦️Oʻzining ichki salohiyatini yuzaga chiqarishni xohlaganlarni;\n'
        '♦️Rivojlanishni davom ettirmoqchi boʻlganlarni;\n'
        '♦️Ayol kishi pul topishi kerakmi bilishni xohlaganlarni taklif qilamiz!\n\n'
        'Vebinarda ishtirok etish mutlaqo BEPUL!\n'
        '🟢 https://t.me/+nDQH74rtV0liNzM6\n🟢 https://t.me/+nDQH74rtV0liNzM6\n🟢 https://t.me/+nDQH74rtV0liNzM6')
