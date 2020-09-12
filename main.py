import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot("1338719649:AAHoWcyTsr8nq6pg-F7-rxoKrHI3bk_DeLI")


print(bot.get_me())


@bot.message_handler(commands= ["start"])
def handle_text(massege):
    try:

        img = 'https://vk.com/mu_trades?z=photo-99600394_457286143%2Falbum-99600394_00%2Frev'
        caption = "*💸 Ну привет: {0};\nЯ жду твоего годного контента!\nОтправь мне фото и увидешь его в группе @i061unmain!*".format(massege.from_user.first_name)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        button1 = types.KeyboardButton(text= "💳 Advertising")
        button2 = types.KeyboardButton(text="🗃 Chats")
        button3 = types.KeyboardButton(text="⚙️ Options")
        button4 = types.KeyboardButton(text="🗂 Сhannel")

        keyboard.add(button1)
        keyboard.add(button2,button4 ,button3)

        bot.send_photo(massege.from_user.id, img, caption, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(-479437333, "*Name: '{0}', \nUsername: '@{1}', \nId: '{2}', \nUse: '{3}'*".format(massege.from_user.first_name, massege.from_user.username, str(massege.from_user.id), massege.text), parse_mode='Markdown')
        print("Name: '{0}', Username: '@{1}', Id: '{2}', Use: '{3}'".format(massege.from_user.first_name, massege.from_user.username, str(massege.from_user.id), massege.text))

    except Exception as e:
        bot.reply_to(massege,"oooops, retry again...")






@bot.message_handler(content_types= ['text'])
def handle_text(massege):
    try:
        if massege.text == "💳 Advertising":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("❤️",callback_data='2' )
            button2 = types.InlineKeyboardButton("🧡",callback_data='2' )
            button4 = types.InlineKeyboardButton("💚", callback_data='2')
            keyboard.add(button1, button2, button4)
            bot.reply_to(massege, "*Тут может быть ваша реклама!*", reply_markup=keyboard , parse_mode='Markdown')
        if massege.text == "◀️ Exit":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            button1 = types.KeyboardButton(text="💳 Advertising")
            button2 = types.KeyboardButton(text="🗃 Chats")
            button3 = types.KeyboardButton(text="⚙️ Options")
            button4 = types.KeyboardButton(text="🗂 Сhannel")

            keyboard.add(button1)
            keyboard.add(button2, button4, button3)
            bot.reply_to(massege, "*Вернул в основное меню !*", reply_markup=keyboard, parse_mode='Markdown')

        if massege.text == "⚙️ Options":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            #button1 = types.InlineKeyboardButton("🤵🏻 Добавить бота в свой чат", url='tg://resolve?domain=allperfection_bot&startgroup=true')
            #button2 = types.InlineKeyboardButton("💡 Новости",callback_data='2' )
            #button3 = types.InlineKeyboardButton("❓ Помощь", callback_data='3',)
            button4 = types.KeyboardButton("⚜️ Administration")
            button5 = types.KeyboardButton("📑 What a bot can do?")
            button10 = types.KeyboardButton("◀️ Exit")
            keyboard.add(button5)
            keyboard.add(button4, button10)
            bot.reply_to(massege, "*Бот с радостью поможет тебе!\nFirstName: {0} \nUserName: @{1} \nId: {2}*".format(massege.from_user.first_name, massege.from_user.username , str(massege.from_user.id)), reply_markup=keyboard, parse_mode='Markdown')
        if massege.text == "🗃 Chats":
            keyboard = types.InlineKeyboardMarkup()

            #button1 = types.InlineKeyboardButton("🤵🏻 Добавить бота в свой чат", url='tg://resolve?domain=allperfection_bot&startgroup=true')
            #button2 = types.InlineKeyboardButton("📩 Поделиться ботом", switch_inline_query=" - Смотри че нашёл!")
            #button5 = types.InlineKeyboardButton("📑 Что умеет бот?", callback_data= '5')
            button3 = types.InlineKeyboardButton("💬 Main", url='https://t.me/i061unmain')
            keyboard.add(button3)
            bot.reply_to(massege, "*Чаты для твоего пользования!*\n_Пока нет в наличии..._",  parse_mode='Markdown')
        if massege.text == "🗂 Сhannel":
            keyboard = types.InlineKeyboardMarkup()
            button3 = types.InlineKeyboardButton("💬 Main", url='https://t.me/i061unmain')
            keyboard.add(button3)
            bot.reply_to(massege, "*Каналы для постинга материалов:*", reply_markup=keyboard, parse_mode='Markdown')

        if massege.text == "⚜️ Administration":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("Instagram.com", url='https://www.instagram.com/_.chupa/?hl=ru')
            button2 = types.InlineKeyboardButton("Telegram.org", url='https://t.me/lilchupaindesu')
            keyboard.add(button1, button2)
            # bot.send_message(call.message.chat.id, ", reply_markup=keyboard, parse_mode='Markdown')
            bot.reply_to(massege, "*Администрация ⛑\n- По вопросам размещение рекламы;\n- Вопросы сотрудничества;\n- Eсли у вас есть какие-то дополнительные идеи по поводу развития проекта;\n💌 Пишите: @lilchupaindesu👇*",
                             parse_mode='Markdown', reply_markup=keyboard)

        if massege.text == "📑 What a bot can do?":
            bot.reply_to(massege, "*🤖 Умения бота:\n\n🖼 Основная функция бота - сохраняет отправленые вами фото - видео, и пересылать в группы;\n🗃 Тут есть чаты, в которых вы можете общаться с людьми (так же можете предлагать свои чаты, на данный момент их '0')\n🗂 Тут можно посмотеть каналы (То куда постятся материалы) в разделе '🗂 Channel'\n💸 Бот может показывать вашу рекламу в разделе '💳 Advertising'*", parse_mode='Markdown')


    except Exception as e:
        bot.reply_to(massege,"oooops, retry again...")










@bot.message_handler(content_types=["photo"])
def photo(message):
    try:
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            button1 = types.KeyboardButton(text="💳 Advertising")
            button2 = types.KeyboardButton(text="🗃 Chats")
            button3 = types.KeyboardButton(text="⚙️ Options")
            button4 = types.KeyboardButton(text="🗂 Сhannel")

            keyboard.add(button1)
            keyboard.add(button2, button4, button3)
            idphoto = message.photo[0].file_id
            caption = "*By: '{0}', \nUsername: '@{1}'*".format(message.from_user.first_name, message.from_user.username)
            bot.reply_to(message, random.choice(["*✅ - Миссия выполнена, продолжай!*",
                                     "*✅ - Хорошая работа, Олег!*",
                                     "*✅ - Я кончаю, продолжай!*",
                                     "*✅ - Хочу ещё!*","*✅ - Я уже тебя люблю!*",
                                     "*✅ - Ты меня обрадовал :3!*",
                                     "*✅ - Иди поцелую!!*",
                                     "*✅ - Жди! Может опубликую в канале!*",
                                     "*✅ - Красиво!*",
                                     "*✅ - Спасибо, Бро!*",
                                     "*✅ - Прекрасно!*",]), reply_markup=keyboard, parse_mode='Markdown')
            bot.send_photo(-387904708, idphoto, caption, parse_mode='Markdown')
    except Exception as e:
        bot.reply_to(message.chat.id,"oooops, retry again...")


@bot.message_handler(content_types=["video"])
def video(message):
    try:
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            button1 = types.KeyboardButton(text="💳 Advertising")
            button2 = types.KeyboardButton(text="🗃 Chats")
            button3 = types.KeyboardButton(text="⚙️ Options")
            button4 = types.KeyboardButton(text="🗂 Сhannel")

            keyboard.add(button1)
            keyboard.add(button2, button4, button3)
            idvideo = message.video.file_id
            caption = "*By: '{0}', \nUsername: '@{1}'*".format(message.from_user.first_name, message.from_user.username)
            bot.reply_to(message, random.choice(["*✅ - Миссия выполнена, продолжай!*",
                                                 "*✅ - Хорошая работа, Олег!*",
                                                 "*✅ - Я кончаю, продолжай!*",
                                                 "*✅ - Хочу ещё!*", "*✅ - Я уже тебя люблю!*",
                                                 "*✅ - Ты меня обрадовал :3!*",
                                                 "*✅ - Иди поцелую!!*",
                                                 "*✅ - Жди! Может опубликую в канале!*",
                                                 "*✅ - Красиво!*",
                                                 "*✅ - Спасибо, Бро!*",
                                                 "*✅ - Прекрасно!*",]), reply_markup=keyboard, parse_mode='Markdown')
            bot.send_video(-387904708, idvideo, caption, parse_mode='Markdown')


    except Exception as e:
        bot.reply_to(message.chat.id,"oooops, retry again...")




"""
@bot.callback_query_handler(func=lambda call: True)
def iqchery(call):
    try:
        if call.message:
            if call.data == '5':
               bot.send_message(call.message.chat.id, "*🤖 Умения бота:\n\n🖼 Бот сохраняет отправленые вами фото и отправляет в группы;\n🗃 Тут есть чаты, в которых вы можете общаться с людьми (так же можете предлагать свои чаты, на данный момент их '0')\n💸 Бот может показывать вашу рекламу в разделе '💳 Advertising'*\n\n_⌚ Бот создан 15.09.2019\n И все ещё в доработке..._", parse_mode='Markdown')

            if call.data == '2':
                bot.answer_callback_query(call.id, text="В разработке...")
            if call.data == '3':
                bot.answer_callback_query(call.id, text="В разработке...")
            if call.data == '4':
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Instagram.com", url='https://www.instagram.com/_.chupa/?hl=ru')
                button2 = types.InlineKeyboardButton("Telegram.org", url='https://t.me/lilchupaindesu')
                keyboard.add(button1,button2)
                #bot.send_message(call.message.chat.id, ", reply_markup=keyboard, parse_mode='Markdown')
                bot.send_message(call.message.chat.id,
                                 "*Администрация ⛑\n- По вопросам размещение рекламы;\n- Вопросы сотрудничества;\n- Eсли у вас есть какие-то дополнительные идеи по поводу развития проекта;\n💌 Пишите: @lilchupaindesu👇*",
                                 parse_mode='Markdown', reply_markup=keyboard)


    except Exception as e:
        bot.reply_to(call.message.chat.id ,"oooops, retry again...")

"""

"""
bot.answer_callback_query(call.id, text="Дата выбрана", show_alert= True)
bot.answer_callback_query(call.id, text="Дата выбрана", show_alert= False)
bot.send_message(call.message.chat.id, "Администрация ⛑\n- По вопросам размещение рекламы\n- При нахождении багов (за нахождение бага вы получите бонус, но т.к. проект новый Х*Й вы что получите)))\n- Или же если у вас есть какие-то дополнительные идеи по поводу развития проекта\n💌 Пишите: @lilchupaindesu👇", parse_mode='Markdown')
"""







bot.polling(none_stop=True)