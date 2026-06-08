default clicks_table = 0
default clicks_window = 0
default clicks_board = 0

screen our_room():

    #ну тут понятно пишет текст
    #text "text"

    #добавляет картинку
    #add "image.png"

    #нажимаешь на картинку и она че то делает
    #imagebutton

    #есть картинка и внутри можно создать всякие кликабельные штуки
    imagemap:
        
        ground "our_room.png"
        hover "our_room_hover.png"
        
        hotspot (260, 107, 592, 596) action [SetVariable("clicks_table", clicks_table + 1), Jump("table")]
        hotspot (774, 0, 484, 273) action [SetVariable("clicks_window", clicks_window + 1), Jump("window")]
        hotspot (1459, 27, 373, 454) action [SetVariable("clicks_board", clicks_board + 1), Jump("board")]

transform slide_in:
    xpos -350
    linear 0.3 xpos 0

transform slide_out:
    xpos 0
    linear 0.3 xpos -350


default notebook_open = False
default notebook_animation = None
default notebook_is = False
default notebook_dictionary = ""

screen notebook:
    layer 'overlay'

    if notebook_is:

        imagebutton:
       
            idle 'notebook_button.png'
            hover 'notebook_button.png'
            xpos 20
            ypos 300
            action ToggleVariable("notebook_open")
    
        if notebook_open and notebook_is:
            frame: #(0, 0, 270, 815)
                xpos 0
                ypos 0
                xsize 270
                ysize 815
                background '#ffffff'

                at slide_in

                vbox:
                    spacing 10
                    xfill True

                    text "Мой блокнот" size 24 color "#ffd700" xalign 0.5
                    null height 10
                
                    frame:
                        background "#2a2a2a"
                        xfill True
                        ysize 600
                        padding (10, 10)
                        text notebook_dictionary size 14 color "#ffffff"
                
                    textbutton "Закрыть":
                        action SetVariable("notebook_open", False)
                        xalign 0.5
                        background "#444"
                        hover_background "#666"

        elif notebook_is and not notebook_open:
            frame: 
                xpos -270
                ypos 0
                xsize 270
                ysize 815

                at slide_out

screen note_mongol:

    add 'zapiska_rashifrovka.png'

screen notebook_pages_1():

    zorder 1000

    if notebook_page == 1:
        imagemap:
            ground "pronouns.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 2)

    elif notebook_page == 2:
        imagemap:
            ground "verbs.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 3)

    elif notebook_page == 3:
        imagemap:
            ground "furniture.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 4)

    elif notebook_page == 4:
        imagemap:
            ground "preposition.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 5)

    elif notebook_page == 5:
        imagemap:
            ground "food.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 6)

    elif notebook_page == 6:
        imagemap:
            ground "directions.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 7)
    
    elif notebook_page == 7:
        imagemap:
            ground "animals.png"

            textbutton "Вперед":
                action SetVariable("notebook_page", 1)

screen blackbg:
    #zorder -100
    add 'blackbg.png'

screen mongolia:

    add 'mongolia_scenery.png'

screen hallway:

    add "hallway.png":
        fit "cover"

screen our_room_non_int:
    #zorder -100
    add "our_room.png"

screen dubki_big:

    add "dubkibig.png"

screen shop_outside:

    add "shop_outside.png"

screen shop_inside:

    add "shop_inside.png":
        fit "cover"

screen shop_inside_bg:

    add "shop_inside_bg.png"
    add "spisok_pipisok.png"

screen kitchen_flashback:

    add 'kitchen_flashback.png'

screen secret_ending:

    text "ВЫ НАШЛИ СЕКРЕТНУЮ КОНЦОВКУ!":
       
        xalign 0.5
        yalign 0.5
        size 60
        color "#ffffff"

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

screen final_crossword():

    modal True

    default game = crossword_game
    default yes_complete = False

    timer 0.1 repeat True action If(
        game.is_complete() and not yes_complete, 
        true=[SetScreenVariable("yes_complete", True), Function(renpy.notify, "Кроссворд разгадан! УРА!!!"), Return("complete")], 
        false=NullAction()
    )

    #key "dismiss" action NullAction()
    #key "rollback" action NullAction()
    #key "game_menu" action NullAction()
    #key "K_RETURN" action NullAction()
    #key "K_ESCAPE" action NullAction()
    #key "K_SPACE" action NullAction()
    
    key "K_UP" action Function(game.moves, -1, 0) 
    key "K_DOWN" action Function(game.moves, 1, 0) 
    key "K_RIGHT" action Function(game.moves, 0, 1) 
    key "K_LEFT" action Function(game.moves, 0, -1) 
    key "K_LSHIFT" action Function(game.change_direction)
    
    key 'K_BACKSPACE' action Function(game.backspace)

    key "K_a" action Function(game.input_letter, 'ф')
    key "K_b" action Function(game.input_letter, 'и')
    key "K_c" action Function(game.input_letter, 'с')
    key "K_d" action Function(game.input_letter, 'в')
    key "K_e" action Function(game.input_letter, 'у')
    key "K_f" action Function(game.input_letter, 'а')
    key "K_g" action Function(game.input_letter, 'п')
    key "K_h" action Function(game.input_letter, 'р')
    key "K_i" action Function(game.input_letter, 'ш')
    key "K_j" action Function(game.input_letter, 'о')
    key "K_k" action Function(game.input_letter, 'л')
    key "K_l" action Function(game.input_letter, 'д')
    key "K_m" action Function(game.input_letter, 'ь')
    key "K_n" action Function(game.input_letter, 'т')
    key "K_o" action Function(game.input_letter, 'щ')
    key "K_p" action Function(game.input_letter, 'з')
    key "K_q" action Function(game.input_letter, 'й')
    key "K_r" action Function(game.input_letter, 'к')
    key "K_s" action Function(game.input_letter, 'ы')
    key "K_t" action Function(game.input_letter, 'е')
    key "K_u" action Function(game.input_letter, 'г')
    key "K_v" action Function(game.input_letter, 'м')
    key "K_w" action Function(game.input_letter, 'ц')
    key "K_x" action Function(game.input_letter, 'ч')
    key "K_y" action Function(game.input_letter, 'н')
    key "K_z" action Function(game.input_letter, 'я')
    
    key "K_LEFTBRACKET" action Function(game.input_letter, 'х')
    key "K_RIGHTBRACKET" action Function(game.input_letter, 'ъ')
    key "K_SEMICOLON" action Function(game.input_letter, 'ж')
    key "K_QUOTE" action Function(game.input_letter, 'э')
    key "K_COMMA" action Function(game.input_letter, 'б')
    key "K_PERIOD" action Function(game.input_letter, 'ю')
    key "K_SLASH" action Function(game.input_letter, 'ё')

    frame: 
        background '#000000'
        xfill True
        yfill True
        padding (20, 20)

        vbox:
            spacing 20
            xalign 0.5

            text 'ФИНАЛЬНОЕ ИСПЫТАНИЕ' size 48 color '#ffffff' xalign 0.5

            $ num_now, word_now, clue_now = game.active_word_info()
            
            frame:
                background "#34495e"
                padding (10, 10)
                xfill True
                if clue_now:
                    text f"{num_now}. {clue_now}" size 20 color "#f1c40f" xalign 0.5
                else:
                    text "Выберите слово, чтобы увидеть его определение" size 18 color "#95a5a6" xalign 0.5
            
            hbox:
                spacing 20
                xalign 0.5
                
                # Сетка
                frame:
                    background "#34495e"
                    padding (10, 10)
                    
                    grid game.rows game.cols:
                        spacing 2
                        for row in range(game.rows):
                            for col in range(game.cols):
                                $ cell_val = game.correct_grid[row][col] if game.correct_grid else ' '
                                $ user_val = game.player_grid[row][col] if game.player_grid else ''
                                $ is_selected = (row == game.selected_row and col == game.selected_col)
                                $ is_active_word = game.is_in_active_word(row, col)
                                $ is_correct = game.check_cell(row, col)
                                
                                if cell_val == ' ':
                                    frame:
                                        background "#1a252f"
                                        xsize 35 ysize 35
                                else:
                                    button:
                        
                                        background (
                                            "#e74c3c" if is_selected else
                                            "#f1c40f" if is_active_word else
                                            "#2ecc71" if (user_val and is_correct) else
                                            "#ecf0f1"
                                        )
                                        xsize 35 ysize 35
                                        action [
                                            Function(game.moves, row - game.selected_row, col - game.selected_col),
                                            If(is_selected, true=Function(game.change_direction))
                                        ]
                                        
                                        text (user_val if user_val else "") size 22 color "#2c3e50" yalign 0.5 xalign 0.5 font "Pangolin-Regular.ttf"

                frame:
                    background "#34495e"
                    padding (15, 15)
                    xsize 320
                    vbox:
                        spacing 10
                        
                        text "Список слов:" size 18 color "#ffffff" bold True
                        
                        viewport:
                            scrollbars "vertical"
                            xsize 300
                            ysize 350
                            
                            vbox:
                                spacing 5
                                for i, w_data in enumerate(game.words):
                                    $ w_text = w_data[0]
                                    $ w_clue = w_data[1]
                                    $ is_done = game.check_word(w_text)
                                        
                                  
                                    if is_done:
                                        text f"{i+1}. {w_text} ✓" color "#2ecc71" bold True
                                    else:
                                        text f"{i+1}. {w_clue}" color "#ecf0f1"
                                        
                        null height 20
                        
                        textbutton "Новая игра":
                            xalign 0.5
                            text_color "#fff"
                            background "#e74c3c"
                            action Return("new")

screen validation(message, yes_action, no_action=None):
    modal True
    zorder 100
    frame:
        xysize (400, 200)
        xalign 0.5 yalign 0.5
        background "#2c3e50"
        vbox:
            spacing 20
            xalign 0.5 yalign 0.5
            text message size 24 color "#fff" xalign 0.5
            hbox:
                xalign 0.5
                textbutton "Да" action yes_action
                if no_action:
                    textbutton "Нет" action no_action



                   
                











































    #imagemap:

        #ground "notebook.png"
        #hover "notebook.png"

        #hotspot (0, 0, 1, 1)







#default show_menu_button = False

#screen notebook_button:
    
    #layer 'overlay'

    #if show_notebook_button:
   
        #imagebutton:
       
            #idle 'notebook_button.png'
            #hover 'notebook_button_hover.png'
            #xpos 1800
            #ypos 150
            #action jump('dictionary')



