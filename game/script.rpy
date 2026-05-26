#Персонажи наши

define kostya = Character('Костя', image = 'kostya', color="#c8ffc8")

image kostya_base = 'kostya_base.png'

define neighbor = Character('Игнат', image = 'neighbor', color= '#235fe4')
define neighbor_secret = Character('???', image = 'neighbor', color = '#235fe4')

image neighbor_base = 'neighbor_base.png'
image neighbor_smile = 'neighbor_smile.png'
image neighbor_surprise = 'neighbor_smile.png'
image neighbor_sad = 'neighbor_sad.png'
image neighbor_joy = 'neighbor_joy.png'
image neighbor_phone = 'neighbor_phone.png'
image neighbor_smart = 'neighbor_smart.png'
image neighbor_glasses = 'neighbor_glasses.png'

define dmitriev = Character('Дмитриев', kind = bubble, image = 'dmitriev', color = '#abc342')

image dmitriev_base = 'dmitriev_base.png'

define rat_1 = Character("Крыса побольше", kind = bubble, image = 'bubble.png', color = '#706d65')

define rat_2 = Character('Крыса поменьше', kind = bubble, image = 'bubble.png', color = '#706d65')

define player = Character("[name]", image = 'None', color = '#ac1234') 

## Заранее извиняемся перед всеми женщинами!!!
## Нам пришлось сделать персонажа мужчиной, потому что он живет в мужском общежитии
## Кроме того, опыт главного героя основан на жизни члена нашей команды, который к сожалению, мужчина

define dad = Character('Папа', image = 'dad')

image dad_base = 'dad_base.png'
image dad_happy = 'dad_happy.png'

define mom = Character('Мама', image = 'mom')

image mom_base = 'mom_base.png'
image mom_happy = 'mom_happy.png'

#Начало игры:
label start:

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
    
    scene blackbg
    #play music snitch volume 0.25 fadein 1.0

    name "Ивушки™ - студенческое общежитие, находящееся во власти Университета™"
    
    name "По слухам, настоящий ад на Земле, условия почти как в тюрьме и полное отсутствие человеческой жизни"
    
    name "И вот сюда мне довелось попасть в первый год учебы…"

    play sound flashback_start 
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

    play sound flashback_end
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

    #show neighbor_phone
    #play music neighbor_theme fadein 1.0

    neighbor_secret "…нет, нет, нет, я тебя не понимаю! Можешь повторить еще раз?"
    
    neighbor_secret "Ааа, ты неправ! В адыгейском же всего три гласных: а, а и а. Чи дэмий яриад байна!"

    name '(Что за бред он несет…)'

    neighbor_secret 'Хүлээгээрэй, би чам руу залгах болно'

    #hide neighbor_phone
    #show neighbor_surprise
    #play music neighbor_theme_alt

    neighbor_secret "???"
    
    neighbor_secret "А ты..?"

    name 'Я [name], видимо мы будем соседями'

    neighbor_secret 'А...'

    #hide neighbor_surprise
    #show neighbor_smile
    #play music neighbor_theme

    neighbor_secret '(Что-то не помню я такого, но пусть живет)'
    
    neighbor_secret "Ну.. тогда будем знакомы, я Игнат"

    #hide neighbor_smile
    #show neighbor_base

    neighbor 'Извини, я как-то не прибрался к твоему приходу…'

    #hide neighbor_base
    #show neighbor_smile

    neighbor 'Я совершенно забыл об этом'

    #hide neighbor_smile
    #show neighbor_smart

    neighbor 'Смотри, я сплю на этой ор, получается эта ор твоя'

    #hide neighbor_smart
    #show neighbor_surprise

    neighbor 'Ой, сейчас!'
    
    neighbor 'На этой…'
    
    neighbor '…'
    
    neighbor 'Точно, кровати!'
    
    neighbor 'Извини, я немного подзабыл этот язык и периодически могу переключаться на монгольский.' 
    
    neighbor 'В последнее время на нем говорю только о науке, а не в обычной жизни'

    #play sound phone_ring
    #hide neighbor_surprise
    #show neighbor_smile

    neighbor 'Ох, мне пора бежать!!!'
    
    neighbor 'Надеюсь, разберешься как тут что'
    
    neighbor 'Увидимся вечером!'

    #hide neighbor_smile

    menu first_impression_menu: 
        name "Это было..."

        "Странно...":
            name "Почему он вообще выбрал этот язык! Он же не в Монголии живет.. "

        "Круто!":
            name "Интересно, почему он выбрал именно этот язык?!"

label after_first_impression:
    name "Что ж, почему бы не осмотреться получше, раз уж есть возможность"

    label look_around:

        call screen our_room


        
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
