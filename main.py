#Idea Opus Proventus
from utils import *

# Win Settings

win.geometry('800x800+550+150')
win.resizable(False, False)
win.iconbitmap('button_icons/fire.ico')
win.title('Prometa')
set_appearance_mode('dark')


win.title('Prometa')
win.iconbitmap('button_icons/fire-white.ico') # Для Макса - Тут для темної теми вікна береш fire-white, а для світлої fire



# Creating buttons
for i, (text, icon, command) in enumerate(zip(button_texts, button_icons, button_command), start=1):
    button = CTkButton(win, text=text, font=button_font, fg_color=button_color,
                       image=icon, compound=button_compound,
                       width=button_g, height=button_g, hover_color=button_hover_color,
                       corner_radius=button_radius, command=command)
    button.place(x=23 + ((i - 1) % 4) * 197, y=90 + ((i - 1) // 4) * 200)
    buttons.append(button)

win.mainloop()
