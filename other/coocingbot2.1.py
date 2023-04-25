import telebot
import json

bot = telebot.TeleBot('5887613919:AAEVJlzAtCLJDiLw_8Q-7EuINfMv_Zo1enQ')
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Салат Цезарь', 'Блины «Ажурные»', 'Лимонад «Домашний»')
keyboard2 = telebot.types.ReplyKeyboardMarkup(True)
keyboard2.row('Назад', 'Далее')
keyboard2.row('К продуктам', 'К рецептам')
Tsezar = {
    0: ["ПРОДУКТЫ(на 2 порции):\n"
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
        "Соль – по вкусу\n"],
    1: [
        "Батон нарезаем кубиками или брусочками. Сбрызгиваем столовой ложкой оливкового масла и натираем зубчиком чеснока.",
        'https://img1.russianfood.com/dycontent/images_upl/198/big_197044.jpg'],
    2: ["Подсушиваем нарезанный хлеб на сковороде до румяной корочки.",
        'https://img1.russianfood.com/dycontent/images_upl/198/big_197045.jpg'],
    3: ["Слегка подмороженную (чтоб удобнее было нарезать) куриную грудку нарезаем небольшими кубиками.",
        'https://img1.russianfood.com/dycontent/images_upl/198/big_197046.jpg'],
    4: [
        "Разогреваем на сковороде 3 ст. ложки оливкового масла. Выкладываем на сковороду с маслом кусочки куриного филе и поджариваем до готовности, примерно 8-10 минут. Затем остужаем.",
        'https://img1.russianfood.com/dycontent/images_upl/198/big_197047.jpg'],
    5: ["Сыр твёрдых сортов натираем на мелкой тёрке.", ''],
    6: [
        "Готовим салатную заправку. В миску выкладываем майонез. Добавляем к майонезу горчицу, оливковое масло (2 ст. ложки), растертый желток, орегано. Приправляем немного солью и черным молотым перцем,",
        '/home/jestroarteon/picture/6_bot.jpg'],
    7: ["Заправка для салата готова.", '/home/jestroarteon/picture/7_bot.jpg'],
    8: ["В тарелку (миску) рвем руками салатные листья.", '/home/jestroarteon/picture/8_bot.jpg'],
    9: ["Добавляем натертый сыр и кусочки курицы. Немного сыра оставляем для оформления салата.",
        '/home/jestroarteon/picture/9_bot.jpg'],
    10: ["Добавляем приготовленную салатную заправку.", '/home/jestroarteon/picture/10_bot.jpg'],
    11: ["Салат с курицей и сыром перемешиваем, пробуем на вкус. При необходимости добавляем специи.",
         '/home/jestroarteon/picture/11_bot.jpg'],
    12: ["Выкладываем салат 'Цезарь' в салатник. Посыпаем оставшимся сыром и добавляем сухарики.",
         '/home/jestroarteon/picture/12_bot.jpg'],
    13: ["Вкусный салат 'Цезарь' с куриной грудкой, сыром и сухариками готов!Приятного аппетита!",
         '/home/jestroarteon/picture/13_bot.jpg'],
}

Limonade = {0:["Продукты (на 5 порций):\n"
             "Апельсин — 300 г (1 шт.)\n"
             "Лимон — 110 г (1 шт.)\n"
             "Мёд — 100 г (по вкусу)\n"
             "Вода минеральная газированная (или столовая) — 1-1,5 л\n"
             "Мята свежая — 1 веточка (по вкусу)\n"]
            1:["Подготовьте все ингредиенты. Количество мёда регулируйте по своему вкусу.Газированную воду лучше заранее хорошо охладите.","https://img1.russianfood.com/dycontent/images_upl/607/big_606293.jpg"],
            2:["Апельсин и лимон ошпарьте кипятком, чтобы удалить восковой налет. Обсушите бумажным полотенцем.","https://img1.russianfood.com/dycontent/images_upl/607/big_606182.jpg"],
            3:["От лимона и апельсина отрежьте по 2-3 кружочка для подачи. С оставшихся фруктов снимите кожуру. Очищенные плоды разрежьте на небольшие кусочки, удалите косточки.","https://img1.russianfood.com/dycontent/images_upl/607/big_606183.jpg"],
            4:["Переместите лимон и апельсин в чашу блендера.","https://img1.russianfood.com/dycontent/images_upl/607/big_606184.jpg"],
            5:["Измельчите до консистенции кашицы.","https://img1.russianfood.com/dycontent/images_upl/607/big_606185.jpg"],
            6:["Цитрусовую кашицу откиньте на сито (или выложите на марлю или другую ткань) и отожмите сок. У меня получилось 160 мл сока.","https://img1.russianfood.com/dycontent/images_upl/607/big_606186.jpg"],
            7:["К свежеотжатому соку добавьте мёд. Перемешайте до его растворения.","https://img1.russianfood.com/dycontent/images_upl/607/big_606187.jpg"],
            8:["В кувшин выложите нарезанные кружочки лимона и апельсина.Листики мяты отделите от стеблей и тоже отправьте в кувшин.","https://img1.russianfood.com/dycontent/images_upl/607/big_606188.jpg"],
            9:["Влейте цитрусовый сок с мёдом.","https://img1.russianfood.com/dycontent/images_upl/607/big_606189.jpg"],
            10:["Влейте холодную газировку. Перемешайте длинной ложкой и подавайте к столу.Домашний лимонад из апельсина и лимона готов.","https://img1.russianfood.com/dycontent/images_upl/607/big_606191.jpg"],
            11:["Вкусного вам лимонада!","https://img1.russianfood.com/dycontent/images_upl/607/big_606292.jpg"]
    }

Blini = [0:["Продукты\n",
        "Молоко - 250 мл\n",
        "Вода (кипяток) - 250 мл\n",
        "Дрожжи сухие быстродействующие - 3 г (0,5 ч. ложки)\n",
        "Мука - 200 г (1,5 стакана объёмом 200 мл)\n",
        "Масло растительное - 1,5 ст. ложки\n",
        "Яйцо - 1 шт.\n",
        "Сахар - 1 ст. ложка\n",
        "Соль - 0,5 ч. ложки\n"
        ]
         1:["Подготовьте продукты по списку.","https://img1.russianfood.com/dycontent/images_upl/457/big_456410.jpg"]
         2:["Молоко налейте в сотейник, поставьте на минимальный нагрев и подогрейте до чуть тёплого состояния (около 30 градусов).","https://img1.russianfood.com/dycontent/images_upl/457/big_456411.jpg"]
         3:["Тёплое молоко перелейте в глубокую миску, добавьте дрожжи и перемешайте. Оставьте смесь примерно на 10-15 минут, для того, чтобы дрожжи активировались - на поверхности молока появится тонкий слой пены.","https://img1.russianfood.com/dycontent/images_upl/457/big_456412.jpg"]
         4:["Добавьте соль, сахар и яйцо.","https://img1.russianfood.com/dycontent/images_upl/457/big_456414.jpg"]
         5:["Тщательно размешайте молочную смесь венчиком несколько секунд, до растворения соли и сахара.","https://img1.russianfood.com/dycontent/images_upl/457/big_456415.jpg"]
         6:["Всейте муку через мелкое сито и хорошо перемешайте, чтобы не осталось комочков. Получится гладкое, густое тесто, по консистенции напоминающее очень густую сметану.","https://img1.russianfood.com/dycontent/images_upl/457/big_456416.jpg"]
         7:["Прикройте ёмкость с тестом полотенцем и оставьте в тёплом уголке кухни примерно на 40 минут. За это время тесто значительно увеличится в объёме и на его поверхности появятся небольшие пузырьки воздуха.","https://img1.russianfood.com/dycontent/images_upl/457/big_456417.jpg"]
         8:["Установите миску с тестом на полотенце. Вскипятите воду (250 мл). Постоянно помешивая тесто венчиком, тонкой струйкой влейте кипяток.","https://img1.russianfood.com/dycontent/images_upl/457/big_456418.jpg"]
         9:["Добавьте растительное масло.","https://img1.russianfood.com/dycontent/images_upl/457/big_456419.jpg"]
         10:["Ещё раз всё перемешайте. Можно приступать к выпечке блинов.","https://img1.russianfood.com/dycontent/images_upl/457/big_456420.jpg"]
         11:["Разогрейте блинную или антипригарную сковороду на сильном огне. Вылейте на сковороду порцию теста и распределите тонким, равномерным слоем по дну. Обжарьте блин примерно 20-30 секунд с одной стороны, пока его поверхность не станет матовой, а края не подрумянятся.","https://img1.russianfood.com/dycontent/images_upl/457/big_456444.jpg"]
         12:["Затем широкой лопаткой аккуратно переверните блин и обжарьте ещё 10-15 секунд с другой стороны, до румяности.","https://img1.russianfood.com/dycontent/images_upl/457/big_456570.jpg"]
         13:["Переложите готовый блин на тарелку и повторите процесс с оставшимся тестом. У меня на сковороде диаметром 24 см получается обычно 12 блинов.","https://img1.russianfood.com/dycontent/images_upl/457/big_456574.jpg"]
         14:["Ажурные блины на дрожжах готовы. Подавайте их к столу, при желании дополнив мёдом, вареньем или джемом.\nПриятного аппетита!","https://img1.russianfood.com/dycontent/images_upl/457/big_456583.jpg"]
]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Добро пожаловать в бот "Кулинар!" \nВыбери рецепт из списка ниже, чтобы начать готовить!',
                     reply_markup=keyboard)  # Дополнить текст приветствия


step = 0


@bot.message_handler(content_types=['text'])
def recept(message):
    global step
    if message.text == 'Салат Цезарь':
        msg = bot.send_message(message.chat.id, Tsezar[0], reply_markup=keyboard2)
        bot.register_next_step_handler(msg, cocking)
        step += 1


def cocking(message):
    global step
    print(step)
    if message.text == "Далее":
        bot.send_photo(message.chat.id, Tsezar[step][1])
        msg = bot.send_message(message.chat.id, Tsezar[step][0], reply_markup=keyboard2)
        step += 1
        bot.register_next_step_handler(msg, cocking)
    elif message.text == "Назад" and step > 0:
        bot.send_photo(message.chat.id, Tsezar[step][1])
        msg = bot.send_message(message.chat.id, Tsezar[step][0], reply_markup=keyboard2)
        step -= 1
        bot.register_next_step_handler(msg, cocking)
    elif message.text == "К продуктам":
        msg = bot.send_message(message.chat.id, Tsezar[0], reply_markup=keyboard2)
        bot.register_next_step_handler(msg, cocking)
        step = 1
    elif message.text == "К рецептам":
        bot.send_message(message.chat.id, "Выбери рецепт из списка ниже, чтобы начать готовить!", reply_markup=keyboard)
        step = 0
    else:
        msg = bot.send_message(message.chat.id, "К сожалению я не могу перейти к этому шагу, выберите другой",
                               reply_markup=keyboard2)
        bot.register_next_step_handler(msg, cocking)