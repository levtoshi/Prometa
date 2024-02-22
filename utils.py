from imports import *
from prog_starts import *

# Config 

win = CTk()
from win import *
from prog_starts import *

# Config

buttons = []


def clear():
    for i in buttons:
        i.destroy()
    ThemeController.change_theme.destroy()
    buttons.clear()

def back():
    global back_
    back_ = CTkButton(win, text='Назад', font=button_font, fg_color=button_color,
                       width=button_g, height=50, hover_color=button_hover_color,
                       corner_radius=button_radius, command=menu)
    back_.place(x=10, y=10)

def menu():
    for i in range(1,12):
        for i, (text, icon, command) in enumerate(zip(button_texts, button_icons, button_command), start=1):
            button = CTkButton(win, text=text, font=button_font, fg_color=button_color,
                               image=icon, compound=button_compound,
                               width=button_g, height=button_g, hover_color=button_hover_color,
                               corner_radius=button_radius, command=command)
            button.place(x=23 + ((i - 1) % 4) * 197, y=90 + ((i - 1) // 4) * 200)
            buttons.append(button)
        ThemeController.createButton()
    back_.destroy()

def calendar():
    clear()
    back()
    calendar_start()
    print('calendar')

def timer():
    clear()
    back()
    timer_start()
    print('timer')

def weather():
    clear()
    back()
    weather_start()
    print('weather')

def notes():
    clear()
    back()
    notes_start()
    print('notes')

def calculator():
    clear()
    back()
    calc_start()
    print('calculator')

def rock_game():
    rock_start()
    print('rock_game')
def snake():
    clear()
    back()
    rock_start()
    print('rock_game')
def snake():
    clear()
    back()
    snake_start()
    print('snake')

def pics():
    clear()
    back()
    pictures_start()
    print('pics')

def cpu():
    clear()
    back()
    pc_start()
    print('cpu')

def python():
    clear()
    back()
    python_start()
    print('python')

def setting():
    clear()
    back()
    setting_start()
    print('setting')


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

button_command = [calendar, timer, weather, notes, calculator, rock_game, snake, pics, cpu, python, setting]

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