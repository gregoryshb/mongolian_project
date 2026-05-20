#Персонажи наши

define kostya = Character('Костя', image = 'kostya', color="#c8ffc8")

image kostyabase = 'kostyabase.png'

define neighbor = Character('Сосед', image = 'neighbor', color= '#235fe4')

image neighborbase = 'neighborbase.png'

define dmitriev = Character('Дмитриев', kind = bubble, image = 'dmitriev', color = '#abc342')

image dmitrievbase = 'dmitrievbase.png'

define rat1 = Character("Крыса побольше", kind = bubble, color = '#706d65')

define rat2 = Character('Крыса поменьше', kind = bubble, color = '#706d65')

define player = Character("[name]", image = 'None', color = '#ac1234') 

#Начало игры:
label start:

    menu choose_your_name:
    
    python:
        name = renpy.input("Введите ваше имя", "", length = 20)
        name = name.strip()

        if not name:
            name = "Студент"

        if name == 'vantral':
            label start
            

    scene bg room

    play music snitch volume 0.75

    name "Ах, первый день в общаге!"

    name "Поступая сюда, я понимал, что не смогу жить в квартире как мои богатые друзья"

    name 'И вот, я здесь, студенческий городок "Ивушки"'

    name 'Это будет долго...'

    show neighborbase

    neighbor 'Привет-привет!'



    return
