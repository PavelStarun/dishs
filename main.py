import sqlite3

# Подключаемся к базе данных один раз
conn = sqlite3.connect('mybd.db')
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
('Пиццы', 'Насладитесь классическими и оригинальными вариантами пиццы, приготовленной на тонком или традиционном тесте. Наши пиццы изготавливаются из высококачественных ингредиентов с добавлением свежих овощей, ароматных специй, выдержанных сыров и первоклассной мясной начинки.');

INSERT INTO categorys(name, descr) VALUES 
('Комбо наборы', 'Идеальное сочетание для полноценного завтрака, обеда или ужина.');

INSERT INTO categorys(name, descr) VALUES 
('Картофель', 'Разнообразие блюд из картофеля: от классических фри до оригинальных гарниров.');

INSERT INTO categorys(name, descr) VALUES 
('Завтраки', 'Начните свой день с идеального завтрака: выберите из разнообразия блюд, чтобы зарядиться энергией.');

INSERT INTO categorys(name, descr) VALUES 
('Напитки', 'Освежите себя с нашим широким выбором напитков. От классических содовых до экзотических фруктовых смесей, каждый найдет напиток по своему вкусу.');

INSERT INTO categorys(name, descr) VALUES 
('Коктейли', 'Искусно смешанные коктейли, приготовленные из свежих ингредиентов и премиального алкоголя. От традиционных классиков до смелых новинок — наша коктейльная карта обещает идеальное сочетание вкуса и стиля.');

INSERT INTO categorys(name, descr) VALUES 
('Десерты', 'Побалуйте себя нашими изысканными десертами и свежей выпечкой. От традиционных пирогов и тортов до модных десертов — каждый сладкоежка найдет что-то по своему вкусу.');

INSERT INTO categorys(name, descr) VALUES 
('Кофе', 'Откройте для себя мир ароматного кофе. Все напитки готовятся из отборных сортов кофе, обжаренных до совершенства, чтобы каждый глоток доставлял вам удовольствие.');

INSERT INTO categorys(name, descr) VALUES 
('Соусы', 'Изысканное дополнение к любому блюду — наши соусы, созданные из натуральных ингредиентов. От классического майонеза до экзотических и острых вариантов, у нас есть все, чтобы удивить ваши вкусовые рецепторы.');


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
    image_url TEXT, 
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id),
    FOREIGN KEY (category_id) REFERENCES categorys(category_id)
);
''')

cursor.executescript('''

INSERT INTO dishs(restaurant_id, category_id, name, descr, price, image_url) VALUES 
(1, 1, 'Биг Спешиал', 'Биг Спешиал - это неповторимый сандвич с большим рубленым бифштексом из 100% отборной говядины на большой булочке с кунжутом. Особенный вкус сандвичу придают три кусочка сыра Эмменталь, два ломтика помидора, свежий салат, лук и соус с дымком.', 269, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/642751924-big-speshial-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Двойной Биг Спешиал', 'Двойной Биг Спешиал - это тот самый Бургер с двумя большими рублеными бифштексами из 100% говядины на булочке с кунжутом. Особенный вкус бургеру придает специальный соус с дымком, 3 кусочка сыра «эмменталь», ломтик помидора, свежий салат и лук.', 355, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/646861530-dvojnoj-big-speshial-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Биг Спешиал Острый Микс', 'Биг Спешиал Острый Микс - это неповторимый сандвич с большим рубленым бифштексом из 100% отборной говядины на большой булочке с кунжутом. Внутри свежие овощи, сыр эмменталь, соус с дымком и специальный пряный соус из микса пикантных перцев.', 319, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/126814652-big-speshial-ostryj-miks-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Гранд', 'Гранд - это сочный бифштекс из натуральной говядины, приготовленный на гриле, карамелизованная булочка с кунжутом, два ломтика сыра Чеддер, кетчуп, горчица, свежий лук и маринованные огурчики.', 164, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/42181128-grand-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Двойной Гранд', 'Двойной Гранд - это два сочных бифштекса из натуральной говядины, приготовленных на гриле, карамелизованная булочка с кунжутом, два ломтика сыра Чеддер, лук, маринованные огурчики, кетчуп и горчица.', 239, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/937512304-dvojnoj-grand-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Гранд Де Люкс', 'Гранд Де Люкс - это сочный бифштекс из натуральной говядины, приготовленный на гриле,карамелизованная булочка с кунжутом, два ломтика сыра Чеддер, свежий салат, кусочек помидора и лук, маринованные огурчики, кетчуп, горчица и специальный соус.', 185, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/65565294-grand-de-lyuks-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Чизбургер', 'Чизбургер - это рубленый бифштекс из натуральной цельной говядины с кусочками сыра Чеддер на карамелизованной булочке, заправленной горчицей, кетчупом, луком и кусочком маринованного огурчика.', 59, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/348457690-chizburger-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Двойной Чизбургер', 'Двойной Чизбургер - это два рубленых бифштекса из натуральной цельной говядины с двумя кусочками сыра Чеддер на карамелизованной булочке, заправленной горчицей, кетчупом, луком и двумя кусочками маринованного огурчика.', 129, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/135249901-dvojnoj-chizburger-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Фиш Бургер', 'Фиш Бургер - это филе хорошо прожаренной рыбы (семейства тресковых), которое подается на пропаренной булочке с половинкой кусочка сыра Чеддер, заправленной специальным соусом Тар-Тар.', 165, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/866801041-fish-burger-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 1, 'Гамбургер', 'Гамбургер - это рубленый бифштекс из натуральной цельной говядины на карамелизованной булочке, заправленной горчицей, кетчупом, луком и кусочком маринованного огурчика.', 55, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/764668645-gamburger-600x600.webp');




INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Ангус По-французски', ' Внутри бифштекс из мраморной говядины Абердин Ангус под ароматным трюфельным соусом и сыр Гауда, тающий в хрустящем кармашке. Плюс свежие овощи: салат Айсберг, два ломтика томата и маринованные огурчики — на французской булочке Бриошь.', 459.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Острый Ангус По-французски', 'Ощути парижский вайб: сочный бифштекс из мраморной говядины Абердин Ангус, трюфельный соус с добавлением жгучего томатного и сыр Гауда, тающий в хрустящем кармашке — на французской булочке Бриошь. А ещё внутри много овощей: салат Айсберг, томаты и маринованные огурчики.', 469.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Ангус По-французски Двойной', 'Бонжор, мясье! Теперь ещё больше соуса! Сразу два бифштекса из мраморной говядины Абердин Ангус с щедрой порцией изысканного трюфельного соуса и сыр Гауда, тающий в хрустящем кармашке. А ещё салат Айсберг, томаты и маринованные огурчики — на французской булочке бриошь.', 629.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Воппер По-французски', 'Один укус — и ты француз! Приготовили Воппер в парижском стиле: 100%-я говядина на огне под пикантным соусом Тар-Тар и сыр Гауда, тающий в хрустящем кармашке. А ещё салат Айсберг, свежий лук, ломтики томата и маринованные огурчики — на мягкой булочке с кунжутом.', 329.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Острый Воппер По-французски', 'Острая тема! Ощути парижский вайб: внутри говядина на огне под пикантным соусом Тар-Тар с добавлением жгучего томатного и сыр Гауда, тающий в хрустящем кармашке. А ещё салат Айсберг, лук, ломтики томата и маринованные огурчики — на мягкой булочке с кунжутом.', 339.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Гауда Чикен', 'Сочная курочка под пикантным соусом Тартар, сыр Гауда, тающий в хрустящем кармашке, салат Айсберг, ломтики томата, лук и маринованные огурчики — на булочке с кунжутом.', 339.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Чикенбургер с хреном', 'Особый соус с бодрящим хреном, сочная курочка, кетчуп, салат Айсберг и булочка с кунжутом — попробуй, если любишь новые впечатления!', 94.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Чикен Тар-Тар', 'Новый соус Тартар подчеркивает вкус сочной курочки с сыром Пармезан! А ещё внутри свежие томаты, салат Айсберг, рубленый лучок — на картофельной булочке с кунжутом.', 209.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Фиш Бургер', 'Обновлённый рецепт: нежное филе из мурманской белой рыбы тресковых пород, богатое полезными омега-3, соус Тар-тар, салат Айсберг, лук и маринованный огурчик на картофельной булочке с кунжутом!', 174.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 1, 'Фиш Бургер Двойной', 'Двойная порция филе белой рыбки, соус Тар-тар, салат Айсберг, маринованный огурчик и лук — на ароматной картофельной булочке.', 219.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Креветки со сладким чили', 'Состав: Креветки, ананасы, соус сладкий чили, сладкий перец, моцарелла, фирменный соус альфредо', 899);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Сырная', 'Состав: Моцарелла, сыры чеддер и пармезан, фирменный соус альфредо', 539);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Пепперони фреш', 'Состав: Пикантная пепперони, увеличенная порция моцареллы, томаты, фирменный томатный соус', 539);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Двойной цыпленок', 'Состав: Цыпленок, моцарелла, фирменный соус альфредо', 619);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Ветчина и сыр', 'Состав: Ветчина, моцарелла, фирменный соус альфредо', 619);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Чоризо фреш', 'Состав: Острые колбаски чоризо, сладкий перец, моцарелла, фирменный томатный соус', 539);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Пицца Жюльен', 'Состав: Цыпленок, шампиньоны, ароматный грибной соус, красный лук, чеснок, моцарелла, смесь сыров чеддер и пармезан, фирменный соус альфредо', 799);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Додо Микс', 'Состав: Бекон, цыпленок, ветчина, сыры чеддер и пармезан, соус песто, кубики брынзы, томаты, красный лук, моцарелла, фирменный соус альфредо, чеснок, итальянские травы', 219);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Песто', 'Состав: Цыпленок, соус песто, кубики брынзы, томаты, моцарелла, фирменный соус альфредо', 799);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 2, 'Карбонара', 'Состав: Бекон, сыры чеддер и пармезан, моцарелла, томаты, красный лук, чеснок, фирменный соус альфредо, итальянские травы', 899);



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



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 3, 'Гранд Комбо', 'Стандартный Комбо состоит из бургера Гранд, картофеля или наггетсов на выбор и напитка на выбор', 240, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/598979133-grand-kombo-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 3, 'Биг Спешиал Комбо', 'Стандартный комбо состоит: из бургера Биг Спешиал, картофеля или наггетсов на выбор и напитка на выбор.', 351, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/514256677-big-speshial-kombo-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 3, 'Фиш Бургер Комбо', 'Стандартный Комбо состоит из Фиш Бургера, картофеля или наггетсов на выбор и напитка на выбор.', 269, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/616739709-fish-burger-kombo-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 3, 'Двойной Чизбургер Комбо', 'Стандартный комбо состоит из Двойного Чизбургера, картофеля или наггетсов на выбор и напитка на выбор.', 210, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/843937367-dvojnoj-chizburger-kombo-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 3, 'Сет для Большой Компании', 'Сет для Большой Компании - это выгодный сет на большую компанию, который состоит из пары бургеров Биг Хит, Картофеля на выбор, Стрипсов (7 шт.) и двух напитков на выбор.', 999, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/26365525-set-dlya-bolshoj-kompanii-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 3, 'Перекусить - Кинг Комбо M', 'Кинг Фри стандартный, Чикенбургер, Эвервесс Кола мал 0,4', 249.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 3, 'Перекусить - Кинг Комбо L', 'Кинг Фри большой, Чикенбургер, Эвервесс Кола большой 0,4', 284.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 3, 'Перекусить - Кинг Комбо XL', 'Кинг Фри большой, Чикенбургер, Эвервесс Кола большой 0,5', 324.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 3, 'Классическое -Кинг Комбо XL', 'Воппер, Кинг Фри большой, Эвервесс Кола большой 0,5', 449.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 3, 'Поесть как следует - Кинг Комбо M', 'Шримп Ролл, Кинг Фри стандартный, Эвервесс Кола мал 0,4', 449.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 3, 'Комбо Леди Баг и Супер-Кота', 'Чудесный набор: маленькая пицца на выбор и брелок с персонажем мультсериала или его квами', 516);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 3, 'Четыре в одном', 'Если хочется всего понемногу. Маленькая пицца, закуска, напиток и соус.', 798);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 3, '3 пиццы', 'Три удовольствия в нашем меню — это 3 средние пиццы на ваш выбор', 1617);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 3, '10 пицц', 'Великолепная десятка. 10 средних пицц на любой вкус. Для компании из 20-30 человек.', 7070);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(3, 3, '2 пиццы и напиток', 'Для уютных посиделок. 2 маленькие пиццы и напиток на выбор. Для компании из 2-4 человек.', 953);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 4, 'Большой Снэк Бокс с Крыльями', 'Большой Снэк Бокс с Крыльями - это пикантные Куриные крылышки в хрустящей панировке – 4 шт. Наггетсы – 4 шт. Сырные треугольники – 4 шт. 2 стандартные порции Картофеля фри.', 469, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/25148752-bolshoj-snek-boks-s-krylyami-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 4, 'Картофель фри', 'Картофель Фри - это вкусные, обжаренные в растительном фритюре и слегка посоленные палочки картофеля.', 75, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/374533923-kartofel-fri-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 4, 'Картофель по-деревенски', 'Картофель по-деревенски - это вкусные, обжаренные в растительном фритюре ломтики картофеля со специями.', 85, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/633541452-kartofel-po-derevenski-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(1, 4, 'Гранд Фри', 'Гранд Фри - это вкусные, обжаренные в растительном фритюре и слегка посоленные палочки картофеля.', 85, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/437772257-grand-fri-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 4, 'Кинг Фри Сметана и Лук', 'Наша фирменная картошечка – с Вкусной штукой, нашей новой приправой со вкусом Сметана и Лук', 124.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 4, 'Картофель Деревенский Сметана и Лук', 'Золотистая картошечка по-деревенски – с Вкусной штукой, нашей новой приправой со вкусом Сметана и Лук.', 169.99);  

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 4, 'Кинг Фри большой', 'Горячий и свежий картофель Кинг Фри - золотистые и хрустящие ломтики отлично дополнят любой обед', 134.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES 
(2, 4, 'Острый Картофель Деревенский стандартный', 'Золотистая картошечка по-деревенски — с Острой штукой, нашей новой приправой с огоньком. Чтобы перемешать картофель с Острой штукой', 169.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 4, 'Картофель из печи с соусом', 'Запеченная в печи картошечка с пряными специями. В комплекте сырный соус', 270);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 4, 'Картофель из печи', 'Запеченная в печи картошечка — привычный вкус и мало масла. В составе пряные специи', 229);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 4, 'Ланчбокс с куриными кусочками', 'Горячий сытный обед из нежных куриных кусочков, пряного картофеля из печи и сырного соуса', 355);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 4, 'Ланчбокс с куриными крыльями', 'Горячий сытный обед из куриных крылышек со специями и ароматом копчения, пряного картофеля из печи и соуса барбекю', 355);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 5, 'Яичница', 'Яичница - это жареные на гриле два яйца в сочетании с ароматными английскими булочками Маффин и джемом или мёдом по вкусу. Продукт доступен только во время завтрака.', 115, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/425964649-yaichnitsa-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 5, 'Двойной Маффин с яйцом и свиной котлетой', 'войной Маффин с яйцом и свиной котлетой - нежная горячая булочка с яйцом, двумя аппетитными котлетами из свинины и двумя ломтиками сыра Чеддер.', 165, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/635329102-dvojnoj-maffin-s-yajtsom-i-svinoj-kotletoj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 5, 'Яичница с ветчиной', 'Яичница с ветчиной - это жареные на гриле два яйца в сочетании с ароматными английскими булочками Маффин, добавлением ветчины и джемом или мёдом по вкусу. Продукт доступен только во время завтрака.', 145, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/518027267-yaichnitsa-s-vetchinoj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 5, 'Омлет с сыром', 'Омлет с сыром - это пышный омлет и два ломтика сыра в сочетании с ароматными английскими булочками Маффин с порцией джема.', 145, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/253350987-omlet-s-syrom-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 5, 'Большой Завтрак', 'Большой завтрак - это полноценный завтрак из пышного омлета, аппетитной свиной котлеты, картофельного оладушка и нежной английской булочки с джемом. Продукт доступен только во время завтрака.', 169, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/590769837-bolshoj-zavtrak-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 6, 'Кока-Кола', 'Прохладительный газированный напиток Кока-Кола в бутылке.', 109, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/56776697-koka-kola-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 6, 'Фанта Мангуава', 'Фанта Мангуава - это прохладительный газированный напиток 500 мл.', 109, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/923875010-fanta-manguava-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 6, 'Питьевая вода Аква Минерале газированная', 'Питьевая газированныя вода Аква Минерале производства компании ПепсиКо.', 89, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/133034994-pitevaya-voda-akva-minerale-gazirovannaya-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 6, 'Питьевая вода Аква Минерале негазированная', 'Питьевая негазированныя вода Аква Минерале производства компании ПепсиКо.', 89, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/601178050-pitevaya-voda-akva-minerale-negazirovannaya-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 6, 'Апельсиновый сок', 'Состав: апельсиновый сок, охлажденная вода, сок апельсиновый концентрированный', 79, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/179546959-apelsinovyj-sok-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 6, 'Эвервесс Кола', 'современная и невероятно вкусная кола от бренда премиальных газированных напитков с более чем полувековой историей. 0,5 л', 109.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 6, 'Фрустайл Апельсин', 'Frustyle - это необычный газированный напиток или лимонад. Фрустайл со вкусом Апельсин - это газировка яркого оранжевого цвета со вкусом спелого сладкого апельсина с освежающей волной из миллиона пузырьков. 0,5 л', 109.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 6, 'Напиток Вода Аква Минерале с газом', 'Aqua Minerale — питьевая вода с удивительно свежим, приятным и мягким вкусом. 0,5 л', 119.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 6, 'Напиток Вода Аква Минерале без газа', 'Aqua Minerale — питьевая вода с удивительно свежим, приятным и мягким вкусом. 0,5 л', 114.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 6, 'Сок J7 Апельсиновый', 'Сок J7 Апельсиновый 0,2 л', 74.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 6, 'Добрый Кола Малина', '0,5 л', 135);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 6, 'Добрый Апельсин', 'Маргарита', 399.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 6, 'Вода BonaAqua негазированная', '0,5 л', 75); 

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 6, 'Морс Клюква', 'Наш фирменный морс для любителей сладкой кислинки. 0,5 л', 149);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 6, 'Яблочный сок Rich', '1 л', 259);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 6, 'Вода Aqua Minerale (без газа)', '0,6 л', 100);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 6, 'Вода Aqua Minerale (с газом)', '0,6 л', 100);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 6, 'Напиток Evervess Апельсин 0,33 л', '0,33 л', 100);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 6, 'Напиток Evervess Апельсин 1,5 л', '1,5 л', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 6, 'Напиток Evervess Лимон-Лайм 1,5 л', '1,5 л', 200);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 7, 'Молочный Коктейль Шоколадный', 'Молочный Коктейль Шоколадный - это великолепно взбитый коктейль, приготовленный из высококачественной молочной смеси и шоколадного сиропа. 0,6 л', 139, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/614820833-molochnyj-koktejl-shokoladnyj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 7, 'Молочный Коктейль Клубничный', 'Молочный Коктейль Клубничный - это великолепно взбитый коктейль, приготовленный из высококачественной молочной смеси и клубничного сиропа. 0,47 л', 115, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/745383714-molochnyj-koktejl-klubnichnyj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 7, 'Молочный Коктейль Ванильный', 'Молочный Коктейль Ванильный - это великолепно взбитый коктейль, приготовленный из высококачественной молочной смеси и ванильного сиропа. 0,3 л', 69, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/409898823-molochnyj-koktejl-vanilnyj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 7, 'Пунш Апельсин - спелые ягоды', 'Пунш Апельсин - спелые ягоды - это горячий напиток, в основе которого натуральное пюре из ягод с добавлением спелого апельсина. 0,2 л', 109, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/324471943-punsh-apelsin-spelye-yagody-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 7, 'Физз Карамель', 'Физз Карамель - освежающий напиток на основе колы и карамельного сиропа. 0,3 л', 109, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/403500183-fizz-karamel-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 7, 'Шейк Пломбир 0,3 л', 'Новый нежный-снежный! У нас появился Милк Шейк с любимым вкусом сливочного пломбира. Один глоток — и сразу в детство! 0,3 л', 144.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 7, 'Шейк Пломбир 0,4 л', 'Новый нежный-снежный! У нас появился Милк Шейк с любимым вкусом сливочного пломбира. Один глоток — и сразу в детство! 0,4 л', 154.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 7, 'Шейк Пломбир 0,5 л', 'Новый нежный-снежный! У нас появился Милк Шейк с любимым вкусом сливочного пломбира. Один глоток — и сразу в детство! 0,5 л', 174.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 7, 'Клубничный шейк', 'Новый нежный-снежный! У нас появился Милк Шейк с любимым вкусом сливочного пломбира. Один глоток — и сразу в детство! 0,3 л', 144.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 7, 'Шоколадный Шейк', 'Новый нежный-снежный! У нас появился Милк Шейк с любимым вкусом сливочного пломбира. Один глоток — и сразу в детство! 0,4 л', 154.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 7, 'Молочный коктейль Ежевика-малина', 'Сливочная прохлада классического молочного коктейля с добавлением лесных ягод. 0,3 л', 220);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 7, 'Молочный коктейль Пина Колада', 'Тропическое сочетание кокоса и ананаса в нежном милкшейке. 0,3 л', 220);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 7, 'Молочный коктейль с печеньем Орео', 'Как вкуснее есть печенье? Его лучше пить! Попробуйте молочный коктейль с мороженым и дробленым печеньем Орео. 0,3 л', 220);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 7, 'Классический молочный коктейль', 'В мире так много коктейлей, но классика — вечна. Попробуйте наш молочный напиток с мороженым. 0,3 л', 195);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 7, 'Клубничный молочный коктейль', 'Не важно, какое время года на улице, этот коктейль с клубничным сиропом вернет вас в лето с одного глотка. 0,3 л', 220);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 7, 'Коктейль Ванильный', '32 см.', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 7, 'Коктейль Клубничный', '32 см.', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 7, 'Коктейль Шоколадный', '32 см.', 200);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 8, 'Пирожок Вишневый', 'Обжаренный во фритюре пирожок со сладкой начинкой из 100% вишни.', 59, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/521573545-pirogok-vishnevyj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 8, 'Мороженое Карамельное', 'Из 100% натурального цельного молока с добавлением карамели.', 84, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/966938266-morogenoe-karamelnoe-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 8, 'Айс Де Люкс Шоколадный брауни', 'Из натурального цельного молока с кусочками шоколадного брауни и топпингом.', 109, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/65476509-ajs-de-lyuks-shokoladnyj-brauni-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 8, 'Айс Де Люкс Шоколадно-клубничное', 'Айс Де Люкс Шоколадно-клубничное - это мороженое из натурального цельного молока, взбитое с клубничным наполнителем и с вафельно-шоколадной крошкой.', 119, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/999598912-ajs-de-lyuks-shokoladno-klubnichnoe-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 8, 'Яблочное пюре Агуша', 'Яблочное пюре Агуша - это натуральное пюре на основе свежих спелых яблок в мягкой упаковке.', 65, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/152088497-yablochnoe-pyure-agusha-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 8, 'Пирожок Клубника-Банан', 'горячий пирожок из тонкого хрустящего теста с двухслойной начинкой: сладость банана оттеняется ароматом клубничного джема — это что-то на богемном!', 94.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 8, 'Горячий Брауни', 'Это горячее нежное пирожное с темным шоколадом внутри.', 124.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 8, 'Горячий Брауни с мороженым', 'Это нежное пирожное с темным шоколадом внутри. Оно подается горячим и особенно вкусно, если добавить сверху мороженое.', 165.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 8, 'Сандэй Клубничный', 'Ванильное мороженое с наполнителем - клубничный соус.', 134.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 8, 'Айс Твист Шоколадный', 'Шоколадный топпинг и нежное взбитое мороженое с хрустящими кусочками песочного печенья. Айс, как вкусно!', 154.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 8, 'Чизкейк Нью Йорк с кокосом', 'Это не классический творожный чизкейк, а похож! Это его нежный брат близнец с новым кокосовым вкусом', 159);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 8, 'Слоеные палочки с ананасами и брусникой', 'Здесь все сразу — брусника и ананас со сгущенкой на слоеном тесте', 269);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 8, 'Макарон манго-маракуйя', 'Bon appétit! Знаменитый французский десерт со вкусом тропических фруктов', 119);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 8, 'Эклеры-мини с заварным кремом', 'Три эклера — это много или мало? Мы считаем, в самый раз. Десерт с нежной начинкой для кофе и компаний', 159);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 8, 'Маффин Три шоколада', 'Ну и кекс этот маффин! Он из натурального какао, а внутри — нежная начинка из кубиков белого и молочного шоколада', 99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 8, 'Чизкейк Нью-Йорк', '200 гр', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 8, 'Чизкейк Малиновый', '200 гр', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 8, 'Чизкейк Клубничный', '200 гр', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 8, 'Чизкейк Шоколадный', '200 гр', 200);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 8, 'Чизкейк Яблочно-Карамельный', '200 гр', 200);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 9, 'Айс Кофе Кленовый пекан', 'Айс Кофе Кленовый пекан - это холодный молочный напиток с тонким ароматом эспрессо со вкусом кленового сиропа и ореха пекан.', 135, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/795425242-ajs-kofe-klenovyj-pekan-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 9, 'Капучино', 'Капучино - это ароматный Эспрессо с добавлением взбитого молока и плотной шапкой молочной пены, сверху посыпанный шоколадной пудрой или корицей.', 65, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/53458915-kapuchino-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 9, 'Латте', 'Состав Латте: горячая вода, кофейные зерна Paulig Espresso Originale, молоко питьевое ультрапастеризованное', 105, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/870119412-latte-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 9, 'Американо', '0,4 л', 93, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/253715394-amerikano-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 9, 'Горячий Шоколад', 'Горячий Шоколад - это напиток с нежным сливочным вкусом, приготовленный на основе вспененного молока с шоколадной пудрой.', 179, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/744497464-goryachij-shokolad-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 9, 'Латте Тирамису', 'Нежный Латте со вкусом знаменитого итальянского десерта Тирамису — с нотками какао, сливочного сыра Маскарпоне и бисквитного печенья. 0,5 л', 199.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 9, 'Латте', 'Нежный молочно-кофейный напиток состоит из трех слоев: молока, кофе и молочной пенки.', 139.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 9, 'Капучино', 'Ароматный кофейный напиток с нежной молочной пенкой.', 79.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 9, 'Кофе', 'Натуральный свежесваренный кофе станет прекрасным началом дня или дополнением к плотному обеду и легкому десерту. 0,3 л', 124.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 9, 'Глясе', 'Натуральный свежесваренный кофе с добавлением мороженого. 0,3 л', 149.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 9, 'Кофе Карамельный капучино', 'Если не шоколад, то карамель! А капучино с карамельным сиропом особенно хорош. 0,3 л', 159);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 9, 'Кокосовый латте', 'Горячий напиток на основе эспрессо с увеличенной порцией молока и кокосовым сиропом. 0,3 л', 159);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 9, 'Айс Капучино', 'Освежающий напиток для любителей кофе. В составе эспрессо, пломбир, молоко и бодрость на весь день. 0,3 л', 220);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 9, 'Капучино', 'Король среди кофейных напитков — классический капучино. Для любителей сбалансированного кофейно-молочного вкуса. 0,4 л', 159);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 9, 'Латте', 'Когда хочется нежную молочную пенку, на помощь приходит классический латте. 0,4 л', 159);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(4, 9, 'Кофе Lavazza', 'в ассортименте, 200 мл', 100);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 10, 'Сырный', 'Соус Сырный - вероятно, самая популярный соус в Макдональдс и не только. Идеально сочетается с блюдами из птицы и запеченым картофелем.', 40, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/984127953-sous-syrnyj-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 10, 'Кисло-Сладкий', 'Традиционный кисло-сладкий соус - это универсальная заправка, которая прекрасно подойдет для мясных, рыбных и овощных блюд. Вес продукта 25 грамм.', 40, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/425341532-sous-kislo-sladkij-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 10, 'Терияки', 'Терияки - это классический солоновато-сладкий соус азиатской кухни на основе соевого соуса. Вес продукта 25 грамм.', 40, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/269049798-sous-teriyaki-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 10, '1000 Островов', 'Соус 1000 Островов - это сочетание майонеза и кетчупа. Пикантная заправка отлично подойдет к любому блюду. Вес продукта 25 грамм.', 40, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/792472636-sous-1000-ostrovov-600x600.webp');

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(1, 10, 'Чесночный', 'Соус Чесночный - пикантная заправка с нежным сливочно-чесночным вкусом на основе растительных масел чеснока. Вес продукта 25 грамм.', 40, 'https://vkusnotochkamenu.ru/image/cachewebp/catalog/photo/347923190-sous-chesnochnyj-600x600.webp');



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 10, 'Соус Тар - Тар', '25 грамм', 64.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 10, 'Соус Сырный', '25 грамм', 59.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 10, 'Сырный соус Пармеджано', '25 грамм', 64.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 10, 'Соус Чесночный', '25 грамм', 59.99);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(2, 10, 'Соус Кисло-сладкий', '25 грамм', 59.99);



INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 10, 'Сырный', 'Фирменный соус с дымным ароматом для бортиков пиццы и горячих закусок, 25 г', 45);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 10, 'Чесночный соус', 'Фирменный соус с чесночным вкусом для бортиков пиццы и горячих закусок, 25 г', 45);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 10, 'Барбекю', 'Фирменный соус с дымным ароматом для бортиков пиццы и горячих закусок, 25 г', 45);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 10, 'Сладкий чили', 'Фирменный соус с дымным ароматом для бортиков пиццы и горячих закусок, 25 г', 45);

INSERT INTO dishs(restaurant_id, category_id, name, descr, price) VALUES
(3, 10, 'Малиновое варенье', 'Идеально к сырникам, 25 г', 45);


''')

conn.commit()
conn.close()

