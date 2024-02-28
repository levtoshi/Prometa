from imports import *

win = CTk()
win.geometry('800x800+550+150')
win.resizable(False, False)

Main_Frame = CTkFrame(win, width = 0, height = 0)
Main_Frame.grid(row=0, column=0, padx=10, pady=80, sticky="nsew")