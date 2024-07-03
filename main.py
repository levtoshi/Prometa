#Idea Opus Proventus
from utils import *

# Win Settings

win.geometry('800x800+550+150')
win.resizable(False, False)
win.iconbitmap('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\fire.ico')
win.title('Prometa')
set_appearance_mode('dark')


win.title('Prometa')
win.iconbitmap('C:\\Users\\Intel\\PycharmProjects\\Prometa\\button_icons\\fire-white.ico') # Для Макса - Тут для темної теми вікна береш fire-white, а для світлої fire

local_time = CTkLabel(win, font=('Arial', 14, 'bold'), anchor='center', text_color='white', width=800, height=10,
                      fg_color='black')
local_time.place(x=0, y=0)

def local_time_f():
    import time
    times = time.strftime('%d %b %H:%M:%S')
    local_time.configure(text=times)
    local_time.after(200, local_time_f)


# Creating buttons
for i, (text, icon, command) in enumerate(zip(button_texts, button_icons, button_command), start=1):
    button = CTkButton(win, text=text, font=button_font, fg_color=button_color,
                       image=icon, compound=button_compound,
                       width=button_g, height=button_g, hover_color=button_hover_color,
                       corner_radius=button_radius, command=command)
    button.place(x=23 + ((i - 1) % 4) * 197, y=90 + ((i - 1) // 4) * 200)
    buttons.append(button)

local_time_f()
win.mainloop()
