#Idea Opus Proventus
from utils import *


#Win Settings
win = CTk()
win.geometry('800x800+550+150')
win.resizable(False, False)

win.iconbitmap('button icons/fire.ico')
win.title('Prometa')


# Button settings
button_font = ('Roboto', 13)
button_color = '#2147cf'
button_hover_color = '#0228b0'
button_g = 150
button_ico_size = (80, 80)
button_radius = 33
button_compound = 'top'
set_appearance_mode('dark')



# Icons for button
calendar_ico = CTkImage(dark_image=Image.open('button icons/calendar.png'), light_image=Image.open(
    'button icons/calendar.png'), size=button_ico_size)

timer_ico = CTkImage(dark_image=Image.open('button icons/timer.png'), light_image=Image.open('button icons/timer.png'), size=button_ico_size)

weather_ico = CTkImage(dark_image=Image.open('button icons/weather.png'), light_image=Image.open(
    'button icons/weather.png'), size=button_ico_size)

notes_ico = CTkImage(dark_image=Image.open('button icons/notes.png'), light_image=Image.open('button icons/notes.png'), size=button_ico_size)

calculator_ico = CTkImage(dark_image=Image.open('button icons/calculator.png'), light_image=Image.open(
    'button icons/calculator.png'), size=button_ico_size)

rock_game_ico = CTkImage(dark_image=Image.open('button icons/rock-paper-scissors.png'), light_image=Image.open(
    'button icons/rock-paper-scissors.png'), size=button_ico_size)

snake_ico = CTkImage(dark_image=Image.open('button icons/snake.png'), light_image=Image.open('button icons/snake.png'), size=button_ico_size)

pics_ico = CTkImage(dark_image=Image.open('button icons/pics.png'), light_image=Image.open('button icons/pics.png'), size=button_ico_size)

processes_ico = CTkImage(dark_image=Image.open('button icons/cpu.png'), light_image=Image.open('button icons/cpu.png'), size=button_ico_size)

python_ico = CTkImage(dark_image=Image.open('button icons/python.png'), light_image=Image.open('button icons/python.png'), size=button_ico_size)

settings_ico = CTkImage(dark_image=Image.open('button icons/setting.png'), light_image=Image.open('button icons/setting.png'), size=button_ico_size)


# Creating buttons
b1 = CTkButton(win, text='Календар', font=button_font, fg_color=button_color,
               image=calendar_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b2 = CTkButton(win, text='Таймер', font=button_font, fg_color=button_color,
               image=timer_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b3 = CTkButton(win, text='Погода', font=button_font, fg_color=button_color,
               image=weather_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b4 = CTkButton(win, text='Блокнот', font=button_font, fg_color=button_color,
               image=notes_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b5 = CTkButton(win, text='Калькулятор', font=button_font, fg_color=button_color,
               image=calculator_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b6 = CTkButton(win, text='Rock', font=button_font, fg_color=button_color,
               image=rock_game_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b7 = CTkButton(win, text='Змійка', font=button_font, fg_color=button_color,
               image=snake_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b8 = CTkButton(win, text='Малюнки', font=button_font, fg_color=button_color,
               image=pics_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b9 = CTkButton(win, text='Python', font=button_font, fg_color=button_color,
               image=python_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)
b10 = CTkButton(win, text='ПК', font=button_font, fg_color=button_color,
               image=processes_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)

b11 = CTkButton(win, text='Налаштування', font=button_font, fg_color=button_color,
               image=settings_ico, compound=button_compound,
               width=button_g, height=button_g, hover_color=button_hover_color,
               corner_radius=button_radius)


# Buttons placing
b1.place(x=23, y=90)
b2.place(x=220, y=90)
b3.place(x=417, y=90)
b4.place(x=623, y=90)
b5.place(x=23, y=290)
b6.place(x=220, y=290)
b7.place(x=417, y=290)
b8.place(x=623, y=290)
b9.place(x=123, y=492)
b10.place(x=320, y=492)
b11.place(x=526, y=492)

win.mainloop()