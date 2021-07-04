# -*- coding: utf-8 -*-
init python:
    mods["Sister_index"] =  u"{font=fonts/timesi.ttf}{size=40}\"Sister\" Project{/size}{/font}"
    import re

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

#не работает ((
    # def create_canon_colored_character(tag, name, ground_color):

    #     """
    #     Оставим если в этом будет смысл
    #     """

    #     if isinstance(ground_color, str):
    #         ground_color = ground_color.replace("#", "")
    #         colors_list = len(ground_color)
    #         if colors_list in [3, 4]:
    #             colors_list = re.findall(r"[0-9a-fA-F]", ground_color)
    #         elif colors_list in [6, 8]:
    #             colors_list = re.findall(r"[0-9a-fA-F][0-9a-fA-F]", ground_color)
    #         else:
    #             text = "Неверное значение цвета #"+ground_color
    #             raise Exception(text)

    #         if len(colors_list) == 3:
    #             colors_list.append("FF")

    #         for i, color in enumerate(colors_list):
    #             if len(color) == 1:
    #                 color += "F"
    #             colors_list[i] = int("0x"+color, base=16)

    #         ground_color = colors_list

    #     cl = tuple(ground_color)

    #     color_list = {
    #         'night': [cl[0]*2, cl[1]*1, cl[2]*2, cl[3]],
    #         'sunset': [cl[0]*2, cl[1]*1, cl[2], cl[3]],
    #         'day': cl,
    #         'prolog': cl
    #     }

    #     global colors, names

    #     colors[tag] = color_list
    #     names[tag] = name
    #     store.names_list.append(tag)

    # create_canon_colored_character("lu", "Луна", "#124391")
    # create_canon_colored_character("sv", "Света", "#124391")
    # create_canon_colored_character("fa", "Отец", "#888")
    # create_canon_colored_character("mih", "Михаил Сергеевич", "#555")

    lu = Character(u'Луна', what_drop_shadow=[(2, 1),(2, 2)], color="#00008B", what_color="#E2C778")#хехе, луна...
    sv = Character(u'Света', what_drop_shadow=[(2, 1),(2, 2)], color="#124391", what_color="#E2C778")
    fa = Character(u'Отец', what_drop_shadow=[(2, 1),(2, 2)], color="#888", what_color="#E2C778")
    mih = Character(u'Михаил Сергеевич', what_drop_shadow=[(2, 1),(2, 2)], color="#555", what_color="#E2C778")




init:
    image bg int_sis_room_anim:
        "mods/Sister/images/bg/int/sis_room_rain.jpg"
        block:
            choice:
                2
            choice:
                10
            5
            choice:
                "mods/Sister/images/bg/int/sis_room_rain.jpg" with dissolve2

            choice:
                "mods/Sister/images/bg/int/sis_room_day.jpg" with dissolve2
            repeat
