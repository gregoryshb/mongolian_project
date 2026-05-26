define dmitriev = Character('ИИИ', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_secret = Character('???', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_full = Character('Иванов Иван Иванович', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_surname = Character('Иван Иванович', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define dmitriev_short = Character('ИИ', image = 'dmitriev', color = '#abc342', slow_cps = 20)
define galina = Character('Галина Олеговна', image = 'galina', color = '#eb23a6', slow_cps = 20)
image dmitriev_base = 'dmitriev_base.png'
default dmitriev_count = 0
image blackbg = 'blackbg.png'
define name = Character("[name_name]", dynamic=True, image='None', color='#ac1234')

label start:

    
    python:
        name = renpy.input("Введите ваше имя", "", length = 20)
        name = name.strip()

        if not name:
            name = "Студент"

        if name == 'vantral':
            renpy.jump("start")



label shop_line:

    scene shop_inside:
        fit "cover"

    show dmitriev_base:
        xpos 50
        ypos 50

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
    show dmitriev_rage:
        xpos 50
        ypos 50

    dmitriev "И когда я их {b}спросил{/b} про ХРИСТИАНИЗАЦИЮ РУСИ! И про {i}{color=#d12d21}стрельцов!{/color}{/i} Они {color=#d12d21}НЕ ответили!!{/color}"

    name "..."

    dmitriev "ИИИ: А вот {color=#d12d21}ДАВАЙТЕ{/color} я у ВАС {b}СПРОШУ{/b}? Я вам {color=#d12d21}ВОПРОС, А ВЫ МНЕ — ОТВЕТ!{/color}"

    dmitriev "{color=#d12d21}{b}ВЫ СОГЛАСНЫ????{/b}{/color}"

    menu:

        "Да":

            name "Что ж... Давайте"

            hide dmitriev_rage
            show dmitriev_base:
                xpos 50
                ypos 50

            dmitriev "{color=#d12d21}Отлично!!!!!!{/color}"

            jump dmitriev_minigame

        "Нет":

            name "Наверное, откажусь"

            hide dmitriev_rage
            show dmitriev_base:
                xpos 50
                ypos 50

            dmitriev "Приму этот ответ за да!"

            jump dmitriev_minigame

label dmitriev_minigame:


    dmitriev "Вот {b}СКАЖИТЕ{/b} мне пожалуйста.."

    scene dmitriev_moloko
    show dmitriev_base:
        xpos 50
        ypos 50

    dmitriev "А вот {b}ПОЧЕМУ{/b} в {color=#d12d21}МОСКОВСКОЙ РУСИ{/color}  было  возможно более  или менее {color=#d12d21}{i}мирное{/i}{/color} сосуществование {b}разных религий{/b}, а на современном Московской Руси {color=#d12d21}{b}ЗАПАДЕ{/b}{/color} это никак {color=#d12d21}{b}не получалось{/b}{/color}?"

    name "Так, ну мне этот разговор не нравится"

    name "Лучше уж я буду делать вид, что понимаю, о чем он говорит, и что-нибудь говорить так, чтобы он не понял, о чем я."

    name "На монгольском"

    name "А если он испугается, как будто бы мне это поможет.. он перестанет со мной говорить."

    label minigame_moloko:
    show dmitriev_base:
        xpos 50
        ypos 50
    
    menu:

        "сүү":

            jump minigame_hleb

        "бяслаг":

            jump minigame_moloko

        "нүгэл":

            $ dmitriev_count += 1

            jump minigame_hleb


    label minigame_hleb:


    scene dmitriev_hleb
    show dmitriev_base:
        xpos 50
        ypos 50

    dmitriev "{b}Что такое — {color=#d12d21}история{/color} или России, или любой иной страны?{/b}"
    
    menu:

        "тахих":

            $ dmitriev_count += 1

            jump minigame_iaico

        "талх":

            jump minigame_iaico

        "өндөгрт":

            jump minigame_hleb  
       
    label minigame_iaico:

    scene dmitriev_iaico
    show dmitriev_base:
        xpos 50
        ypos 50

    dmitriev "{b}И — вообще: населения мира (берите любую страну!) России, СССР, РСФСР, РФ…. — оно разве гомогенно?{/b}"
    
    menu:

        "өндөг":

            jump dmitriev_win

        "диваажин":

            $ dmitriev_count += 1

        "гоймон":

            jump minigame_iaico 



if dmitriev_count == 3:
    jump dmitriev_secret
else:
    jump dmitriev_win

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

    scene blackbg
    $ renpy.pause(5.0, hard = True)

    jump mongolia

label mongolia:

    scene mongolia_scenery
    #play music mongol_song

    "Пять лет спустя"

    name "Вот так я и стал паломником в Монголии"

    name "Я путешествую со своим наставником, Ивановым Иваном Ивановичем"

    name "Вместе мы обучаем людей христианским ценностям и традициям."

    name "Я не жалею о том, что ушел из Университета, ведь я нашел свой смысл в таком образе жизни"

    name "Правда немного жаль, что мы так и не подружились с Игнатом..."

    name "Но это сейчас не важно, мне нужно идти, дело праведное не ждёт."

    $ renpy.pause(5.0, hard = True)

    window hide

    pause 5.0

    call screen secret_ending

    $ renpy.pause(5.0, hard = True)

    jump main_menu

label dmitriev_win:

    dmitriev "Что ж, я '{color=#d12d21}{i}ВАШУ{/color}{/i} {b}ТОЧКУ ЗРЕНИЯ{/b} понял"

    dmitriev "Но я вам, конечно, {color=#d12d21}{b}советую{/color}{/b} прийти на мою {b}{i}лекцию.{/b}{/i}"

    dmitriev "ПОРАССУЖДАЕМ над идеей Достоевского русского - ВСЕЧЕЛОВЕКА"

    name "С-спасибо, но нет"

    dmitriev "А вот и {color=#d12d21}{i}моя очередь{/color}{/i}"

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

    scene blackbg

    $ renpy.pause(5.0, hard=True)
