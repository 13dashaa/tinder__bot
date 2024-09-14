from telegram.ext import ApplicationBuilder, MessageHandler, filters, CallbackQueryHandler, CommandHandler

from gpt import *
from util import *

# тут будем писать наш код :)

async def start(update, context):
    dialog.mod= 'main'
    text = load_message('main')
    await send_photo(update, context, "main")
    await send_text(update, context, text)
    await show_main_menu(update, context, {
        'start': 'главное меню бота',
        'profile': 'генерация Tinder-профля 😎',
        'opener': 'сообщение для знакомства 🥰',
        'message': 'переписка от вашего имени 😈',
        'date': ' переписка со звездами 🔥',
        'gpt': 'задать вопрос чату GPT 🧠'
    })

async def gpt(update, context):
    dialog.node ='gpt'
    text = load_message('gpt')
    await send_photo(update, context, "gpt")
    await send_text(update, context, text)

async def gpt_dialog(update, context):
    text = update.message.text
    promt  =  load_prompt('gpt')
    answer = await chatgpt.send_question(promt, text)
    await send_text(update, context, answer)


async def date(update, context):
    dialog.node='date'
    text = load_message('date')
    await send_photo(update, context, "date")
    await send_text_buttons(update, context, text, {
        'date_grande': 'Ариана Гранде',
        'date_robbie': 'Марго Робби',
        'date_zendaya': 'Зендея',
        'date_gosling': 'Райан Гослинг',
        'date_hardy': 'Том Харди'

    })

async def date_dialog(update, context):
    text = update.message.text
    my_message = await send_text(update, context, 'Печатает...')
    answer = await chatgpt.add_message(text)
    await my_message.edit_text(answer)



async def date_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

    await send_photo(update, context, query)
    await send_text(update, context, 'Отличный выбор. Пригласите девушку (парня) на свидание за 5 сообщений.')

    promt = load_prompt(query)
    chatgpt.set_prompt(promt)


async def message(update, context):
    dialog.node ='message'
    text = load_message('message')
    await send_photo(update, context, "message")
    await send_text_buttons(update, context, text,{
         'message_next': 'Следующее сообщение',
        'message_date': 'Пригласить на свидание'})
    dialog.list.clear()

async def message_button(update, context):
    query = update.callback_query.data
    await update.callback_query.answer()

    promt = load_prompt(query)
    user_chat_history = '\n\n'.join(dialog.list)
    my_message = await send_text(update, context, 'Думаю...')
    answer = await chatgpt.send_question(promt, user_chat_history)
    await my_message.edit_text(answer)

async def message_dialog(update, context):
    text = update.message.text
    dialog.list.append(text)

async def profile(update, context):
    dialog.node='profile'
    text = load_message('profile')
    await send_photo(update, context, 'profile')
    await send_text(update, context, text)

    dialog.user.clear()
    dialog.counter=0
    await send_text(update, context, 'Сколько Вам лет?')


async def profile_dialog(update, context):
    text = update.message.text
    dialog.counter += 1
    if dialog.counter ==1 :
        dialog.user['age']=text
        await send_text(update, context, 'Кем вы работаете?')
    elif dialog.counter==2:
        dialog.user["occupation"] = text
        await send_text(update, context, "У вас есть хобби?")
    elif dialog.counter == 3:
        dialog.user["hobby"] = text
        await send_text(update, context, "Что вам НЕ нравится в людях?")
    elif dialog.counter == 4:
        dialog.user["annoys"] = text
        await send_text(update, context, "Цель знакомства?")
    elif dialog.counter == 5:
        dialog.user["goals"] = text
        promt=load_prompt('profile')
        user_info = dialog_user_info_to_str(dialog.user)

        my_message = await send_text(update, context,'Создаю профиль🧠...')
        answer = await chatgpt.send_question(promt, user_info)
        await my_message.edit_text(answer)

async def opener(update, context):
    dialog.node = "opener"
    text = load_message('opener')
    await send_photo(update, context, 'opener')
    await send_text(update, context, text)

    dialog.user.clear()
    dialog.counter=0
    await send_text(update, context, 'Имя девушки?')


async def opener_dialog(update, context):
    text = update.message.text
    dialog.counter += 1
    if dialog.counter == 1:
        dialog.user['name'] = text
        await send_text(update, context, 'Сколько ей лет?')
    elif dialog.counter == 2:
        dialog.user["age"] = text
        await send_text(update, context, "Оцените ее внешность: 1-10 баллов?")
    elif dialog.counter == 3:
        dialog.user["handsome"] = text
        await send_text(update, context, "Кем она работает?")
    elif dialog.counter == 4:
        dialog.user["job"] = text
        await send_text(update, context, "Цель знакомства?")
    elif dialog.counter == 5:
        dialog.user["goals"] = text
        promt = load_prompt('opener')
        user_info = dialog_user_info_to_str(dialog.user)

        my_message = await send_text(update, context,'Создаю профиль🧠...')
        answer = await chatgpt.send_question(promt, user_info)
        await my_message.edit_text(answer)
async def hello(update, context):
    if dialog.node =="gpt":
        await gpt_dialog(update, context)
    if dialog.node == "date":
        await date_dialog(update, context)
    if dialog.node == "message":
        await message_dialog(update, context)
    if dialog.node == "profile":
        await profile_dialog(update, context)
    if dialog.node == "opener":
        await opener_dialog(update, context)
    else:
        await send_text(update, context, '*Привет*, ' + update.message.chat.first_name)
        await send_text(update, context, '_Как дела?_')
        await send_text(update, context, 'Вы написали ' + update.message.text)
        await  send_photo(update, context, "avatar_main")
        await send_text_buttons(update, context, 'Запустить процесс',
                                {'start': 'Запустить', 'stop':'Остановить'})
async def hello_buttons(update, context):
    query = update.callback_query.data
    if query == 'start':
        await send_text(update, context, 'Процесс запущен')
    else:
        await send_text(update, context, 'Процесс остановлен')


dialog = Dialog()
dialog.node = None
dialog.list =[]
dialog.user ={}
dialog.counter=0

chatgpt = ChatGptService(token='gpt:61rNHlA6YvvAAhkXHkjMJFkblB3T1ra23XYN7pLIKmOsUDqe')

app = ApplicationBuilder().token("7077700280:AAEDTaFt-vhCzlq0WGKIulzMb-Mx0FaFQoY").build()
app.add_handler(CommandHandler('start', start))
app.add_handler(CommandHandler('gpt', gpt))
app.add_handler(CommandHandler('date', date))
app.add_handler(CommandHandler('message', message))
app.add_handler(CommandHandler('profile', profile))
app.add_handler(CommandHandler('opener', opener))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, hello))

app.add_handler(CallbackQueryHandler(date_button, pattern="^date_.*"))
app.add_handler(CallbackQueryHandler(message_button, pattern="^message_.*"))
app.add_handler(CallbackQueryHandler(hello_buttons))
app.run_polling()
