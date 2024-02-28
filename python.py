from win import *

def python_start(parent):
    from utils import menu

    win = parent

    label_soon = CTkLabel(win, text='СКОРО...', font=('Arial', 72, 'bold'), anchor='center', width=780, height=700)
    label_soon.place(x=0, y=0)

'''    # Obj settings

    frame_wight = 750
    frame_height = 600
    scrollbar_button_color='#242423'
    scrollbar_button_hover_color='#40403f'
    orientation = 'vertical'
    frame_x = 0
    frame_y = 0

    button_font = ('Roboto', 13)
    button_radius = 33
    button_compound = 'top'
    button_color = '#383733'
    button_hover_color = '#474644'
    button_g = 25

    font = ('Arial', 15)
    string_w = 780
    string_h = 20
    str_x = 0

    # Tabview settings
    tabview = CTkTabview(win, width=780, height=700)
    tabview.pack()

    tabview.add('DATA')
    tabview.add('BASIC FUNC')
    tabview.add('INDEXING')
    tabview.add('IF,ELIF,ELSE')
    tabview.add('OPERATORS')
    tabview.add('RANDOM')
    tabview.add('MATH')
    tabview.add('FUNCTION')


    # DATA TYPES

    # Pics
    str_p = CTkImage(dark_image=Image.open('button_icons/py/str.png'), size=(20, 20))
    int_p = CTkImage(dark_image=Image.open('button_icons/py/int.png'), size=(string_w, 20))
    float_p = CTkImage(dark_image=Image.open('button_icons/py/float.png'), size=(string_w, 20))
    bool_p = CTkImage(dark_image=Image.open('button_icons/py/bool.png'), size=(string_w, 20))
    list_p = CTkImage(dark_image=Image.open('button_icons/py/list.png'), size=(string_w, 20))
    set_p = CTkImage(dark_image=Image.open('button_icons/py/set.png'), size=(string_w, 20))
    tuple_p = CTkImage(dark_image=Image.open('button_icons/py/tuple.png'), size=(string_w, 20))
    tuple1_p = CTkImage(dark_image=Image.open('button_icons/py/tupte with one.png'), size=(string_w, 20))
    dict_p  = CTkImage(dark_image=Image.open('button_icons/py/dictionary.png'), size=(string_w, 20))


    l1 = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                  font=font, width=string_w, height=string_h, text_color='white', anchor='w')

    l_str = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                     font=font, width=string_w, height=string_h, text_color='white', image=str_p)

    l2 = CTkLabel(tabview.tab('DATA'), text='int - це ціле число',
                  font=font, width=string_w, height=string_h, text_color='white', anchor='w')

    l_int = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                     font=font, width=string_w, height=string_h, text_color='white', image=int_p)

    l3 = CTkLabel(tabview.tab('DATA'), text='float - це дріб',
                  font=font, width=string_w, height=string_h, anchor='w')

    l_float = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                       font=font, width=string_w, height=string_h, text_color='white', image=float_p)

    l4 = CTkLabel(tabview.tab('DATA'), text='boolean(bool) - це логічне значення',
                  font=font, width=string_w, height=string_h, anchor='w')

    l_bool = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                      font=font, width=string_w, height=string_h, text_color='white', image=bool_p)

    l5 = CTkLabel(tabview.tab('DATA'), text='Тут може бути тільки або True, або False, 0 - це False, всі інші числа - True',
                  font=font, width=string_w, height=string_h, anchor='w')

    l6 = CTkLabel(tabview.tab('DATA'), text='list - це ряд значень, які мають індекс і їх можна змінити',
                  font=font, width=string_w, height=string_h, anchor='w')

    l_list = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                      font=font, width=string_w, height=string_h, text_color='white', image=list_p)

    l7 = CTkLabel(tabview.tab('DATA'), text='set - це ряд значень, які не мають індексу, дублікат не допускається,',
                  font=font, width=string_w, height=string_h, anchor='w')

    l_set = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                     font=font, width=string_w, height=string_h, text_color='white', image=set_p)

    l8 = CTkLabel(tabview.tab('DATA'),text='bool значення не допускається, але їх можна змінити',
                  font=font, width=string_w, height=string_h, anchor='w')

    l9 = CTkLabel(tabview.tab('DATA'), text='tuple - це ряд значень, які мають індекс і їх не можна змінити',
                  font=font, width=string_w, height=string_h, anchor='w')

    l_tuple = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                       font=font, width=string_w, height=string_h, text_color='white', image=tuple_p)

    l10 = CTkLabel(tabview.tab('DATA'), text='tuple з однією змінною позначається з комою в кінці:',
                   font=font, width=string_w, height=string_h, anchor='w')

    l_tuple1 = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                        font=font, width=string_w, height=string_h,
                        text_color='white', image=tuple1_p)

    l11 = CTkLabel(tabview.tab('DATA'), text='dictionary(dict) - це значення, які мають key та value до нього,',
                   font=font, width=string_w, height=string_h, anchor='w')

    l_dict = CTkLabel(tabview.tab('DATA'), text='string(str) - це текст',
                      font=font, width=string_w, height=string_h, text_color='white', image=dict_p)

    l12 = CTkLabel(tabview.tab('DATA'),text='їх можна змінити, дублікати не допускаються',
                   font=font, width=string_w, height=string_h, anchor='w')

    l1.place(x=str_x, y=0)
    l_str.place(x=str_x, y=30)
    l2.place(x=str_x, y=60)
    l_int.place(x=str_x, y=90)
    l3.place(x=str_x, y=120)
    l_float.place(x=str_x, y=150)
    l4.place(x=str_x, y=180)
    l_bool.place(x=str_x, y=210)
    l5.place(x=str_x, y=240)
    l6.place(x=str_x, y=270)
    l_list.place(x=str_x, y=300)
    l7.place(x=str_x, y=330)
    l_set.place(x=str_x, y=360)
    l8.place(x=str_x, y=390)
    l9.place(x=str_x, y=420)
    l_tuple.place(x=str_x, y=450)
    l10.place(x=str_x, y=480)
    l_tuple1.place(x=str_x, y=510)
    l11.place(x=str_x, y=540)
    l_dict.place(x=str_x, y=570)
    l12.place(x=str_x, y=600)

    tabview.update()
    tabview.tab('DATA').update()


    # BASIC FUNC
    basic_func = CTkScrollableFrame(tabview.tab('BASIC FUNC'), width=frame_wight, height=frame_height, orientation = orientation,
                                scrollbar_button_color=scrollbar_button_color,
                                scrollbar_button_hover_color=scrollbar_button_hover_color)
    basic_func.place(x=frame_x, y=frame_y)

    l14 = CTkLabel(basic_func, text='string(str) - це текст', font=font, width=string_w, height=string_h,
                  text_color='white')
    l14.place(x=0, y=0)

    l15 = CTkLabel(basic_func, text='int - це ціле число', font=font, width=string_w, height=string_h,
                  text_color='white')
    l15.place(x=0, y=110)

    l16 = CTkLabel(basic_func, text='float - це дріб', font=font, width=string_w, height=string_h)
    l16.place(x=0, y=210)

    l17 = CTkLabel(basic_func, text='boolean(bool) - це логічне значення', font=font, width=string_w, height=string_h)
    l17.place(x=0, y=310)

    l18 = CTkLabel(basic_func, text='Тут може бути тільки або True, або False, 0 - це False, всі інші числа - True',
                  font=font, width=string_w, height=string_h)
    l18.place(x=0, y=410)

    l19 = CTkLabel(basic_func, text='list - це ряд значень, які мають індекс і їх можна змінити', font=font,
                  width=string_w, height=string_h)
    l19.place(x=0, y=510)

    l20 = CTkLabel(basic_func, text='set - це ряд значень, які не мають індексу, дублікат не допускається,', font=font,
                  width=string_w, height=string_h)
    l20.place(x=0, y=610)

    l21 = CTkLabel(basic_func, text='bool значення не допускається, але їх можна змінити', font=font, width=string_w,
                  height=string_h)
    l21.place(x=0, y=710)

    l22 = CTkLabel(basic_func, text='tuple - це ряд значень, які мають індекс і їх не можна змінити', font=font,
                  width=string_w, height=string_h)
    l22.place(x=0, y=810)

    l23 = CTkLabel(basic_func, text='tuple - це ряд значень, які мають індекс і їх не можна змінити', font=font,
                   width=string_w, height=string_h)
    l23.place(x=0, y=910)

    l24 = CTkLabel(basic_func, text='tuple з однією змінною позначається з комою в кінці:', font=font, width=string_w,
                   height=string_h)
    l24.place(x=0, y=1010)

    l25 = CTkLabel(basic_func, text='dictionary(dict) - це значення, які мають key та value до нього,', font=font, width=string_w, height=string_h)
    l25.place(x=0, y=1110)

    l26 = CTkLabel(basic_func, text='їх можна змінити, дублікати не допускаються', font=font, width=string_w,
                   height=string_h)
    l26.place(x=0, y=1210)

    tabview.update()
    tabview.tab('BASIC FUNC').update()
    basic_func.update()





    # INDEXING
    indexing = CTkScrollableFrame(tabview.tab('INDEXING'), width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
    indexing.place(x=frame_x, y=frame_y)







    # IF,ELIF,ELSE
    branch_func = CTkScrollableFrame(tabview.tab('IF,ELIF,ELSE'), width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
    branch_func.place(x=frame_x, y=frame_y)






    # OPERATORS
    operators = CTkScrollableFrame(tabview.tab('OPERATORS'), width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
    operators.place(x=frame_x, y=frame_y)






    # RANDOM
    random = CTkScrollableFrame(tabview.tab('RANDOM'), width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
    random.place(x=frame_x, y=frame_y)






    # MATH
    math = CTkScrollableFrame(tabview.tab('MATH'), width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
    math.place(x=frame_x, y=frame_y)





    # FUNCTION
    def_ = CTkScrollableFrame(tabview.tab('FUNCTION'), width=frame_wight, height=frame_height, orientation = orientation,
                                   scrollbar_button_color=scrollbar_button_color,
                                   scrollbar_button_hover_color=scrollbar_button_hover_color)
    def_.place(x=frame_x, y=frame_y)'''


