import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import authentication


t= open("token.txt","r")
if t.mode == 'r':
    contents = t.read()
TOKEN=contents
bot = telepot.Bot(TOKEN)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text' and msg['text'].startswith('/'):
        if msg['text'] == '/start':
            bot.sendMessage(chat_id, 'Welcome dear friend👩‍💻 👨‍💻!\nДля початку натисни🔑 /help \nЯкщо ти знайомий з ботом, то /menu')
        elif msg['text'] == '/help':
            bot.sendMessage(chat_id, 'Застряг🤯? Зараз допоможемо🤖. Ознайомся з цим гайдом: https://telegra.ph/Korotkij-ekskurs-po-botu-11-04')
        elif msg['text'] == '/menu':
            bot.sendMessage(chat_id, 'Почати вивчення криптографії😎- \n /lection \n Спробувати свої сили🕵️‍♀️🕵️‍♂️- \n /practice')
        elif msg['text'] == '/lection':
            bot.sendMessage(chat_id,'/l1 - Шифр Цезаря \n /l2- SHifr-Vizhenera\n /l3- Машина Беббіджа  \n /l4- \n /l5-' )
        elif msg['text'] == '/l1':
            bot.sendMessage(chat_id,'https://telegra.ph/SHifr-Cezarya-11-06' ) #1 lection
        elif msg['text'] == '/l2':
            bot.sendMessage(chat_id, 'https://uk.wikipedia.org/wiki/%D0%A8%D0%B8%D1%84%D1%80_%D0%92%D1%96%D0%B6%D0%B5%D0%BD%D0%B5%D1%80%D0%B0')#2lection
        elif msg['text'] == '/l3':
            bot.sendMessage(chat_id, 'https://telegra.ph/Mashina-Bebb%D1%96dzhaanal%D1%96tichna-mashina--pershij-prototip-suchasnogo-kompyutera-11-07')#3lection
        elif msg['text'] == '/l4':
            bot.sendMessage(chat_id, 'still nothing')#4lection
        elif msg['text'] == '/l5':
            bot.sendMessage(chat_id, 'we are in progress')# 5 lection
        #
        #
        # in case we need some more stuff
        #
        #
        elif msg['text'] == '/practice':
            bot.sendMessage(chat_id, '/p1 - Ceasar \n /p2 \n /p3  \n /p4 \n /p5')
        elif msg['text'] == '/p1':
            bot.sendMessage(chat_id, ' https://telegra.ph/Zadacha-2-SHifr-Vizheneral2-11-07' ) #1task
        elif msg['text'] == '/p2':
            bot.sendMessage(chat_id, '...')#2task
        elif msg['text'] == '/p3':
            bot.sendMessage(chat_id, 'ENIGMA ONE LOVE')#3task
        elif msg['text'] == '/p4':
            bot.sendMessage(chat_id, 'still nothing')#4task
        elif msg['text'] == '/p5':
            bot.sendMessage(chat_id, 'ESPRESSO PATRONUM')# 5task
            #
            #answers

            #
    elif content_type == 'text':
       bot.sendMessage(chat_id, 'Невідомий текст: /menu \n Натисніть /help для детальнішої інформації.')
    elif content_type != 'text':
     bot.sendMessage(chat_id, 'Невідомий текст: /menu \n Натисніть /help для детальнішої інформації.')

print (authentication.load_users())

#def on_chat_message(msg):


MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')
# Keep the program running.
while 1:
    time.sleep(10)