#Импортирование-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
from tkinter import *
import pygame
import pickle
#Импортирование---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Создание файла "game.data"(если уже есть, то игнорируется)------------------------------------------------------------------------------------------------------------------------------------------------
d = {'click': 0, 'money': 100, 'crystal': 0, 'income': 0, 'up1': ['Empty outer space', 'Пустое косм. пространство', 0, 100, 1, 0], 'up2': ['Meteorite', 'Метеорит', 0, 500, 4, 0], 'up3': ['Planet', 'Планета', 0, 3000, 20, 0], 'up4': ['Sun', 'Звезда', 0, 9500, 80, 0], 'up5': ['Solar system', 'Солнечная система', 0, 39000, 220, 0], 'up6': ['Nebula', 'Туманность', 0, 200000, 880, 0], 'up7': ['Supernova', 'Сверхновая', 0, 1600000, 12000, 0], 'up8': ['Black hole', 'Чёрная дыра', 0, 120000000, 200000, 0], 'up9': ['Galaxy', 'Галактика', 0, 4000000000, 2000000, 0], 'up10': ['Superclusters', 'Сверхскопление', 0, 15, 6000000, 0], 'up11': ['Dark energy', 'Тёмная энергия', 0, 100, 30000000, 0], 'up12': ['Universe', 'Вселенная', 0, 500, 120000000, 0], 'setting': ['Music', 'Музыка'], 'on': ['Turn on', 'Включить'], 'off': ['Turn off', 'Выключить'], 'music': ['Music:', 'Музыка:'], 'click1': ['click', 'клик'], 'imp1': [5000, 1000], 'imp2': [25000, 2000], 'imp3': [150000, 3000], 'imp4': [500000, 5000], 'imp5': [2000000, 7000], 'imp6': [10000000, 9000], 'imp7': [80000000, 12000], 'imp8': [6000000000, 16000], 'imp9': [80000000000, 20000], 'imp10': [200, 30000], 'imp11': [1500, 40000], 'imp12': [7000, 50000], 'name1': ['Buy 25 Empty outer space', 'Купить 25 Пустых косм. пространств'], 'name2': ['Buy 25 Meteorite', 'Купить 25 Метеоритов'], 'name3': ['Buy 25 Planet', 'Купить 25 Планет'], 'name4': ['Buy 25 Sun', 'Купить 25 Звёзд'], 'name5': ['Buy 25 Solar system', 'Купить 25 Солнечных систем'], 'name6': ['Buy 25 Nebula', 'Купить 25 Туманностей'], 'name7': ['Buy 25 Supernova', 'Купить 25 Сверхновых'], 'name8': ['Buy 25 Black hole', 'Купить 25 Чёрных дыр'], 'name9': ['Buy 10 Galaxy', 'Купить 10 Галактик'], 'name10': ['Buy 10 Superclusters', 'Купить 10 Сверхскоплений'], 'name11': ['Buy 10 Dark energy', 'Купить 10 Тёмных энергий'], 'name12': ['Buy 10 Universe', 'Купить 10 Вселенных'], 'buy': ['Obtained', 'Приобретено'], 'i': 0}
data = None
try:
    with open('game.data', 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    pass

if data == None:
    with open('game.data', 'wb') as file:
        pickle.dump(d, file)
#Создание файла "game.data"(если уже есть, то игнорируется)-----------------------------------------------------------------------------------------------------------------------------------------------------------


#Загрузка данных(если файл уже имеется, то игнорируется)----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
if data == None:
    with open('game.data', 'rb') as file:
        data = pickle.load(file)
#Загрузка данных(если файл уже имеется, то игнорируется)---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Фоновая музыка------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
pygame.mixer.init()
pygame.mixer.music.load('music_space.mp3')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
#Фоновая музыка------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                        


#Главное окно------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
window = Tk()
window.geometry('500x693+400+0')
window.title('Space Clicker')
window.resizable(False, False)
window['bg'] = 'black'


#Вставить изображение
class Image:
    def __init__(self, x, y, f, bg, a, b, root):
        self.x = x
        self.y = y
        self.f = f
        self.bg = bg
        self.a = a
        self.b = b
        self.root = root

    def _place_(self):
        img = PhotoImage(file=self.f)
        img_lbl = Label(self.root, bg=self.bg)
        img = img.subsample(self.a, self.b)
        img_lbl.image = img
        img_lbl['image'] = img_lbl.image
        img_lbl.place(x=self.x, y=self.y)


#Границы
lbl1 = Label(window, text='__________________________________________________________________________________________________________________', bg='black', fg='white')
lbl1.place(x=-5, y=156)
lbl2 = Label(window, text='__________________________________________________________________________________________________________________', bg='black', fg='white')
lbl2.place(x=-5, y=259)
lbl3 = Label(window, text='__________________________________________________________________________________________________________________', bg='black', fg='white')
lbl3.place(x=-5, y=580)


#Картинки значений
img_coin = Image(3, 2, 'image\coin.png', 'black', 60, 60, window)
img_coin._place_()

img_crystal = Image(3, 36, 'image\crystal.png', 'black', 7, 7, window)
img_crystal._place_()

img_income = Image(3, 86, 'image\income.png', 'black', 14, 14, window)
img_income._place_()


#Отображение значений
_money_ = Label(window, text=str("{:,}".format(data['money'])), bg='black', fg='yellow', font=('Comic Sans MS', 15))
_money_.place(x=35, y=4)
_crystal_ = Label(window, text=str("{:,}".format(data['crystal'])), bg='black', fg='pink', font=('Comic Sans MS', 15))
_crystal_.place(x=35, y=43)
_income_ = Label(window, text=str("{:,}".format(data['income'])), bg='black', fg='#8CD41B', font=('Comic Sans MS', 15))
_income_.place(x=35, y=84)
#Главное окно------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Upgrade--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
n = 1.15


def up1():
    if data['money'] >= data['up1'][3]:
        data['income'] += data['up1'][4]
        data['money'] -= data['up1'][3]
        data['up1'][3] *= n
        data['up1'][3] = int(data['up1'][3])
        data['up1'][2] += 1
        data['up1'][-1] += data['up1'][4]

        name_empty.configure(text='(' + str(data['up1'][2]) + ') ' + data['up1'][data['i']])
        cost_empty.configure(text=str("{:,}".format(data['up1'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up1'][3]:
            cost_empty.configure(fg='#2FC800')
        else:
            cost_empty.configure(fg='red')

        if data['money'] >= data['up2'][3]:
            cost_meteorite.configure(fg='#2FC800')
        else:
            cost_meteorite.configure(fg='red')

        if data['money'] >= data['up3'][3]:
            cost_planet.configure(fg='#2FC800')
        else:
            cost_planet.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)

        
def up2():
    if data['money'] >= data['up2'][3]:
        data['income'] += data['up2'][4]
        data['money'] -= data['up2'][3]
        data['up2'][3] *= n
        data['up2'][3] = int(data['up2'][3])
        data['up2'][2] += 1
        data['up2'][-1] += data['up2'][4]

        name_meteorite.configure(text='(' + str(data['up2'][2]) + ') ' + data['up2'][data['i']])
        cost_meteorite.configure(text=str("{:,}".format(data['up2'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up1'][3]:
            cost_empty.configure(fg='#2FC800')
        else:
            cost_empty.configure(fg='red')

        if data['money'] >= data['up2'][3]:
            cost_meteorite.configure(fg='#2FC800')
        else:
            cost_meteorite.configure(fg='red')

        if data['money'] >= data['up3'][3]:
            cost_planet.configure(fg='#2FC800')
        else:
            cost_planet.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
        

def up3():
    if data['money'] >= data['up3'][3]:
        data['income'] += data['up3'][4]
        data['money'] -= data['up3'][3]
        data['up3'][3] *= n
        data['up3'][3] = int(data['up3'][3])
        data['up3'][2] += 1
        data['up3'][-1] += data['up3'][4]

        name_planet.configure(text='(' + str(data['up3'][2]) + ') ' + data['up3'][data['i']])
        cost_planet.configure(text=str("{:,}".format(data['up3'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up1'][3]:
            cost_empty.configure(fg='#2FC800')
        else:
            cost_empty.configure(fg='red')

        if data['money'] >= data['up2'][3]:
            cost_meteorite.configure(fg='#2FC800')
        else:
            cost_meteorite.configure(fg='red')

        if data['money'] >= data['up3'][3]:
            cost_planet.configure(fg='#2FC800')
        else:
            cost_planet.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up4():
    if data['money'] >= data['up4'][3]:
        data['income'] += data['up4'][4]
        data['money'] -= data['up4'][3]
        data['up4'][3] *= n
        data['up4'][3] = int(data['up4'][3])
        data['up4'][2] += 1
        data['up4'][-1] += data['up4'][4]

        name_sun.configure(text='(' + str(data['up4'][2]) + ') ' + data['up4'][data['i']])
        cost_sun.configure(text=str("{:,}".format(data['up4'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up4'][3]:
            cost_sun.configure(fg='#2FC800')
        else:
            cost_sun.configure(fg='red')

        if data['money'] >= data['up5'][3]:
            cost_solar_system.configure(fg='#2FC800')
        else:
            cost_solar_system.configure(fg='red')

        if data['money'] >= data['up6'][3]:
            cost_nebula.configure(fg='#2FC800')
        else:
            cost_nebula.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up5():
    if data['money'] >= data['up5'][3]:
        data['income'] += data['up5'][4]
        data['money'] -= data['up5'][3]
        data['up5'][3] *= n
        data['up5'][3] = int(data['up5'][3])
        data['up5'][2] += 1
        data['up5'][-1] += data['up5'][4]

        name_solar_system.configure(text='(' + str(data['up5'][2]) + ') ' + data['up5'][data['i']])
        cost_solar_system.configure(text=str("{:,}".format(data['up5'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up4'][3]:
            cost_sun.configure(fg='#2FC800')
        else:
            cost_sun.configure(fg='red')

        if data['money'] >= data['up5'][3]:
            cost_solar_system.configure(fg='#2FC800')
        else:
            cost_solar_system.configure(fg='red')

        if data['money'] >= data['up6'][3]:
            cost_nebula.configure(fg='#2FC800')
        else:
            cost_nebula.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up6():
    if data['money'] >= data['up6'][3]:
        data['income'] += data['up6'][4]
        data['money'] -= data['up6'][3]
        data['up6'][3] *= n
        data['up6'][3] = int(data['up6'][3])
        data['up6'][2] += 1
        data['up6'][-1] += data['up6'][4]

        name_nebula.configure(text='(' + str(data['up6'][2]) + ') ' + data['up6'][data['i']])
        cost_nebula.configure(text=str("{:,}".format(data['up6'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up4'][3]:
            cost_sun.configure(fg='#2FC800')
        else:
            cost_sun.configure(fg='red')

        if data['money'] >= data['up5'][3]:
            cost_solar_system.configure(fg='#2FC800')
        else:
            cost_solar_system.configure(fg='red')

        if data['money'] >= data['up6'][3]:
            cost_nebula.configure(fg='#2FC800')
        else:
            cost_nebula.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up7():
    if data['money'] >= data['up7'][3]:
        data['income'] += data['up7'][4]
        data['money'] -= data['up7'][3]
        data['up7'][3] *= n
        data['up7'][3] = int(data['up7'][3])
        data['up7'][2] += 1
        data['up7'][-1] += data['up7'][4]

        name_supernova.configure(text='(' + str(data['up7'][2]) + ') ' + data['up7'][data['i']])
        cost_supernova.configure(text=str("{:,}".format(data['up7'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up7'][3]:
            cost_supernova.configure(fg='#2FC800')
        else:
            cost_supernova.configure(fg='red')

        if data['money'] >= data['up8'][3]:
            cost_black_hole.configure(fg='#2FC800')
        else:
            cost_black_hole.configure(fg='red')

        if data['money'] >= data['up9'][3]:
            cost_galaxy.configure(fg='#2FC800')
        else:
            cost_galaxy.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up8():
    if data['money'] >= data['up8'][3]:
        data['income'] += data['up8'][4]
        data['money'] -= data['up8'][3]
        data['up8'][3] *= n
        data['up8'][3] = int(data['up8'][3])
        data['up8'][2] += 1
        data['up8'][-1] += data['up8'][4]

        name_black_hole.configure(text='(' + str(data['up8'][2]) + ') ' + data['up8'][data['i']])
        cost_black_hole.configure(text=str("{:,}".format(data['up8'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up7'][3]:
            cost_supernova.configure(fg='#2FC800')
        else:
            cost_supernova.configure(fg='red')

        if data['money'] >= data['up8'][3]:
            cost_black_hole.configure(fg='#2FC800')
        else:
            cost_black_hole.configure(fg='red')

        if data['money'] >= data['up9'][3]:
            cost_galaxy.configure(fg='#2FC800')
        else:
            cost_galaxy.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up9():
    if data['money'] >= data['up9'][3]:
        data['income'] += data['up9'][4]
        data['money'] -= data['up9'][3]
        data['up9'][3] *= n
        data['up9'][3] = int(data['up9'][3])
        data['up9'][2] += 1
        data['up9'][-1] += data['up9'][4]

        name_galaxy.configure(text='(' + str(data['up9'][2]) + ') ' + data['up9'][data['i']])
        cost_galaxy.configure(text=str("{:,}".format(data['up9'][3])))
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['up7'][3]:
            cost_supernova.configure(fg='#2FC800')
        else:
            cost_supernova.configure(fg='red')

        if data['money'] >= data['up8'][3]:
            cost_black_hole.configure(fg='#2FC800')
        else:
            cost_black_hole.configure(fg='red')

        if data['money'] >= data['up9'][3]:
            cost_galaxy.configure(fg='#2FC800')
        else:
            cost_galaxy.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up10():
    if data['crystal'] >= data['up10'][3]:
        data['income'] += data['up10'][4]
        data['crystal'] -= data['up10'][3]
        data['up10'][3] *= 1.1
        data['up10'][3] = int(data['up10'][3])
        data['up10'][2] += 1
        data['up10'][-1] += data['up10'][4]

        name_superclusters.configure(text='(' + str(data['up10'][2]) + ') ' + data['up10'][data['i']])
        cost_superclusters.configure(text=str("{:,}".format(data['up10'][3])))
        _crystal_.configure(text=str("{:,}".format(data['crystal'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['crystal'] >= data['up10'][3]:
            cost_superclusters.configure(fg='#2FC800')
        else:
            cost_superclusters.configure(fg='red')

        if data['crystal'] >= data['up11'][3]:
            cost_dark_energy.configure(fg='#2FC800')
        else:
            cost_dark_energy.configure(fg='red')

        if data['crystal'] >= data['up12'][3]:
            cost_universe.configure(fg='#2FC800')
        else:
            cost_universe.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up11():
    if data['crystal'] >= data['up11'][3]:
        data['income'] += data['up11'][4]
        data['crystal'] -= data['up11'][3]
        data['up11'][3] *= 1.1
        data['up11'][3] = int(data['up11'][3])
        data['up11'][2] += 1
        data['up11'][-1] += data['up11'][4]

        name_dark_energy.configure(text='(' + str(data['up11'][2]) + ') ' + data['up11'][data['i']])
        cost_dark_energy.configure(text=str("{:,}".format(data['up11'][3])))
        _crystal_.configure(text=str("{:,}".format(data['crystal'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['crystal'] >= data['up10'][3]:
            cost_superclusters.configure(fg='#2FC800')
        else:
            cost_superclusters.configure(fg='red')

        if data['crystal'] >= data['up11'][3]:
            cost_dark_energy.configure(fg='#2FC800')
        else:
            cost_dark_energy.configure(fg='red')

        if data['crystal'] >= data['up12'][3]:
            cost_universe.configure(fg='#2FC800')
        else:
            cost_universe.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def up12():
    if data['crystal'] >= data['up12'][3]:
        data['income'] += data['up12'][4]
        data['crystal'] -= data['up12'][3]
        data['up12'][3] *= 1.1
        data['up12'][3] = int(data['up12'][3])
        data['up12'][2] += 1
        data['up12'][-1] += data['up12'][4]

        name_universe.configure(text='(' + str(data['up12'][2]) + ') ' + data['up12'][data['i']])
        cost_universe.configure(text=str("{:,}".format(data['up12'][3])))
        _crystal_.configure(text=str("{:,}".format(data['crystal'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['crystal'] >= data['up10'][3]:
            cost_superclusters.configure(fg='#2FC800')
        else:
            cost_superclusters.configure(fg='red')

        if data['crystal'] >= data['up11'][3]:
            cost_dark_energy.configure(fg='#2FC800')
        else:
            cost_dark_energy.configure(fg='red')

        if data['crystal'] >= data['up12'][3]:
            cost_universe.configure(fg='#2FC800')
        else:
            cost_universe.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
        
        
def _upgrade_str1():
    global name_empty, name_meteorite, name_planet, cost_empty, cost_meteorite, cost_planet
    
    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    #Изображения
    img_empty = Image(2, 287, 'image\empty.png', 'black', 16, 14, window)
    img_empty._place_()

    img_meteorite = Image(0, 362, 'image\meteorite.png', 'black', 8, 6, window)
    img_meteorite._place_()

    img_planet = Image(0, 445, 'image\planet.png', 'black', 27, 27, window)
    img_planet._place_()

    #Названия
    name_empty = Label(window, text='(' + str(data['up1'][2]) + ') ' + data['up1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_meteorite = Label(window, text='(' + str(data['up2'][2]) + ') ' + data['up2'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_planet = Label(window, text='(' + str(data['up3'][2]) + ') ' + data['up3'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))

    name_empty.place(x=80, y=290)
    name_meteorite.place(x=80, y=362)
    name_planet.place(x=80, y=445)
    
    #Цена
    cost_empty = Label(window, text=str("{:,}".format(data['up1'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_empty.place(x=110, y=323)
    img_coin1 = Image(85, 323, 'image\coin.png', 'black', 75, 75, window)
    img_coin1._place_()

    cost_meteorite = Label(window, text=str("{:,}".format(data['up2'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_meteorite.place(x=110, y=394)
    img_coin2 = Image(85, 394, 'image\coin.png', 'black', 75, 75, window)
    img_coin2._place_()

    cost_planet = Label(window, text=str("{:,}".format(data['up3'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_planet.place(x=110, y=478)
    img_coin3 = Image(85, 478, 'image\coin.png', 'black', 75, 75, window)
    img_coin3._place_()

    if data['money'] >= data['up1'][3]:
        cost_empty.configure(fg='#2FC800')

    if data['money'] >= data['up2'][3]:
        cost_meteorite.configure(fg='#2FC800')

    if data['money'] >= data['up3'][3]:
        cost_planet.configure(fg='#2FC800')

    
    #Кнопка покупки
    btn_empty = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up1)
    btn_empty.place(x=380, y=290)

    btn_meteorite = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up2)
    btn_meteorite.place(x=380, y=367)

    btn_planet = Button(window, text='Buy' , bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up3)
    btn_planet.place(x=380, y=445)
    
    
    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_upgrade_str2)
    btn_continue.place(x=415, y=550)

    def click1():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))

        if data['money'] >= data['up1'][3]:
            cost_empty.configure(fg='#2FC800')
        else:
            cost_empty.configure(fg='red')

        if data['money'] >= data['up2'][3]:
            cost_meteorite.configure(fg='#2FC800')
        else:
            cost_meteorite.configure(fg='red')

        if data['money'] >= data['up3'][3]:
            cost_planet.configure(fg='#2FC800')
        else:
            cost_planet.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)

        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

    
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click1)
    btn_click.place(x=100, y=610)


def _upgrade_str2():
    global name_sun, name_solar_system, name_nebula, cost_sun, cost_solar_system, cost_nebula
    
    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    #Изображения
    img_sun = Image(7, 285, 'image\sun1.png', 'black', 3, 3, window)
    img_sun._place_()

    img_solar_system = Image(0, 362, 'image\solar_system.png', 'black', 15, 15, window)
    img_solar_system._place_()

    img_nebula = Image(-5, 436, 'image\_nebula1.png', 'black', 7, 7, window)
    img_nebula._place_()

    #Названия
    name_sun = Label(window, text='(' + str(data['up4'][2]) + ') ' + data['up4'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_solar_system = Label(window, text='(' + str(data['up5'][2]) + ') ' + data['up5'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_nebula = Label(window, text='(' + str(data['up6'][2]) + ') ' + data['up6'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))

    name_sun.place(x=80, y=290)
    name_solar_system.place(x=80, y=362)
    name_nebula.place(x=80, y=445)
    
    #Цена
    cost_sun = Label(window, text=str("{:,}".format(data['up4'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_sun.place(x=110, y=323)
    img_coin1 = Image(85, 323, 'image\coin.png', 'black', 75, 75, window)
    img_coin1._place_()

    cost_solar_system = Label(window, text=str("{:,}".format(data['up5'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_solar_system.place(x=110, y=394)
    img_coin2 = Image(85, 394, 'image\coin.png', 'black', 75, 75, window)
    img_coin2._place_()

    cost_nebula = Label(window, text=str("{:,}".format(data['up6'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_nebula.place(x=110, y=478)
    img_coin3 = Image(85, 478, 'image\coin.png', 'black', 75, 75, window)
    img_coin3._place_()

    if data['money'] >= data['up4'][3]:
        cost_sun.configure(fg='#2FC800')

    if data['money'] >= data['up5'][3]:
        cost_solar_system.configure(fg='#2FC800')

    if data['money'] >= data['up6'][3]:
        cost_nebula.configure(fg='#2FC800')
    
    #Кнопка покупки
    btn_sun = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up4)
    btn_sun.place(x=380, y=290)

    btn_solar_system = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up5)
    btn_solar_system.place(x=380, y=367)

    btn_nebula = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up6)
    btn_nebula.place(x=380, y=445)
    
    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_upgrade_str3)
    btn_continue.place(x=415, y=550)

    btn_exit = Button(window, text='<----', width=10, height=2, bg='black', fg='blue', command=_upgrade_str1)
    btn_exit.place(x=5, y=550)

    def click2():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))

        if data['money'] >= data['up4'][3]:
            cost_sun.configure(fg='#2FC800')
        else:
            cost_sun.configure(fg='red')

        if data['money'] >= data['up5'][3]:
            cost_solar_system.configure(fg='#2FC800')
        else:
            cost_solar_system.configure(fg='red')

        if data['money'] >= data['up6'][3]:
            cost_nebula.configure(fg='#2FC800')
        else:
            cost_nebula.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)

        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click2)
    btn_click.place(x=100, y=610)


def _upgrade_str3():
    global name_supernova, name_black_hole, name_galaxy, cost_supernova, cost_black_hole, cost_galaxy
    
    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    #Изображения
    img_supernova = Image(0, 285, 'image\supernova1.png', 'black', 14, 10, window)
    img_supernova._place_()

    img_black_hole = Image(-4, 364, 'image\_black_hole.png', 'black', 7, 7, window)
    img_black_hole._place_()

    img_galaxy = Image(-7, 440, 'image\galaxy1.png', 'black', 17, 21, window)
    img_galaxy._place_()

    #Названия
    name_supernova = Label(window, text='(' + str(data['up7'][2]) + ') ' + data['up7'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_black_hole = Label(window, text='(' + str(data['up8'][2]) + ') ' + data['up8'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_galaxy = Label(window, text='(' + str(data['up9'][2]) + ') ' + data['up9'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    
    name_supernova.place(x=80, y=290)
    name_black_hole.place(x=80, y=362)
    name_galaxy.place(x=80, y=445)
    
    #Цена
    cost_supernova = Label(window, text=str("{:,}".format(data['up7'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_supernova.place(x=110, y=323)
    img_coin1 = Image(85, 323, 'image\coin.png', 'black', 75, 75, window)
    img_coin1._place_()

    cost_black_hole = Label(window, text=str("{:,}".format(data['up8'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_black_hole.place(x=110, y=394)
    img_coin2 = Image(85, 394, 'image\coin.png', 'black', 75, 75, window)
    img_coin2._place_()

    cost_galaxy = Label(window, text=str("{:,}".format(data['up9'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_galaxy.place(x=110, y=478)
    img_crystal = Image(85, 475, 'image\coin.png', 'black', 75, 75, window)
    img_crystal._place_()

    if data['money'] >= data['up7'][3]:
        cost_supernova.configure(fg='#2FC800')

    if data['money'] >= data['up8'][3]:
        cost_black_hole.configure(fg='#2FC800')

    if data['money'] >= data['up9'][3]:
        cost_galaxy.configure(fg='#2FC800')
    
    #Кнопка покупки
    btn_supernova = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up7)
    btn_supernova.place(x=380, y=290)

    btn_black_hole = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up8)
    btn_black_hole.place(x=380, y=367)

    btn_galaxy = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up9)
    btn_galaxy.place(x=380, y=445)
    
    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_upgrade_str4)
    btn_continue.place(x=415, y=550)

    btn_exit = Button(window, text='<----', width=10, height=2, bg='black', fg='blue', command=_upgrade_str2)
    btn_exit.place(x=5, y=550)

    def click3():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))

        if data['money'] >= data['up7'][3]:
            cost_supernova.configure(fg='#2FC800')
        else:
            cost_supernova.configure(fg='red')

        if data['money'] >= data['up8'][3]:
            cost_black_hole.configure(fg='#2FC800')
        else:
            cost_black_hole.configure(fg='red')

        if data['money'] >= data['up9'][3]:
            cost_galaxy.configure(fg='#2FC800')
        else:
            cost_galaxy.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)

        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click3)
    btn_click.place(x=100, y=610)


def _upgrade_str4():
    global name_superclusters, name_dark_energy, name_universe, cost_superclusters, cost_dark_energy, cost_universe

    bg = Image(-25, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    #Изображения
    img_superclusters = Image(0, 285, 'image\superclusters.png', 'black', 11, 9, window)
    img_superclusters._place_()

    img_dark_energy = Image(3, 363, 'image\dark_energy1.png', 'black', 13, 11, window)
    img_dark_energy._place_()

    img_universe = Image(0, 445, 'image\_universe.png', 'black', 8, 6, window)
    img_universe._place_()

    #Названия
    name_superclusters = Label(window, text='(' + str(data['up10'][2]) + ') ' + data['up10'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_dark_energy = Label(window, text='(' + str(data['up11'][2]) + ') ' + data['up11'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    name_universe = Label(window, text='(' + str(data['up12'][2]) + ') ' + data['up12'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 12))
    
    name_superclusters.place(x=80, y=290)
    name_dark_energy.place(x=80, y=362)
    name_universe.place(x=80, y=445)
    
    #Цена
    cost_superclusters = Label(window, text=str("{:,}".format(data['up10'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_superclusters.place(x=110, y=323)
    img_crystal1 = Image(85, 320, 'image\crystal.png', 'black', 10, 10, window)
    img_crystal1._place_()

    cost_dark_energy = Label(window, text=str("{:,}".format(data['up11'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_dark_energy.place(x=110, y=394)
    img_crystal2 = Image(85, 391, 'image\crystal.png', 'black', 10, 10, window)
    img_crystal2._place_()

    cost_universe = Label(window, text=str("{:,}".format(data['up12'][3])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_universe.place(x=110, y=478)
    img_crystal3 = Image(85, 475, 'image\crystal.png', 'black', 10, 10, window)
    img_crystal3._place_()

    if data['crystal'] >= data['up10'][3]:
        cost_superclusters.configure(fg='#2FC800')

    if data['crystal'] >= data['up11'][3]:
        cost_dark_energy.configure(fg='#2FC800')

    if data['crystal'] >= data['up12'][3]:
        cost_universe.configure(fg='#2FC800')
    
    #Кнопка покупки
    btn_superclusters = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up10)
    btn_superclusters.place(x=380, y=290)

    btn_dark_energy = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up11)
    btn_dark_energy.place(x=380, y=367)

    btn_universe = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=up12)
    btn_universe.place(x=380, y=445)

    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_upgrade_str1)
    btn_continue.place(x=415, y=550)

    btn_exit = Button(window, text='<----', width=10, height=2, bg='black', fg='blue', command=_upgrade_str3)
    btn_exit.place(x=5, y=550)

    def click4():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))

        if data['crystal'] >= data['up10'][3]:
            cost_superclusters.configure(fg='#2FC800')
        else:
            cost_superclusters.configure(fg='red')

        if data['crystal'] >= data['up11'][3]:
            cost_dark_energy.configure(fg='#2FC800')
        else:
            cost_dark_energy.configure(fg='red')

        if data['crystal'] >= data['up12'][3]:
            cost_universe.configure(fg='#2FC800')
        else:
            cost_universe.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)

        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click4)
    btn_click.place(x=100, y=610)

    
#Меню Upgrade
btn_up = Button(window, bg='black', width=16, height=4, command=_upgrade_str1)
btn_up.place(x=0, y=189)
img_up = Image(29, 195, 'image\_up.png', 'black', 5, 5, window)
img_up._place_()
#Upgrade-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Converter---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def converter():
    global btn_con_money, btn_con_crystal
    
    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()
    
    _money_ = Label(window, text='1,000,000,000', bg='black', fg='yellow', font=('Comic Sans MS', 15))
    _money_.place(x=117, y=300)

    lbl_con = Label(window, text='=', bg='black', fg='white', font=('Comic Sans MS', 20))
    lbl_con.place(x=297, y=294)

    _crystal_ = Label(window, text='1', bg='black', fg='pink', font=('Comic Sans MS', 15))
    _crystal_.place(x=380, y=300)

    img_coin = Image(85, 299, 'image\coin.png', 'black', 60, 60, window)
    img_coin._place_()

    img_crystal = Image(350, 295, 'image\crystal.png', 'black', 8, 8, window)
    img_crystal._place_()

    btn_con_crystal = Button(window, text=str("{:,}".format(data['money'] // 1_000_000_000)), fg='pink', bg='black', font=('Comic Sans MS', 12), command=convert_crystal, width=23)
    btn_con_money = Button(window, text=str("{:,}".format(data['crystal'] * 1_000_000_000)), fg='yellow', bg='black', font=('Comic Sans MS', 12), command=convert_money, width=23)
    btn_con_crystal.place(x=10, y=400)
    btn_con_money.place(x=251, y=400)
    
    with open('game.data', 'wb') as file:
            pickle.dump(data, file)
    

def convert_crystal():
    crystals = data['money'] // 1_000_000_000
    data['crystal'] += crystals
    data['money'] -= crystals * 1_000_000_000
    btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))
    btn_con_money.configure(text=str("{:,}".format(data['crystal'] * 1_000_000_000)))
    _money_.configure(text=str("{:,}".format(data['money'])))
    _crystal_.configure(text=str("{:,}".format(data['crystal'])))

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def convert_money():
    money = data['crystal'] * 1_000_000_000
    data['money'] += money
    data['crystal'] -= money // 1_000_000_000
    btn_con_money.configure(text=str("{:,}".format(data['crystal'] * 1_000_000_000)))
    btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))
    _money_.configure(text=str("{:,}".format(data['money'])))
    _crystal_.configure(text=str("{:,}".format(data['crystal'])))

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)
            

#Меню converter   
btn_converter = Button(window, bg='black', width=16, height=4, command=converter)
btn_converter.place(x=253, y=189)
img_con = Image(281, 194, 'image\converter.png', 'black', 14, 14, window)
img_con._place_()
btn_con_crystal = Button(window, text=str("{:,}".format(data['money'] // 1_000_000_000)), fg='pink', bg='black', font=('Comic Sans MS', 12), command=convert_crystal, width=23)
btn_con_money = Button(window, text=str("{:,}".format(data['crystal'] * 1_000_000_000)), fg='yellow', bg='black', font=('Comic Sans MS', 12), command=convert_money, width=23)

#Converter---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Settings-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def on():
    pygame.mixer.music.unpause()

def off():
    pygame.mixer.music.pause()

def settings():
    global btn_on, btn_off, lbl_music
    
    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()
    
    btn_ru = Button(window, text='Russian\Русский', font=('Comic Sans MS', 15), bg='black', fg='white', width=40, command=ru)
    btn_ru.place(x=6, y=300)
    btn_en = Button(window, text='English\Английский', font=('Comic Sans MS', 15), bg='black', fg='white', width=40, command=en)
    btn_en.place(x=6, y=360)

    lbl_music = Label(window, text=data['music'][data['i']], font=('Comic Sans MS', 15), bg='black', fg='white')
    lbl_music.place(x=210, y=420)

    btn_on = Button(window, text=data['on'][data['i']], font=('Comic Sans MS', 15), bg='black', fg='white', width=10, command=on)
    btn_off = Button(window, text=data['off'][data['i']], font=('Comic Sans MS', 15), bg='black', fg='white', width=10, command=off)
    btn_on.place(x=105, y=460)
    btn_off.place(x=255, y=460)


#Изменить язык
def en():
    data['i'] = 0

    lbl_music.configure(text=data['music'][data['i']])

    btn_on.configure(text=data['on'][data['i']])
    btn_off.configure(text=data['off'][data['i']])

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)

    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click)
    btn_click.place(x=100, y=610)
    
def ru():
    data['i'] = 1
   
    btn_on.configure(text=data['on'][data['i']])
    btn_off.configure(text=data['off'][data['i']])

    lbl_music.configure(text=data['music'][data['i']])

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)

    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click)
    btn_click.place(x=100, y=610)
        
    
#Меню настроек
btn_settings = Button(window, bg='black', width=16, height=4, command=settings)
btn_settings.place(x=379, y=189)
img_settings = Image(411, 196, 'image\settings.png', 'black', 12, 12, window)
img_settings._place_()
#Settings-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Improvement--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
x = 2
b = 1


def imp1():
    if data['up1'][2] >= 25 and data['money'] >= data['imp1'][0]:
        data['money'] -= data['imp1'][0]
        data['income'] += data['up1'][-1] * b
        data['up1'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp1'][0]:
            cost_empty_imp1.configure(fg='#2FC800')
        else:
            cost_empty_imp1.configure(fg='red')
            
        if data['money'] >= data['imp2'][0]:
            cost_meteorite_imp1.configure(fg='#2FC800')
        else:
            cost_meteorite_imp1.configure(fg='red')

        if data['money'] >= data['imp3'][0]:
            cost_planet_imp1.configure(fg='#2FC800')
        else:
            cost_planet_imp1.configure(fg='red')

        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy1 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy1.place(x=100, y=290)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
            

def imp2():
    if data['up2'][2] >= 25 and data['money'] >= data['imp2'][0]:
        data['money'] -= data['imp2'][0]
        data['income'] += data['up2'][-1] * b
        data['up2'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp1'][0]:
            cost_empty_imp1.configure(fg='#2FC800')
        else:
            cost_empty_imp1.configure(fg='red')
            
        if data['money'] >= data['imp2'][0]:
            cost_meteorite_imp1.configure(fg='#2FC800')
        else:
            cost_meteorite_imp1.configure(fg='red')

        if data['money'] >= data['imp3'][0]:
            cost_planet_imp1.configure(fg='#2FC800')
        else:
            cost_planet_imp1.configure(fg='red')

        bg = Image(85, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy2 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy2.place(x=100, y=370)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
            

def imp3():
    if data['up3'][2] >= 25 and data['money'] >= data['imp3'][0]:
        data['money'] -= data['imp3'][0]
        data['income'] += data['up3'][-1] * b
        data['up3'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp1'][0]:
            cost_empty_imp1.configure(fg='#2FC800')
        else:
            cost_empty_imp1.configure(fg='red')
            
        if data['money'] >= data['imp2'][0]:
            cost_meteorite_imp1.configure(fg='#2FC800')
        else:
            cost_meteorite_imp1.configure(fg='red')

        if data['money'] >= data['imp3'][0]:
            cost_planet_imp1.configure(fg='#2FC800')
        else:
            cost_planet_imp1.configure(fg='red')

        bg = Image(85, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy3 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy3.place(x=100, y=450)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
            

def imp4():
    if data['up4'][2] >= 25 and data['money'] >= data['imp4'][0]:
        data['money'] -= data['imp4'][0]
        data['income'] += data['up4'][-1] * b
        data['up4'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp4'][0]:
            cost_sun_imp1.configure(fg='#2FC800')
        else:
            cost_sun_imp1.configure(fg='red')
            
        if data['money'] >= data['imp5'][0]:
            cost_solar_system_imp1.configure(fg='#2FC800')
        else:
            cost_solar_system_imp1.configure(fg='red')

        if data['money'] >= data['imp6'][0]:
            cost_nebula_imp1.configure(fg='#2FC800')
        else:
            cost_nebula_imp1.configure(fg='red')

        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy4 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy4.place(x=100, y=290)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def imp5():
    if data['up5'][2] >= 25 and data['money'] >= data['imp5'][0]:
        data['money'] -= data['imp5'][0]
        data['income'] += data['up5'][-1] * b
        data['up5'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp4'][0]:
            cost_sun_imp1.configure(fg='#2FC800')
        else:
            cost_sun_imp1.configure(fg='red')
            
        if data['money'] >= data['imp5'][0]:
            cost_solar_system_imp1.configure(fg='#2FC800')
        else:
            cost_solar_system_imp1.configure(fg='red')

        if data['money'] >= data['imp6'][0]:
            cost_nebula_imp1.configure(fg='#2FC800')
        else:
            cost_nebula_imp1.configure(fg='red')

        bg = Image(85, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy5 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy5.place(x=100, y=370)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def imp6():
    if data['up6'][2] >= 25 and data['money'] >= data['imp6'][0]:
        data['money'] -= data['imp6'][0]
        data['income'] += data['up6'][-1] * b
        data['up6'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp4'][0]:
            cost_sun_imp1.configure(fg='#2FC800')
        else:
            cost_sun_imp1.configure(fg='red')
            
        if data['money'] >= data['imp5'][0]:
            cost_solar_system_imp1.configure(fg='#2FC800')
        else:
            cost_solar_system_imp1.configure(fg='red')

        if data['money'] >= data['imp6'][0]:
            cost_nebula_imp1.configure(fg='#2FC800')
        else:
            cost_nebula_imp1.configure(fg='red')

        bg = Image(85, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy6 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy6.place(x=100, y=450)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def imp7():
    if data['up7'][2] >= 25 and data['money'] >= data['imp7'][0]:
        data['money'] -= data['imp7'][0]
        data['income'] += data['up7'][-1] * b
        data['up7'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp7'][0]:
            cost_supernova_imp1.configure(fg='#2FC800')
        else:
            cost_supernova_imp1.configure(fg='red')
            
        if data['money'] >= data['imp8'][0]:
            cost_black_hole_imp1.configure(fg='#2FC800')
        else:
            cost_black_hole_imp1.configure(fg='red')

        if data['money'] >= data['imp9'][0]:
            cost_galaxy_imp1.configure(fg='#2FC800')
        else:
            cost_galaxy_imp1.configure(fg='red')

        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy7 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy7.place(x=100, y=290)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def imp8():
    if data['up8'][2] >= 25 and data['money'] >= data['imp8'][0]:
        data['money'] -= data['imp8'][0]
        data['income'] += data['up8'][-1] * b
        data['up8'][4] *= x
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp7'][0]:
            cost_supernova_imp1.configure(fg='#2FC800')
        else:
            cost_supernova_imp1.configure(fg='red')
            
        if data['money'] >= data['imp8'][0]:
            cost_black_hole_imp1.configure(fg='#2FC800')
        else:
            cost_black_hole_imp1.configure(fg='red')

        if data['money'] >= data['imp9'][0]:
            cost_galaxy_imp1.configure(fg='#2FC800')
        else:
            cost_galaxy_imp1.configure(fg='red')

        bg = Image(85, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy8 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy8.place(x=100, y=370)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
            

def imp9():
    if data['up9'][2] >= 10 and data['money'] >= data['imp9'][0]:
        data['money'] -= data['imp9'][0]
        data['income'] += data['up9'][-1] * 3
        data['up9'][4] *= 4
        _money_.configure(text=str("{:,}".format(data['money'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        if data['money'] >= data['imp7'][0]:
            cost_supernova_imp1.configure(fg='#2FC800')
        else:
            cost_supernova_imp1.configure(fg='red')
            
        if data['money'] >= data['imp8'][0]:
            cost_black_hole_imp1.configure(fg='#2FC800')
        else:
            cost_black_hole_imp1.configure(fg='red')

        if data['money'] >= data['imp9'][0]:
            cost_galaxy_imp1.configure(fg='#2FC800')
        else:
            cost_galaxy_imp1.configure(fg='red')

        bg = Image(85, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy9 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy9.place(x=100, y=450)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def imp10():
    if data['up10'][2] >= 10 and data['crystal'] >= data['imp10'][0]:
        data['crystal'] -= data['imp10'][0]
        data['income'] += data['up10'][-1] * 3
        data['up10'][4] *= 4
        _crystal_.configure(text=str("{:,}".format(data['crystal'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy10 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy10.place(x=100, y=290)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
        

def imp11():
    if data['up11'][2] >= 10 and data['crystal'] >= data['imp11'][0]:
        data['crystal'] -= data['imp11'][0]
        data['income'] += data['up11'][-1] * 3
        data['up11'][4] *= 4
        _crystal_.configure(text=str("{:,}".format(data['crystal'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        bg = Image(82, 363, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy11 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy11.place(x=100, y=370)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def imp12():
    if data['up12'][2] >= 10 and data['crystal'] >= data['imp12'][0]:
        data['crystal'] -= data['imp12'][0]
        data['income'] += data['up12'][-1] * 3
        data['up12'][4] *= 4
        _crystal_.configure(text=str("{:,}".format(data['crystal'])))
        _income_.configure(text=str("{:,}".format(data['income'])))

        bg = Image(82, 443, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy12 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy12.place(x=100, y=450)

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)


def _imp_str1():
    global cost_empty_imp1, cost_meteorite_imp1, cost_planet_imp1

    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    img_empty = Image(10, 295, 'image\empty1.png', 'black', 9, 9, window)
    img_empty._place_()

    img_meteorite = Image(0, 362, 'image\meteorite1.png', 'black', 6, 6, window)
    img_meteorite._place_()

    img_planet = Image(5, 446, 'image\planet1.png', 'black', 3, 3, window)
    img_planet._place_()

    #Названия
    imp1_empty = Label(window, text=data['name1'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_meteorite = Label(window, text=data['name2'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_planet = Label(window, text=data['name3'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))

    imp1_empty.place(x=85, y=290)
    imp1_meteorite.place(x=85, y=367)
    imp1_planet.place(x=85, y=445)
    
    #Цена
    cost_empty_imp1 = Label(window, text=str("{:,}".format(data['imp1'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_empty_imp1.place(x=110, y=323)
    imp1_coin1 = Image(85, 323, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin1._place_()

    cost_meteorite_imp1 = Label(window, text=str("{:,}".format(data['imp2'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_meteorite_imp1.place(x=110, y=399)
    imp1_coin2 = Image(85, 399, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin2._place_()

    cost_planet_imp1 = Label(window, text=str("{:,}".format(data['imp3'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_planet_imp1.place(x=110, y=478)
    imp1_coin3 = Image(85, 478, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin3._place_()
        
    
    #Кнопка покупки
    btn_empty_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp1)
    btn_empty_imp1.place(x=380, y=290)

    btn_meteorite_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp2)
    btn_meteorite_imp1.place(x=380, y=372)

    btn_planet_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp3)
    btn_planet_imp1.place(x=380, y=452)

    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_imp_str2)
    btn_continue.place(x=415, y=550)

    if data['money'] >= data['imp1'][0]:
        cost_empty_imp1.configure(fg='#2FC800')

    if data['money'] >= data['imp2'][0]:
        cost_meteorite_imp1.configure(fg='#2FC800')

    if data['money'] >= data['imp3'][0]:
        cost_planet_imp1.configure(fg='#2FC800')

    if data['up1'][2] >= 25:
        imp1_empty.configure(fg='#2FC800')

    if data['up2'][2] >= 25:
        imp1_meteorite.configure(fg='#2FC800')

    if data['up3'][2] >= 25:
        imp1_planet.configure(fg='#2FC800')

    if data['up1'][4] == 1 * 2:
        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy1 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy1.place(x=100, y=290)

    if data['up2'][4] == 4 * 2:
        bg = Image(85, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy2 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy2.place(x=100, y=360)

    if data['up3'][4] == 20 * 2:
        bg = Image(85, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy3 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy3.place(x=100, y=440)

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)
        

    def click1():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))
        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        if data['money'] >= data['imp1'][0]:
            cost_empty_imp1.configure(fg='#2FC800')
        else:
            cost_empty_imp1.configure(fg='red')
            
        if data['money'] >= data['imp2'][0]:
            cost_meteorite_imp1.configure(fg='#2FC800')
        else:
            cost_meteorite_imp1.configure(fg='red')

        if data['money'] >= data['imp3'][0]:
            cost_planet_imp1.configure(fg='#2FC800')
        else:
            cost_planet_imp1.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
    
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click1)
    btn_click.place(x=100, y=610)
        


def _imp_str2():
    global cost_sun_imp1, cost_solar_system_imp1, cost_nebula_imp1

    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    img_sun = Image(7, 286, 'image\sun.png', 'black', 10, 10, window)
    img_sun._place_()

    img_solar_system = Image(0, 367, 'image\solar_system1.png', 'black', 15, 15, window)
    img_solar_system._place_()

    img_nebula = Image(-20, 434, 'image\_nebula2.png', 'black', 13, 13, window)
    img_nebula._place_()

    #Названия
    imp1_sun = Label(window, text=data['name4'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_solar_system = Label(window, text=data['name5'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_nebula = Label(window, text=data['name6'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))

    imp1_sun.place(x=85, y=290)
    imp1_solar_system.place(x=85, y=367)
    imp1_nebula.place(x=85, y=445)
    
    #Цена
    cost_sun_imp1 = Label(window, text=str("{:,}".format(data['imp4'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_sun_imp1.place(x=110, y=323)
    imp1_coin1 = Image(85, 323, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin1._place_()

    
    cost_solar_system_imp1 = Label(window, text=str("{:,}".format(data['imp5'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_solar_system_imp1.place(x=110, y=399)
    imp1_coin2 = Image(85, 399, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin2._place_()


    cost_nebula_imp1 = Label(window, text=str("{:,}".format(data['imp6'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_nebula_imp1.place(x=110, y=478)
    imp1_coin3 = Image(85, 478, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin3._place_()
    
    #Кнопка покупки
    btn_sun_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp4)
    btn_sun_imp1.place(x=380, y=290)

    btn_solar_system_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp5)
    btn_solar_system_imp1.place(x=380, y=372)

    btn_nebula_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp6)
    btn_nebula_imp1.place(x=380, y=452)
    
    
    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_imp_str3)
    btn_continue.place(x=415, y=550)

    btn_exit = Button(window, text='<----', width=10, height=2, bg='black', fg='blue', command=_imp_str1)
    btn_exit.place(x=5, y=550)

    if data['up4'][4] == 80 * 2:
        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy1 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy1.place(x=100, y=290)

    if data['up5'][4] == 220 * 2:
        bg = Image(85, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy2 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy2.place(x=100, y=360)

    if data['up6'][4] == 880 * 2:
        bg = Image(85, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy3 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy3.place(x=100, y=440)

    if data['money'] >= data['imp4'][0]:
        cost_sun_imp1.configure(fg='#2FC800')

    if data['money'] >= data['imp5'][0]:
        cost_solar_system_imp1.configure(fg='#2FC800')

    if data['money'] >= data['imp6'][0]:
        cost_nebula_imp1.configure(fg='#2FC800')

    if data['up4'][2] >= 25:
        imp1_sun.configure(fg='#2FC800')

    if data['up5'][2] >= 25:
        imp1_solar_system.configure(fg='#2FC800')

    if data['up6'][2] >= 25:
        imp1_nebula.configure(fg='#2FC800')

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)

    def click2():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))
        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        if data['money'] >= data['imp4'][0]:
            cost_sun_imp1.configure(fg='#2FC800')
        else:
            cost_sun_imp1.configure(fg='red')
            
        if data['money'] >= data['imp5'][0]:
            cost_solar_system_imp1.configure(fg='#2FC800')
        else:
            cost_solar_system_imp1.configure(fg='red')

        if data['money'] >= data['imp6'][0]:
            cost_nebula_imp1.configure(fg='#2FC800')
        else:
            cost_nebula_imp1.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
    
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click2)
    btn_click.place(x=100, y=610)


def _imp_str3():
    global cost_supernova_imp1, cost_black_hole_imp1, cost_galaxy_imp1

    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    img_supernova = Image(0, 285, 'image\supernova.png', 'black', 4, 4, window)
    img_supernova._place_()

    img_black_hole = Image(-4, 364, 'image\_black_hole1.png', 'black', 10, 7, window)
    img_black_hole._place_()

    img_galaxy = Image(-7, 440, 'image\galaxy.png', 'black', 17, 21, window)
    img_galaxy._place_()
    
    #Названия
    imp1_supernova = Label(window, text=data['name7'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_black_hole = Label(window, text=data['name8'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_galaxy = Label(window, text=data['name9'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))

    imp1_supernova.place(x=85, y=290)
    imp1_black_hole.place(x=85, y=367)
    imp1_galaxy.place(x=85, y=445)
    
    #Цена
    cost_supernova_imp1 = Label(window, text=str("{:,}".format(data['imp7'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_supernova_imp1.place(x=110, y=323)
    imp1_coin1 = Image(85, 323, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin1._place_()
    
    cost_black_hole_imp1 = Label(window, text=str("{:,}".format(data['imp8'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_black_hole_imp1.place(x=110, y=399)
    imp1_coin2 = Image(85, 399, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin2._place_()
    
    cost_galaxy_imp1 = Label(window, text=str("{:,}".format(data['imp9'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_galaxy_imp1.place(x=110, y=478)
    imp1_coin3 = Image(85, 478, 'image\coin.png', 'black', 75, 75, window)
    imp1_coin3._place_()
    
    #Кнопка покупки
    btn_supernova_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp7)
    btn_supernova_imp1.place(x=380, y=290)

    btn_black_hole_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp8)
    btn_black_hole_imp1.place(x=380, y=372)

    btn_galaxy_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp9)
    btn_galaxy_imp1.place(x=380, y=452)
    
    
    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_imp_str4)
    btn_continue.place(x=415, y=550)

    btn_exit = Button(window, text='<----', width=10, height=2, bg='black', fg='blue', command=_imp_str2)
    btn_exit.place(x=5, y=550)

    if data['up7'][4] == 12000 * 2:
        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy1 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy1.place(x=100, y=290)

    if data['up8'][4] == 200_000 * 2:
        bg = Image(85, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy2 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy2.place(x=100, y=360)

    if data['up9'][4] == 2_000_000 * 4:
        bg = Image(85, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy3 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy3.place(x=100, y=440)

    if data['money'] >= data['imp7'][0]:
        cost_supernova_imp1.configure(fg='#2FC800')

    if data['money'] >= data['imp8'][0]:
        cost_black_hole_imp1.configure(fg='#2FC800')

    if data['money'] >= data['imp9'][0]:
        cost_galaxy_imp1.configure(fg='#2FC800')

    if data['up7'][2] >= 25:
        imp1_supernova.configure(fg='#2FC800')

    if data['up8'][2] >= 25:
        imp1_black_hole.configure(fg='#2FC800')

    if data['up9'][2] >= 10:
        imp1_galaxy.configure(fg='#2FC800')

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)


    def click3():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))
        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        if data['money'] >= data['imp7'][0]:
            cost_supernova_imp1.configure(fg='#2FC800')
        else:
            cost_supernova_imp1.configure(fg='red')
            
        if data['money'] >= data['imp8'][0]:
            cost_black_hole_imp1.configure(fg='#2FC800')
        else:
            cost_black_hole_imp1.configure(fg='red')

        if data['money'] >= data['imp9'][0]:
            cost_galaxy_imp1.configure(fg='#2FC800')
        else:
            cost_galaxy_imp1.configure(fg='red')

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
    
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click3)
    btn_click.place(x=100, y=610)


def _imp_str4():
    global cost_superclusters_imp1, cost_dark_energy_imp1, cost_universe_imp1

    bg = Image(0, 276, 'image\_bg_black.png', 'black', 4, 4, window)
    bg._place_()

    img_superclusters = Image(0, 285, 'image\superclusters1.png', 'black', 10, 6, window)
    img_superclusters._place_()

    img_dark_energy = Image(3, 363, 'image\dark_energy.png', 'black', 4, 4, window)
    img_dark_energy._place_()

    img_universe = Image(0, 440, 'image\_universe1.png', 'black', 27, 27, window)
    img_universe._place_()

    #Названия
    imp1_superclusters = Label(window, text=data['name10'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_dark_energy = Label(window, text=data['name11'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))
    imp1_universe = Label(window, text=data['name12'][data['i']], bg='black', fg='red', font=('Comic Sans MS', 12))

    imp1_superclusters.place(x=85, y=290)
    imp1_dark_energy.place(x=85, y=367)
    imp1_universe.place(x=85, y=445)
    
    #Цена
    cost_superclusters_imp1 = Label(window, text=str("{:,}".format(data['imp10'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_superclusters_imp1.place(x=110, y=325)
    imp1_crystal1 = Image(85, 322, 'image\crystal.png', 'black', 10, 10, window)
    imp1_crystal1._place_()

    cost_dark_energy_imp1 = Label(window, text=str("{:,}".format(data['imp11'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_dark_energy_imp1.place(x=110, y=401)
    imp1_crystal2 = Image(85, 398, 'image\crystal.png', 'black', 10, 10, window)
    imp1_crystal2._place_()

    cost_universe_imp1 = Label(window, text=str("{:,}".format(data['imp12'][0])), bg='black', fg='red', font=('Comic Sans MS', 12))
    cost_universe_imp1.place(x=110, y=480)
    imp1_crystal3 = Image(85, 477, 'image\crystal.png', 'black', 10, 10, window)
    imp1_crystal3._place_()
    
    #Кнопка покупки
    btn_superclusters_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp10)
    btn_superclusters_imp1.place(x=380, y=290)

    btn_dark_energy_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp11)
    btn_dark_energy_imp1.place(x=380, y=372)

    btn_universe_imp1 = Button(window, text='Buy', bg='black', fg='white', font=('Comic Sans MS', 12), width=10, height=1, command=imp12)
    btn_universe_imp1.place(x=380, y=452)
    
    
    btn_continue = Button(window, text='---->', width=10, height=2, bg='black', fg='blue', command=_imp_str1)
    btn_continue.place(x=415, y=550)

    btn_exit = Button(window, text='<----', width=10, height=2, bg='black', fg='blue', command=_imp_str3)
    btn_exit.place(x=5, y=550)

    if data['up10'][4] == 6_000_000 * 4:
        bg = Image(85, 290, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy1 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy1.place(x=90, y=290)

    if data['up11'][4] == 30_000_000 * 4:
        bg = Image(84, 360, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy2 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy2.place(x=90, y=360)

    if data['up12'][4] == 120_000_000 * 4:
        bg = Image(84, 440, 'image\_bg_black.png', 'black', 8, 20, window)
        bg._place_()
        lbl_buy3 = Label(window, text=data['buy'][data['i']], font=('Comic Sans MS', 14), bg='black', fg='green')
        lbl_buy3.place(x=90, y=440)

    if data['crystal'] >= data['imp10'][0]:
        cost_superclusters_imp1.configure(fg='#2FC800')

    if data['crystal'] >= data['imp11'][0]:
        cost_dark_energy_imp1.configure(fg='#2FC800')

    if data['crystal'] >= data['imp12'][0]:
        cost_universe_imp1.configure(fg='#2FC800')

    if data['up10'][2] >= 10:
        imp1_superclusters.configure(fg='#2FC800')

    if data['up11'][2] >= 10:
        imp1_dark_energy.configure(fg='#2FC800')

    if data['up12'][2] >= 10:
        imp1_universe.configure(fg='#2FC800')

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)

    def click4():
        global click, money, btn_click

        data['money'] += data['income']
        _money_.configure(text=str("{:,}".format(data['money'])))
        btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

        with open('game.data', 'wb') as file:
            pickle.dump(data, file)
    
    btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click4)
    btn_click.place(x=100, y=610)

#Меню improvement
btn_imp = Button(window, bg='black', width=16, height=4, command=_imp_str1)
btn_imp.place(x=126, y=189)
img_imp = Image(153, 195, 'image\improvement.png', 'black', 6, 7, window)
img_imp._place_()
#Improvement--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Взаимодействие с кнопкой "click"
def click():
    global click, money, btn_click

    data['money'] += data['income']
    _money_.configure(text=str("{:,}".format(data['money'])))
    btn_con_crystal.configure(text=str("{:,}".format(data['money'] // 1_000_000_000)))

    with open('game.data', 'wb') as file:
            pickle.dump(data, file)

    
btn_click = Button(window, text=data['click1'][data['i']], bg='black', fg='white', font=('Comic Sans MS', 15), width=25, height=2, command=click)
btn_click.place(x=100, y=610)
#Взаимодействие с кнопкой "click"


window.mainloop()
