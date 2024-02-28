from imports import *
def calc_start(parent):

    #app = CTk()
    #app.title('Калькулятор')
    #app.geometry('310x564')
    #app.config(bg='#c9c9c9')
    #app.resizable(False, False)

    app = parent

    font1 = ('Comic Sans MS',40,'bold')
    font2 = ('e-Ukraine',20,'head')

    def button_click(number):
        equation_entry.insert(END,number)

    def clear():
        equation_entry.delete(0,END)

    def calculate():
        try:
            equation = equation_entry.get()
            new_equation = equation.replace('X','*')
            result = eval(new_equation)
            clear()
            equation_entry.insert(0,result)
        except ZeroDivisionError:
            messagebox.showerror('Error','На 0 ділити не можна!!!\nНавіть не намагайся бо System32 видалю')
        except:
            messagebox.showerror('Error','Введено не правильні значення')


    #Screen
    equation_entry = CTkEntry(app,font=font1,text_color='#FFFFFF',fg_color='#5a5a5a',width=295,height=155,corner_radius=15)
    equation_entry.place(x=220+7,y= 50+12)

    #Buttons:

    #C/Clear
    b1_button = CTkButton(app,command=clear,font=font1, text_color='#ffffff', text='С',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b1_button.place(x=220+7,y= 50+176)

    #/
    b2_button = CTkButton(app,command=lambda: button_click('/'),font=font1, text_color='#ffffff', text='/',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b2_button.place(x=220+82,y= 50+176)

    #*
    b3_button = CTkButton(app,command=lambda: button_click('*'),font=font1, text_color='#ffffff', text='*',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b3_button.place(x=220+158,y= 50+176)

    #%
    b4_button = CTkButton(app,command=lambda: button_click('%'),font=font1, text_color='#ffffff', text='%',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b4_button.place(x=220+234,y= 50+176)

    #-
    b5_button = CTkButton(app,command=lambda: button_click('-'),font=font1, text_color='#ffffff', text='-',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b5_button.place(x=220+234,y= 50+253)

    #+
    b6_button = CTkButton(app,command=lambda: button_click('+'),font=font1, text_color='#ffffff', text='+',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b6_button.place(x=220+234,y= 50+330)

    #=
    b7_button = CTkButton(app,command=calculate,font=font1, text_color='#ffffff', text='=',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=146,width=68,corner_radius=16)
    b7_button.place(x=220+234,y= 50+409)

    #.
    b8_button = CTkButton(app,command=lambda: button_click('.'),font=font1, text_color='#ffffff', text='.',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b8_button.place(x=220+158,y= 50+482)

    #Цифра
    #0
    b9_button = CTkButton(app,command=lambda: button_click('0'),font=font1, text_color='#ffffff', text='0',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=142,corner_radius=16)
    b9_button.place(x=220+9,y= 50+482)

    #1
    b10_button = CTkButton(app,command=lambda: button_click('1'),font=font1, text_color='#ffffff', text='1',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b10_button.place(x=220+9,y= 50+409)

    #2
    b11_button = CTkButton(app,command=lambda: button_click('2'),font=font1, text_color='#ffffff', text='2',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b11_button.place(x=220+84,y= 50+409)

    #3
    b12_button = CTkButton(app,command=lambda: button_click('3'),font=font1, text_color='#ffffff', text='3',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b12_button.place(x=220+158,y= 50+409)

    #4
    b13_button = CTkButton(app,command=lambda: button_click('4'),font=font1, text_color='#ffffff', text='4',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b13_button.place(x=220+9,y= 50+329)

    #5
    b14_button = CTkButton(app,command=lambda: button_click('5'),font=font1, text_color='#ffffff', text='5',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b14_button.place(x=220+84,y= 50+329)

    #6
    b15_button = CTkButton(app,command=lambda: button_click('6'),font=font1, text_color='#ffffff', text='6',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b15_button.place(x=220+158,y= 50+329)

    #7
    b16_button = CTkButton(app,command=lambda: button_click('7'),font=font1, text_color='#ffffff', text='7',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b16_button.place(x=220+9,y= 50+253)

    #8
    b17_button = CTkButton(app,command=lambda: button_click('8'),font=font1, text_color='#ffffff', text='8',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b17_button.place(x=220+85,y= 50+253)

    #9
    b18_button = CTkButton(app,command=lambda: button_click('9'),font=font1, text_color='#ffffff', text='9',fg_color='#a0a0a0',hover_color='#3d3d3d',border_color='#000000', cursor='hand2', height=68,width=68,corner_radius=16)
    b18_button.place(x=220+158,y= 50+253)

    #title

    """title = CTkLabel(app, text_color='#ffffff', text='Калькулятор', font=font2, fg_color='#a0a0a0', hover_color='#3d3d3d', border_color='#000000', height=68, width=10, corner_radius=16)  # Замінено CTkTextbox на CTkLabel
    title.place(x=83, y= 50+10)"""

    copyright = CTkLabel(app, text='by Bogdan', font=('Arial', 18, 'bold'), width=150, height=50, anchor='center')
    copyright.place(x=5, y=5)