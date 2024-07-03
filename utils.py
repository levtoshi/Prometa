from prog_starts import *
from win import *

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
                      width=button_g, height=45, hover_color=button_hover_color,
                      corner_radius=button_radius, command=menu)
    back_.place(x=10, y=25)
    ThemeController.createButton()


def menu():
    ThemeController.ShowMainFrame(False)
    child_elem = Main_Frame.winfo_children()  # Всі обєкти які в фреймі
    for child in child_elem:
        child.destroy()

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
    ThemeController.ShowMainFrame(True)
    calendar_start(Main_Frame)


def timer():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    timer_start(Main_Frame)


def weather():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    weather_start(Main_Frame)


def notes():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    notes_start(Main_Frame)


def calculator():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    calc_start(Main_Frame)


def rock_game():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    rock_start(Main_Frame)


def snake():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    snake_start(Main_Frame)


def pics():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    pictures_start(Main_Frame)

def python():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    python_start(Main_Frame)

def cpu():
    clear()
    back()
    ThemeController.ShowMainFrame(True)
    pc_start(Main_Frame)


# Button settings
button_font = ('Roboto', 13, 'bold')
button_color = '#2147cf'
button_hover_color = '#0228b0'
button_g = 150
button_ico_size = (80, 80)
button_radius = 33
button_compound = 'top'

# Icons for button
icon_names = ['calendar', 'timer', 'weather', 'notes', 'calculator', 'rock-paper-scissors',
              'snake', 'pics', 'python', 'cpu']
button_icons = [CTkImage(dark_image=Image.open(f'C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\{name}.png'),
                         light_image=Image.open(f'C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\{name}.png'),
                         size=button_ico_size) for name in icon_names]

button_command = [calendar, timer, weather, notes, calculator, rock_game, snake, pics, python, cpu]

# Button texts
button_texts = ['Календар', 'Таймер', 'Погода', 'Блокнот', 'Калькулятор',
                'Rock', 'Змійка', 'Малюнки', 'Python', 'ПК']

# Theme config
Themes = {
    "dark": [
        "#2147cf",  # Btns color
        "#074D8E",  # Btns-hover color
    ],
    "light": [
        "#DA9715",  # Btns color
        "#B67B08",  # Btns-hover color
    ],
}


def changeTheme():
    if ThemeController.GetTheme() == "light":
        ThemeController.changeTheme("dark")
    else:
        ThemeController.changeTheme("light")


class ThemeController():
    def __init__(self, theme):
        self.theme = str(theme)

    def changeTheme(self, theme):
        for button in buttons:
            if theme == 'light':
                button.configure(text_color='black')
            else:
                button.configure(text_color='white')
            button.configure(fg_color=Themes[theme][0], hover_color=Themes[theme][1])
            self.theme = theme
            self.change_theme.configure(fg_color=Themes[theme][0], hover_color=Themes[theme][1])

    def createButton(self):
        _ico = CTkImage(dark_image=Image.open('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\calendar.png'), light_image=Image.open(
            'C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\calendar.png'), size=(20, 20))

        self.change_theme = CTkButton(win, width=32, height=32, image=_ico, corner_radius=min(32, 32) // 2, text="",
                                      command=changeTheme)
        self.change_theme.place(x=695, y=30)

    def ShowMainFrame(self, state):
        if state:
            Main_Frame.configure(width=780, height=700)
        else:
            Main_Frame.configure(width=0, height=0)

    def GetTheme(self):
        return self.theme


ThemeController = ThemeController("dark")
ThemeController.createButton()