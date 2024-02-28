from imports import *
from win import win
import tkinter
import psutil
import math

def pc_start(parent):
    win = parent
    copyright = CTkLabel(win, text='by Maksym', font=('Arial', 18, 'bold'), width=150, height=50, anchor='center')
    copyright.place(x=5, y=5)

    memory_info = psutil.virtual_memory()
    cpu_count = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq()

    memory_info_total_lbl = CTkLabel(win, text=f"Всього ОЗУ пам'яті: {round(memory_info.total / (1024 ** 3) )} ГБ", font=("Times New Roman", 16, "bold"))
    memory_info_total_lbl.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    memory_info_avalible_lbl = CTkLabel(win, text=f"Обсяг доступно ОЗУ: {round(memory_info.available / (1024 ** 3))} ГБ", font=("Times New Roman", 16, "bold"))
    memory_info_avalible_lbl.place(relx=0.5, rely=0.15, anchor=tkinter.CENTER)

    cpu_count_lbl = CTkLabel(win, text=f"Фізичні ядра: {cpu_count}", font=("Times New Roman", 16, "bold"))
    cpu_count_lbl.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

    cpu_freq_lbl = CTkLabel(win, text=f"Частота процесора: {cpu_freq.max} Гц/с", font=("Times New Roman", 16, "bold"))
    cpu_freq_lbl.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)

