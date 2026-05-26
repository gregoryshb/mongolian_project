define rat_1 = Character("Крыса побольше", kind = bubble, image = 'rat', color = '#706d65')

define rat_2 = Character('Крыса поменьше', kind = bubble, image = 'rat', color = '#706d65', what_bold=True)

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


define name = Character("[name_name]", dynamic=True, image='None', color='#ac1234')



image hp_high = "hp_high.png"
image hp_medium = "hp_medium.png"
image hp_low = "hp_low.png"



default name_hp = 3
default rat_attack = 1
default is_dream = 0

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

#play sound loud_screech
    scene kitchen_open_door
    show rat

    name "???"

    name "Это что... МЫШИ???"

    name "Я точно не сплю???"

    #play sound relief
    #$ renpy.pause(3.0, hard=True)

    "Вы ущипнули себя, но ничего не произошло"

    menu is_it_dream:

        "Это не сон...":
            
            $ is_dream -= 1

        "Ущипнуть себя еще раз":

            $ is_dream += 1

name "Здравствуйте.."
rat_1 "Привет, сопляк! Что, испугался? Вхахаха"
name "Нужно просто протереть глаза"

#темный фон на некоторое время, потом возвращается
#в следующий раз крысы уже ближе - на столе

rat_1 "Ну и?"
menu:
        "Я схожу с ума..":
            
            $ is_dream -= 1

        "Это сон, это сон, это сон":

            $ is_dream += 1


if is_dream <= 0:
        rat_1 "Психиатру это скажи, мы тут при чем?"
        rat_1 "У тебя сыра (монг) не найдется?"
        name "Монг? Аа, это сыр."
        name "А что..?"
        rat_1 "Ответишь - узнаешь"
        name "Нет, сыра вроде нет"

if is_dream >= 1:
        rat_1 "Сейчаааас проверим"
        rat_1 "А ну-ка помоги мне запустить в него зубочисткой!"

#анимация запуска зубочистки

        name "Ай! Больно же."
        rat_1 "Отдашь монг и мы уйдем с миром"
        name "Монг? Аа, это сыр."
        name "А у меня нет сыра.."



rat_1 "А если найдем? Кхехехе"
rat_2 "Найдем. У него есть монг." 
name "Он соседский, я не могу его вам дать!"
rat_2 "Врать плохо."
rat_1 "Лгунишек мы не прощаем. В атаку!!!"

#меняется музыка

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
        rat_1 "Вот как так получилось, что люди кормят других адгуус (животные), а нас - нет!!"
        rat_1 "Мы, харх, честный народ."
        rat_2 "И тоже заслуживаем уважения."
    elif rat_attack == 2:
        rat_1 "Вот скажи, эта тахиа, что несет өндөг, чем она лучше нас?"
        rat_1 "А үнээ, она же только траву жует!"
        rat_2 "Ещё сүү дает."
        rat_1 "Это не важно!!!"
        rat_1 "Муур вообще ничего полезного не делает!! Она только убивает и ест бедных харх!!"
        rat_2 "Это правда."
    else:  # rat_attack == 3
        rat_1 "А эта.. нохой, она что? Лает постоянно и всё!"
        rat_1 "И всех их человек кормит, а харх (крысы) остаются голодными."
        rat_2 "Мы вдвоем всю жизнь перебиваемся остатками пищи, но так и не пробовали сыра."
        rat_1 "Заткнисссььь!!!!"

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

    rat_1 "Ну ты погоди!!! Мы ещё вернемся!! С местью!!!!!!!!!!!!!!!!!!!!!!!!!!"
    rat_2 "Пока."
    name "Мда уж, это было что-то странное"
    name "Зато записал новые слова.."
    name "Интересно, какой сон мне приснится, если вот это была реальность"
    jump neighbor_scene


label rats_lose:

    show rat

    hide screen hp_screen

    rat_1 "Говорили же! Вся еда должна достаться нам!!"
    rat_2 "Еда."
    rat_1 " А то эти люди явно неправильно используют ресурсы. Вот этого мы вообще за пять секунд победили?"
    rat_2 "Минут."
    rat_1 "Заткнись- Что ты ел?? Явно не кашу!"
    jump neighbor_scene


#темный фон, музыка комнаты
label neighbor_scene:
name "И так я целыми днями готовился: к парам, к монгольскому, к парам, к монгольскому..."
name "И вот пришел день n"

scene room

name "Так, [name], соберись. От сегодняшнего дня зависит многое: получить конспект и признание соседа или..."
show neighbor_base
neighbor "О, ты уже встал? Как себя чувствуешь перед тестированием?" 
name "Я готовился к этому достаточно усердно, и мне кажется, что…"
menu  choice:
    "Я готов":
        jump choice_ready
    "Я не готов":
        jump choice_unready

label choice_ready:
    show neighbor_joy
    neighbor "Вот это отличный настрой! Ты прям сайн эр!"
    jump crossword_game

label choice_unready:
    show neighbor_surprise
    neighbor "Ох."
    show neighbor_sad
    neighbor "Понимаю, мне тоже всегда было очень страшно и тревожно перед любыми событиями."
    neighbor "Поэтому точно могу дать тебе пару советов для успокоения нервов."
    show neighbor_glasses
    neighbor "Тот конспект, который ты хочешь именно с того времени. Когда я осознал, что могу делать вещи только для себя и в силу своих возможностей."
    show neighbor_joy
    neighbor "Тогда жизнь открылась для меня с новой стороны. Учиться и узнавать таких же, как я, людей, жить в своё удовольствие.."
    neighbor "Я надеюсь, что и у тебя будет всё то же самое. С конспектом или без него."
    neighbor  "Надеюсь теперь ты чувствуешь себя лучше по этому поводу."
    name "Да, спасибо."
    jump crossword_game


label crossword_game:
show neighbor_glasses
neighbor "Перед тем, как мы начнем, позволь рассказать тебе правила."
neighbor "Я выдам тебе кроссворд со словами, которые ты учил. На него у тебя будет 10 минут."
show neighbor_smart
neighbor "Определения будут на русском, а слова, естественно, на монгольском. Всё, что тебе нужно будет сделать - вписать их в слоты. В каждой клеточке по одной букве."
neighbor "Итак, начнем."

#музыка - какая-то традиционная монгольская
#мини игра
