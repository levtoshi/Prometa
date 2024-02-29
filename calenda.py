from imports import *
from win import win
from tkcalendar import *
def calendar_start(parent):
    win = parent

    button_color = '#2147cf'
    button_hover_color = '#0228b0'

    cal = Calendar(win, firstweekday='monday', showweeknumbers=False, font="Arial 24",
                   date_pattern='dd-mm-y', selectmode='day', width=500, height=500, bordercolor='#2147cf',
                   selectbackground='#2147cf',
                   weekendbackground='#aacafa', weekendforeground='#000000', othermonthbackground='#93a4bd',
                   othermonthwebackground='#93a4bd', othermonthforeground='#2f2f30',
                   othermonthweforeground='#2f2f30')
    cal.place(x=125, y=50)

    def date():
        button_date.configure(width=0, height=0)
        button_clear.configure(text='Очистити', width=200, height=70)
        label.configure(text=f'{cal.get_date()}')

    def start():
        global button_date, button_clear, label
        button_date = CTkButton(win, text='Повна дата', font=('Arial', 24, 'bold'), fg_color=button_color, hover_color=button_hover_color,
                           width=200, height=70, anchor='center', command=date)
        button_date.place(x=290, y=450)

        button_clear = CTkButton(win, text='', font=('Arial', 24, 'bold'), fg_color='transparent',
                                 hover_color='#525252', border_width=3, border_color='white',
                                 width=0, height=0, anchor='center', command=start)
        button_clear.place(x=290, y=450)

        label = CTkLabel(win, text='', font=('Arial', 24, 'bold'), width=150, height=50, anchor='center')
        label.place(x=315, y=550)

    copyright = CTkLabel(win, text='by Dmytro', font=('Arial', 24, 'bold'), width=150, height=50, anchor='center')
    copyright.place(x=600, y=620)

    start()