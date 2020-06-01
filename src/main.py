from tkinter import *
from field import *


class App:
    columns, rows = 10, 10
    number_of_bombs = 10
    bomb_fields = []

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.fields = [[Field(x, y) for x in range(self.columns)]
                       for y in range(self.rows)]

        self.printBoardButton = Button(
            frame, text="print board", command=self.print_board)
        self.printBoardButton.pack(side=LEFT)

    def print_board(self):
        for column in range(self.columns):
            rowRepresentation = ""
            for row in range(self.rows):
                rowRepresentation = rowRepresentation + " " + \
                    self.show_field(self.fields[column][row])

            print(str(column) + " " + rowRepresentation)

    def show_field(self, field):
        if field.hasBomb:
            return "x"
        else:
            return "o"


root = Tk()

app = App(root)

root.mainloop()
root.destroy()
