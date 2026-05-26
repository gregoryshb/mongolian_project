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
        hover "our_romm.png"
        hotspot (0, 0, 1920, 1080) action Jump("look_around")

