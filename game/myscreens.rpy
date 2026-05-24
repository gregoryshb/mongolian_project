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

    layer 'overlay'
    add "hallway.png"





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




