import telebot

t= open("token.txt","r")
if t.mode == 'r':
    contents = t.read()
    TOKEN=contents
    bot = telebot.TeleBot(TOKEN)
# reading token
keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True , resize_keyboard=True)
keyboard.row('Лекції👩‍🎓 👨‍🎓', 'Практичні🕴🏼')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт '+message.from_user.first_name +'! 👩‍💻 👨‍💻!\n Для початку натисни🔑 /help \nЯкщо ти знайомий з ботом, то продовжуй.', reply_markup=keyboard)
    data=message.chat.id
    print("start",message.from_user.username)
    n = open("Chat_ID.txt", "a")
    if n.mode == 'a':
        n.write(str('@'+message.from_user.username)+' ' + str(data) +'\n')

@bot.message_handler(commands=['help']) # допомога
def start_message(message):
    bot.send_message(message.chat.id,'PEBKAC'+'\n'+'Застряг🤯? Зараз допоможемо🤖. Ознайомся з цим гайдом: https://telegra.ph/Korotkij-ekskurs-po-botu-11-04' )
    print('using help', '\n')
    data = message.chat.id
    #
@bot.message_handler(content_types=['text'])
def send_text(message):
    data = message.chat.id
    if message.text == 'Лекції👩‍🎓 👨‍🎓':
        bot.send_message(message.chat.id, 'Зміст \n /l1 - Шифр Цезаря \n /l2- Шифр Віженера \n /l3- Машина Беббіджа  \n /l4- Шифр ADFGVX \n /l5-"Великий шифр" \n /l6-Енігма \n /l7-Шифр Хілла \n ')
        bot.send_message(message.chat.id, '\n /l8 -Омофонічний шифр заміни \n /l9-Шифр Марії Стюарт \n /l10- Матричний шифр обходу  \n /l11-Шифр Бекона \n /l12- \n /l13- \n /l14- \n ')
    elif message.text.lower() == '/l1':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-Cezarya-11-06')  # 1 lection`
    elif message.text.lower() == '/l2':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-Vizhenera-11-19')  # 2lection`
    elif message.text.lower() == '/l3':
        bot.send_message(message.chat.id, 'https://telegra.ph/Mashina-Bebb%D1%96dzhaanal%D1%96tichna-mashina--pershij-prototip-suchasnogo-kompyutera-11-07')  # 3lection`
    elif message.text.lower() == '/l4':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-ADFGVX-11-30')  # 4lection`
    elif message.text.lower() == '/l5':
        bot.send_message(message.chat.id, 'https://telegra.ph/Velikij-shifr-12-01')  # 5 lection`
    elif message.text.lower() == '/l6':
        bot.send_message(message.chat.id, 'https://telegra.ph/En%D1%96gma-12-01')  # 6 lection`
    elif message.text.lower() == '/l7':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-H%D1%96lla-12-01')  # 7 lection`
    elif message.text.lower() == '/l8':
        bot.send_message(message.chat.id, 'https://telegra.ph/Omofon%D1%96chna-zam%D1%96na-12-03')  # 8 lection`
    elif message.text.lower() == '/l9':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-Mar%D1%96i-Styuart-12-03')  # 9 lection`
    elif message.text.lower() == '/l10':
        bot.send_message(message.chat.id, 'https://telegra.ph/Matrichnij-shifr-obhodu-12-04')  # 10 lection`
    elif message.text.lower() == '/l11':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-Bekona-12-04')  # 11 lection`
    elif message.text == 'Практичні🕴🏼':
        bot.send_message(message.chat.id, '/p1 - Шифр Цезаря \n /p2 - Шифр Віженера\n /p3 - Шифр Плейфера  \n /p4 - Шифр Хілла \n /p5')
    elif message.text.lower() == '/p1':
        bot.send_message(message.chat.id, 'https://telegra.ph/Zavdannya-11-21')
    elif message.text.lower() == '/p2':
        bot.send_message(message.chat.id, 'https://telegra.ph/Zadacha-2-SHifr-Vizheneral2-11-07')
    elif message.text.lower() == '/p3':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-Plejfera-12-04-2')
    elif message.text.lower() == '/p4':
        bot.send_message(message.chat.id, 'https://telegra.ph/SHifr-H%D1%96lla-12-04')
    print (data)

print ('Listening ...')
bot.polling()