#Персонажи наши

define kostya = Character('Костя', image = 'kostya', color="#c8ffc8", slow_cps = 20)
define kostya_mystery = Character('???', image = 'kostya', color = '#c8ffc8', slow_cps = 20)

image kostya_base = 'kostya_base.png'
image kostya_mystery = 'kostya_mystery.png'
image kostya_happy = 'kostya_happy.png'
image kostya_think = 'kostya_think.png'

define neighbor = Character('Игнат', image = 'neighbor', color= '#235fe4', slow_cps = 20)
define neighbor_secret = Character('???', image = 'neighbor', color = '#235fe4', slow_cps = 20)

image neighbor_base = 'neighbor_base.png'
image neighbor_smile = 'neighbor_smile.png'
image neighbor_surprise = 'neighbor_smile.png'
image neighbor_sad = 'neighbor_sad.png'
image neighbor_joy = 'neighbor_joy.png'
image neighbor_phone = 'neighbor_phone.png'
image neighbor_smart = 'neighbor_smart.png'
image neighbor_glasses = 'neighbor_glasses.png'

define dmitriev = Character('ИИИ', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_secret = Character('???', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_full = Character('Иванов Иван Иванович', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_surname = Character('Иван Иванович', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_short = Character('ИИ', image = 'dmitriev', color = '#abc342', slow_cps = 20)

image dmitriev_base = 'dmitriev_base.png'

define rat_1 = Character("Крыса побольше", kind = bubble, image = 'bubble.png', color = '#706d65', slow_cps = 20)

define rat_2 = Character('Крыса поменьше', kind = bubble, image = 'bubble.png', color = '#706d65', slow_cps = 20)

define player = Character("[name]", image = 'None', color = '#ac1234', slow_cps = 20) 

## Заранее извиняемся перед всеми женщинами!!!
## Нам пришлось сделать персонажа мужчиной, потому что он живет в мужском общежитии
## Кроме того, опыт главного героя основан на жизни члена нашей команды, который к сожалению, мужчина

define dad = Character('Папа', image = 'dad', slow_cps = 20)

image dad_base = 'dad_base.png'
image dad_happy = 'dad_happy.png'

define mom = Character('Мама', image = 'mom', slow_cps = 20)

image mom_base = 'mom_base.png'
image mom_happy = 'mom_happy.png'

define galina = Character('Галина Олеговна', image = 'galina', color = '#eb23a6', slow_cps = 20)

image galina = 'galina.png'

define bus_stranger = Character('???', image = 'bus_stranger', color='#235fe4')

image bus_stranger = "bus_stranger.png"

default neighbor_approval = 0
default kostya_approval = 0
default kostya_asked = 0
default kostya_questioned = []

default kostya_ignat = False
default kostya_kostya = False
default kostya_ivushki = False

default is_dream = False

default show_overlay_now = False

#Начало игры:
label start:

    #init python:
        #config.overlay_screens.append("notebook_1")

    show screen notebook
    jump choose_name

    label choose_name:

        python:
            name = renpy.input("Введите Ваше имя", "", length = 20)
            name = name.strip()

            if not name:
                name = "Студент"

        menu name:
            "Вы уверены, что Ваше имя - [name]?"

            "Да":
                jump beginning

            "Нет":
                jump choose_name

label beginning:
    
    #scene blackbg
    #play music snitch volume 0.25 fadein 1.0

    name "Ивушки™ - студенческое общежитие, находящееся во власти Университета™"
    
    name "По слухам, настоящий ад на Земле, условия почти как в тюрьме и полное отсутствие человеческой жизни"
    
    name "И вот сюда мне довелось попасть в первый год учебы…"

    #jump crossword_imba
    jump look_around

    #play sound flashback_start 
    #play music flashback fadein 1.0
    #scene flashback_room with dissolve
    #show dad_base with dissolve
    #show mom_base with dissolve

    mom "[name], я понимаю, что ты не хочешь жить с чужими людьми, но пойми, мы в твоем возрасте все прошли через такое"

    dad "Да, я на первом курсе дрался за еду с общажными крысами!"

    mom "Дорогой, что ты его пугаешь!" 
    
    mom "Не волнуйся, малыш, твой папа учился в ПТУ. Я уверена, что в твоем Университете™ такого точно не будет"

    dad "Чемпион, не грусти! Ты знаешь, что мы тебя очень любим и всегда поддержим! Звони и пиши в любое время!"

    name "Мам, пап, спасибо за поддержку! Буду молиться, чтобы вы оказались правы. Я вас тоже очень люблю!"

    #play sound flashback_end
    #play music ambient_1
    #scene blackbg with dissolve
    #hide dad_base dissolve with dissolve
    #hide mom_base dissolve with dissolve

    name "Я очень надеюсь, что слухи не правдивы."
    
    name "Я очень хочу подружиться со своими соседями, точнее соседом."
    
    name "Мне сказали, что в комнате со мной будет только один человек"
    
    name "Хоть какое-то утешение..."
    
    name "..."

    #play sound timelapse

    name "Спустя 2 часа в очереди наконец-то пора заселяться"
    
    name "Пора посмотреть, где я буду жить"
    
    name "Удачи мне..."

label first_meet:

    #play sound door_open

    #scene room 
    #play music ambient_1

    name "..."
    
    name "Странно, как будто никто не знал о моем приезде..."
    
    name "Даже со стола не убрались! А это, между прочим, должен быть наш общий!"
    
    name "И на стене календарь за 2023!?"
    
    name "..."
    
    name "Но зато как хорошо устроился - ковер на полу лежит"
    
    name "Интересно, где же мой таинственный сосед?"

    #play sound door_open_long

    show neighbor_phone
    #play music neighbor_theme fadein 1.0

    neighbor_secret "…нет, нет, нет, я тебя не понимаю! Можешь повторить еще раз?"
    
    neighbor_secret "Ааа, ты неправ! В адыгейском же всего три гласных: а, а и а. Чи дэмий яриад байна!"

    name '(Что за бред он несет…)'

    neighbor_secret 'Хүлээгээрэй, би чам руу залгах болно'

    hide neighbor_phone
    show neighbor_surprise
    #play music neighbor_theme_alt

    neighbor_secret "???"
    
    neighbor_secret "А ты..?"

    name 'Я [name], видимо мы будем соседями'

    neighbor_secret 'А...'

    hide neighbor_surprise
    show neighbor_smile
    #play music neighbor_theme

    neighbor_secret '(Что-то не помню я такого, но пусть живет)'
    
    neighbor_secret "Ну.. тогда будем знакомы, я Игнат"

    hide neighbor_smile
    show neighbor_base

    neighbor 'Извини, я как-то не прибрался к твоему приходу…'

    hide neighbor_base
    show neighbor_smile

    neighbor 'Я совершенно забыл об этом'

    hide neighbor_smile
    show neighbor_smart

    neighbor 'Смотри, я сплю на этой ор, получается эта ор твоя'

    hide neighbor_smart
    show neighbor_surprise

    neighbor 'Ой, сейчас!'
    
    neighbor 'На этой…'
    
    neighbor '…'
    
    neighbor 'Точно, кровати!'

    hide neighbor_surprise
    show neighbor_smile
    
    neighbor 'Извини, я немного подзабыл этот язык и периодически могу переключаться на монгольский.' 
    
    neighbor 'В последнее время на нем говорю только о науке, а не в обычной жизни'

    #play sound phone_ring
    hide neighbor_smile
    show neighbor_surprise

    neighbor 'Ох, мне пора бежать!!!'
    
    neighbor 'Надеюсь, разберешься как тут что'
    
    neighbor 'Увидимся вечером!'

    hide neighbor_surprise

    menu first_impression_menu: 
        
        name "Это было..."

        "Странно...":

            $ neighbor_approval -= 1

            name "Почему он вообще выбрал этот язык! Он же не в Монголии живет.. "

        "Круто!":

            $ neighbor_approval += 1

            name "Интересно, почему он выбрал именно этот язык?!"

label after_first_impression:
    name "Что ж, почему бы не осмотреться получше, раз уж есть возможность"

    jump look_around

label look_around:

    call screen our_room

    jump look_around

label table:
            
    if clicks_table == 1:

        name "Мдаа..."
                
        name "Ну и пылища.. Кружка со следами кофе... Банка из-под энергетика..."
                
        name "Кто-то явно пытался сосредоточиться в последний момент перед дедлайном..."
                
        name "Какие-то записки и скомканные бумажки..."
                
        name "Наверняка среди них есть заметка “НЕ ЗАБУДЬ СДЕЛАТЬ УБОРКУ ПЕРЕД ПРИЕЗДОМ НОВОГО СОСЕДА”" 
                
        name "..."
                
        name "Надеюсь..."

    elif clicks_table == 2:

        name "Стоп..."

        name "Он что, забыл свой ноутбук?!"

    elif clicks_table >= 3:

        name "Тут больше не на что смотреть."

    jump look_around

label window:

    if clicks_window == 1:

        name "..."

        name "Уныло."

        name "Впрочем, чего еще следовало ожидать?"

        name "Не стоит тратить время на счет ворон."

    elif clicks_window >= 2:

        name "Тут больше не на что смотреть."

    jump look_around

label board:

    if clicks_board == 1:

        name "Здесь куча каких-то непонятных слов"

        name "Наверное, это монгольский"

        name "Думаю, мне это пригодится"

        name "Надо бы записать все себе в блокнот, чтобы точно не забыть" 

        jump look_around

    if clicks_board == 2:

        name "Думаю, можно выйти в коридор"

        name "Пора бы познакомиться с другими жильцами..."

        name 'Надо бы не забыть взять блокнот'

        $ show_overlay_now = True
        show screen notebook_1

        if neighbor_approval <= -1:

            name "Может быть, они более адекватные, чем этот чудик!"

        if neighbor_approval >= 1:

            name "Надеюсь, я и с ними полажу"

        jump hallway

label hallway:
    
    show screen hallway

    play music mystery loop

    name "Как-то тут очень тихо..."

    name "???"

    show kostya_mystery

    kostya_mystery "Парень!"

    kostya_mystery "Ты что, не знаешь, как здороваться с незнакомцами?"

    kostya_mystery "Подойди и пожми мне руку"

    hide kostya_mystery
    show kostya_base
    stop music

    kostya_mystery "Ха-ха, шучу! Извини, если вдруг напугал. Меня зовут Костя."

    kostya "Ты ведь новенький в комнате Игната, да?"
    
    hide kostya_happy
    show kostya_happy

    kostya "Я тут все и обо всех знаю, так что спрашивай сколько хочешь!"

    name "О чем бы мне его спросить?.."

    name "Ну, есть три вещи, о которых я бы хотел узнать"

    jump kostya_interrogation

label kostya_interrogation:

    menu kostya_questions:

        "об Игнате": 
            
            if not kostya_ignat:
                
                $ kostya_ignat = True

                hide kostya_happy
                show kostya_base

                kostya "В этой комнате Игнат уже давно живет один."

                kostya "Все, кто туда заселяется, как через некоторое время пытаются переселиться"

                kostya "Возможно, поэтому он забывает, как говорить по-русски"

                hide kostya_base
                show kostya_think

                kostya "(Между нами, мне кажется, он немного помешался на этом)"

                kostya "Что ж, не мне судить человека!"

                hide kostya_think
                show kostya_base

                kostya "На самом деле, это даже по-своему круто"

                kostya "Я и сам интересуюсь языками и очень его понимаю"

                kostya "Вообще, я недавно поставил себе цель научиться говорить по-английски без акцента"

                kostya "Поэтому очень приятно видеть человека, который так горит своим делом"

                jump kostya_interrogation
            
            else:

                kostya 'Я уже говорил, что Игнат - хороший парень!'

                kostya 'Помни об этом!'

                jump kostya_interrogation

        "О Косте":

            if not kostya_kostya:

                $ kostya_kostya = True

                kostya "Ой, да что обо мне говорить"

                kostya "Я, как и ты, застрял здесь, но стараюсь не терять духа!"
            
                kostya "Столько ребят уже застал, но о каждом теплые воспоминания"
            
                kostya "Игнат меня называет старожилом, да и остальные тоже"

                kostya "Поэтому я считаю своим долгом помогать первашам освоиться на новом месте"

                jump kostya_interrogation

            else:

                kostya "Да что обо мне говорить? Может о себе расскажешь?"

                jump kostya_interrogation

        "Об Ивушках": 

            if not kostya_ivushki:
                
                $ kostya_ivushki = True

                kostya "Знаешь, когда я сам сюда попал, я просто ужаснулся!"

                kostya "У меня были не самые лучшие соседи, особенно для такого чистюли, как я"

                kostya "Но ничего, во всем нужно искать позитив!"

                kostya "Я нашел много новых знакомых и много чему научился"

                kostya "Уверен, что твой опыт будет лучше моего, все-таки Игнат - нормальный парень"

                if neighbor_approval <= -1:

                    name "(Ага, конечно...)"

                    jump kostya_interrogation

                else: 

                    jump kostya_interrogation

            else:

                kostya "Рано или поздно ты привыкнешь"

                jump kostya_interrogation

        "Наверное, мне пора" if kostya_ignat and kostya_ivushki and kostya_kostya:

            jump hallway_2

label hallway_2:

    if not renpy.get_screen("notebook"):
        show screen notebook

    show screen hallway
    show kostya_happy

    name "Ладно, я наверное пойду обратно к себе в комнату"

    kostya "Фух, да и мне, кажется, пора бежать"
    
    kostya "Ну все, [name], еще увидимся!"

    name 'Пока, приятно было познакомиться!'

    hide kostya_happy

    $ renpy.pause(5.0, hard=True)

    show kostya_mystery

    kostya "Стой-стой-стой! Я кое о чем вспомнил!"

    hide kostya_mystery
    show kostya_base

    kostya "Игнат недавно одолжил у меня молоко."

    kostya "Обещал отдать сегодня, но я от него получил только записку."

    kostya "Чувак опять все перепутал и написал ее на монгольском"

    kostya "Сможешь помочь с расшифровкой? За это я могу рассказать тебе кое-что полезное"

    menu useful_stuff:

        "Так... Ты меня заинтриговал":

            $ kostya_approval += 1

            hide kostya_base
            show kostya_mystery

            kostya "Это такая вещь, которую хотят все первокурсники с твоей программы: [[КОНСПЕКТ ПО ДИСКРЕ]]"

            name "Договорились!"

            name "(Звучит правда полезно)"

        "А если мне не интересно?":

            $ kostya_approval -= 1

            kostya "Это такая вещь, которую хотят все первокурсники с твоей программы: [[КОНСПЕКТ ПО ДИСКРЕ]]"

            hide kostya_base
            show kostya_mystery

            name "Ладно..."

            name "(Так уж и быть... Сдался мне этот конспект?)"

    hide kostya_mystery
    show kostya_smile
    
    kostya 'Отлично, как закончишь - скажи!'

    hide screen hallway

    jump back_to_our_room

label back_to_our_room:

    show screen our_room_non_int

    name 'Я что-то говорю потому что в сценарии пока что нету текста'

    hide screen our_room_non_int

    jump hallway_3

label hallway_3:

    show screen hallway
    show kostya_mystery

    if kostya_approval >= 1:

        name "На"

    elif kostya_approval <= 1:

        name "Вот и твое молоко!"

    kostya "Ооо! Спасибо большое!"

    kostya "Теперь я расскажу тебе о конспекте, слушай внимательно..."

    kostya "На самом деле, у тебя сейчас очень большие шансы его заполучить"

    kostya "Потому что находится он у твоего соседа"

    kostya "Я не знаю, чей это конспект и как он попал к Игнату"

    kostya "Но одно остаётся фактом - без него конспект ты не достанешь"

    if kostya_approval >= 1:

        name "(Ну вот, придется ещё что-то у этого чудика просить)"

        name 'Спасибо...'

        kostya 'Обращайся, если что!'
    
    elif kostya_approval <= 1:

        name 'Ого, спасибо большое!'

        kostya 'Обращайся, друг!'

    hide screen hallway

label evening_1:

    show screen our_room_non_int

    name "Ну и день..."

    name "Интересно, что это всё-таки за конспект и как он оказался у Игната?"

    name "Надо бы расспросить наших кураторов, может быть они что-то знают"

    name "..."

    name "Ну ладно, завтра мне на адаптационку, стоит хорошенько выспаться"

    $ renpy.pause(10.0, hard=True)

    hide screen our_room_non_int
    show screen blackbg
    play sound night_skip fadein 1.0

    "День второй."

label morning_2:

    show screen our_room_non_int
    stop night_skip fadeout 1.0

    name "Вот блин, я проспал адаптационку!"

    name "Что ж, ничего не поделать, до Университета все равно полтора часа ехать..."

    name "Видимо, останусь здесь"

    name "???"

    name "Что это за записка на столе?"

    name "“Привет, это твой сосед, сегодня я приду очень поздно, поэтому не успею купить продукты”" 
    
    name "“Можешь, пожалуйста, сходить в Пятерочку?”"

    menu neighbor_asks:

        "Да за кого он меня принимает???":

            $ neighbor_approval -= 1

            name "Только заселился, а уже как мальчик на побегушках!"

            name "Ладно, ничего не поделаешь, не ругаться же с ним"

            name "Когда не терпели..."

        "Хм, а я даже не против":

            $ neighbor_approval += 1

            name "Думаю, это неплохой способ наладить отношения"

            name "Все-таки Костя сказал, что Игнат - неплохой парень"

    scene blackbg
    jump shop_outside

label shop_outside:

    show screen shop_outside

    name "Первый раз иду в эту Пятерочку"

    name 'Надейся на худшее, готовься к лучшему.'

    name 'Кажется, так говорят...'

    name 'Зато какие крутые тачки тут стоят!'

    name 'Ладно, не стоит терять времени'

    hide screen shop_outside

    jump shop_inside

label shop_inside:

    show screen shop_inside

    name "Так-так-так"

    name "Что там нужно было купить..."

    hide screen shop_inside
    show screen shop_inside_bg

    name "..."

    $ renpy.pause(3.0, hard=True)

    name "....."

    $ renpy.pause(3.0, hard=True)

    name "Он..."

    name "На монгольском..."

    menu shopping:

        "Ну приехали":

            $ neighbor_approval -= 1

            name "За что мне все это?.."

        "Ничего страшного":

            $ neighbor_approval += 1

            name "Похоже, Игнат опять запутался"

            name "Ну ладно, поищу информацию в блокноте"

    name "Окей, нужно как-то соединить слова с продуктами"

    #вставить игру найди пару

    name "Фух, вроде со списком разобрался..."

    name "Пора все это купить"

label shop_line:

    #show screen line_dmitriev

    show dmitriev_base

    dmitriev_secret "Молодой человек, у вас есть минутка?"

    menu dmitriev_serious_question:

        "Да":

            name "(Все равно в очереди стоять)"

            name "Да, есть"

            dmitriev_secret "Чудесно!"

        "Нет":

            name "(Только этого не хватало)"

            name "Извините, нет"

            dmitriev_secret "Приму этот ответ за “да”"

    dmitriev_secret "Меня зовут Иванов Иван Иванович"

    dmitriev_full "Меня зовут Иванов Иван Иванович"

    dmitriev_surname "Меня зовут Иванов Иван Иванович"

    dmitriev_short "Меня зовут Иванов Иван Иванович"

    dmitriev "Меня зовут Иванов Иван Иванович"

    dmitriev "Я вот хотел у Вас спросить, как у представителя {color=#d12d21}ПОКОЛЕНИЯ Z...{/color}"

    dmitriev "Вот {b}ЧТО{/b} Вы знаете об {i}истории{/i} ??"

    dmitriev "На днях.. Я разговаривал со своими {color=#d12d21}внуками{/color}"

    hide dmitriev_base
    show dmitriev_rage

    dmitriev "И когда я их {b}спросил{/b} про ХРИСТИАНИЗАЦИЮ РУСИ! И про {i}{color=#d12d21}стрельцов!{/color}{/i} Они {color=#d12d21}НЕ ответили!!{/color}"

    name "..."

    dmitriev "ИИИ: А вот {color=#d12d21}ДАВАЙТЕ{/color} я у ВАС {b}СПРОШУ{/b}? Я вам {color=#d12d21}ВОПРОС, А ВЫ МНЕ — ОТВЕТ!{/color}"

    dmitriev "{color=#d12d21}{b}ВЫ СОГЛАСНЫ????{/b}{/color}"

    menu:

        "Да":

            name "Что ж... Давайте"

            hide dmitriev_rage
            show dmitriev_base

            dmitriev "{color=#d12d21}Отлично!!!!!!{/color}"

            jump dmitriev_minigame

        "Нет":

            name "Наверное, откажусь"

            hide dmitriev_rage
            show dmitriev_base

            dmitriev "Приму этот ответ за да!"

            jump dmitriev_minigame

label dmitriev_minigame:

    #разобраться

    dmitriev 'я что-то говорю потому что я плейсхолдер'


label dmitriev_secret:

    dmitriev "{color=#d12d21}Ого!!!!{/color} да вы прямо {b}МОЛОДЕЦ!{/b} {color=#d12d21}{i}Вдумчиво{/i} отвечаете на вопросы!!{/color}"

    name "Спасибо!"

    dmitriev "Теперь у меня больше {i}уверенности{/i} в {color=#d12d21}{b}Вашем поколении{/b}{/color}"

    dmitriev "{color=#d12d21}Не ХОТИТЕ ли,{/color} кстати, {color=#d12d21}{i}прийти{/i}{/color} ко мне на {b}ОТКРЫТУЮ ЛЕКЦИЮ В БИБЛИОТЕКЕ ИМЕНИ НЕКРАСОВА{/b}"

    dmitriev "Она на тему {b}{i}первородного греха и влияния христианство на Русь.{/b}{/i}"

    menu final_choice:

        "Да!":

            jump hooray

        "Нет...":

            dmitriev 'Очень {color=#d12d21}жаль!{/color}'

            jump dmitriev_win

label hooray:
    
    name "Хочу! А когда она будет происходить?"

    dmitriev "Она в эту {color=#d12d21}пятницу, {i}в 16:30{/i}{/color}"

    dmitriev "А на каком, {b}ЯЗЫКЕ{/b} {color=#d12d21}Вы {i}говорили{/i}{/color} только что?"

    name "На монгольском.. я недавно начал его учить"

    dmitriev '{color=#d12d21}О, это правильно!!!!{/color} Хотел бы я {i}вести свои лекции{/i} и там, в МОНГОЛИИ...'

    show screen blackbg fadein 5.0
    $ renpy.pause(5.0, hard = True)

    jump mongolia

label mongolia:

    show screen blackbg fadein 5.0
    play music mongol_song fadein 5.0 

    "Пять лет спустя"

    name "Вот так я и стал паломником в Монголии"

    name "Я путешествую со своим наставником, Ивановым Иваном Ивановичем"

    name "Вместе мы обучаем людей христианским ценностям и традициям."

    name "Я не жалею о том, что ушел из Университета, ведь я нашел свой смысл в таком образе жизни"

    name "Правда немного жаль, что мы так и не подружились с Игнатом..."

    name "Но это сейчас не важно, мне нужно идти, дело праведное не ждёт."

    $ renpy.pause(20.0, hard = True)

    window hide

    pause 20.0

    call screen secret_ending

    $ renpy.pause(5.0, hard = True)

    jump main_menu

label dmitriev_win:

    dmitriev "Что ж, я '{color=#d12d21}{i}ВАШУ{/color}{/i} {b}ТОЧКУ ЗРЕНИЯ{/b} понял"

    dmitriev "Но я вам, конечно, {color=#d12d21}{b}советую{/color}{/b} прийти на мою {b}{i}лекцию.{/b}{/i}"

    dmitriev "ПОРАССУЖДАЕМ над идеей Достоевского русского - ВСЕЧЕЛОВЕКА"

    name "С-спасибо, но нет"

    dmitriev "А вот и {color=#d12d21}{i}моя очередь{/color}}{/i}"

    dmitriev "Спасибо, {b}молодой человек{/b}, за {i}РАЗГОВОР.{/i} Я вынужден с вами попрощаться"

    menu:

        "Ну и к лучшему":

            jump our_turn

        "Это было даже интересно":

            jump our_turn

label our_turn:

    #show galya_background
    #show galina

    name "???"

    name "Пока я отходил от того, что произошло, подошла моя очередь"

    galina "Проходите!"

    scene blackbg fadein 1.5

    $ renpy.pause(5.0, hard=True)

    jump neighbor_notes

label neighbor_notes:

    scene our_room_non_int fadein 1.5

    name "(Последние два дня я никак не мог поговорить с Игнатом по поводу конспекта...)"

    name '(Сегодня я просто обязан это сделать!)'

    name 'Игнат, можно я кое о чем тебя спрошу?'

    show neighbor_surprise

    neighbor "Ну да, коенечно. Что такое?"

    name '(Блин, как бы аккуратно об этом сказать?..)'

    name 'Слушай... Мне тут...'

    name 'Мне тут Костя сказал, что у тебя есть... эммм...'

    name "Конспект. Конспект по дискретной математике"

    hide neighbor_surprise
    show neighbor_base

    neighbor "Так"

    name "Так вот..."
    
    name "Можно ли его у тебя позаимствовать? На время"

    name 'Я все-таки первокурсник, а тебе, наверное, он все равно сейчас не нужен'

    hide neighbor_base
    show neighbor_glasses

    neighbor "Хммм..."

    neighbor 'Ну, этот конспект для меня очень важен. Я не хочу его отдавать кому попало'

    neighbor '...'

    hide neighbor_glasses
    show neighbor_smart

    neighbor 'Идея!'

    neighbor 'Ты ведь не забыл, что я постоянно переключаюсь с монгольского на русский и обратно?'

    neighbor 'Я стараюсь больше говорить с тобой по-русски, но хотел бы увидеть подобный шаг и с твоей стороны'

    hide neighbor_smart
    show neighbor_smile

    neighbor 'Попробуй подучить монгольский, чтобы меня понимать в случае чего'

    neighbor "Через пару дней я проверю, насколько добросовестно ты подходишь к обучению"

    hide neighbor_smile
    show neighbor_glasses

    neighbor 'Если сможешь пройти мой тест, то получишь блокнот'

    neighbor 'Договорились?'

    menu notes_attitude:

        "Звучит"

        "Неплохо":

            name "(Как будто для меня в этом только плюсы)"

            name '(Изучу новый язык, начну понимать Игната, еще и конспект заполучу)'

            name 'Да, с радостью!'

            hide neighbor_glasses
            show neighbor_joy

            neighbor 'Супер!' 

        "Ужасно":

            name '(О боже...)'

            name '(Неужели мне настолько сильно нужен конспект?)'

            if kostya_approval >= 1:

                name '(Ладно, поверю Косте, что это стоит того)'

            name 'Ладно уж, давай'

            hide neighbor_glasses
            show neighbor_smile
            
            neighbor 'Отлично, готовься'

    name '(Отлично, теперь пора в Университет)'

    name '(Надо успеть на ивовозку)'

    name '...'

    name 'Кто вообще придумал это тупое слово..?'

    jump ivovozka

label ivovozka:

    name "Отлично, а теперь в университет"

    name "По коням! Точнее по ивовозкам!"

    name "..Или как там называют автобус из Ивушек.."

    scene bus

    name "Пока еду в университет, попробую узнать какие-то новые слова на монгольском"

    name "Так..."

    name "направо – “баруун тийш”"

    name "налево – “зүүнш”"
    
    name "назад – “буцаан”"
    
    name "вперед – “урагш”"
    
    name "Теперь нужно только заучить"
 
    show bus_stranger

    bus_stranger "Водителю плохо!"
    
    bus_stranger "Кто-нибудь, возьмите управление на себя, я врач, я приведу его в чувство"
    
    bus_stranger "Эй, ты, парень! Водить умеешь?"
    
    name "Да."
    
    bus_stranger "Ну вот и иди к рулю!! Быстро!!!"

    scene rul
    
label ivovozka_game:

    show screen number_controls

    scene directions

    menu:
        "куда едем?"

        "1. баруун тийш":
            jump lose

        "2. зүүнш":
            jump lose

        "3. буцаан":
            jump lose

        "4. урагш":
            jump tupik

label tupik:

    show screen number_controls_tupik

    scene tupik

    menu:
        "куда едем?"

        "1. буцаан":
            jump yama

        "2. урагш":
            jump lose

        "3. баруун тийш":
            jump lose

        "4. зүүнш":
            jump lose

label yama:

    show screen number_controls_yama

    scene yama

    menu:
        "куда едем?"

        "1. зүүнш":
            jump lose

        "2. баруун тийш":
            jump win

        "3. урагш":
            jump lose

        "4. буцаан":
            jump lose

label win:
    hide screen number_controls
    hide screen number_controls_tupik
    hide screen number_controls_yama

    scene resultpie

    "ура молодец возьми из бардачка пирожок."

    jump ivovozka_end

label lose:
    hide screen number_controls
    hide screen number_controls_tupik
    hide screen number_controls_yama

    scene resultdeath

    "але куда неправильно! все умерли."

    pause 1.5

    jump ivovozka_game


label ivovozka_end:

    scene bus

    name "Фух, доехали"
    
    name "Врач, как там водитель?"
    
    show bus_stranger
    
    bus_stranger "Нормально. Точнее не очень, но жить будет."
    
    name "Ну ладно, мне пора в вуз, вы уж дальше сами!"

    jump kitchen_sequence

label kitchen_sequence:

    scene our_room_non_int

    name "В тот день я так устал. что по приезде сразу лег спать"

    name "А на следующий день я все утро рассказывал родителям о том, что произошло и повторял монгольские слова"

    name "Только вот со мной произошло кое-что странное..."

    scene kitchen_flashback

    if neighbor_approval <= -3:
        
        name "Твари."

    else:

        name "Вот блин"

    name "Опять развели бардак на столе"

    name "Неужели так сложно за собой убрать?"

    name "Эх, ну приятного аппетита мне"

    play sound loud_screech
    scene kitchen_open_door

    name "???"

    name "Это что... МЫШИ???"

    name "Я точно не сплю???"

    play sound relief
    $ renpy.pause(3.0, hard=True)

    "Вы ущипнули себя, но ничего не произошло"

    menu is_it_dream:

        "Это не сон...":
            
            $ is_dream = False

        "Ущипнуть себя еще раз":

            $ is_dream = True



label crossword_imba:

    python:
        wordlist = [
            ["ПРИВЕТ", "Приветствие"],
            ["МИР", "Планета Земля"],
            ["КОТ", "Домашнее животное, мяукает"],
            ["СОБАКА", "Друг человека"],
            ["СОЛНЦЕ", "Светит днем"],
            ["ЛУНА", "Светит ночью"],
            ["ПРОГРАММА", "Код для компьютера"],
            ["ПИТОН", "Язык программирования (змея)"],
            ["РЕНПИ", "Движок для визуальных новелл"],
            ["ИГРА", "Развлечение"]
        ]
        
        crossword_game = Crossword_shape(rows=12, cols=12)
        crossword_game.generate_new(wordlist, time_permitted=3.0)

    call screen final_crossword

    while True:
        call screen final_crossword
        
        if _return == "new":
            python:
                crossword_game.generate_new(wordlist, time_permitted=3.0)




        














    


        

    


















    






    






               


                #show screen notebook_button
                #$ show_notebook_button = True
                    #at transform:
                        #alpha 0.0
                        #linear 0.5 alpha 1.0

#label dictionary:

    #show notebook



            


        
        # это первая часть считывания инпута от мышки пользователя
        # оно тип ищет позицию мышки и потом мы должны проверять если она находится в таком то диапазоне
        # то при нажатии у нас открывается такое то меню
        # и еще было бы круто подсвечивать интерактивный предмет но я пока не понял как оно делается
       
    #init python:
            
        #def getMousePosition():
                
            #import pygame
            #x, y = pygame.mouse.get_pos()
            #store.mouse_x = x
            #store.mouse_y = y
                
        
     
    # mouse_pressed = renpy.mouse.get_mouse_button_down_1
    #if mouse_pressed == True and x == 12 and y == 12:

        #$ counter_table = 0
            
        #label table:

            #$ counter_table = 0
                
            #name "Мдаа...
                
            #Ну и пылища.. Кружка со следами кофе... Банка из-под энергетика...
                
            #Кто-то явно пытался сосредоточиться в последний момент перед дедлайном...
                
            #Какие-то записки и скомканные бумажки...
                
            #Наверняка среди них есть заметка “НЕ ЗАБУДЬ СДЕЛАТЬ УБОРКУ ПЕРЕД ПРИЕЗДОМ НОВОГО СОСЕДА” 
                
            #...
                
            #Надеюсь..."

            #$ counter_table += 1

        #if counter_table > 1 and mouse_pressed == True and x == 12 and y == 12:
                 
            #name "Стоп...
                
            #Он забыл ноутбук??!"
            
        
        
        #if mouse_pressed == True and x == 24 and y == 24:

            #label window:


            







    



        











    return
