#Персонажи наши

define rat1 = Character("Крыса побольше", kind = bubble, image = 'rat', color = '#706d65')

define rat2 = Character('Крыса поменьше', kind = bubble, image = 'rat', color = '#706d65', what_bold=True)

define name = Character("[name_name]", dynamic=True, image='None', color='#ac1234')



image hp_high = "hp_high.png"
image hp_medium = "hp_medium.png"
image hp_low = "hp_low.png"



default name_hp = 3
default rat_attack = 1



screen hp_screen():

    frame:
        xalign 0.02
        yalign 0.02
        padding (15, 15)

        vbox:
            spacing 10

            text "HP: [name_hp]" size 40 color "#ffffff"

            if name_hp == 3:
                add "hp_high"

            elif name_hp == 2:
                add "hp_medium"

            else:
                add "hp_low"

label start:

    
    python:
        name = renpy.input("Введите ваше имя", "", length = 20)
        name = name.strip()

        if not name:
            name = "Студент"

        if name == 'vantral':
            renpy.jump("start")
            


label rats_game:

    scene black

    $ name_hp = 3
    $ rat_attack = 1

    show screen hp_screen

    "На тебя нападают крысы!"

    jump rat_round



label rat_round:

    if rat_attack > 3:
        jump rats_win

    if name_hp <= 0:
        jump rats_lose

    scene black

    show rat
    with dissolve
    show rat_attack1
    with dissolve
    show rat_attack2

    # Разные тексты перед атакой
    if rat_attack == 1:
        rat1 "Вот как так получилось, что люди кормят других адгуус (животные), а нас - нет!!"
        rat1 "Мы, харх, честный народ."
        rat2 "И тоже заслуживаем уважения."
    elif rat_attack == 2:
        rat1 "Вот скажи, эта тахиа, что несет өндөг, чем она лучше нас?"
        rat1 "А үнээ, она же только траву жует!"
        rat2 "Ещё сүү дает."
        rat1 "Это не важно!!!"
        rat1 "Муур вообще ничего полезного не делает!! Она только убивает и ест бедных харх!!"
        rat2 "Это правда."
    else:  # rat_attack == 3
        rat1 "А эта.. нохой, она что? Лает постоянно и всё!"
        rat1 "И всех их человек кормит, а харх (крысы) остаются голодными."
        rat2 "Мы вдвоем всю жизнь перебиваемся остатками пищи, но так и не пробовали сыра."
        rat1 "Заткнисссььь!!!!"

    "Атака крыс #[rat_attack]!"

    "Чем отбиться?"

    menu:

        "Яйцо":

            "Крысам это не понравилось."

            $ name_hp -= 1

        "Молоко":

            "Крысы стали ещё злее."

            $ name_hp -= 1

        "Сыр":

            "Правильно! Крысы отвлеклись на сыр."

    if name_hp <= 0:
        jump rats_lose

    $ rat_attack += 1

    jump rat_round


label rats_win:

    show rat

    hide screen hp_screen

    rat1 "Ну ты погоди!!! Мы ещё вернемся!! С местью!!!!!!!!!!!!!!!!!!!!!!!!!!"
    rat2 "Пока."
    name "Мда уж, это было что-то странное"
    name "Зато записал новые слова.."
    name "Интересно, какой сон мне приснится, если вот это была реальность"

    return


label rats_lose:

    show rat

    hide screen hp_screen

    rat1 "Говорили же! Вся еда должна достаться нам!!"
    rat2 "Еда."
    rat1 " А то эти люди явно неправильно используют ресурсы. Вот этого мы вообще за пять секунд победили?"
    rat2 "Минут."
    rat1 "Заткнись- Что ты ел?? Явно не кашу!"


    return


return