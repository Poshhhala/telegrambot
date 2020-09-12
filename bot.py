import telebot
from telebot import types
import os
import random

bot = telebot.TeleBot("1000999911:AAGrYMbOD8iwMkAktyxQE3Fcl_C1w8Mko0o")


print(bot.get_me())


@bot.message_handler(commands= ["start"])
def handle_text(massege):
    try:
        dir = "C:/photoo/photo_2020-08-18_15-18-50.jpg"
        img = open(dir,'rb')
        caption = "*💸 Ну привет: {0};\n⌨️ Пользуйся клавиатурой и всё будет как надо.*".format(massege.from_user.first_name)
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        button1 = types.KeyboardButton(text= "♻️ Save")
        button2 = types.KeyboardButton(text="💁 Music")
        button3 = types.KeyboardButton(text="♨️ Video")
        button4 = types.KeyboardButton(text= "☠️ Keyboard 2")
        keyboard.add(button1)
        keyboard.add(button2, button3)
        keyboard.add(button4)
        bot.send_photo(massege.from_user.id, img, caption, reply_markup=keyboard, parse_mode='Markdown')
        bot.send_message(-479437333, "*Name: '{0}', \nUsername: '@{1}', \nId: '{2}', \nUse: '{3}*'".format(massege.from_user.first_name, massege.from_user.username, str(massege.from_user.id), massege.text), parse_mode='Markdown')
        print("Name: '{0}', Username: '@{1}', Id: '{2}', Use: '{3}'".format(massege.from_user.first_name, massege.from_user.username, str(massege.from_user.id), massege.text))

    except Exception as e:
        bot.reply_to(massege,"oooops, retry again...")


"""
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
       for id in range((message.message_id-50),message.message_id):
            bot.delete_message(message.chat.id, id)

             bot.send_message(message.chat.id, 'ms')
"""


@bot.message_handler(content_types= ['text'])
def handle_text(massege):
    try:
        if massege.text == "♻️ Save":
            dir = "C:/photoo"
            all_files_in_directory = os.listdir(dir)
            file = random.choice(all_files_in_directory)
            img = open(dir + '/' + file, 'rb')
            caption = random.choice(["*Бот умеет сохранять фото которые ему отправляют :3 \n- Отправь ему нюдсы*",
                                     "*💸💸💸💸💸💸💸💸💸💸💸💸*",
                                     "*👹👹👹👹👹👹👹👹👹👹👹👹*",
                                     "*🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️🧚🏿‍♀️*",
                                     "*🥺🥺🥺🥺🥺🥺🥺🥺🥺🥺🥺🥺*",
                                     "*❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️*",
                                     "*💎💎💎💎💎💎💎💎💎💎💎💎*",
                                     "*🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡*",
                                     "*😻😻😻😻😻😻😻😻😻😻😻😻*",
                                     "*👀👀👀👀👀👀👀👀👀👀👀👀*",
                                     "*🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋🦋*",
                                     "*🐋🐋🐋🐋🐋🐋🐋🐋🐋🐋🐋🐋*",
                                     "*🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉🦉*",
                                     "*🕯🕯🕯🕯🕯🕯🕯🕯🕯🕯🕯🕯*",
                                     "*💰💰💰💰💰💰💰💰💰💰💰💰*",
                                     "*💣💣💣💣💣💣💣💣💣💣💣💣*",
                                     "*🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓🪓*",
                                     "*🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱🔱*",
                                     "*⚜️⚜️⚜️⚜️⚜️⚜️⚜️⚜️⚜️⚜️⚜️⚜️*"])
            bot.send_photo(massege.chat.id, img, caption, parse_mode='Markdown')

        if massege.text == "💁 Music":
            keybord = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton("SoundCloud", url="https://soundcloud.com/user-823167710/sets/by-musixx")
            keybord.add(button)
            bot.reply_to(massege, "*Солнышко моё, вставай!*", reply_markup = keybord, parse_mode='Markdown')
        if massege.text == "♨️ Video":
            dir = "C:/viiideo"
            all_files_in_directory = os.listdir(dir)
            file = random.choice(all_files_in_directory)
            img = open(dir + '/' + file, 'rb')
            caption = "Бот умеет сохранять фото которые ему отправляют :3 \nОтправь ему нюдсы"
            bot.send_video(massege.chat.id, img, caption)
        if massege.text == "☠️ Keyboard 2":
            keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
            button1 = types.KeyboardButton(text="💳 Advertising")
            button2 = types.KeyboardButton(text="⚙️ Options")
            button3 = types.KeyboardButton(text="☠️ Keyboard 1")
            button4 = types.KeyboardButton(text="🗃 Chats")
            keyboard2.add(button1)
            keyboard2.add(button4,button2)
            keyboard2.add(button3)
            bot.reply_to(massege, "*Открыл вторую клавиатуру*" , reply_markup=keyboard2, parse_mode='Markdown')
        if massege.text == "☠️ Keyboard 1":
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            button1 = types.KeyboardButton(text="♻️ Save")
            button2 = types.KeyboardButton(text="💁 Music")
            button3 = types.KeyboardButton(text="♨️ Video")
            button4 = types.KeyboardButton(text="☠️ Keyboard 2")
            keyboard.add(button1)
            keyboard.add(button2, button3)
            keyboard.add(button4)
            bot.reply_to(massege, "*Открыл первую клавиатуру*", reply_markup=keyboard, parse_mode='Markdown')
        if massege.text == "💳 Advertising":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("❤️",callback_data='2' )
            button2 = types.InlineKeyboardButton("🧡",callback_data='2' )
            button4 = types.InlineKeyboardButton("💚", callback_data='2')
            keyboard.add(button1, button2, button4)
            bot.reply_to(massege, "*Тут может быть ваша реклама!*", reply_markup=keyboard , parse_mode='Markdown')

        if massege.text == "⚙️ Options":
            keyboard = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton("🤵🏻 Добавить бота в свой чат", url='tg://resolve?domain=allperfection_bot&startgroup=true')
            button2 = types.InlineKeyboardButton("💡 Новости",callback_data='2' )
            button3 = types.InlineKeyboardButton("❓ Помощь", callback_data='3',)
            button4 = types.InlineKeyboardButton("😈 Администрация", callback_data='4')
            button5 = types.InlineKeyboardButton("📑 Что умеет бот?", callback_data= '5')
            keyboard.add(button5)
            keyboard.add(button2, button3)
            keyboard.add(button4)
            bot.reply_to(massege, "*Бот с радостью поможет тебе!\nFirstName: {0} \nUserName: @{1} \nId: {2}*".format(massege.from_user.first_name, massege.from_user.username , str(massege.from_user.id)), reply_markup=keyboard, parse_mode='Markdown')
        if massege.text == "🗃 Chats":
            keyboard = types.InlineKeyboardMarkup()

            button1 = types.InlineKeyboardButton("🤵🏻 Добавить бота в свой чат", url='tg://resolve?domain=allperfection_bot&startgroup=true')
            button2 = types.InlineKeyboardButton("📩 Поделиться ботом", switch_inline_query=" - Смотри че нашёл!")
            button5 = types.InlineKeyboardButton("📑 Что умеет бот?", callback_data= '5')
            button3 = types.InlineKeyboardButton("💬 Main", url='https://t.me/i061unmain')
            keyboard.add(button3)
            keyboard.add(button2)
            keyboard.add(button1)
            bot.reply_to(massege, "*Чаты для твоего пользования!*".format(massege.from_user.first_name, massege.from_user.username , str(massege.from_user.id)), reply_markup=keyboard, parse_mode='Markdown')

    except Exception as e:
        bot.reply_to(massege,"oooops, retry again...")


@bot.callback_query_handler(func=lambda call: True)
def iqchery(call):
    try:
        if call.message:
            if call.data == '5':
               bot.send_message(call.message.chat.id, "*🤖 Умения бота:\n\n🖼 Работа с фото (Отправка и Сохранение);\n🎞 Отправлять видео\n      -В будущем и сохранение;\n🎧 Отправка аккаунтов с музыкой (на данный момент их {1});\n🗃 Тут есть чаты, в которых вы можете общаться в с людьми (так же можете предлагать свои чаты, на данный момент их '0')\n💸 Бот может показывать вашу рекламу в разделе '💳 Advertising'*\n\n_⌚ Бот создан 15.09.2019\n И все ещё в доработке..._", parse_mode='Markdown')

            if call.data == '2':
                bot.answer_callback_query(call.id, text="В разработке...")
            if call.data == '3':
                bot.answer_callback_query(call.id, text="В разработке...")
            if call.data == '4':
                keyboard = types.InlineKeyboardMarkup()
                button1 = types.InlineKeyboardButton("Instagram.com", url='https://www.instagram.com/_.chupa/?hl=ru')
                button2 = types.InlineKeyboardButton("Telegram.org", url='https://t.me/lilchupaindesu')
                keyboard.add(button1,button2)
                bot.send_message(call.message.chat.id, "Администрация ⛑\n- По вопросам размещение рекламы\n- При нахождении багов (за нахождение бага вы получите бонус, но т.к. проект новый Х*Й вы что получите)))\n- Или же если у вас есть какие-то дополнительные идеи по поводу развития проекта\n💌 Пишите: @lilchupaindesu👇",reply_markup=keyboard)

    except Exception as e:
        bot.reply_to(call.message.chat.id ,"oooops, retry again...")








@bot.message_handler(content_types=["photo"])
def photo(message):
    try:
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            button1 = types.KeyboardButton(text="♻️ save")
            button2 = types.KeyboardButton(text="💁 music")
            button3 = types.KeyboardButton(text="♨️ video")
            button4 = types.KeyboardButton(text="☠️ keyboard 2")
            keyboard.add(button1)
            keyboard.add(button2, button3)
            keyboard.add(button4)
            idphoto = message.photo[0].file_id
            caption = "*By '{0}', \nUsername: '@{1}'*".format(message.from_user.first_name, message.from_user.username)
            bot.reply_to(message, random.choice(["*✅ - Миссия выполнена, продолжай!*","*✅ - Хорошая работа, Олег!*", "*✅ - Я кончаю, продолжай!*","*✅ - Хочу ещё!*"]), reply_markup=keyboard, parse_mode='Markdown')
            bot.send_photo(-387904708, idphoto, caption)


    except Exception as e:
        bot.reply_to(message.chat.id,"oooops, retry again...")








"""
bot.answer_callback_query(call.id, text="Дата выбрана", show_alert= True)
bot.answer_callback_query(call.id, text="Дата выбрана", show_alert= False)
bot.send_message(call.message.chat.id, "Администрация ⛑\n- По вопросам размещение рекламы\n- При нахождении багов (за нахождение бага вы получите бонус, но т.к. проект новый Х*Й вы что получите)))\n- Или же если у вас есть какие-то дополнительные идеи по поводу развития проекта\n💌 Пишите: @lilchupaindesu👇", parse_mode='Markdown')
"""







bot.polling(none_stop=True)