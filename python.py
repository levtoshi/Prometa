from win import *

def python_start(parent):
    from utils import menu

    '''win = parent

    # Obj settings

    frame_wight = 650
    frame_height = 700
    scrollbar_button_color='#242423'
    scrollbar_button_hover_color='#40403f'
    orientation = 'vertical'
    frame_x = 55
    frame_y = 0

    ico_size = (25, 25)

    button_font = ('Roboto', 13)
    button_radius = 33
    button_compound = 'top'
    button_color = '#383733'
    button_hover_color = '#474644'
    button_g = 25

    # Icons
    button_next_ico = CTkImage(dark_image=Image.open('button_icons/right.png'),
                                   light_image=Image.open('button_icons/right.png'), size=ico_size)

    button_back_ico = CTkImage(dark_image=Image.open('button_icons/left.png'),
                                   light_image=Image.open('button_icons/left.png'), size=ico_size)


    page = 0

    def next():
        nonlocal page
        if -1 < page < 7:
            child_elem = check_list[0].winfo_children()  # Всі обєкти які в фреймі
            for child in child_elem:
                child.destroy()
            check_list.clear()
            frame_list[page + 1]
            page += 1
        else:
            pass

    def back():
        nonlocal page

        if 0 < page < 8:
            child_elem = check_list[0].winfo_children()  # Всі обєкти які в фреймі
            for child in child_elem:
                child.destroy()
            check_list.clear()
            frame_list[page - 1]
            page -= 1
        else:
            pass

    if page < 7:

        button_next = CTkButton(win, width=button_g, height=button_g, text='', image=button_next_ico, command=next,
                                fg_color=button_color, hover_color=button_hover_color)
        button_next.place(x=733, y=335)

    if 0 < page < 8:

        button_back = CTkButton(win, width=button_g, height=button_g, text='', image=button_back_ico, command=back,
                                fg_color=button_color, hover_color=button_hover_color)
        button_back.place(x=7, y=335)

    check_list = []

    def fdata(v):
        vs = v

        data_types = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                scrollbar_button_color=scrollbar_button_color,
                                scrollbar_button_hover_color=scrollbar_button_hover_color)
        data_types.place(x=frame_x, y=frame_y)

        l1 = CTkLabel(data_types, text='Label1')
        l1.pack()

        check_list.append(data_types)


    def fbasic_func():
        basic_func = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                scrollbar_button_color=scrollbar_button_color,
                                scrollbar_button_hover_color=scrollbar_button_hover_color)
        basic_func.place(x=frame_x, y=frame_y)

        l2 = CTkLabel(basic_func, text='Label2')
        l2.pack()

        check_list.append(basic_func)

    def findex():

        indexing = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        indexing.place(x=frame_x, y=frame_y)

        l3 = CTkLabel(indexing, text='Label3')
        l3.pack()

        check_list.append(indexing)

    def fbranch():

        branch_func = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        branch_func.place(x=frame_x, y=frame_y)
        l4 = CTkLabel(branch_func, text='Label4')
        l4.pack()

        check_list.append(branch_func)

    def foperators():

        operators = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        operators.place(x=frame_x, y=frame_y)
        l5 = CTkLabel(operators, text='Label5')
        l5.pack()

        check_list.append(operators)

    def frandom():

        random = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        random.place(x=frame_x, y=frame_y)
        l6 = CTkLabel(random, text='Label6')
        l6.pack()

        check_list.append(random)

    def fmath():

        math = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        math.place(x=frame_x, y=frame_y)
        l7 = CTkLabel(math, text='Label7')
        l7.pack()

        check_list.append(math)

    def fdef_():

        def_ = CTkScrollableFrame(win, width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        def_.place(x=frame_x, y=frame_y)
        l8 = CTkLabel(def_, text='Label8')
        l8.pack()

        check_list.append(def_)

    frame_list = [fdata(0), fbasic_func, findex, fbranch, foperators, frandom, fmath, fdef_]
    fdata(0)
'''