class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hasBomb = False
        self.isDiscovered = False

    def show(self):
        return "Field[x:" + str(self.x)+", y: " + str(self.y) + ", hasBomb: " + str(self.hasBomb) + ", isDiscovered: " + str(self.isDiscovered) + "]"

    def get_gui_content(self):
        if not self.isDiscovered:
            return "?"
        else:
            if self.hasBomb:
                return "X"
            else:
                return "O"

    def __repr__(self):
        return self.show()

    def __str__(self):
        return self.show()
