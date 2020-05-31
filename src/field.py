class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return "Field[x:"+str(self.x)+", y"+str(self.y)+"]"

    def __repr__(self):
        return self.show()

    def __str__(self):
        return self.show()
