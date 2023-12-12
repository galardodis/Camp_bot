from telebot import *
from tokens import TELE_TOKEN
from import_game import data, app_filter
from special_symbols import sp_symbols
from tag import tags

bot = telebot.TeleBot(TELE_TOKEN)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Все игры')
    btn2 = types.KeyboardButton('Иры по тэгам')
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id,
                     f'Привет, *{sp_symbols(message.from_user.first_name)}*, я знаю {len(data)} игры\n\n'
                     f'Нажми кнопку "ВСЕ ИГРЫ" и я покажу какие игры я знаю\n\n'
                     f'Или же нажми кнопку "ИГРЫ ПО ТЭГАМ" и я отсортирую игры для твоего удобства\n\n'
                     f'Я обучаюсь, поэтому количество игр будет расти, да и я буду меняться 😉',
                     parse_mode='MarkdownV2',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data in tags:
        games = app_filter('A-z', callback.data)
        num_game = len(games)
        n_max = 0
        while True:
            markup = types.InlineKeyboardMarkup()
            for game in games[n_max::]:
                markup.add(types.InlineKeyboardButton(game, callback_data=game))
            if num_game - n_max > 100:
                bot.send_message(callback.message.chat.id,
                                 f'Игры по тэгу "{callback.data}" {n_max + 1} - {n_max + 100}', parse_mode='html',
                                 reply_markup=markup)
            else:
                bot.send_message(callback.message.chat.id,
                                 f'Игры по тэгу "{callback.data}" {n_max + 1} - {n_max + num_game % 100}',
                                 parse_mode='html',
                                 reply_markup=markup)
            n_max += 100
            if n_max >= num_game:
                break
    else:
        for game in data:
            if game['name'] == callback.data:
                bot.send_message(callback.message.chat.id,
                                 f'*{sp_symbols(callback.data)}*\n\n{sp_symbols(game["description"])}',
                                 parse_mode='MarkdownV2')


@bot.message_handler(content_types=['text', ])
def type_sort(message: telebot.types.Message):
    if message.text == 'Все игры':
        games = app_filter('A-z')
        num_game = len(games)
        n_max = 0
        while True:
            markup = types.InlineKeyboardMarkup()
            for game in games[n_max::]:
                markup.add(types.InlineKeyboardButton(game, callback_data=game))
            if num_game - n_max > 100:
                bot.send_message(message.chat.id, f'{message.text} {n_max + 1} - {n_max + 100}',
                                 parse_mode='html', reply_markup=markup)
            else:
                bot.send_message(message.chat.id, f'{message.text} {n_max + 1} - {n_max + num_game % 100}',
                                 parse_mode='html', reply_markup=markup)
            n_max += 100
            if n_max >= num_game:
                break


    elif message.text == 'Иры по тэгам':
        markup = types.InlineKeyboardMarkup()
        for tag in tags:
            markup.add(types.InlineKeyboardButton(tag, callback_data=tag))
        bot.send_message(message.chat.id, f'Я знаю вот эти тэги:',
                         parse_mode='html', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Я не знаю как на это реагировать, но я все еще учусь')


bot.polling()
