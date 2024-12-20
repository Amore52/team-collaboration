import telebot

from .models import Salon, Specialist, WorkingHour, Service, SalonManager, Payment, Notification, Appointment

from .keyboards import (create_consent_keyboard,
                        create_first_keyboard, create_second_keyboard,
                        create_salons_inline_keyboard,
                        create_specialits_inline_keyboard, return_chosen_salon, return_chosen_specialist)


# Обработчик команды /start

def handle_start(bot: telebot.TeleBot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        with open('agreement.txt', 'rb') as file:
            bot.send_document(message.chat.id, file)
        bot.send_message(message.chat.id, "Для продолжения работы с ботом необходимо принять соглашение "
                                          "об обработке персональных данных."
                         " Прочтите соглашение и нажмите кнопку 'Принять'.",
                         reply_markup=create_consent_keyboard()
                         )


def handle_callbacks(bot: telebot.TeleBot):
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callback(call):
        if call.data == 'accept':
            bot.send_message(call.message.chat.id, "Спасибо! Вы приняли соглашение. Теперь вы можете продолжить.",
                             reply_markup=create_first_keyboard())
        elif call.data == 'reject':
            bot.send_message(call.message.chat.id,
                             "Вы не приняли соглашение. Для продолжения работы с ботом необходимо дать согласие.")


# обработчик стандартной клавиатуры


def handle_messages(bot: telebot.TeleBot):
    managers = SalonManager.objects.all()
    services = Service.objects.all()
    print(services)

    @bot.message_handler(func=lambda message: True)
    def handler_message(message):
        if message.text == "Хочу записаться по номеру телефона":
            response = "Number:\n"
            for manager in managers:
                response += f"{manager.phone_number}  - ({manager.name})\n"
            bot.send_message(message.chat.id, response)

        elif message.text == "Выбрать салон":
            bot.send_message(message.chat.id, "Далее вы можете узнать цены на процедуры или записаться по времени",
                             reply_markup=create_second_keyboard())
        elif message.text == 'Прайс на процедуры':
            services = Service.objects.all()
            if not services:
                bot.send_message(message.chat.id, "Список услуг пуст.")
            else:
                response = "Прайс на процедуры:\n\n"
                for service in services:
                    response += f"""{service.category}\nЦена:{service.price} руб.\nДлительность:{
                        service.duration}  минут\nОписание{service.description}\n\n"""
                bot.send_message(message.chat.id, response)

        elif message.text == 'Назад':
            bot.send_message(message.chat.id, "Вы вернулись в Главное Меню",
                             reply_markup=create_first_keyboard())
        elif message.text == 'Наши салоны':
            bot.send_message(message.chat.id, "Выберите салон:",
                             reply_markup=create_salons_inline_keyboard())
        elif message.text == "Выбрать любимого специалиста":
            bot.send_message(message.chat.id, "Наши специалисты",
                             reply_markup=create_specialits_inline_keyboard())


print()
# Обработчик нажатий  инлайн-кнопки
