Делая гм - пришел к выводу что можно и без composite род директории обойтись

Новая структура

Character_tag: # например lu у Луны
    distance: # close|normal|far # если не добавлять эту директорию - будет считать элемент для расстояния normal
        Element_name: # например emotions # обозначает композитный элемент # body|emotions|dresses|accessory
            composite_image # lu_1_smile где lu это Character_tag, 1 - индекс позы (не обязательно цифра) и smile - название элемента (не должно повторятся)
        static_image # lu_neko_pioneer где lu это Character_tag а все последующее - название элемента (спрайта) (не должно повторятся) # Статический элемент
