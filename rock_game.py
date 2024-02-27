from imports import *
def rock_start(parent):
    #win = CTk()
    #win.title('Prometa')
    #win.geometry('800x800')
    #win.config(bg='#1A1A1A')
    #win.resizable(False, False)

    win = parent

    # TITLE
    text = CTkLabel(master=win, text="Гра “Камінь, Ножниці, Папір”", font=("Ermilov", 30), text_color="#FFFFFF",
                    )
    text.place(x=137, y=139)

    # Stone

    stone_button = CTkButton(master=win, height=289, width=231, fg_color="#545454", hover_color="#0FB700",
                             corner_radius=30, text="Камінь", font=("Ermilov", 20), )
    stone_button.place(x=22-15, y=255)

    # Scissors
    scissors_button = CTkButton(master=win, height=289, width=231, fg_color="#545454", hover_color="#0FB700",
                                corner_radius=30, text="Ножниці", font=("Ermilov", 20), )
    scissors_button.place(x=285-15, y=255)

    # Paper

    paper_button = CTkButton(master=win, height=289, width=231, fg_color="#545454", hover_color="#0FB700",
                             corner_radius=30, text="Папір", font=("Ermilov", 20),)
    paper_button.place(x=547-15, y=255)
    Image.place(x=100,y=100)


    # Play Button
    play_button = CTkButton(master=win, height=82, width=366, fg_color="#00147B", hover_color="#DB5C00",
                            corner_radius=50, text="Грати", font=("Ermilov", 20), )
    play_button.place(x=217, y=602)