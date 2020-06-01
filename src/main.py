from tkinter import *
from field import *
from random import randint


class App:
    columns, rows = 10, 10
    number_of_bombs = 10
    bomb_fields = []

    def __init__(self, master):
        frame = Frame(master)
        frame.grid(columns=self.columns, rows=self.rows)

        self.btn = [[0 for x in range(self.columns)] for y in range(self.rows)]

        self.fields = [[Field(x, y) for x in range(self.columns)]
                       for y in range(self.rows)]

        self.place_bombs()

        for x in range(self.columns):
            for y in range(self.rows):
                self.btn[x][y] = Button(
                    frame, text=self.fields[x][y].get_gui_content(), command=lambda x=x, y=y: self.click_button(x, y))
                self.btn[x][y].grid(column=x, row=y)

    def click_button(self, col, row):
        print(str(self.fields[col][row])+" clicked.")

        clickedField = self.fields[col][row]
        clickedField.isDiscovered = True

        self.print_board()
        self.update_gui()

    def update_gui(self):
        print("update_gui")

        for x in range(self.columns):
            for y in range(self.rows):
                self.btn[x][y]['text'] = self.fields[x][y].get_gui_content()

    def place_bombs(self):
        for i in range(self.number_of_bombs):
            self.place_bomb()

    def place_bomb(self):
        x = randint(0, self.columns - 1)
        y = randint(0, self.rows - 1)

        self.fields[x][y].hasBomb = True

    def print_board(self):
        print("Field:")

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
