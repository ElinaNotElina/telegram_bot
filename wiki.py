# wikipedia.set_lang("ru")
# # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
# def getwiki(s):
#     try:
#         ny = wikipedia.page(s)
#         # Получаем первую тысячу символов
#         wikitext=ny.content[:1000]
#         # Разделяем по точкам
#         wikimas=wikitext.split('.')
#         # Отбрасываем всЕ после последней точки
#         wikimas = wikimas[:-1]
#         # Создаем пустую переменную для текста
#         wikitext2 = ''
#         # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
#         for x in wikimas:
#             if not('==' in x):
#                     # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем
#                     # утерянные при разделении строк точки на место
#                 if(len((x.strip()))>3):
#                    wikitext2=wikitext2+x+'.'
#             else:
#                 break
#         # Теперь при помощи регулярных выражений убираем разметку
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\([^()]*\)', '', wikitext2)
#         wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
#         # Возвращаем текстовую строку
#         return wikitext2
#     # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
#     except Exception as e:
#         return 'В энциклопедии нет информации об этом'
# @bot.message_handler(commands=["hi"])
# def hi(m, res=False):
#     bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
# # Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
# #     bot.send_message(message.chat.id, getwiki(message.text))
# @bot.message_handler(content_types=["text"])
# def handle_text(message):
#     global vopros
#     global helper
#     if message.text.strip() == 'Вопрос':
#         helper = random.randint(0, 3)
#         vopros = quest[helper]
#     # Отсылаем юзеру сообщение в его чат
#     bot.send_message(message.chat.id, vopros)
#
# def send_text(message):
#     if message.text == str(1):
#         bot.send_message(message.chat.id, 'Молодец! ')
#     elif message.text != str(1):
#         bot.send_message(message.chat.id, 'Не правильно ...')