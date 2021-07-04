# -*- coding: utf-8 -*-
init:

    #####BG####



    image bg int_sis_room_day = "mods/Sister/images/bg/int/sis_room_day.jpg"
    image bg int_sis_room_rain = "mods/Sister/images/bg/int/sis_room_rain.jpg"
    image bg int_sis_stairs = "mods/Sister/images/bg/int/sis_stairs.jpg"
    image bg sis_prologue_incar = "mods/Sister/images/bg/sis_prologue_incar.jpg"


    ####SPRITES####



    image de smile close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/close/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/close/emotions/de_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/close/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/close/emotions/de_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/close/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/close/emotions/de_1_smile.png")
    )

    image de angry close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/close/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/close/emotions/de_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/close/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/close/emotions/de_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/close/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/close/emotions/de_1_angry.png")
    )


    image de smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/normal/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/normal/emotions/de_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/normal/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/normal/emotions/de_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/normal/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/normal/emotions/de_1_smile.png")
    )

    image de angry = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/normal/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/normal/emotions/de_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/normal/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/normal/emotions/de_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/de/normal/body/de_1_body.png", (0, 0), "mods/Sister/images/sprites/de/normal/emotions/de_1_angry.png")
    )




    image sv surprise2 close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_surprise2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_surprise2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_surprise2.png")
    )

    image sv shy close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_shy.png")
    )

    image sv scared close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_1_scared.png")
    )

    image sv smile2 close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_smile2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_smile2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_smile2.png")
    )

    image sv serious close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_serious.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_serious.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_serious.png")
    )

    image sv shy close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_shy.png")
    )

    image sv laugh close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_laugh.png")
    )

    image sv happy close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_happy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_happy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_3_happy.png")
    )

    image sv sorrow close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_sorrow.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_sorrow.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_sorrow.png")
    )

    image sv smile1 close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_smile1.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_smile1.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_smile1.png")
    )

    image sv cry_smile close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_cry_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_cry_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_2_cry_smile.png")
    )

    image sv scared2 close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_scared2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_scared2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_scared2.png")
    )

    image sv omg close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_omg.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_omg.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_omg.png")
    )

    image sv surprise close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_surprise.png")
    )

    image sv muse close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_muse.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_muse.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_muse.png")
    )

    image sv smile3 close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_smile3.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_smile3.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_5_smile3.png")
    )

    image sv shocked2 close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_shocked2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_shocked2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_shocked2.png")
    )

    image sv rage close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_rage.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_rage.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_rage.png")
    )

    image sv angry close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_angry.png")
    )

    image sv sad close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_sad.png")
    )

    image sv calm close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_calm.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_calm.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_calm.png")
    )

    image sv indifference close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_indifference.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_indifference.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_indifference.png")
    )

    image sv grin close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_grin.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_grin.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/close/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/close/emotions/sv_4_grin.png")
    )


    image sv surprise2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_surprise2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_surprise2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_surprise2.png")
    )

    image sv shy = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_shy.png")
    )

    image sv scared = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_1_scared.png")
    )

    image sv smile2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_smile2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_smile2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_smile2.png")
    )

    image sv serious = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_serious.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_serious.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_serious.png")
    )

    image sv shy = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_shy.png")
    )

    image sv laugh = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_laugh.png")
    )

    image sv happy = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_happy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_happy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_3_happy.png")
    )

    image sv sorrow = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_sorrow.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_sorrow.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_sorrow.png")
    )

    image sv smile1 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_smile1.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_smile1.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_smile1.png")
    )

    image sv cry_smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_cry_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_cry_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_2_cry_smile.png")
    )

    image sv scared2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_scared2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_scared2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_scared2.png")
    )

    image sv omg = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_omg.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_omg.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_omg.png")
    )

    image sv surprise = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_surprise.png")
    )

    image sv muse = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_muse.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_muse.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_muse.png")
    )

    image sv smile3 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_smile3.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_smile3.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_5_smile3.png")
    )

    image sv shocked2 = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_shocked2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_shocked2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_shocked2.png")
    )

    image sv rage = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_rage.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_rage.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_rage.png")
    )

    image sv angry = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_angry.png")
    )

    image sv sad = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_sad.png")
    )

    image sv calm = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_calm.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_calm.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_calm.png")
    )

    image sv indifference = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_indifference.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_indifference.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_indifference.png")
    )

    image sv grin = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_grin.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_grin.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/normal/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/normal/emotions/sv_4_grin.png")
    )


    image sv surprise2 far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_surprise2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_surprise2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_surprise2.png")
    )

    image sv shy far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_shy.png")
    )

    image sv scared far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_1_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_1_scared.png")
    )

    image sv smile2 far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_smile2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_smile2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_smile2.png")
    )

    image sv serious far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_serious.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_serious.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_serious.png")
    )

    image sv shy far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_shy.png")
    )

    image sv laugh far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_laugh.png")
    )

    image sv happy far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_happy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_happy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_3_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_3_happy.png")
    )

    image sv sorrow far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_sorrow.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_sorrow.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_sorrow.png")
    )

    image sv smile1 far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_smile1.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_smile1.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_smile1.png")
    )

    image sv cry_smile far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_cry_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_cry_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_2_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_2_cry_smile.png")
    )

    image sv scared2 far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_scared2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_scared2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_scared2.png")
    )

    image sv omg far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_omg.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_omg.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_omg.png")
    )

    image sv surprise far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_surprise.png")
    )

    image sv muse far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_muse.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_muse.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_muse.png")
    )

    image sv smile3 far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_smile3.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_smile3.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_5_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_5_smile3.png")
    )

    image sv shocked2 far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_shocked2.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_shocked2.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_shocked2.png")
    )

    image sv rage far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_rage.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_rage.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_rage.png")
    )

    image sv angry far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_angry.png")
    )

    image sv sad far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_sad.png")
    )

    image sv calm far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_calm.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_calm.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_calm.png")
    )

    image sv indifference far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_indifference.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_indifference.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_indifference.png")
    )

    image sv grin far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_grin.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_grin.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/sv/far/body/sv_4_body.png", (0, 0), "mods/Sister/images/sprites/sv/far/emotions/sv_4_grin.png")
    )



    image mix smile close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_smile.png")
    )

    image mix surprise close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_surprise.png")
    )

    image mix normal close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/close/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/close/emotions/mix_1_normal.png")
    )


    image mix smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_smile.png")
    )

    image mix surprise = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_surprise.png")
    )

    image mix normal = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/normal/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/normal/emotions/mix_1_normal.png")
    )


    image mix smile far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_smile.png")
    )

    image mix surprise far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_surprise.png")
    )

    image mix normal far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/mix/far/body/mix_1_body.png", (0, 0), "mods/Sister/images/sprites/mix/far/emotions/mix_1_normal.png")
    )



    image lu smile swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png")
    )

    image lu angry swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png")
    )

    image lu normal swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png")
    )

    image lu smile pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png")
    )
    image lu smile close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png")
    )

    image lu angry pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png")
    )
    image lu angry close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png")
    )

    image lu normal pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png")
    )
    image lu normal close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png")
    )

    image lu smile tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_smile.png")
    )

    image lu angry tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_angry.png")
    )

    image lu normal tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_1_normal.png")
    )

    image lu shocked body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png")
    )

    image lu laugh body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png")
    )

    image lu sad body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png")
    )

    image lu shocked pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png")
    )
    image lu shocked close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png")
    )

    image lu laugh pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png")
    )
    image lu laugh close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png")
    )

    image lu sad pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png")
    )
    image lu sad close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png")
    )

    image lu shocked tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png")
    )

    image lu laugh tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png")
    )

    image lu sad tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png")
    )

    image lu shocked swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_shocked.png")
    )

    image lu laugh swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_laugh.png")
    )

    image lu sad swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_3_sad.png")
    )

    image lu shy body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png")
    )

    image lu scared body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png")
    )

    image lu cry body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png")
    )

    image lu guilty body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png")
    )

    image lu surprise body close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_body.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png")
    )

    image lu shy pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png")
    )
    image lu shy close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png")
    )

    image lu scared pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png")
    )
    image lu scared close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png")
    )

    image lu cry pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png")
    )
    image lu cry close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png")
    )

    image lu guilty pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png")
    )
    image lu guilty close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png")
    )

    image lu surprise pioneer close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png")
    )
    image lu surprise close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png")
    )

    image lu shy tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png")
    )

    image lu scared tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png")
    )

    image lu cry tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png")
    )

    image lu guilty tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png")
    )

    image lu surprise tshirt close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png")
    )

    image lu shy swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_shy.png")
    )

    image lu scared swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_scared.png")
    )

    image lu cry swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_cry.png")
    )

    image lu guilty swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_guilty.png")
    )

    image lu surprise swim close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/close/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/close/emotions/lu_2_surprise.png")
    )


    image lu smile swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png")
    )

    image lu angry swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png")
    )

    image lu normal swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png")
    )

    image lu smile pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png")
    )
    image lu smile = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png")
    )

    image lu angry pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png")
    )
    image lu angry = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png")
    )

    image lu normal pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png")
    )
    image lu normal = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png")
    )

    image lu smile tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_smile.png")
    )

    image lu angry tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_angry.png")
    )

    image lu normal tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_1_normal.png")
    )

    image lu shocked swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png")
    )

    image lu laugh swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png")
    )

    image lu sad swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png")
    )

    image lu shocked pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png")
    )
    image lu shocked = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png")
    )

    image lu laugh pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png")
    )
    image lu laugh = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png")
    )

    image lu sad pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png")
    )
    image lu sad = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png")
    )

    image lu shocked tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_shocked.png")
    )

    image lu laugh tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_laugh.png")
    )

    image lu sad tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_3_sad.png")
    )

    image lu shy swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png")
    )

    image lu scared swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png")
    )

    image lu cry swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png")
    )

    image lu guilty swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png")
    )

    image lu surprise swim = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png")
    )

    image lu shy pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png")
    )
    image lu shy = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png")
    )

    image lu scared pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png")
    )
    image lu scared = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png")
    )

    image lu cry pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png")
    )
    image lu cry = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png")
    )

    image lu guilty pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png")
    )
    image lu guilty = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png")
    )

    image lu surprise pioneer = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png")
    )
    image lu surprise = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png")
    )

    image lu shy tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_shy.png")
    )

    image lu scared tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_scared.png")
    )

    image lu cry tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_cry.png")
    )

    image lu guilty tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_guilty.png")
    )

    image lu surprise tshirt = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/normal/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/normal/emotions/lu_2_surprise.png")
    )


    image lu smile swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png")
    )

    image lu angry swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png")
    )

    image lu normal swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png")
    )

    image lu smile pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png")
    )
    image lu smile far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png")
    )

    image lu angry pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png")
    )
    image lu angry far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png")
    )

    image lu normal pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png")
    )
    image lu normal far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png")
    )

    image lu smile tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_smile.png")
    )

    image lu angry tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_angry.png")
    )

    image lu normal tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_1_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_1_normal.png")
    )

    image lu shocked swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png")
    )

    image lu laugh swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png")
    )

    image lu sad swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png")
    )

    image lu shocked pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png")
    )
    image lu shocked far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png")
    )

    image lu laugh pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png")
    )
    image lu laugh far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png")
    )

    image lu sad pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png")
    )
    image lu sad far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png")
    )

    image lu shocked tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_shocked.png")
    )

    image lu laugh tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_laugh.png")
    )

    image lu sad tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_3_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_3_sad.png")
    )

    image lu shy swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png")
    )

    image lu scared swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png")
    )

    image lu cry swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png")
    )

    image lu guilty swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png")
    )

    image lu surprise swim far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_swim.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png")
    )

    image lu shy pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png")
    )
    image lu shy far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png")
    )

    image lu scared pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png")
    )
    image lu scared far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png")
    )

    image lu cry pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png")
    )
    image lu cry far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png")
    )

    image lu guilty pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png")
    )
    image lu guilty far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png")
    )

    image lu surprise pioneer far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png")
    )
    image lu surprise far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_pioneer.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png")
    )

    image lu shy tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_shy.png")
    )

    image lu scared tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_scared.png")
    )

    image lu cry tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_cry.png")
    )

    image lu guilty tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_guilty.png")
    )

    image lu surprise tshirt far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/lu/far/body/lu_2_tshirt.png", (0, 0), "mods/Sister/images/sprites/lu/far/emotions/lu_2_surprise.png")
    )



    image ax grin close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/close/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/close/emotions/ax_1_grin.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/close/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/close/emotions/ax_1_grin.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/close/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/close/emotions/ax_1_grin.png")
    )

    image ax normal close = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/close/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/close/emotions/ax_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/close/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/close/emotions/ax_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/close/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/close/emotions/ax_1_normal.png")
    )


    image ax grin = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/normal/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/normal/emotions/ax_1_grin.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/normal/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/normal/emotions/ax_1_grin.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/normal/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/normal/emotions/ax_1_grin.png")
    )

    image ax normal = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/normal/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/normal/emotions/ax_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/normal/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/normal/emotions/ax_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/normal/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/normal/emotions/ax_1_normal.png")
    )


    image ax grin far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/far/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/far/emotions/ax_1_grin.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/far/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/far/emotions/ax_1_grin.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/far/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/far/emotions/ax_1_grin.png")
    )

    image ax normal far = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/far/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/far/emotions/ax_1_normal.png"),
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/far/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/far/emotions/ax_1_normal.png"),
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            im.Composite((630,1080), (0, 0), "mods/Sister/images/sprites/ax/far/body/ax_1_body.png", (0, 0), "mods/Sister/images/sprites/ax/far/emotions/ax_1_normal.png")
    )



    image pi 1_dark = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/close/pi_1_dark.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/close/pi_1_dark.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/close/pi_1_dark.png"
    )
    image pi 1_light = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/close/pi_1_light.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/close/pi_1_light.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/close/pi_1_light.png"
    )
    image pi 1_mid = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/close/pi_1_mid.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/close/pi_1_mid.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/close/pi_1_mid.png"
    )



    image pi 1_dark = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/normal/pi_1_dark.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/normal/pi_1_dark.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/normal/pi_1_dark.png"
    )
    image pi 1_mid = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/normal/pi_1_mid.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/normal/pi_1_mid.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/normal/pi_1_mid.png"
    )
    image pi 1_light = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/normal/pi_1_light.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/normal/pi_1_light.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/normal/pi_1_light.png"
    )



    image pi 1_dark = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/far/pi_1_dark.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/far/pi_1_dark.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/far/pi_1_dark.png"
    )
    image pi 1_light = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/far/pi_1_light.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/far/pi_1_light.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/far/pi_1_light.png"
    )
    image pi 1_mid = ConditionSwitch(
        "persistent.sprite_time=='sunset'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/far/pi_1_mid.png",
                im.matrix.tint(0.94, 0.82, 1.0)
                ),
        "persistent.sprite_time=='night'",
            im.MatrixColor(
                "mods/Sister/images/sprites/pi/far/pi_1_mid.png",
                im.matrix.tint(0.63, 0.78, 0.82)
            ),
        True,
            "mods/Sister/images/sprites/pi/far/pi_1_mid.png"
    )

