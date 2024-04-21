import sqlite3

# Подключаемся к базе данных один раз
conn = sqlite3.connect('../mydatabase.db')
cursor = conn.cursor()

# Создаём таблицу "Рестораны"
cursor.execute('''
CREATE TABLE IF NOT EXISTS restaurants (
    restaurant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL
);
''')

# Добавляем записи в таблицу "Рестораны"
cursor.executescript('''
INSERT INTO restaurants(name, address) VALUES ('Вкусно и точка', 'Москва ул Лесная д 5');
INSERT INTO restaurants(name, address) VALUES ('Бургер Кинг', 'Москва ул Металлургов д 10');
INSERT INTO restaurants(name, address) VALUES ('Додо Пицца', 'Москва Волгоградский проспект д 110');
INSERT INTO restaurants(name, address) VALUES ('Пипони', 'Москва ул Вавилова д 37');
''')

# Создаём таблицу "Категории"
cursor.execute('''
CREATE TABLE IF NOT EXISTS categorys (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    descr TEXT NOT NULL
);
''')

# Добавляем записи в таблицу "Категории"
cursor.executescript('''
INSERT INTO categorys(name, descr) VALUES 
('Бургеры', 'Вкусные бургеры из отборной мелкорубленой говядины или котлеты из говяжьего фарша, подаваемые в ароматной круглой булке.');

INSERT INTO categorys(name, descr) VALUES 
('Пиццы', 'Насладитесь классическими и оригинальными вариантами пиццы, приготовленной на тонком или традиционном тесте. 
Наши пиццы изготавливаются из высококачественных ингредиентов с добавлением свежих овощей, ароматных специй, выдержанных сыров и первоклассной мясной начинки.');

INSERT INTO categorys(name, descr) VALUES 
('Комбо наборы', 'Идеальное сочетание для полноценного завтрака, обеда или ужина.');

INSERT INTO categorys(name, descr) VALUES 
('Картофель, стартеры', 'Разнообразие блюд из картофеля: от классических фри до оригинальных гарниров.');

INSERT INTO categorys(name, descr) VALUES 
('Завтраки', 'Начните свой день с идеального завтрака: выберите из разнообразия блюд, чтобы зарядиться энергией.');

INSERT INTO categorys(name, descr) VALUES 
('Напитки', 'Освежите себя с нашим широким выбором напитков. От классических содовых до экзотических фруктовых смесей, 
каждый найдет напиток по своему вкусу.');

INSERT INTO categorys(name, descr) VALUES 
('Коктейли', 'Искусно смешанные коктейли, приготовленные из свежих ингредиентов и премиального алкоголя. От традиционных классиков до смелых новинок — 
наша коктейльная карта обещает идеальное сочетание вкуса и стиля.');

INSERT INTO categorys(name, descr) VALUES 
('Десерты', 'Побалуйте себя нашими изысканными десертами и свежей выпечкой. От традиционных пирогов и тортов до модных десертов — 
каждый сладкоежка найдет что-то по своему вкусу.');

INSERT INTO categorys(name, descr) VALUES 
('Кофе', 'Откройте для себя мир ароматного кофе. Все напитки готовятся из отборных сортов кофе, обжаренных до совершенства, 
чтобы каждый глоток доставлял вам удовольствие.');

INSERT INTO categorys(name, descr) VALUES 
('Соусы', 'Изысканное дополнение к любому блюду — наши соусы, созданные из натуральных ингредиентов. 
От классического майонеза до экзотических и острых вариантов, у нас есть все, чтобы удивить ваши вкусовые рецепторы.');


''')


# Создаём таблицу "Блюда"
cursor.execute('''
CREATE TABLE IF NOT EXISTS dishs (
    dish_id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    descr TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (category_id) REFERENCES categorys(category_id)
);
''')

cursor.executescript('''

# Добавляем 10 бургеров - "Вкусно и точка"
INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Биг Спешиал', 'Биг Спешиал - это неповторимый сандвич с большим рубленым бифштексом из 100% отборной 
говядины на большой булочке с кунжутом. Особенный вкус сандвичу придают три кусочка сыра Эмменталь, два ломтика помидора, свежий салат, лук и соус с дымком.', 269);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Двойной Биг Спешиал', 'Двойной Биг Спешиал - это тот самый Бургер с двумя большими рублеными бифштексами 
из 100% говядины на булочке с кунжутом. Особенный вкус бургеру придает специальный соус с дымком, 3 кусочка сыра «эмменталь», ломтик помидора, свежий салат и лук.', 355);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Биг Спешиал Острый Микс', 'Биг Спешиал Острый Микс - это неповторимый сандвич с большим рубленым бифштексом 
из 100% отборной говядины на большой булочке с кунжутом. Внутри свежие овощи, сыр эмменталь, соус с дымком и специальный пряный соус из микса пикантных перцев.', 319);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Гранд', 'Гранд - это сочный бифштекс из натуральной говядины, приготовленный на гриле, 
карамелизованная булочка с кунжутом, два ломтика сыра Чеддер, кетчуп, горчица, свежий лук и маринованные огурчики.', 164);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Двойной Гранд', 'Двойной Гранд - это два сочных бифштекса из натуральной говядины, приготовленных на гриле, 
карамелизованная булочка с кунжутом, два ломтика сыра Чеддер, лук, маринованные огурчики, кетчуп и горчица.', 239);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Гранд Де Люкс', 'Гранд Де Люкс - это сочный бифштекс из натуральной говядины, приготовленный на гриле, 
карамелизованная булочка с кунжутом, два ломтика сыра Чеддер, свежий салат, кусочек помидора и лук, маринованные огурчики, кетчуп, горчица и специальный соус.', 185);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Чизбургер', 'Чизбургер - это рубленый бифштекс из натуральной цельной говядины с кусочками сыра Чеддер 
на карамелизованной булочке, заправленной горчицей, кетчупом, луком и кусочком маринованного огурчика.', 59);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Двойной Чизбургер', 'Двойной Чизбургер - это два рубленых бифштекса из натуральной цельной говядины с двумя 
кусочками сыра Чеддер на карамелизованной булочке, заправленной горчицей, кетчупом, луком и двумя кусочками маринованного огурчика.', 129);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Фиш Бургер', 'Фиш Бургер - это филе хорошо прожаренной рыбы (семейства тресковых), 
которое подается на пропаренной булочке с половинкой кусочка сыра Чеддер, заправленной специальным соусом Тар-Тар.', 165);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (1, 1, 'Гамбургер', 'Гамбургер - это рубленый бифштекс из натуральной цельной говядины на карамелизованной булочке, 
заправленной горчицей, кетчупом, луком и кусочком маринованного огурчика.', 55);


# Добавляем 10 бургеров - "Бургер Кинг"

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Ангус По-французски', ' Внутри бифштекс из мраморной говядины Абердин Ангус под ароматным трюфельным соусом 
и сыр Гауда, тающий в хрустящем кармашке. Плюс свежие овощи: салат Айсберг, два ломтика томата и маринованные огурчики — на французской булочке Бриошь.', 459.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Острый Ангус По-французски', 'Ощути парижский вайб: сочный бифштекс из мраморной говядины Абердин Ангус, 
трюфельный соус с добавлением жгучего томатного и сыр Гауда, тающий в хрустящем кармашке — на французской булочке Бриошь. А ещё внутри много овощей: салат Айсберг, 
томаты и маринованные огурчики.', 469.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Ангус По-французски Двойной', 'Бонжор, мясье! Теперь ещё больше соуса! Сразу два бифштекса из мраморной 
говядины Абердин Ангус с щедрой порцией изысканного трюфельного соуса и сыр Гауда, тающий в хрустящем кармашке. А ещё салат Айсберг, томаты и маринованные огурчики — на французской булочке 
бриошь.', 629.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Воппер По-французски', 'Один укус — и ты француз! Приготовили Воппер в парижском стиле: 100%-я говядина на огне 
под пикантным соусом Тар-Тар и сыр Гауда, тающий в хрустящем кармашке. А ещё салат Айсберг, свежий лук, ломтики томата и маринованные огурчики — на мягкой булочке с кунжутом.', 329.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Острый Воппер По-французски', 'Острая тема! Ощути парижский вайб: внутри говядина на огне под пикантным соусом 
Тар-Тар с добавлением жгучего томатного и сыр Гауда, тающий в хрустящем кармашке. А ещё салат Айсберг, лук, ломтики томата и маринованные огурчики — на мягкой булочке с кунжутом.', 339.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Гауда Чикен', 'Сочная курочка под пикантным соусом Тартар, сыр Гауда, тающий в хрустящем кармашке, 
салат Айсберг, ломтики томата, лук и маринованные огурчики — на булочке с кунжутом.', 339.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Чикенбургер с хреном', 'Особый соус с бодрящим хреном, сочная курочка, кетчуп, 
салат Айсберг и булочка с кунжутом — попробуй, если любишь новые впечатления!', 94.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Чикен Тар-Тар', 'Новый соус Тартар подчеркивает вкус сочной курочки с сыром Пармезан! 
А ещё внутри свежие томаты, салат Айсберг, рубленый лучок — на картофельной булочке с кунжутом.', 209.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Фиш Бургер', 'Обновлённый рецепт: нежное филе из мурманской белой рыбы тресковых пород, 
богатое полезными омега-3, соус Тар-тар, салат Айсберг, лук и маринованный огурчик на картофельной булочке с кунжутом!', 174.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (2, 1, 'Фиш Бургер Двойной', 'Двойная порция филе белой рыбки, соус Тар-тар, салат Айсберг, 
маринованный огурчик и лук — на ароматной картофельной булочке.', 219.99);


# Добавляем 10 пицц - "Додо пицца"
INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Креветки со сладким чили', 'Состав: Креветки, ананасы, соус сладкий чили, сладкий перец, моцарелла, 
фирменный соус альфредо', 899);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Сырная', 'Состав: Моцарелла, сыры чеддер и пармезан, фирменный соус альфредо', 539);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Пепперони фреш', 'Состав: Пикантная пепперони, увеличенная порция моцареллы, томаты, 
фирменный томатный соус', 539);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Двойной цыпленок', 'Состав: Цыпленок, моцарелла, фирменный соус альфредо', 619);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Ветчина и сыр', 'Состав: Ветчина, моцарелла, фирменный соус альфредо', 619);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Чоризо фреш', 'Состав: Острые колбаски чоризо, сладкий перец, моцарелла, фирменный томатный соус', 
539);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Пицца Жюльен', 'Состав: Цыпленок, шампиньоны, ароматный грибной соус, красный лук, чеснок, 
моцарелла, смесь сыров чеддер и пармезан, фирменный соус альфредо', 799);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Додо Микс', 'Состав: Бекон, цыпленок, ветчина, сыры чеддер и пармезан, соус песто, кубики брынзы, 
томаты, красный лук, моцарелла, фирменный соус альфредо, чеснок, итальянские травы', 219);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Песто', 'Состав: Цыпленок, соус песто, кубики брынзы, томаты, моцарелла, фирменный соус альфредо', 799);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES (3, 2, 'Карбонара', 'Состав: Бекон, сыры чеддер и пармезан, моцарелла, томаты, красный лук, чеснок, 
фирменный соус альфредо, итальянские травы', 899);


# Добавляем 10 пицц - "Пипони"
INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Цезарь', 'Состав: Куриная грудка, салат Айсберг, помидоры Черри, сухарики, сыр Моцарелла, сыр Пармезан, соус Цезарь, зелень.', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Пипони', 'Состав: Говядина, салями, перец болгарский, шампиньоны, помидоры, маслины, зелень, специи, сыр Моцарелла, соус Пипони', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Мясная', 'Состав: Говядина, салями, сыр Моцарелла, соус Пипони', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Ко-ко', 'Состав: Куриные грудки, перец болгарский, помидоры, зелень, сыр Моцарелла, соус Пипони', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, '4 сыра', 'Состав: Сыр Моцарелла, Сыр Горгонзола, сыр Пармезан, сыр Дор-блю, зелень, соус Пипони', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Морская', 'Состав: Сёмга, маслины, помидоры, сыр Моцарелла, соус Пипони', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Винченцо', 'Состав: Салями, куриные грудки, перец болгарский, помидоры, зелень, сыр Моцарелла, соус Пипони', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Французская', 'Состав: Жаренный лук, французский соус с травами (розмарин, тимьян, чабер, базилик, эстрагон), тёртое яйцо, сыр Моцарелла, перепелиные яйца, панированные в сыре Пармезан, зелень', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Греческая', 'Состав: Помидоры, свежие огурцы, перец болгарский, маслины, сыр Фетаки, сыр Моцарелла, зелень, оливковое масло', 800);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(4, 2, 'Океанская', 'Состав: Креветки, кальмары, осьминоги, помидоры, специи, сыр Моцарелла, соус Пипони', 800);







# Завершаем транзакцию и закрываем соединение
conn.commit()
conn.close()