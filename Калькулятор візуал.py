import customtkinter
from tkinter import *
from tkinter import messagebox
from customtkinter import *

app = customtkinter.CTk()
app.title('Калькулятор')
app.geometry('310x564')
app.config(bg='#c9c9c9')
app.resizable(False, False)

font1 = ('Comic Sans MS',40,'bold')
font2 = ('e-Ukraine',20,'head')

#Screen
equation_entry = customtkinter.CTkEntry(app,font=font1,text_color='#FFFFFF',fg_color='#5a5a5a',width=295,height=155,corner_radius=15,bg_color='#c9c9c9')
equation_entry.place(x=7,y=12)

#Buttons:

#C/Clear
b1_button = customtkinter.CTkButton(app,command=lambda: button_click('С'),font=font1, text_color='#ffffff', text='С',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b1_button.place(x=7,y=176)

#/
b2_button = customtkinter.CTkButton(app,command=lambda: button_click('/'),font=font1, text_color='#ffffff', text='/',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b2_button.place(x=82,y=176)

#*
b3_button = customtkinter.CTkButton(app,command=lambda: button_click('*'),font=font1, text_color='#ffffff', text='*',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b3_button.place(x=158,y=176)

#%
b4_button = customtkinter.CTkButton(app,command=lambda: button_click('%'),font=font1, text_color='#ffffff', text='%',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b4_button.place(x=234,y=176)

#-
b5_button = customtkinter.CTkButton(app,command=lambda: button_click('-'),font=font1, text_color='#ffffff', text='-',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b5_button.place(x=234,y=253)

#+
b6_button = customtkinter.CTkButton(app,command=lambda: button_click('+'),font=font1, text_color='#ffffff', text='+',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b6_button.place(x=234,y=330)

#+
b7_button = customtkinter.CTkButton(app,command=lambda: button_click('='),font=font1, text_color='#ffffff', text='=',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=146,width=68,corner_radius=16)
b7_button.place(x=234,y=409)

#.
b8_button = customtkinter.CTkButton(app,command=lambda: button_click('.'),font=font1, text_color='#ffffff', text='.',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b8_button.place(x=158,y=482)

#Цифра
#0
b9_button = customtkinter.CTkButton(app,command=lambda: button_click('0'),font=font1, text_color='#ffffff', text='0',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=142,corner_radius=16)
b9_button.place(x=9,y=482)

#1
b10_button = customtkinter.CTkButton(app,command=lambda: button_click('1'),font=font1, text_color='#ffffff', text='1',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b10_button.place(x=9,y=409)

#2
b11_button = customtkinter.CTkButton(app,command=lambda: button_click('2'),font=font1, text_color='#ffffff', text='2',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b11_button.place(x=84,y=409)

#3
b12_button = customtkinter.CTkButton(app,command=lambda: button_click('3'),font=font1, text_color='#ffffff', text='3',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b12_button.place(x=158,y=409)

#4
b13_button = customtkinter.CTkButton(app,command=lambda: button_click('4'),font=font1, text_color='#ffffff', text='4',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b13_button.place(x=9,y=329)

#5
b14_button = customtkinter.CTkButton(app,command=lambda: button_click('5'),font=font1, text_color='#ffffff', text='5',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b14_button.place(x=84,y=329)

#6
b15_button = customtkinter.CTkButton(app,command=lambda: button_click('6'),font=font1, text_color='#ffffff', text='6',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b15_button.place(x=158,y=329)

#7
b16_button = customtkinter.CTkButton(app,command=lambda: button_click('7'),font=font1, text_color='#ffffff', text='7',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b16_button.place(x=9,y=253)

#8
b17_button = customtkinter.CTkButton(app,command=lambda: button_click('8'),font=font1, text_color='#ffffff', text='8',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b17_button.place(x=85,y=253)

#9
b18_button = customtkinter.CTkButton(app,command=lambda: button_click('9'),font=font1, text_color='#ffffff', text='9',fg_color='#a0a0a0',hover_color='#3d3d3d',bg_color='#c9c9c9',border_color='#000000', height=68,width=68,corner_radius=16)
b18_button.place(x=158,y=253)

#title

"""title = customtkinter.CTkLabel(app, text_color='#ffffff', text='Калькулятор', font=font2, fg_color='#a0a0a0', hover_color='#3d3d3d', border_color='#000000', height=68, width=10, corner_radius=16)  # Замінено CTkTextbox на CTkLabel
title.place(x=83, y=10)"""

app.mainloop()