import time
import telebot
from model import is_user_alive

bot = telebot.TeleBot('5643030605:AAEb6UirhSaiKaWa3hCk_cRxvlamYphlQYQ')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет! Назови Класс билета, Имя (одним словом), '
                                      'Пол (male/female), Возраст, Прибыл ли он с супругом (1-да, 0-нет), '
                                      'с Ребенком (1-да, 0-нет), Номер билета, его Стоимость и Порт '
                                      'пасадки, - а я предскажу, выжил ли этот пассажир на Титанике!')


@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, 'Анализируем...')
    passenger_data = message.text.split()
    passenger_data.insert(0, 0)
    passenger_data.insert(9, ',')
    passenger_data[2] = '"',passenger_data[2],'"'

    answer = is_user_alive(passenger_data)

    if int(answer) == 1:
        bot.send_message(message.chat.id, 'Везунчик! Видимо, этот пассажир успел на спасательную шлюпку.')
    elif int(answer) == 0:
        bot.send_message(message.chat.id, 'Увы, но Титаник ваш пассажир... не пережил бы.')

    do_again(message)


def do_again(message):
    bot.send_message(message.chat.id, 'Проверить живучесть кого-нибудь еще?')


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except ():
            time.sleep(5)
