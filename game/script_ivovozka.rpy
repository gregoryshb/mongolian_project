define kostya = Character('Костя', image = 'kostya', color="#c8ffc8", slow_cps = 20)
define neighbor = Character('Игнат', image = 'neighbor', color= '#235fe4', slow_cps = 20)
define player = Character("[name]", image = 'None', color = '#ac1234', slow_cps = 20) 
define busstranger = Character('???', image = 'bus_stranger', color='#235fe4')



screen number_controls():

    key "K_1" action Jump("lose")
    key "K_2" action Jump("lose")
    key "K_3" action Jump("lose")
    key "K_4" action Jump("tupik")


screen number_controls_tupik():

    key "K_1" action Jump("yama")
    key "K_2" action Jump("lose")
    key "K_3" action Jump("lose")
    key "K_4" action Jump("lose")



screen number_controls_yama():

    key "K_1" action Jump("lose")
    key "K_2" action Jump("win")
    key "K_3" action Jump("lose")
    key "K_4" action Jump("lose")

#Начало игры:
label start:

    
    python:
        name = renpy.input("Введите ваше имя", "", length = 20)
        name = name.strip()

        if not name:
            name = "Студент"

        if name == 'vantral':
            renpy.jump("start")
            

    scene bg room

    play music snitch volume 0.75

    name "Ах, первый день в общаге!"

    name "Поступая сюда, я понимал, что не смогу жить в квартире как мои богатые друзья"

    name 'И вот, я здесь, студенческий городок "Ивушки"'

    name 'Это будет долго...'

    show neighborbase

    neighbor 'Привет-привет!'

jump ivovozka


label ivovozka:

name "Отлично, а теперь в университет"

name "По коням! Точнее по ивовозкам!"

name "..Или как там называют автобус из Ивушек.."


scene bus

name "Пока еду в университет, попробую узнать какие-то новые слова на монгольском"
name "Так.."
name "направо – “баруун тийш”"
name "налево – “зүүнш”"
name "назад – “буцаан”"
name "вперед – “урагш”"
name "Теперь нужно только заучить"

show busstranger

busstranger "Водителю плохо!"
busstranger "Кто-нибудь, возьмите управление на себя, я врач, я приведу его в чувство"
busstranger "Эй, ты, парень! Водить умеешь?"
name "Да."
busstranger "Ну вот и иди к рулю!! Быстро!!!"

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
show busstranger
busstranger "Нормально. Точнее не очень, но жить будет."
name "Ну ладно, мне пора в вуз, вы уж дальше сами!"

