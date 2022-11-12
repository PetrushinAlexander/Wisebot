from aiogram import Bot, types 
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import token
from random import randint
from config import quotes
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time



bot=Bot(token=token,parse_mode="HTML")
dp=Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_message(message:types.Message):
    await message.reply('<i> Привет, {0.first_name}!\nОднажды все мудрецы мира собрались и решили создать нечто, что по своей мудрости превзойдет всех...</i>'.format(message.from_user))
    time.sleep(1)
    await bot.send_photo(message.from_user.id,photo=open('1.jpg','rb'))
    time.sleep(3)
    await message.reply('Так появился я... <b>Мудробот!</b>')
    time.sleep(1)
    await bot.send_photo(message.from_user.id,photo=open('2.jpg','rb'))
    time.sleep(3)
    await message.reply('И я готов поделиться этой мудростью с тобой!')
    time.sleep(3)
    bt1=InlineKeyboardButton(text='Утром', callback_data= 'daypart|утро')
    bt2=InlineKeyboardButton(text='Днём', callback_data= 'daypart|день')
    bt3=InlineKeyboardButton(text='Вечером', callback_data= 'daypart|вечер')
    daypart=InlineKeyboardMarkup().add(bt1,bt2,bt3)
    await message.reply('Когда ты хочешь получать мои сообщения?', reply_markup= daypart)

async def send_random_quote(message_id):
    x= quotes[randint(0,388)]
    await bot.send_message(message_id, x)

@dp.message_handler(commands=['цитата'])
async def random_quote(message: types.Message):
    x= quotes[randint(0,388)]
    await bot.send_message(message.from_user.id,x)

@dp.callback_query_handler(lambda c:c.data.startswith('daypart'))
async def daypart_changer(callback_query: types.CallbackQuery):
    if callback_query.data == 'daypart|утро':
        m_bt1= InlineKeyboardButton(text='06:00', callback_data ='current_time|06:00')
        m_bt2= InlineKeyboardButton(text='07:00', callback_data ='current_time|07:00')
        m_bt3= InlineKeyboardButton(text='08:00', callback_data ='current_time|08:00')
        m_bt4= InlineKeyboardButton(text='09:00', callback_data ='current_time|09:00')
        m_bt5= InlineKeyboardButton(text='10:00', callback_data ='current_time|10:00')
        m_bt6= InlineKeyboardButton(text='11:00', callback_data ='current_time|11:00')
        keyboard_morning=InlineKeyboardMarkup().add(m_bt1,m_bt2,m_bt3,m_bt4,m_bt5,m_bt6)
        await bot.answer_callback_query(callback_query.id,'Выбери удобное время')
        await bot.send_message(callback_query.from_user.id,'Выбери удобное время', reply_markup= keyboard_morning)
           
    elif callback_query.data == 'daypart|день':
        d_bt1= InlineKeyboardButton(text='12:00', callback_data ='current_time|12:00')
        d_bt2=InlineKeyboardButton(text='13:00', callback_data = 'current_time|13:00')
        d_bt3=InlineKeyboardButton(text='14:00', callback_data = 'current_time|14:00')
        d_bt4=InlineKeyboardButton(text='15:00', callback_data = 'current_time|15:00')
        d_bt5=InlineKeyboardButton(text='16:00', callback_data = 'current_time|16:00')
        d_bt6=InlineKeyboardButton(text='17:00', callback_data = 'current_time|17:00')
        keyboard_day= InlineKeyboardMarkup().add(d_bt1,d_bt2,d_bt3,d_bt4,d_bt5,d_bt6)
        await bot.answer_callback_query(callback_query.id,'Выбери удобное время')
        await bot.send_message(callback_query.from_user.id,'Выбери удобное время', reply_markup= keyboard_day)

    elif callback_query.data == 'daypart|вечер':
        e_bt1=InlineKeyboardButton('18:00', callback_data= 'current_time|18:00')
        e_bt2=InlineKeyboardButton('19:00', callback_data= 'current_time|19:00')
        e_bt3=InlineKeyboardButton('20:00', callback_data= 'current_time|20:00')
        e_bt4=InlineKeyboardButton('21:00', callback_data= 'current_time|21:00')
        e_bt5=InlineKeyboardButton('22:00', callback_data= 'current_time|22:00')
        e_bt6=InlineKeyboardButton('23:00', callback_data= 'current_time|23:00')
        keyboard_evening=InlineKeyboardMarkup().add(e_bt1,e_bt2,e_bt3,e_bt4,e_bt5,e_bt6)
        await bot.answer_callback_query(callback_query.id,'Выбери удобное время')
        await bot.send_message(callback_query.from_user.id,'Выбери удобное время', reply_markup= keyboard_evening)


@dp.callback_query_handler(lambda x:x.data.startswith('current_time'))
async def hour_changer(callback_query: types.CallbackQuery):
    if callback_query.data == 'current_time|06:00': 
        await bot.send_message(callback_query.from_user.id,'А ты ранняя пташка! \nХорошо, буду присылать сообщения в 06:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler(timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=6,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
        
    elif callback_query.data == 'current_time|07:00':
        await bot.send_message(callback_query.from_user.id,'А ты ранняя пташка! \nХорошо, буду присылать сообщения в 07:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=7,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()

    elif callback_query.data == 'current_time|08:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 08:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=8,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|09:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 09:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=9,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|10:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 10:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=10,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|11:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 11:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=11,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|12:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 12:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=12,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|13:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 13:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=13,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|14:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 14:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=14,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|15:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 15:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=15,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|16:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 16:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=16,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|17:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 17:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=17,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|18:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 18:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=18,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|19:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 19:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=19,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|20:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 20:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=20,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|21:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 21:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=21,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|22:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 22:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано')  
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=22,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    elif callback_query.data == 'current_time|23:00':
        await bot.send_message(callback_query.from_user.id,'Хорошо, буду присылать сообщения в 23:00.\n Ты также можешь получить одну из цитат в любое время, введя команду "/цитата"')
        await bot.answer_callback_query(callback_query.id,text='Выбрано') 
        scheduler= AsyncIOScheduler( timezone="Europe/Moscow")
        scheduler.add_job(send_random_quote,'cron',day_of_week='mon-sun', hour=23,kwargs={'message_id':  callback_query.from_user.id})
        scheduler.start()
    
                




if __name__ == '__main__':
    executor.start_polling(dp)