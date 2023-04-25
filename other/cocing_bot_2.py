import telebot
import json

bot = telebot.TeleBot('5887613919:AAEVJlzAtCLJDiLw_8Q-7EuINfMv_Zo1enQ')
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Цезарь')

Tsezar = {1:["Батон нарезаем кубиками или брусочками. Сбрызгиваем столовой ложкой оливкового масла и натираем зубчиком чеснока.",'/home/jestroarteon/picture/1_bot.jpg'],
          2:["Подсушиваем нарезанный хлеб на сковороде до румяной корочки.",'/home/jestroarteon/picture/2_bot.jpg'],
          3:["Слегка подмороженную (чтоб удобнее было нарезать) куриную грудку нарезаем небольшими кубиками.",'/home/jestroarteon/picture/3_bot.jpg'],
          4:["Разогреваем на сковороде 3 ст. ложки оливкового масла. Выкладываем на сковороду с маслом кусочки куриного филе и поджариваем до готовности, примерно 8-10 минут. Затем остужаем.",'/home/jestroarteon/picture/4_bot.jpg'],
          5:["Сыр твёрдых сортов натираем на мелкой тёрке.",'/home/jestroarteon/picture/5_bot.jpg'],
          6:["Готовим салатную заправку. В миску выкладываем майонез. Добавляем к майонезу горчицу, оливковое масло (2 ст. ложки), растертый желток, орегано. Приправляем немного солью и черным молотым перцем,",'/home/jestroarteon/picture/6_bot.jpg'],
          7:["Заправка для салата готова.",'/home/jestroarteon/picture/7_bot.jpg'],
          8:["В тарелку (миску) рвем руками салатные листья.",'/home/jestroarteon/picture/8_bot.jpg'],
          9:["Добавляем натертый сыр и кусочки курицы. Немного сыра оставляем для оформления салата.",'/home/jestroarteon/picture/9_bot.jpg'],
          10:["Добавляем приготовленную салатную заправку.",'/home/jestroarteon/picture/10_bot.jpg'],
          11:["Салат с курицей и сыром перемешиваем, пробуем на вкус. При необходимости добавляем специи.",'/home/jestroarteon/picture/11_bot.jpg'],
          12:["Выкладываем салат 'Цезарь' в салатник. Посыпаем оставшимся сыром и добавляем сухарики.",'/home/jestroarteon/picture/12_bot.jpg'],
          13:["Вкусный салат 'Цезарь' с куриной грудкой, сыром и сухариками готов!Приятного аппетита!",'/home/jestroarteon/picture/13_bot.jpg'],
}

Limonade = {0:["Продукты (на 5 порций):\n"
             "Апельсин — 300 г (1 шт.)\n"
             "Лимон — 110 г (1 шт.)\n"
             "Мёд — 100 г (по вкусу)\n"
             "Вода минеральная газированная (или столовая) — 1-1,5 л\n"
             "Мята свежая — 1 веточка (по вкусу)\n"]
            1:["Подготовьте все ингредиенты. Количество мёда регулируйте по своему вкусу.Газированную воду лучше заранее хорошо охладите.",""],
            2:["Апельсин и лимон ошпарьте кипятком, чтобы удалить восковой налет. Обсушите бумажным полотенцем.",""],
            3:["От лимона и апельсина отрежьте по 2-3 кружочка для подачи. С оставшихся фруктов снимите кожуру. Очищенные плоды разрежьте на небольшие кусочки, удалите косточки.",""],
            4:["Переместите лимон и апельсин в чашу блендера.",""],
            5:["Измельчите до консистенции кашицы.",""],
            6:["Цитрусовую кашицу откиньте на сито (или выложите на марлю или другую ткань) и отожмите сок. У меня получилось 160 мл сока.",""],
            7:["К свежеотжатому соку добавьте мёд. Перемешайте до его растворения.",""],
            8:["В кувшин выложите нарезанные кружочки лимона и апельсина.Листики мяты отделите от стеблей и тоже отправьте в кувшин.",""],
            9:["Влейте цитрусовый сок с мёдом.",""],
            10:["Влейте холодную газировку. Перемешайте длинной ложкой и подавайте к столу.Домашний лимонад из апельсина и лимона готов.",""],
            11:["Вкусного вам лимонада!",""]
    }
    
T = ["ПРОДУКТЫ(на 2 порции):\n"
    "Куриная грудка (подмороженная) – 250 г\n"
    "Сыр твердый – 50 г\n"
    "Батон – 5 ломтиков\n"
    "Чеснок – 1 зубчик\n"
    "Салат листовой (айсберг, пекинская капуста и т. п.) – 150 г\n"
    "Масло оливковое – 4 ст. ложки\n"
    "Соль – по вкусу\n"
    "Перец черный молотый – по вкусу\n"
    "ДЛЯ ЗАПРАВКИ:\n"
    "Майонез - 2,5 ст. ложки\n"
    "Масло оливковое – 2 ст. ложки\n"
    "Желток – 1 шт\m"
    "Горчица столовая – 1 ч. ложка\n"
    "Орегано сушёный – 1 щепотка\n"
    "Соль – по вкусу\n"
  ]

@bot.message_handler(commands=['start'])

def start_message(message):
    bot.send_message(message.chat.id, 'I am cooking_bot.', reply_markup=keyboard)
  
keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('1','2','3','4','5','6','7','8','9','10','11','12','13','x')
  
@bot.message_handler(content_types=['text'])
def TSEZAR(message):
    if message.text == 'Цезарь':
        bot.send_message(message.chat.id, T, reply_markup=keyboard1)
    elif message.text == '1':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197044.jpg')
        bot.send_message(message.chat.id, Tsezar[1])
    elif message.text == '2':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197045.jpg')
        bot.send_message(message.chat.id, Tsezar[2])
    elif message.text == '3':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197046.jpg')
        bot.send_message(message.chat.id, Tsezar[3])
    elif message.text == '4':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197047.jpg')
        bot.send_message(message.chat.id, Tsezar[4])
    elif message.text == '5':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197048.jpg')
        bot.send_message(message.chat.id, Tsezar[5])
    elif message.text == '6':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/513/big_512550.jpg')
        bot.send_message(message.chat.id, Tsezar[6])
    elif message.text == '7':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/513/big_512552.jpg')
        bot.send_message(message.chat.id, Tsezar[7])
    elif message.text == '8':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197052.jpg')
        bot.send_message(message.chat.id, Tsezar[8])
    elif message.text == '9':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197053.jpg')
        bot.send_message(message.chat.id, Tsezar[9])
    elif message.text == '10':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197054.jpg')
        bot.send_message(message.chat.id, Tsezar[10])
    elif message.text == '11':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197055.jpg')
        bot.send_message(message.chat.id, Tsezar[11])
    elif message.text == '12':
        bot.send_photo(message.chat.id, '<img src="https://img1.russianfood.com/dycontent/images_upl/198/big_197056.jpg" alt="big_197056.jpg (673×447)"/>')
        bot.send_message(message.chat.id, Tsezar[12])
    elif message.text == '13':
        bot.send_photo(message.chat.id, 'https://img1.russianfood.com/dycontent/images_upl/198/big_197057.jpg')
        bot.send_message(message.chat.id, Tsezar[13])
    elif message.text == 'x':
        bot.send_message(message.chat.id, "you exit recipe", reply_markup=keyboard)
        exit()
bot.polling()