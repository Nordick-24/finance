from loguru import logger
import telebot
import os
import psycopg2
from config import host, user, password, db_name


token = os.getenv("FINBOTTOKEN")
bot = telebot.TeleBot(token)

def get_money(table_name, bot):
    @bot.message_handler()
    def get_user_moneylose(message):
        cursor.execute(f"insert into {table_name} (price) values ('{message.text}')")

def actioen(table_name, action, message, bot):

    if message.from_user.id == 'your id':
        if action == 'look':
            cursor.execute(f"select * from {table_name}")
            row = cursor.fetchall()
            bot.send_message(message.chat.id, 'date : price')
            for rowd in row:
                data = f"""{rowd}"""
                bot.send_message(message.chat.id, data)

        elif action == 'insert':
            bot.send_message(message.chat.id, "How much money do lose?:")

            get_money(table_name, bot)

    else:
        bot.send_message(message.chat.id, "Sorry , ask sysadmin")

try:
    database = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
    )
    database.autocommit = True
    cursor = database.cursor()

    @bot.message_handler(commands=['start'])
    def start(message):
        actions = """
        What do spiding do you want?
        \n1)Execute apartament /exeapa
        \n2)Execute car /execar
        \n3)Execute clothings /execlot
        \n4)Execute restaurant /exerest
        \n5)Look History apartament /lookapa
        \n6)Look History car /lookcar
        \n7)Look History restaurant /lookrest
        \n8)Look History clothings /lookcloth
        """
        bot.send_message(message.chat.id, actions)
        
    @bot.message_handler(commands=['lookapa'])
    def lookapa(message):
        actioen('apartament', 'look', message, bot)

    @bot.message_handler(commands=['lookcar'])
    def lookcar(message):
        actioen('car', 'look', message, bot)

    @bot.message_handler(commands=['lookrest'])
    def lookrest(message):
        actioen('reastaurants', 'look', message, bot)
    
    @bot.message_handler(commands=['lookcloth'])
    def lookcloth(message):
        actioen('clothings', 'look', message, bot)

    @bot.message_handler(commands=['exeapa'])
    def exeapa(message):
        actioen('apartament', 'insert', message, bot)

    @bot.message_handler(commands=['execar'])
    def execar(message):
        actioen('car', 'insert', message, bot)

    @bot.message_handler(commands=['execloth'])
    def execloth(message):
        actioen('clothings', 'insert', message, bot)

    @bot.message_handler(commands=['exerest'])
    def exerest(message):
        actioen('reastaurants', 'insert', message, bot)


    bot.polling(none_stop=True)

except Exception as _ex:
    logger.error(f"Database Error : {_ex}")

finally:
    cursor.close()
    database.close()
