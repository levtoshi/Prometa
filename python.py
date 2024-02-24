import time

from imports import *
from win import win

#python_frame_obj_list = []

def python_start():
    print('In process')
    '''from utils import menu
    global python_frame_obj_list

    # Obj settings

    frame_g = 800
    scrollbar_button_color='#242423'
    scrollbar_button_hover_color='#40403f'
    orientation = 'vertical'

    ico_size = (50, 50)

    button_font = ('Roboto', 13)
    button_color = '#2147cf'
    button_hover_color = '#0228b0'
    button_g = 150
    button_ico_size = (80, 80)
    button_radius = 33
    button_compound = 'top'

    # Icons
    button_next_ico = CTkImage(dark_image=Image.open('button_icons/next_for_black.png'),
                                   light_image=Image.open('button_icons/next_for_white.png'), size=ico_size)

    button_back_ico = CTkImage(dark_image=Image.open('button_icons/previous_for_black.png'),
                                   light_image=Image.open('button_icons/previous_for_white.png'), size=ico_size)


    page = 0

    def next():
        nonlocal page
        if -1 < page < 7:
            for i in check_list:
                for j in i:
                    j.destroy()
            check_list.clear()
            frame_list[page + 1]
            page += 1
        else:
            pass

    def back():
        nonlocal page

        if 0 < page < 8:
            for i in check_list:
                for j in i:
                    j.destroy()
            check_list.clear()
            frame_list[page - 1]
            page -= 1
        else:
            pass


    check_list = []

    fdata_obj = []
    data_obj = fdata_obj
    def fdata(v):
        vs = v

        data_types = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                scrollbar_button_color=scrollbar_button_color,
                                scrollbar_button_hover_color=scrollbar_button_hover_color)
        data_types.place(x=0, y=0)
        back_ = CTkButton(data_types, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l1 = CTkLabel(data_types, text='Label1')
        l1.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        fdata_obj.append(button_next)
        fdata_obj.append(l1)
        fdata_obj.append(data_types)
        fdata_obj.append(back_)

        check_list.append(fdata_obj)


    fbasic_obj = []
    def fbasic_func():
        basic_func = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                scrollbar_button_color=scrollbar_button_color,
                                scrollbar_button_hover_color=scrollbar_button_hover_color)
        basic_func.place(x=0, y=0)
        back_ = CTkButton(basic_func, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l2 = CTkLabel(basic_func, text='Label2')
        l2.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        fbasic_obj.append(button_next)
        fbasic_obj.append(button_back)
        fbasic_obj.append(l2)
        fbasic_obj.append(basic_func)
        fbasic_obj.append(back_)
        check_list.append(fbasic_obj)

    findex_obj = []
    def findex():

        indexing = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        indexing.place(x=0, y=0)
        back_ = CTkButton(indexing, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l3 = CTkLabel(indexing, text='Label3')
        l3.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        findex_obj.append(button_next)
        findex_obj.append(button_back)
        findex_obj.append(l3)
        findex_obj.append(indexing)
        findex_obj.append(back_)
        check_list.append(findex_obj)

    fbranch_obj = []
    def fbranch():

        branch_func = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        branch_func.place(x=0, y=0)
        back_ = CTkButton(branch_func, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l4 = CTkLabel(branch_func, text='Label4')
        l4.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        fbranch_obj.append(button_next)
        fbranch_obj.append(button_back)
        fbranch_obj.append(l4)
        fbranch_obj.append(branch_func)
        fbranch_obj.append(back_)
        check_list.append(fbranch_obj)

    foperators_obj = []
    def foperators():

        operators = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        operators.place(x=0, y=0)
        back_ = CTkButton(operators, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l5 = CTkLabel(operators, text='Label5')
        l5.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        foperators_obj.append(button_next)
        foperators_obj.append(button_back)
        foperators_obj.append(l5)
        foperators_obj.append(operators)
        foperators_obj.append(back_)
        check_list.append(foperators_obj)

    frandom_obj = []
    def frandom():

        random = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        random.place(x=0, y=0)
        back_ = CTkButton(random, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l6 = CTkLabel(random, text='Label6')
        l6.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        frandom_obj.append(button_next)
        frandom_obj.append(button_back)
        frandom_obj.append(l6)
        frandom_obj.append(random)
        frandom_obj.append(back_)
        check_list.append(frandom_obj)

    fmath_obj = []
    def fmath():

        math = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        math.place(x=0, y=0)
        back_ = CTkButton(math, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l7 = CTkLabel(math, text='Label7')
        l7.pack()

        button_next = CTkButton(win, width=50, height=50, text='', image=button_next_ico, command=next)
        button_next.place(x=730, y=375)

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        fmath_obj.append(button_next)
        fmath_obj.append(button_back)
        fmath_obj.append(l7)
        fmath_obj.append(math)
        fmath_obj.append(back_)
        check_list.append(fmath_obj)

    fdef_obj = []
    def fdef_():

        def_ = CTkScrollableFrame(win, width=frame_g, height=frame_g, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
        def_.place(x=0, y=0)
        back_ = CTkButton(def_, text='Назад', font=button_font, fg_color=button_color,
                          width=button_g, height=50, hover_color=button_hover_color,
                          corner_radius=button_radius, command=menu)
        back_.place(x=10, y=10)
        l8 = CTkLabel(def_, text='Label8')
        l8.pack()

        button_back = CTkButton(win, width=50, height=50, text='', image=button_back_ico, command=back)
        button_back.place(x=5, y=375)

        fdef_obj.append(button_back)
        fdef_obj.append(l8)
        fdef_obj.append(def_)
        fdef_obj.append(back_)
        check_list.append(fdef_obj)

    frame_list = [fdata(0), fbasic_func, findex, fbranch, foperators, frandom, fmath, fdef_]
    fdata(0)

    python_frame_obj_list += data_obj
    python_frame_obj_list += fbasic_obj
    python_frame_obj_list += findex_obj
    python_frame_obj_list += fbranch_obj
    python_frame_obj_list += foperators_obj
    python_frame_obj_list += frandom_obj
    python_frame_obj_list += fmath_obj
    python_frame_obj_list += fdef_obj



def clear_py():
    global python_frame_obj_list
    print(python_frame_obj_list)
    for list in python_frame_obj_list:
        print(list)
        for obj in list:
            print(obj)
            obj.destroy()

'''