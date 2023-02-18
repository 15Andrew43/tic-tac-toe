
from tkinter import *

from model import Field, BadStep

is_win = False




def get_str_player(player):
    if player == 1:
        return 'X'
    elif player == -1:
        return 'O'


def click(root, field, row, col):
    global is_win
    try:
        is_win, player = field.make_step((row, col))
    except BadStep:
        print('Bad step is done, make another step.')
    if is_win:
        label = Label(root, text=f'{get_str_player(player)} won!!!')
        label.grid(row=0, column=0, columnspan=4, sticky="nsew")
    draw(root, field)
    

def draw(root, field):
    global is_win
    for row in range(field.sizes):
        for col in range(field.sizes):
            button = Button(root, text=get_str_player(field[row][col]),
                    command=lambda root=root, field=field, row=row, col=col: click(root, field, row, col))
            button.grid(row=row + 2, column=col, sticky="nsew")
            if is_win:
                button['state'] = DISABLED


def play_again(root, field, sizes):
    global is_win
    field = Field(sizes)
    is_win = False
    draw(root, field)
    label = Label(root, text='')
    label.grid(row=0, column=0, columnspan=4, sticky="nsew")


def play_desktop(sizes=3):

    field = Field(3)

    root = Tk()
    root.title('tic-tac-toe')

    button = Button(root, text='start again', command=lambda root=root, field=field, sizes=sizes: play_again(root, field, sizes))
    button.grid(row=2, column=3, sticky="nsew")

    draw(root, field)

    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)

    root.mainloop()


if __name__ == '__main__':
    play_desktop(sizes=3)
