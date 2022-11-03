import telebot 
from config import token
from datetime import datetime
from random import randint
from config import quotes
import os
from telebot import TeleBot
from telebot import types
import time
import schedule
import requests

bot=telebot.TeleBot(token,parse_mode='html')
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.reply_to(message,'<i> Привет, {0.first_name}!\nОднажды все мудрецы мира собрались и решили создать нечто, что по своей мудрости превзойдет всех...</i>'.format(message.from_user))
    bot.send_photo(message.chat.id,photo=open(r'C:\Users\zaggg\Desktop\WiseBot\мудрецы.jpg','rb'))
    bot.send_message(message.chat.id,'Так появился я... <b>Мудробот!</b>')
    bot.send_photo(message.chat.id,photo=open(r'C:\Users\zaggg\Desktop\WiseBot\мудробот.jpg','rb'))
    bot.send_message(message.chat.id, 'И я готов поделиться этой мудростью с вами!')
    daytime= types.InlineKeyboardMarkup()
    but1= types.InlineKeyboardButton('Утром', callback_data= 'daypart|утро')
    but2= types.InlineKeyboardButton('Днём', callback_data= 'daypart|день')
    but3= types.InlineKeyboardButton('Вечером', callback_data= 'daypart|вечер')
    daytime.add(but1,but2,but3)
    bot.reply_to(message,'Когда вы хотите получать мои сообщения?', reply_markup= daytime)



@bot.callback_query_handler(func=lambda call: call.data.split('|')[0]=='daypart')
def hour_changer(call):
    if call.data == 'daypart|утро':
        keyboard_morning= types.InlineKeyboardMarkup()
        m_bt1= types.InlineKeyboardButton('06:00', callback_data ='current_time|06:00')
        m_bt2= types.InlineKeyboardButton('07:00', callback_data ='current_time|07:00')
        m_bt3= types.InlineKeyboardButton('08:00', callback_data ='current_time|08:00')
        m_bt4= types.InlineKeyboardButton('09:00', callback_data ='current_time|09:00')
        m_bt5= types.InlineKeyboardButton('10:00', callback_data ='current_time|10:00')
        m_bt6= types.InlineKeyboardButton('11:00', callback_data ='current_time|11:00')
        m_bt7= types.InlineKeyboardButton('12:00', callback_data ='current_time|12:00')
        keyboard_morning.add(m_bt1, m_bt2, m_bt3, m_bt4, m_bt5, m_bt6, m_bt7)
        bot.answer_callback_query(call.id, 'Выберите удобное время')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Выберите удобное время', reply_markup= keyboard_morning)
           
    elif call.data == 'daypart|день':
        keyboard_day= types.InlineKeyboardMarkup()
        d_bt1= types.InlineKeyboardButton('13:00', callback_data = 'current_time|13:00')
        d_bt2= types.InlineKeyboardButton('14:00', callback_data = 'current_time|14:00')
        d_bt3= types.InlineKeyboardButton('15:00', callback_data = 'current_time|15:00')
        d_bt4= types.InlineKeyboardButton('16:00', callback_data = 'current_time|16:00')
        d_bt5= types.InlineKeyboardButton('17:00', callback_data = 'current_time|17:00')
        d_bt6= types.InlineKeyboardButton('18:00', callback_data = 'current_time|18:00')
        keyboard_day.add(d_bt1, d_bt2, d_bt3, d_bt4, d_bt5, d_bt6)
        bot.answer_callback_query(call.id, 'Выберите удобное время')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Выберите удобное время', reply_markup= keyboard_day)

    elif call.data == 'daypart|вечер':
        keyboard_evening= types.InlineKeyboardMarkup()
        e_bt1= types.InlineKeyboardButton('19:00', callback_data= 'current_time|19:00')
        e_bt2= types.InlineKeyboardButton('20:00', callback_data= 'current_time|20:00')
        e_bt3= types.InlineKeyboardButton('21:00', callback_data= 'current_time|21:00')
        e_bt4= types.InlineKeyboardButton('22:00', callback_data= 'current_time|22:00')
        e_bt5= types.InlineKeyboardButton('23:00', callback_data= 'current_time|23:00')
        keyboard_evening.add(e_bt1, e_bt2, e_bt3, e_bt4, e_bt5)
        bot.answer_callback_query(call.id, 'Выберите удобное время')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Выберите удобное время', reply_markup= keyboard_evening)


@bot.message_handler(types='')
def random_quote():
    bot.send_message(quotes[randint(0,388)])

    
@bot.callback_query_handler(func=lambda call: call.data.split('|')[0]== 'current_time')
def send_qoute(call):
    if call.data == 'current_time|06:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'А вы ранняя пташка! Хорошо, буду присылать сообщения в 06:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        schedule.every().day.at("06:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|07:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 07:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|08:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 08:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("16:05").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|09:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 09:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("09:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|10:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 10:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("10:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|11:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 11:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("11:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|12:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 12:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("12:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|13:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 13:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("13:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|14:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 14:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("14:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|15:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 15:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("15:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|16:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 16:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("16:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|17:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 17:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("17:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|18:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 18:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("18:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|19:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 19:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("19:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|20:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 20:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("20:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|21:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 21:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
       
        schedule.every().day.at("21:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|22:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 22:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        
        schedule.every().day.at("22:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    elif call.data == 'current_time|23:00':
        bot.answer_callback_query(call.id, 'Выбрано')
        bot.edit_message_text(chat_id= call.message.chat.id, message_id= call.message.message_id, text= 'Договорились! Буду присылать сообщения в 23:00.\n Вы также можете получить одну из цитат в любое время, введя команду "/цитата"')
        schedule.every().day.at("23:00").do(random_quote)
        while True:
            schedule.run_pending()
            time.sleep(10)
    
@bot.message_handler(commands=['цитата'])
def quote_send(message):
    bot.send_message(message.chat.id,quotes[randint(0,388)])
                
    













bot.polling()