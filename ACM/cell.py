class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.top = True
        self.bottom = True
        self.left = True
        self.right = True
        self.visited = False

    
    def __repr__(self):
        return f"({self.row}, {self.col})"