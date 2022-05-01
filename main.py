import telebot
import wikipedia, re
import random
from telebot import types

bot = telebot.TeleBot('5315433770:AAHkrYzfFASHXxXrBerYy1v28L2KPYWUL7c')

wikipedia.set_lang("ru")
# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext=ny.content[:1000]
        # Разделяем по точкам
        wikimas=wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем
                    # утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
@bot.message_handler(commands=['start'])
def start(m, res=False):
    name, surname = m.from_user.first_name, m.from_user.last_name
    ans = f'Добро пожаловать в игру, {name} {surname}'
    bot.send_message(m.from_user.id, ans)


f = open('questions.txt', 'r')
quest = f.read().split('\n')
f.close()
f = open('answer.txt', 'r')
answers = f.read().split('\n')
f.close()

@bot.message_handler(commands=['toplay'])
def toplay(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Вопрос")
    markup.add(item1)
    msg = bot.reply_to(m, 'Нажми: \nВопрос для начала викторины', reply_markup=markup)
    bot.register_next_step_handler(msg, start_2)
    # ожидания ввода от пользователя с переходом на другой шаг

def start_2(message):
    global vopros
    global helper
    if message.text.strip() == 'Вопрос':
        helper = random.randint(0, 2)
        vopros = quest[helper]
    msg = bot.send_message(message.chat.id, vopros.format(message.text))
    bot.register_next_step_handler(msg, answer)


def answer(message):
    global score
    score = 0
    if message.text == answers[helper]:
        score += 1
        bot.send_message(message.chat.id, 'теперь у вас {} балл/ов!'.format(score))
        global a
        a = message.text
        bot.send_message(message.chat.id, 'Хотите прочитать статью про {}?'.format(a))
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("ДА")
        markup.add(item2)
        msg = bot.reply_to(message, 'Нажми: \n"ДА" для чтения', reply_markup=markup)
        bot.register_next_step_handler(msg, wiki)
    else:
        bot.send_message(message.chat.id, 'Неправильный ответ! Извините, вы не получаете балл!')
def wiki(message):
    bot.send_message(message.chat.id, getwiki(a))





bot.polling(none_stop=True, interval=0)
