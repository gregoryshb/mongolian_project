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


#screen test:

    #layer 'overlay'
    #add "notebook.png"

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

screen hallway:

    add "hallway.png"

screen our_room_non_int:

    add "our_room.png"

screen dubki_big:

    add "dubkibig.png"

screen shop_outside:

    add "shop_outside.png"

screen shop_inside:

    add "shop_inside.png"

screen shop_inside_bg:

    add "shop_inside_bg.png"
    add "shopping_list.png"

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

python:

    from operator import itemgetter
    from collections import defaultdict

    class Crossword:
        
        def __init__ (self, rows, cols, empty = ' ', available_words = []):

            self.rows = rows
            self.cols = cols
            self.empty = empty
            self.available_words = available_words
            self.let_coords = defaultdict(list)
            self.original_words = available_words.copy()

        def prep_grid_words(self):

            self.current_wordlist = []
            self.let_coords.clear()
            self.grid = [[self.empty]*self.cols for i in range(self.rows)]
            self.first_word(self.available_words[0][0])

        def compute_crossword(self, time_permitted = 1.0):

            self.best_wordlist = []
            wordlist_length = len(self.available_words)
            time_permitted = float(time_permitted)
            start_full = float(time.time())

            while (float(time.time()) - start_full) < time_permitted:

                self.prep_grid_words()
                for word in self.available_words():
                    
                    if word[0] not in [w[0] for w in self.current_wordlist]:
                        
                        self.add_words(word)

                if len(self.current_wordlist) > len(self.best_wordlist):

                    best_wordlist = list(self.current_wordlist)
                    self.best_grid = [row[:] for row in self.grid]

                if len(self.best_wordlist) == wordlist_length:
                    break
            
            return self.best_grid, self.best_wordlist

        def 

















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




