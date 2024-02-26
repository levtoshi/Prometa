from win import *
def timer_start(parent):
    win = parent

    '''# Settings
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
        g = 1

    label_secl_sch = CTkLabel(win, text='0', width=num_width, height=num_height, font=text_font, text_color=text_color)
    label_secl_sch.place(x=462, y=230)

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


    def clear(g):
        global secl_sch, secb_sch, minl_sch, minb_sch, hl_sch, hb_sch, sec
        sec = 0
        secl_sch = 0
        secb_sch = 0
        minl_sch = 0
        minb_sch = 0
        hl_sch = 0
        hb_sch = 0

        first(1)

    def start(g):
        global button_stop, secl_sch, secb_sch, minl_sch, minb_sch, hl_sch, hb_sch, sec

        button_stop = CTkButton(win, width=200, height=70, text="Стоп",
                             font=('Arial',32), fg_color=button_stop_color, hover_color=button_stop_hover_color,
                             command=stop, corner_radius=33)
        button_stop.place(x=290, y=450)

        sec = 0
        secl_sch = 0
        secb_sch = 0
        minl_sch = 0
        minb_sch = 0
        hl_sch = 0
        hb_sch = 0

        if sec < 3600:

            label_secl_sch.place(x=462, y=230)
            label_secb_sch.place(x=407, y=230)
            label_sym2.place(x=377, y=220)
            label_minl_sch.place(x=319, y=230)
            label_minb_sch.place(x=266, y=230)

            for mb in range(6):
                for ml in  range(10):
                    for sb in range(6):
                        for sl in range(10):
                            sleep(1)
                            secl_sch += 1
                            sec += 1
                            label_secl_sch.configure(text=str(secl_sch))
                            label_secb_sch.configure(text=str(secb_sch))
                            label_minl_sch.configure(text=str(minl_sch))
                            label_minb_sch.configure(text=str(minb_sch))
                        secb_sch += 1
                    minl_sch += 1
                minb_sch += 1
            sec += 1

        if 72000 > sec >= 3600:

            label_secl_sch.place(x=529, y=230)
            label_secb_sch.place(x=474, y=230)
            label_sym2.place(x=444, y=220)
            label_minl_sch.place(x=389, y=230)
            label_minb_sch.place(x=336, y=230)
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
                                    secl_sch += 1
                                    sec += 1
                                    label_secl_sch.configure(text=str(secl_sch))
                                    label_secb_sch.configure(text=str(secb_sch))
                                    label_minl_sch.configure(text=str(minl_sch))
                                    label_minb_sch.configure(text=str(minb_sch))
                                    label_hl.configure(text=str(hl_sch))
                                    label_hb.configure(text=str(hb_sch))
                                secb_sch += 1
                            minl_sch += 1
                        minb_sch += 1
                    hl_sch += 1
                hb_sch += 1
            sec += 1

        if 86400 > sec >= 72000:

            label_secl_sch.place(x=529, y=230)
            label_secb_sch.place(x=474, y=230)
            label_sym2.place(x=444, y=220)
            label_minl_sch.place(x=389, y=230)
            label_minb_sch.place(x=336, y=230)
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
                                secl_sch += 1
                                sec += 1
                                label_secl_sch.configure(text=str(secl_sch))
                                label_secb_sch.configure(text=str(secb_sch))
                                label_minl_sch.configure(text=str(minl_sch))
                                label_minb_sch.configure(text=str(minb_sch))
                                label_hl.configure(text=str(hl_sch))
                            secb_sch += 1
                        minl_sch += 1
                    minb_sch += 1
                hl_sch += 1
            sec += 1

        if sec == 86400:
            clear(1)

    def stop():

        if button_stop.winfo_exists():
            button_stop.destroy()

        if sec < 3600:
            label_secl_sch.configure(text=str(secl_sch))
            label_secb_sch.configure(text=str(secb_sch))
            label_minl_sch.configure(text=str(minl_sch))
            label_minb_sch.configure(text=str(minb_sch))
        if 86400 > sec >= 3600:
            label_secl_sch.configure(text=str(secl_sch))
            label_secb_sch.configure(text=str(secb_sch))
            label_minl_sch.configure(text=str(minl_sch))
            label_minb_sch.configure(text=str(minb_sch))
            label_hl.configure(text=str(hl_sch))
            label_hb.configure(text=str(hb_sch))
        if sec == 86400:
            clear(1)

        button_reset = CTkButton(win, width=250, height=70, text="Закінчити",
                                 font = ('Arial',32), fg_color=button_start_color, hover_color=button_start_hover_color,
                                 command=first(1), corner_radius=33)
        button_reset.place(x=417, y=455)

    button_start = CTkButton(win, width=200, height=70, text="Старт",
                             font=('Arial', 32), fg_color=button_start_color, hover_color=button_start_hover_color,
                             command=start(1), corner_radius=33)
    button_start.place(x=290, y=450)

    start(1)
'''