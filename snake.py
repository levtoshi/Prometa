from imports import *
from win import win
def snake_start(parent):

    winx = parent

    game_width = 780
    game_height = 700
    snake_speed = 70
    size = 40
    snake_parts = 3
    snake_color = 'green'
    food_color = 'red'
    bg_color = 'black'
    button_color = '#2147cf'
    button_hover_color = '#0228b0'


    class Snake:

        def __init__(self):

            self.body_parts = snake_parts
            self.coordinates = []
            self.squares = []


            for i in range(0, self.body_parts):
                self.coordinates.append([0, 0])


            for x, y in self.coordinates:
                square = board.create_rectangle(x, y, x + size, y + size, fill=snake_color, tags='snake')
                self.squares.append(square)


    class Food:

        def __init__(self):

            x = randint(0, (game_width // size) - 1) * size
            y = randint(0, (game_height // size) - 1) * size

            self.coordinates = [x, y]

            board.create_oval(x, y, x + size, y + size, fill=food_color, tags='food')

    def game_over():
        nonlocal score

        board.destroy()

        end = CTkLabel(winx, text='GAME OVER', font=('ArcadeClassic', 100), width=500, height=100, anchor='center',
                       text_color='#edbc34')
        end.place(x=140, y=150)

        tsc = CTkLabel(winx, text=f'TOTAL SCORE: {score}', font=('ArcadeClassic', 50), text_color='#8366d4',
                       width=300, height=100, anchor='center')
        tsc.place(x=240, y=300)

        button_start = CTkButton(winx, text='Start', font=('ArcadeClassic', 40), width=250, height=100, command=start,
                                 fg_color=button_color, hover_color=button_hover_color)
        button_start.place(x=265, y=450)

        score = 0

    def next_turn(snake, food):
        nonlocal size, score

        x, y = snake.coordinates[0]

        if direction == 'up':
            y -= size

        elif direction == 'down':
            y += size

        elif direction == 'right':
            x += size

        elif direction == 'left':
            x -= size

        snake.coordinates.insert(0, (x, y))

        square = board.create_rectangle(x, y, x + size, y + size, fill=snake_color)

        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:

            score += 1

            board.itemconfig(label, text=f'Score: {score}')

            board.delete('food')

            food = Food()

        else:

            del snake.coordinates[-1]

            board.delete(snake.squares[-1])

            del snake.squares[-1]

        if collision(snake):
            game_over()

        else:
            win.after(snake_speed, next_turn, snake, food)

    def ch_direction(new_direction):
        nonlocal direction

        if new_direction == 'up':
            if new_direction != 'down':
                direction = new_direction

        elif new_direction == 'down':
            if new_direction != 'up':
                direction = new_direction

        elif new_direction == 'right':
            if new_direction != 'left':
                direction = new_direction

        elif new_direction == 'left':
            if new_direction != 'right':
                direction = new_direction

    def collision(snake):

        x, y = snake.coordinates[0]

        if x < 0 or x >= game_width:
            return True

        elif y < 0 or y >= game_height:
            return True

        for snake_part in snake.coordinates[1:]:
            if x == snake_part[0] and y == snake_part[1]:
                return True

        return False


    score = 0
    direction = 'right'

    def start():
        global label, board

        button_start.destroy(), end.destroy(), tsc.destroy()
        board = CTkCanvas(winx, bg=bg_color, width=game_width, height=game_height)
        board.pack()
        label = board.create_text(50, 20, text=f'Score: {score}', font=('ArcadeClassic', 16), fill='white')

        win.update()
        snake = Snake()
        food = Food()

        win.bind('<Up>', lambda event: ch_direction('up'))
        win.bind('<Down>', lambda event: ch_direction('down'))
        win.bind('<Right>', lambda event: ch_direction('right'))
        win.bind('<Left>', lambda event: ch_direction('left'))

        win.bind('<w>', lambda event: ch_direction('up'))
        win.bind('<s>', lambda event: ch_direction('down'))
        win.bind('<d>', lambda event: ch_direction('right'))
        win.bind('<a>', lambda event: ch_direction('left'))

        next_turn(snake, food)


    button_start = CTkButton(winx, text='Start', font=('ArcadeClassic', 40), width=250, height=100, command=start,
                             fg_color=button_color, hover_color=button_hover_color)

    button_start.place(x=265, y=300)

    end = CTkLabel(winx, text='', font=('ArcadeClassic', 100), width=500, height=100, anchor='center',
                   text_color='#edbc34')
    end.place(x=140, y=150)

    tsc = CTkLabel(winx, text=f'', font=('ArcadeClassic', 50), text_color='#8366d4',
                   width=300, height=100, anchor='center')
    tsc.place(x=240, y=100)