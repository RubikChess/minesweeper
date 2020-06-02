from tkinter import *
from field import *
from random import randint


class App:
    columns, rows = 10, 10
    number_of_bombs = 20
    bomb_fields = []

    def __init__(self, master):
        self.btn = [[0 for x in range(self.columns)] for y in range(self.rows)]

        self.fields = [[Field(x, y) for x in range(self.columns)]
                       for y in range(self.rows)]

        self.place_bombs()

        self.init_buttons(master)

    def place_bombs(self):
        for i in range(self.number_of_bombs):
            self.place_bomb()

    def place_bomb(self):
        col = randint(0, self.columns - 1)
        row = randint(0, self.rows - 1)

        self.fields[col][row].hasBomb = True

    def get_gui_content(self, col, row):
        field = self.fields[col][row]

        if not field.isDiscovered:
            return "?"
        else:
            if field.hasBomb:
                return "X"
            else:
                neighbor_bombs = self.count_neighbor_bombs(col, row)
                return str(neighbor_bombs)

    def count_neighbor_bombs(self, col, row):
        number_of_bombs = 0

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if col+i > 0 and col+i < self.columns and row+j > 0 and row+j < self.rows:
                    if self.fields[col+i][row+j].hasBomb:
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

        for col in range(self.columns):
            for row in range(self.rows):
                self.btn[col][row]["text"] = self.get_gui_content(col, row)

    def init_buttons(self, frame):
        for col in range(self.columns):
            for row in range(self.rows):
                self.btn[col][row] = Button(
                    master=frame,
                    text=self.get_gui_content(col, row),
                    command=lambda x=col, y=row: self.click_button(x, y))

                self.btn[col][row].place(x=row*40, y=col*40, width=40, height=40)
