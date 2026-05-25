#Персонажи наши

define kostya = Character('Костя', image = 'kostya', color="#c8ffc8")

image kostyabase = 'kostyabase.png'

define neighbor = Character('Сосед', image = 'neighbor', color= '#235fe4')

image neighborbase = 'neighborbase.png'

define dmitriev = Character('Дмитриев', kind = bubble, image = 'dmitriev', color = '#abc342')

image dmitrievbase = 'dmitrievbase.png'

define rat1 = Character("Крыса побольше", kind = bubble, image = 'rat', color = '#706d65')

#define rat2 = Character('Крыса поменьше', kind = bubble, color = '#706d65')

define name = Character("[name]", image = 'None', color = '#ac1234') 

define busstranger = Character('???', image = 'busstranger', color='#235fe4')

image hp_high = "hp_high.png"
image hp_medium = "hp_medium.png"
image hp_low = "hp_low.png"



default player_hp = 3
default rat_attack = 1



screen hp_screen():

    frame:
        xalign 0.02
        yalign 0.02
        padding (15, 15)

        vbox:
            spacing 10

            text "HP: [player_hp]" size 40 color "#ffffff"

            if player_hp == 3:
                add "hp_high"

            elif player_hp == 2:
                add "hp_medium"

            else:
                add "hp_low"


label start:

    "Игра началась."

label rats_game:

    scene black

    $ player_hp = 3
    $ rat_attack = 1

    show screen hp_screen

    "На тебя нападают крысы!"

    jump rat_round



label rat_round:

    if rat_attack > 3:
        jump rats_win

    if player_hp <= 0:
        jump rats_lose

    scene black

    show rat
    with dissolve
    show rat_attack1
    with dissolve
    show rat_attack2

    # Разные тексты перед атакой
    if rat_attack == 1:
        "Крысы с шумом выбегают из темноты!"
    elif rat_attack == 2:
        "Крысы окружают тебя и злобно пищат!"
    else:  # rat_attack == 3
        "Главная крыса готовится к прыжку!"

    "Атака крыс #[rat_attack]!"

    "Чем отбиться?"

    menu:

        "Яйцо":

            "Крысам это не понравилось."

            $ player_hp -= 1

        "Молоко":

            "Крысы стали ещё злее."

            $ player_hp -= 1

        "Сыр":

            "Правильно! Крысы отвлеклись на сыр."

    if player_hp <= 0:
        jump rats_lose

    $ rat_attack += 1

    jump rat_round


label rats_win:

    scene black

    hide screen hp_screen

    "Ты пережил все атаки крыс!"

    return


label rats_lose:

    scene black

    hide screen hp_screen

    "Крысы тебя победили..."

    return


return