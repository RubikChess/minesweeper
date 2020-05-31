from tkinter import *
from field import *


class App:
    columns, rows = 10, 10

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.fields = [[Field(x,y) for x in range(self.columns)] for y in range(self.rows)]

        self.printBoardButton = Button(frame, text="print board", command=self.printBoard)
        self.printBoardButton.pack(side=LEFT)

    def printBoard(self):
        print(self.fields)


root = Tk()

app = App(root)

root.mainloop()
root.destroy()