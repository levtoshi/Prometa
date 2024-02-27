from win import *
'''def timer_start(parent):
    win = parent

    # Settings
    button_start_color = '#2147cf'
    button_start_hover_color = '#0228b0'
    button_stop_color = '#525252'
    button_stop_hover_color = '#707070'
    text_font = ('Arial', 96)
    text_color = 'white'
    num_width = 55
    num_height = 110
    sym_width = 30
    sym_height = 100

    def first(g):
        global label_secl, label_secb, label_sym2, label_minl, label_minb, label_sym1, label_hl, label_hb
        g = 1

        label_secl = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)
        label_secl.place(x=462, y=230)

        label_secb_sch = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)
        label_secb_sch.place(x=407, y=230)

        label_sym2 = CTkLabel(win, text=':', width=sym_width, height=sym_height, font=text_font, text_color=text_color)
        label_sym2.place(x=377, y=220)

        label_minl_sch = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)
        label_minl_sch.place(x=319, y=230)

        label_minb_sch = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)
        label_minb_sch.place(x=266, y=230)

        label_sym1 = CTkLabel(win, text=':', width=num_width, height=num_height, font=text_font, text_color=text_color)
        label_hl = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)
        label_hb = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)

        button_start = CTkButton(win, width=200, height=70, text="Старт",
                                 font=('Arial', 32), fg_color=button_start_color, hover_color=button_start_hover_color,
                                 command=start, corner_radius=33)
        button_start.place(x=290, y=450)

        print('FIRST')


    def start():
        global button_stop, secl, secb, minl, minb, hl, hb, sec

        button_stop = CTkButton(win, width=200, height=70, text="Стоп",
                             font=('Arial',32), fg_color=button_stop_color, hover_color=button_stop_hover_color,
                             command=stop, corner_radius=33)
        button_stop.place(x=290, y=450)

        sec = 0
        secl = 0
        secb = 0
        minl = 0
        minb = 0
        hl = 0
        hb = 0

        if sec < 3600:

            label_secl.place(x=462, y=230)
            label_secb.place(x=407, y=230)
            label_sym2.place(x=377, y=220)
            label_minl.place(x=319, y=230)
            label_minb.place(x=266, y=230)

            for mb in range(6):
                for ml in  range(10):
                    for sb in range(6):
                        for sl in range(10):
                            sleep(1)
                            secl += 1
                            sec += 1
                            label_secl.configure(text=str(secl))
                            label_secb.configure(text=str(secb))
                            label_minl.configure(text=str(minl))
                            label_minb.configure(text=str(minb))
                            print(f'{minb}:{minl}:{secb}:{secl}')
                        secb += 1
                    minl += 1
                minb += 1
            sec += 1

        if 72000 > sec >= 3600:

            label_secl.place(x=529, y=230)
            label_secb.place(x=474, y=230)
            label_sym2.place(x=444, y=220)
            label_minl.place(x=389, y=230)
            label_minb.place(x=336, y=230)
            label_sym1.place(x=306, y=220)
            label_hl.place(x=253, y=230)
            label_hb.place(x=200, y=230)

            for hb in range(2):
                for hl in range(10):
                    for mb in range(6):
                        for ml in range(10):
                            for sb in range(6):
                                for sl in range(10):
                                    sleep(1)
                                    secl += 1
                                    sec += 1
                                    label_secl.configure(text=str(secl))
                                    label_secb.configure(text=str(secb))
                                    label_minl.configure(text=str(minl))
                                    label_minb.configure(text=str(minb))
                                    label_hl.configure(text=str(hl))
                                    label_hb.configure(text=str(hb))
                                secb += 1
                            minl += 1
                        minb += 1
                    hl += 1
                hb += 1
            sec += 1

        if 86400 > sec >= 72000:

            label_secl.place(x=529, y=230)
            label_secb.place(x=474, y=230)
            label_sym2.place(x=444, y=220)
            label_minl.place(x=389, y=230)
            label_minb.place(x=336, y=230)
            label_sym1.place(x=306, y=220)
            label_hl.place(x=253, y=230)
            label_hb.place(x=200, y=230)

            label_hb.configure(text=str(2))
            for hl in range(5):
                for mb in range(6):
                    for ml in range(10):
                        for sb in range(6):
                            for sl in range(10):
                                sleep(1)
                                secl += 1
                                sec += 1
                                label_secl.configure(text=str(secl))
                                label_secb.configure(text=str(secb))
                                label_minl.configure(text=str(minl))
                                label_minb.configure(text=str(minb))
                                label_hl.configure(text=str(hl))
                            secb += 1
                        minl += 1
                    minb += 1
                hl += 1
            sec += 1

        if sec == 86400:
            clear()

    def clear():

        sec = 0
        secl = 0
        secb = 0
        minl = 0
        minb = 0
        hl = 0
        hb = 0

        first(1)

    def stop():

        if button_stop.winfo_exists():
            button_stop.destroy()

        if sec < 3600:
            label_secl.configure(text=str(secl))
            label_secb.configure(text=str(secb))
            label_minl.configure(text=str(minl))
            label_minb.configure(text=str(minb))
        if 86400 > sec >= 3600:
            label_secl.configure(text=str(secl))
            label_secb.configure(text=str(secb))
            label_minl.configure(text=str(minl))
            label_minb.configure(text=str(minb))
            label_hl.configure(text=str(hl))
            label_hb.configure(text=str(hb))
        if sec == 86400:
            clear()

        button_reset = CTkButton(win, width=250, height=70, text="Закінчити",
                                 font = ('Arial',32), fg_color=button_start_color, hover_color=button_start_hover_color,
                                 command=first(1), corner_radius=33)
        button_reset.place(x=417, y=455)

    first(1)
    win.mainloop()
timer_start(Main_Frame)'''

def timer_start(parent):
    win = parent

    font = ('Arial', 33, 'bold')
    color = '#2147cf'
    hover_color = '#0228b0'
    radius = 33
    width = 200
    height = 70

    status = False
    hours, minutes, seconds = 0, 0, 0

    def start():
        nonlocal status

        if not status:
            update_func()
            status = True

    def pause():
        nonlocal status

        if status:
            stopwatch.after_cancel(time_update)
            status = False

    def reset_func():
        nonlocal status, hours, minutes, seconds

        if status:
            stopwatch.after_cancel(time_update)
            status = False

        hours, minutes, seconds = 0, 0, 0
        stopwatch.configure(text='00:00:00')

    def update_func():
        nonlocal hours, minutes, seconds
        global time_update

        seconds += 1

        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            hours += 1
            minutes = 0

        if hours > 9:
            hours_str = f'{hours}'
        else:
            hours_str = f'0{hours}'

        if minutes > 9:
            minutes_str = f'{minutes}'
        else:
            minutes_str = f'0{minutes}'

        if seconds > 9:
            seconds_str = f'{seconds}'
        else:
            seconds_str = f'0{seconds}'

        stopwatch.configure(text=f'{hours_str}:{minutes_str}:{seconds_str}')

        time_update = stopwatch.after(1000, update_func)

    stopwatch = CTkLabel(win, text='00:00:00', font=('Arial', 96), text_color='white',
                         width=400, height=100)
    stopwatch.place(x=190, y=200)

    button_start = CTkButton(win , text='СТАРТ', font=font, fg_color=color,
                             hover_color=hover_color, command=start, width=width, height=height)
    button_pause = CTkButton(win , text='ПАУЗА', font=font, fg_color=color,
                             hover_color=hover_color, command=pause, width=width, height=height)
    button_reset = CTkButton(win , text='СКИНУТИ', font=font, fg_color=color,
                             hover_color=hover_color, command=reset_func, width=width, height=height)

    button_start.place(x=50, y=450)
    button_pause.place(x=290, y=450)
    button_reset.place(x=530, y=450)
    
