# -*- coding: utf-8 -*-
init python:
    mods["Sister_index"] =  u"{font=fonts/timesi.ttf}{size=40}"Sister" Project{/size}{/font}"

    def make_sprite_timed(image):
        return ConditionSwitch(
            "persistent.sprite_time == 'sunset'",
            im.MatrixColor(
                image,
                im.matrix.tint(0.94, 0.82, 1.0) # При свете дня...
            ),
            "persistent.sprite_time == 'night'",
            im.MatrixColor(
                image,
                im.matrix.tint(0.63, 0.78, 0.82) # Во тьме ночной...
            ),
            True,
            image # Но на случаи когда ни туда ни сюда, выходит обычное изображение
        )

    for file in renpy.list_files(): # Что, новомодное объявление файлов хотите? Ну смотрите, даже разьясню что это за бублик
        if "Sister" in file: # Проверяет от нашего ли мода этот файл
            file_name = os.path.splitext(os.path.basename(file))[0] # Достаем имя файла

            if file.endswith((".png", ".jpg", ".webp")): # Фильтр на изображения

                if "sprites" in file and  not "composite" in file: # Если он в директории спрайтов, то по красоте с матрицой добавляет спрайт # За исключением компонентных спрайтов, они будут обьявлены дальше
                    renpy.image( # По факту, так же обьявляет изображение, но реализуемо подругому. Не забудьте использовать bg cg и подобную херотеть в названии папок
                        file_name.replace("_", " "), # имя по которому будем обращаться
                        make_sprite_timed(file)
                    )
                elif not "gui" in file: # Компоненты меню обьявляются в самом меню
                    renpy.image(file.split("/")[-2]+" "+file_name,  # Ну а обычные ваши фончики фоточки обьявляются вот так
                        
                        file,
                        
                        )
            elif file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")): # Если хотите потусить под музычку
                globals()[file_name] = file # Разьяснения нужны?
