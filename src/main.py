from tkinter import *
from app import App

if __name__ == '__main__':
    root = Tk()
    root.title("Minesweeper")
    root.geometry("400x400")

    app = App(root)
    root.title = "Minesweeper"

    root.mainloop()
    root.destroy()
