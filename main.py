from telebot import types
import telebot

bot = telebot.TeleBot('7221708552:AAHcXDv-hNywS1N1DReWk0U6vViqhAoKAEE')

global n
data = ["Х", "И", "Н", "К", "А", "Л", "И"]


def webAppKeyboard():  # создание клавиатуры с webapp кнопкой
    keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
    webAppTest = types.WebAppInfo("https://iakovleven.github.io/tap/")  # создаем webappinfo - формат хранения url
    one_butt = types.KeyboardButton(text="Тапай хинкали!", web_app=webAppTest)  # создаем кнопку типа webapp
    keyboard.add(one_butt)  # добавляем кнопки в клавиатуру

    return keyboard  # возвращаем клавиатуру


def webAppKeyboardInline():  # создание inline-клавиатуры с webapp кнопкой
    keyboard = types.InlineKeyboardMarkup(row_width=1)  # создаем клавиатуру inline
    webApp = types.WebAppInfo("https://telegram.mihailgok.ru")  # создаем webappinfo - формат хранения url
    one = types.InlineKeyboardButton(text="Веб приложение", web_app=webApp)  # создаем кнопку типа webapp
    keyboard.add(one)  # добавляем кнопку в клавиатуру

    return keyboard  # возвращаем клавиатуру


@bot.message_handler(commands=['start'])  # обрабатываем команду старт
def start_fun(message):
    bot.send_message(message.chat.id,
                     "Хинкали",
                     parse_mode="Markdown", reply_markup=webAppKeyboard())
    n += 1


@bot.message_handler(content_types="text")
def new_mes(message):
    start_fun(message)


@bot.message_handler(content_types="web_app_data")  # получаем отправленные данные
def answer(webAppMes):
    print(webAppMes)  # вся информация о сообщении
    print(webAppMes.web_app_data.data)  # конкретно то что мы передали в бота
    bot.send_message(webAppMes.chat.id, f"получили инофрмацию из веб-приложения: {webAppMes.web_app_data.data}")
    # отправляем сообщение в ответ на отправку данных из веб-приложения


if __name__ == '__main__':
    n = 0
    bot.infinity_polling()
