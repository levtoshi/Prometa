from imports import *
import tkinter
from tkinter import filedialog

def Save():

    if len(txt.get()) > 1:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(txt.get())
                messagebox.showinfo('Успіх', 'Файл успішно збережено!')


def notes_start(parent):
    global txt
    txt = CTkEntry(master=parent, placeholder_text="Введіть свій текст", width=600, height=400, border_width=2,
                   corner_radius=10)
    txt.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    save = CTkButton(master=parent, width=120,
                     height=32,
                     border_width=0,
                     corner_radius=8,
                     text="Зберегти",
                     command=Save)

    save.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)

    copyright = CTkLabel(parent, text='by Maksym', font=('Arial', 18, 'bold'), width=150, height=50, anchor='center')
    copyright.place(x=5, y=5)