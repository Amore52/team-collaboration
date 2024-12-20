import os
import sys
import django
import telebot
from .models import Salon, Specialist


def create_back_button():
    return telebot.types.KeyboardButton('Назад')


# создаем кнопки согласия на обработку персональных данных
def create_consent_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    assept_button = telebot.types.InlineKeyboardButton(
        'Принять', callback_data='accept')
    reject_button = telebot.types.InlineKeyboardButton(
        'Отклонить', callback_data='reject')
    keyboard.add(assept_button, reject_button)
    return keyboard


# Создаем первый набор кнопок
def create_first_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("Выбрать салон")
    button2 = telebot.types.KeyboardButton("Выбрать любимого специалиста")
    button3 = telebot.types.KeyboardButton(
        "Хочу записаться по номеру телефона")

    keyboard.row(button1)
    keyboard.row(button2, button3)

    return keyboard

# Создаем второй набор кнопок


def create_second_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button5 = telebot.types.KeyboardButton("Прайс на процедуры")
    button6 = telebot.types.KeyboardButton("Запись по времени")
    button7 = telebot.types.KeyboardButton("Наши салоны")
    back_button = create_back_button()
    keyboard.row(button5, button6)
    keyboard.row(button7, back_button)

    return keyboard

# создаем инлайн кнопки


def create_salons_inline_keyboard():
    keyboard = telebot.types.InlineKeyboardMarkup()
    salons = Salon.objects.all()
    for salon in salons:
        salon = telebot.types.InlineKeyboardButton(
            salon.name, callback_data=f'salon_{salon}')
        keyboard.row(salon)
    return keyboard


print()


def create_specialits_inline_keyboard():
    specialists = Specialist.objects.all()
    keyboard = telebot.types.InlineKeyboardMarkup()
    for specialist in specialists:
        master = telebot.types.InlineKeyboardButton(
            f"{specialist.name}", callback_data=f'specialist_{specialist}')
        keyboard.row(master)
    return keyboard


def return_chosen_salon(call):
    return call.data.split('_')[1]


def return_chosen_specialist(call):
    return call.data.split('_')[1]
