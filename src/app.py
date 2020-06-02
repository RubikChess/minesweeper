from tkinter import *
from field import *
from random import randint


class App:
    columns, rows = 10, 10
    number_of_bombs = 20
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
                    frame, text=self.get_gui_content(x, y), command=lambda x=x, y=y: self.click_button(x, y))
                self.btn[x][y].grid(column=x, row=y)

    def place_bombs(self):
        for i in range(self.number_of_bombs):
            self.place_bomb()

    def place_bomb(self):
        x = randint(0, self.columns - 1)
        y = randint(0, self.rows - 1)

        self.fields[x][y].hasBomb = True

    def get_gui_content(self, x, y):
        field = self.fields[x][y]

        if not field.isDiscovered:
            return "?"
        else:
            if field.hasBomb:
                return "X"
            else:
                neighbor_bombs = self.count_neighbor_bombs(x, y)
                return str(neighbor_bombs)

    def count_neighbor_bombs(self, x, y):
        number_of_bombs = 0

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if x+i > 0 and x+i < self.columns and y+j > 0 and y+j < self.rows:
                    if self.fields[x+i][y+j].hasBomb:
                        number_of_bombs = number_of_bombs+1

        return number_of_bombs

    def click_button(self, col, row):
        print(str(self.fields[col][row])+" clicked.")

        clickedField = self.fields[col][row]
        clickedField.isDiscovered = True
        self.btn[col][row]["state"] = "disabled"

        self.print_board()
        self.update_gui()

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

    def update_gui(self):
        print("update_gui")

        for x in range(self.columns):
            for y in range(self.rows):
                self.btn[x][y]["text"] = self.get_gui_content(x, y)