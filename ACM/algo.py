from cell import Cell
from PIL import Image, ImageDraw
import random

class Maze:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for y in range(height)] for x in range(width)]

    def generate(self):
        x, y = 0, 0
        self.cells[x][y].visited = True
        route = [(x, y)]

        while len(route)>0:
            x, y = route[-1]
            possible_cells = []

            if self.checker(x, y - 1):  
                possible_cells.append((x, y - 1, "top"))
            if self.checker(x, y + 1):  
                possible_cells.append((x, y + 1, "bottom"))
            if self.checker(x - 1, y):  
                possible_cells.append((x - 1, y, "left"))
            if self.checker(x + 1, y):
                possible_cells.append((x + 1, y, "right"))

            if len(possible_cells)>0:
                p, q, direction = random.choice(possible_cells)
                if direction == "top":
                    self.cells[x][y].top = False
                    self.cells[p][q].bottom = False
                elif direction == "bottom":
                    self.cells[x][y].bottom = False
                    self.cells[p][q].top = False
                elif direction == "left":
                    self.cells[x][y].left = False
                    self.cells[p][q].right = False
                elif direction == "right":
                    self.cells[x][y].right = False
                    self.cells[p][q].left = False

                self.cells[p][q].visited = True
                route.append((p, q))
            else:
                route.pop()

        self.cells[0][0].left = False
        self.cells[self.width-1][self.height -1].right = False


    def checker(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return not self.cells[x][y].visited
        return False

    def draw(self):
        m_width , m_height= (self.width * 20) +1, (self.height * 20 )+1

        img = Image.new("RGB", (m_width, m_height))
        draw = ImageDraw.Draw(img)

        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]
                if cell.top:
                    draw.line([(x * 20, y * 20), ((x + 1) * 20, y * 20)])
                if cell.bottom:
                    draw.line([(x * 20, (y + 1) * 20), ((x + 1) * 20, (y + 1) * 20)])
                if cell.left:
                    draw.line([(x * 20, y * 20), (x * 20, (y + 1) * 20)])
                if cell.right:
                    draw.line([((x + 1) * 20, y * 20), ((x + 1) * 20, (y + 1) * 20)])

        img.show()

