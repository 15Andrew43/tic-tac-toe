
from tkinter import *

from model import Field, BadStep

# root = Tk()
# root.title('Calculator')

# buttons = (('7', '8', '9', '/', '4'),
#            ('4', '5', '6', '*', '4'),
#            ('1', '2', '3', '-', '4'),
#            ('0', '.', '=', '+', '4')
#            )

# activeStr = ''
# stack = []


# def calculate():
#     global stack
#     global label
#     result = 0
#     operand2 = Decimal(stack.pop())
#     operation = stack.pop()
#     operand1 = Decimal(stack.pop())

#     if operation == '+':
#         result = operand1 + operand2
#     if operation == '-':
#         result = operand1 - operand2
#     if operation == '/':
#         result = operand1 / operand2
#     if operation == '*':
#         result = operand1 * operand2
#     label.configure(text=str(result))



# def click(text):
#     global activeStr
#     global stack
#     if text == 'CE':
#         stack.clear()
#         activeStr = ''
#         label.configure(text='0')
#     elif '0' <= text <= '9':
#         activeStr += text
#         label.configure(text=activeStr)
#     elif text == '.':
#         if activeStr.find('.') == -1:
#             activeStr += text
#             label.configure(text=activeStr)
#     else:
#         if len(stack) >= 2:
#             stack.append(label['text'])
#             calculate()
#             stack.clear()
#             stack.append(label['text'])
#             activeStr = ''
#             if text != '=':
#                 stack.append(text)
#         else:
#             if text != '=':
#                 stack.append(label['text'])
#                 stack.append(text)
#                 activeStr = ''
#                 label.configure(text='0')



# label = Label(root, text='0', width=35)
# label.grid(row=0, column=0, columnspan=4, sticky="nsew")

# button = Button(root, text='CE', command=lambda text='CE': click(text))
# button.grid(row=1, column=3, sticky="nsew")
# for row in range(4):
#     for col in range(4):
#         button = Button(root, text=buttons[row][col],
#                 command=lambda row=row, col=col: click(buttons[row][col]))
#         button.grid(row=row + 2, column=col, sticky="nsew")

# root.grid_rowconfigure(6, weight=1)
# root.grid_columnconfigure(4, weight=1)

# root.mainloop()

def get_text(player):
    if player == 1:
        return 'X'
    elif player == -1:
        return 'O'


def click(root, field, row, col):
    try:
        field.make_step((row, col))
    except BadStep:
        print('Bad step is done, make another step.')

    print(field)
    draw(root, field)
    

def draw(root, field):
    for row in range(field.sizes):
        for col in range(field.sizes):
            button = Button(root, text=get_text(field[row][col]),
                    command=lambda root=root, field=field, row=row, col=col: click(root, field, row, col))
            button.grid(row=row + 2, column=col, sticky="nsew")



def play_desktop(sizes=3):

    field = Field(3)

    root = Tk()
    root.title('tic-tac-toe')

    button = Button(root, text='start again', command=lambda coordinates: click(coordinates))
    button.grid(row=2, column=3, sticky="nsew")

    draw(root, field)

    root.grid_rowconfigure(6, weight=1)
    root.grid_columnconfigure(4, weight=1)

    root.mainloop()




    

if __name__ == '__main__':
    play_desktop(sizes=3)