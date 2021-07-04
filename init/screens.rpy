# -*- coding: utf-8 -*-
label Sister_index:

    scene black with fade

    jump Sister_start

label Sister_true_exit:

    window hide dissolve
    stop music fadeout 3
    scene black with fade
    pause 1
    $ MainMenu(confirm=False)()
