from win import *
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

    copyright = CTkLabel(win, text='by Dmytro', font=('Arial', 18, 'bold'), width=150, height=50, anchor='center')
    copyright.place(x=5, y=5)