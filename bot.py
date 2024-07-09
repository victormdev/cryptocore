import telebot

from data import get_all_topic,get_topic,get_question,get_text


bot = telebot.TeleBot("6715337967:AAGmvEO5yX74gZntjplTGPgImfx5DbT_suk")


@bot.message_handler(commands=['start', 'course'])
def send_welcome(message):
    all_item = get_all_topic()
    markup  = telebot.types.InlineKeyboardMarkup()
    for item in all_item:
        markup.add(telebot.types.InlineKeyboardButton(text=f'{item.name}',callback_data=f"topic{item.id}"),)
    get_info_text = get_text()
    text = get_info_text.start_text
    bot.send_message(message.chat.id, text,reply_markup=markup)




@bot.callback_query_handler(func=lambda call: True)
def test_callback(call):
    if call.data.startswith("topic"):
        topic = call.data
        topic = topic.replace("topic", "")
        topic_get = get_topic(topic)
        all_question = topic_get.questions.all()
        markup  = telebot.types.InlineKeyboardMarkup()
        for item in all_question:
            markup.add(telebot.types.InlineKeyboardButton(text=f'{item.question}',callback_data=f"question{item.id}"),)


        get_info_text = get_text()
        text = get_info_text.question_text
        bot.send_message(call.from_user.id,text,reply_markup=markup)



    elif call.data.startswith("question"):
        question = call.data
        question = question.replace("question", "")
        question_get = get_question(question)
        text = question_get.ans
        markup  = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text=f'< Back',callback_data=f"delete"),)
        bot.send_message(call.from_user.id,text,reply_markup=markup)
    elif call.data == "delete":
        #print(call.message.chat.id)
        #print(call.message.id)
        bot.delete_message(call.message.chat.id,call.message.id)
    


bot.infinity_polling()

















