from imports import *
from win import win
import tkinter
from emoji import emojize

emoji_list = [emojize(":win:")]

class Rock():
    def __init__(self, parent):
        self.root = parent
        self.startUI()

    def startUI(self):
        copyright = CTkLabel(self.root, text='by Maksym', font=('Arial', 18, 'bold'), width=150, height=50, anchor='center')
        copyright.place(relx=0.9, rely=0.05, anchor=tkinter.CENTER)
        btn = CTkButton(self.root, text="Камінь",
                     command=lambda x=1: self.btn_click(x), width=120,
                                 height=50)
        btn2 = CTkButton(self.root, text="Ножиці",
                      command=lambda x=2: self.btn_click(x), width=120,
                                 height=50)
        btn3 = CTkButton(self.root, text="Папір",
                      command=lambda x=3: self.btn_click(x), width=120,
                                 height=50)

        #btn.place(x=10, y=100)
        btn.place(relx=0.3, rely=0.25, anchor=tkinter.CENTER)
        btn2.place(relx=0.5, rely=0.25, anchor=tkinter.CENTER)
        btn3.place(relx=0.7, rely=0.25, anchor=tkinter.CENTER)

        self.lbl = CTkLabel(self.root, text="Початок гри!", font=("Times New Roman", 21, "bold"))
        self.lbl.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.win = self.drow = self.lose = 0

        self.lbl2 = CTkLabel(self.root, justify="left", font=("Times New Roman", 13),
                         text=f"Виграшей: {self.win}\nПрограшів:"
                              f" {self.lose}\nНічей: {self.drow}")
        self.lbl2.place(x=5, y=5)

    def btn_click(self, choise):
        comp_choise = randint(1, 3)

        if choise == comp_choise:
            self.drow += 1
            self.lbl.configure(text="🙃Нічия")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl.configure(text=f"😋Виграш")
        else:
            self.lose += 1
            self.lbl.configure(text="🤬Програш")

        self.lbl2.configure(text=f"Виграшей: {self.win}\nПрограшей:"
                              f" {self.lose}\nНічей: {self.drow}")

        del comp_choise

def rock_start(parent):
    app = Rock(parent)
    



