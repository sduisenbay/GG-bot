
# coding: utf-8

# In[11]:


'''
import telebot
from telebot import types
import pandas as pd
from flask import Flask, request

TOKEN = '554106274:AAGu1mSfZVpCg64F2zNnh1iee6g_syzYYBU'

#app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

df = pd.read_excel('./static/database.xlsx', index_col=0)
list_of_values = df.loc[df['node_id'] == 1, ['id','body']].to_csv(sep="\t", header=False)

@app.route("/")
def index():
    bot.polling(none_stop=True, interval=0, timeout=20)


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот проекта Global Grants! Если нужна подсказка"+
    " то набери /help (не забудь \"/\" в начале). Для доступа к информации набери /info.")

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Для того чтобы получить информацию о проекте наберите "+
    "/info. Дальше ориентируйтесь нажимая на соответствующие кнопки, которые проваливаются на несколько уровней.")

@bot.message_handler(commands=['info'])
@bot.message_handler(regexp = '^Узнать еще о кое чем$')
def send_ask(message):
    bot.send_message(message.chat.id, "О чем бы вы хотели узнать: \n" + list_of_values,
    reply_markup = buttons(df.loc[df.node_id == 1].index.astype('str')))

# Handling questions
@bot.message_handler(regexp = '\d')
def send_answer(message):
    answer_id = int(message.text)
    ref_node_id = df.get_value(answer_id,'ref_node_id')

    flag = False
    if len(list(df.loc[df['node_id'] == ref_node_id, 'ref_node_id'])) == 1:
        flag = True

    result = df.loc[df['node_id'] == ref_node_id, ['body']].reset_index().to_csv(sep="\t", header=False, index=False)
    markup = buttons(df.loc[df['node_id'] == ref_node_id].index, end=flag)
    #markup = buttons(df.loc[df['node_id'] == ref_node_id].index.astype('str'), end=flag)

    bot.reply_to(message, result, reply_markup=markup)

# Echo questions
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Для подсказки наберите /help. Для информации нажмите /info.")

#Buttons markup
def buttons(list, end=False):
    markup = types.ReplyKeyboardMarkup(selective=False)
    if end == True:
        markup.row(types.KeyboardButton('Узнать еще о кое чем'))
    else:
        for item in list:
            markup.row(types.KeyboardButton(item))
    return markup

bot.polling(none_stop=True, interval=0, timeout=20)

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=80)'''


# In[9]:





# In[10]:





# In[ ]:


import telebot
from telebot import types
import os
from flask import Flask, request

TOKEN = '554106274:AAGu1mSfZVpCg64F2zNnh1iee6g_syzYYBU'

app = Flask(__name__)
bot = telebot.TeleBot(TOKEN)

port = os.getenv('PORT',443)
@app.route("/")
def index():
    while True:

        try:

            bot.polling(none_stop=True, interval=0, timeout=20)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # TypeError for moviepy errors
        # maybe there are others, therefore Exception
        except Exception as e:
            logger.error(e)
            time.sleep(5)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Привет! Я бот проекта [Global Grants](www.global-grants.com)! Если нужна подсказка"+
    " то набери /help (не забудь \"/\" в начале). Для доступа к информации набери /info.", parse_mode = 'Markdown')

@bot.message_handler(commands=['help'])
def send_welcome(message):
	bot.reply_to(message, "Для того чтобы получить информацию о проекте наберите "+
    "/info. Дальше ориентируйтесь нажимая на соответствующие кнопки, которые проваливаются на несколько уровней.")

@bot.message_handler(commands=['info'])
@bot.message_handler(regexp = 'Назад в главное меню$')
def send_ask(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtna = types.KeyboardButton(u'\U00002705'+'  Информация об услугах')
    itembtnb = types.KeyboardButton(u'\U0001F3AF'+'  Проведенные мероприятия')
    markup.row(itembtna)
    markup.row(itembtnb)
    bot.send_message(message.chat.id, "О чем бы вы хотели узнать?", reply_markup = markup, parse_mode='Markdown')

@bot.message_handler(regexp = 'Проведенные мероприятия$')
def send_answer(message):
    photo1 = open('./static/speaking_hardcore_small.jpg','rb')
    photo2 = open('./static/webinar_small.jpg','rb')
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnh = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnh)
    bot.send_photo(message.chat.id,photo1)
    bot.send_photo(message.chat.id,photo2, reply_markup=markup, parse_mode = 'Markdown')


# Handling questions
@bot.message_handler(regexp = 'Информация об услугах$')
@bot.message_handler(regexp = 'Назад к услугам$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F91D'+'  Полная поддержка')
    itembtnc = types.KeyboardButton(u'\U0001F4D1'+'  Мотивационное письмо')
    itembtnd = types.KeyboardButton(u'\U0001F4DC'+'  Рекомендат. письмо')
    itembtne = types.KeyboardButton(u'\U0001F4DD'+'  Составление резюме (CV)')
    itembtnf = types.KeyboardButton(u'\U0001F5E3' +'  Консультация')
    itembtng = types.KeyboardButton(u'\U0001F4DA' +'  Подготовка к IELTS')
    itembtnh = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtnd,itembtne)
    markup.row(itembtnf,itembtng)
    markup.row(itembtnh)

    bot.reply_to(message, 'Какая именно услуга Вас интересует?', reply_markup=markup, parse_mode = 'Markdown')

    # Handling questions
@bot.message_handler(regexp = 'Полная поддержка$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F58B'+'  Описание полной поддержки при поступлении')
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+ '  Стоимость полной поддержки при поступлении')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Что именно Вас интересует по полной поддержке?', reply_markup=markup, parse_mode = 'Markdown')

    # Handling questions
@bot.message_handler(regexp = 'Мотивационное письмо$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F58B'+'  Описание услуги по написанию мотивационного письма')
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги по написанию мотивационного письма')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Что именно Вас интересует по услуге написания мотивационного письма?', reply_markup=markup, parse_mode = 'Markdown')

    # Handling questions
@bot.message_handler(regexp = 'Рекомендат. письмо$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F58B'+'  Описание услуги по написанию рекомендательного письма')
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги по написанию рекомендательного письма')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Что именно Вас интересует по услуге написания рекомендательного письма?', reply_markup=markup, parse_mode = 'Markdown')

    # Handling questions
@bot.message_handler(regexp = '(Составление резюме)')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F58B'+'  Описание услуги составления резюме (CV)')
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги составления резюме (CV)')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Что именно Вас интересует по услуге составления резюме (CV)?', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'Консультация$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F58B'+'  Описание консультации')
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость консультации')
    itembtne = types.KeyboardButton(u'\U0001F4E5'+'  Скачать анкету для консультации')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtne)
    markup.row(itembtnd)
    bot.reply_to(message, 'Что именно Вас интересует по услуге консультации?', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'анкету для консультации$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnd)
    doc = open('./static/anketa.doc', 'rb')
    bot.send_document(message.chat.id,doc, caption = 'Анкета в формате .doc',reply_markup=markup, parse_mode = 'Markdown')


@bot.message_handler(regexp = 'Подготовка к IELTS$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
    itembtnb = types.KeyboardButton(u'\U0001F58B'+'  Описание услуги подготовки к IELTS')
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги подготовки к IELTS')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnb,itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Что именно Вас интересует по услуге подготовки к IELTS?', reply_markup=markup, parse_mode = 'Markdown')
    # Echo questions

@bot.message_handler(regexp = 'Описание полной поддержки при поступлении$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость полной поддержки при поступлении')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Полная поддержка подразумевает комплекс услуг, включающий в себя подбор программы'+
                 ', университета, и специальности, составление рекомендательных и мотивационных писем, составление '+
                 'резюме. Также в этот комплект входят 20 занятий IELTS, заполнение анкеты для поступления и подготовка '+
                 'к интервью (при необходимости).', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'Стоимость полной поддержки при поступлении$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnd)
    bot.reply_to(message, '1 стипендия = *$600*\n2 cтипендии = *$800*\n3 стипендии = *$1000*', reply_markup=markup, parse_mode = 'Markdown')
#######################################################################
@bot.message_handler(regexp = 'Описание услуги по написанию мотивационного письма$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги по написанию мотивационного письма')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Мотивационное письмо - одна из *ключевых* составляющих вашей заявки в '+
                 'университет. Оно  дает возможность показать Вас как *личность*, а не как набор грамот '+
                 'и дипломов. Для помощи в написании мотивационного письма мы изучим требования университета '+
                 'к нему, обсудим с вами содержание, подготовим письмо и профессионально отредактируем!', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'Стоимость услуги по написанию мотивационного письма$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnd)
    bot.reply_to(message, '*25000 тенге*', reply_markup=markup, parse_mode = 'Markdown')

##############################################################################################
@bot.message_handler(regexp = 'Описание услуги по написанию рекомендательного письма$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги по написанию рекомендательного письма')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Цель рекомендательного письма – показать университету, как вас оценивают '+
                 'со стороны. Для того, чтобы рекомендательное письмо оказало положительное влияние '+
                 'на вашу заявку в университет, оно должно быть правильно написано! Обсудив с Вами его '+
                 'содержание, мы сможем написать письмо, которое охарактеризует Вас с нужных лучших сторон.', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'Стоимость услуги по написанию рекомендательного письма$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnd)
    bot.reply_to(message, '*20000 тенге*', reply_markup=markup, parse_mode = 'Markdown')

#######################################################################################
@bot.message_handler(regexp = '(Описание услуги составления резюме)')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги составления резюме')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'Резюме - это самопрезентация. У резюме есть конкретная цель '+
                 '- показать почему именно Вы достойны получения стипендии или учебы в университете'+
                 '. У вас может быть огромный багаж опыта, знаний и навыков, однако в резюме необходимо '+
                 'лаконично отобразить нужную информацию - мы также проанализируем требования программы '+
                 'и составим с Вами отличное резюме!', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = '(Стоимость услуги составления резюме)')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnd)
    bot.reply_to(message, '*15000 тенге*', reply_markup=markup, parse_mode = 'Markdown')

################################################################
@bot.message_handler(regexp = 'Описание консультации$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость консультации')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'С удовольствием проконсультируем по поводу стипендиальных '+
                 'программ на базе Ваших предпочтений. Вы заполняете заявку и указываете '+
                 'предпочтения - мы анализируем их и подбираем программы - организовываем '+
                 'звонок по Skype и разбираем стипендии', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'Стоимость консультации$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnd)
    bot.reply_to(message, '*10000 тенге*', reply_markup=markup, parse_mode = 'Markdown')
############################################################################
@bot.message_handler(regexp = 'Описание услуги подготовки к IELTS$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnc = types.KeyboardButton(u'\U0001F4B8'+'  Стоимость услуги подготовки к IELTS')
    itembtnd = types.KeyboardButton(u'\U0001F519'+'  Назад к услугам')
    markup.row(itembtnc)
    markup.row(itembtnd)
    bot.reply_to(message, 'На данный момент мы предоставляем индивидуальные занятия '+
                 'через Skype - это экономит время и позволяет заниматься где и когда '+
                 'угодно. Существует возможность видео- и аудио-записи каждого урока для студента'+
                 ', также у каждого студента будет личная папка, в которой будут храниться все материалы '+
                 'пройденных уроков. Закажите пробный урок абсолютно бесплатно!', reply_markup=markup, parse_mode = 'Markdown')

@bot.message_handler(regexp = 'Стоимость услуги подготовки к IELTS$')
def send_answer(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    itembtnd = types.KeyboardButton(u'\U0001F448'+'  Назад в главное меню')
    markup.row(itembtnd)
    bot.reply_to(message, '1 занятие (75 минут) - *4000 тенге*', reply_markup=markup, parse_mode = 'Markdown')
#######################################################################################
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Для подсказки наберите /help. Для информации нажмите /info.")


if __name__ == '__main__':
        app.run(host='0.0.0.0',
            port=int(port))
