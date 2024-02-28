from imports import *
from win import win
def calendar_start(parent):
    win = parent

    label_soon = CTkLabel(win, text='СКОРО...', font=('Arial', 72, 'bold'), anchor='center', width=780, height=700)
    label_soon.place(x=0, y=0)