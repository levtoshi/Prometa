from customtkinter import *
from turtle import *
from time import *
from PIL import Image


# Config 

win = CTk()

buttons = []

# Button settings
button_font = ('Roboto', 13)
button_color = '#2147cf'
button_hover_color = '#0228b0'
button_g = 150
button_ico_size = (80, 80)
button_radius = 33
button_compound = 'top'

# Icons for button
icon_names = ['calendar', 'timer', 'weather', 'notes', 'calculator', 'rock-paper-scissors',
              'snake', 'pics', 'cpu', 'python', 'setting']
button_icons = [CTkImage(dark_image=Image.open(f'button_icons/{name}.png'),
                         light_image=Image.open(f'button_icons/{name}.png'),
                         size=button_ico_size) for name in icon_names]

# Button texts
button_texts = ['Календар', 'Таймер', 'Погода', 'Блокнот', 'Калькулятор',
                'Rock', 'Змійка', 'Малюнки', 'Python', 'ПК', 'Налаштування']

# Theme config
Themes = {
    "dark": [
        "#2147cf", # Btns color
        "#074D8E", # Btns-hover color
    ],
    "light": [
        "#DA9715", # Btns color
        "#B67B08", # Btns-hover color
    ],
}


def changeTheme():
    if ThemeController.GetTheme() == "light":
        ThemeController.changeTheme("dark")
    else:
        ThemeController.changeTheme("light")


class ThemeController():
    def __init__ (self, theme):
        self.theme = str(theme)

    def changeTheme(self, theme):
        for button in buttons:
            button.configure(fg_color = Themes[theme][0], hover_color = Themes[theme][1])
            self.theme = theme
            self.change_theme.configure(fg_color = Themes[theme][0], hover_color = Themes[theme][1])

    def createButton(self):
        _ico = CTkImage(dark_image=Image.open('button_icons/calendar.png'), light_image=Image.open(
        'button_icons/calendar.png'), size=(20, 20))

        self.change_theme = CTkButton(win, width = 32, height = 32, image = _ico, corner_radius= min(32, 32) // 2, text = "", command=changeTheme  )
        self.change_theme.place(x = 695, y = 20)

    def GetTheme(self):
        return self.theme


ThemeController = ThemeController("dark")
ThemeController.createButton()