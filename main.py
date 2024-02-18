from utils import *

# Win Settings

win.geometry('800x800+550+150')
win.resizable(False, False)
<<<<<<< HEAD
win.iconbitmap('button_icons/fire.ico')
win.title('Prometa')
set_appearance_mode('dark')


=======
win.title('Prometa')
win.iconbitmap('button icons/fire-white.ico') # Для Макса - Тут для темної теми вікна береш fire-white, а для світлої fire


# Button settings
button_font = ('e-Ukraine Regular', 15)
button_color = '#2147cf'
button_hover_color = '#0936d9'
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


>>>>>>> af6a04470ae3705305e9494a04818227bc6dd7ba
# Creating buttons
for i, (text, icon) in enumerate(zip(button_texts, button_icons), start=1):
    button = CTkButton(win, text=text, font=button_font, fg_color=button_color,
                       image=icon, compound=button_compound,
                       width=button_g, height=button_g, hover_color=button_hover_color,
                       corner_radius=button_radius)
    button.place(x=23 + ((i - 1) % 4) * 197, y=90 + ((i - 1) // 4) * 200)
    buttons.append(button)

win.mainloop()

