import customtkinter
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image

app = customtkinter.CTk()
app.title('Prometa')
app.geometry('800x800')
app.config(bg='#1A1A1A')
app.resizable(False, False)

#TITLE
text = CTkLabel(master=app, text="Гра “Камінь, Ножниці, Папір”",font=("Gagalin",40),text_color="#FFFFFF",bg_color='#1A1A1A')
text.place(x=137,y=139)

#Stone

stone_button = CTkButton(master=app, height=289, width=231, fg_color="#545454",hover_color="#0FB700", bg_color='#1A1A1A', corner_radius=30,text="Камінь", font = ("Ermilov",20),)
stone_button.place(x=22,y=255)

#Scissors
scissors_button = CTkButton(master=app, height=289, width=231, fg_color="#545454",hover_color="#0FB700", bg_color='#1A1A1A', corner_radius=30,text="Ножниці", font = ("Ermilov",20),)
scissors_button.place(x=285,y=255)

#Paper
paper_button = CTkButton(master=app, height=289, width=231, fg_color="#545454",hover_color="#0FB700", bg_color='#1A1A1A', corner_radius=30,text="Папір", font = ("Ermilov",20),)
paper_button.place(x=547,y=255)

#Play Button
play_button = CTkButton(master=app, height=82, width=366, fg_color="#00147B",hover_color="#DB5C00", bg_color='#1A1A1A', corner_radius=50,text="Грати", font = ("Ermilov",20),)
play_button.place(x=217,y=602)


app.mainloop()