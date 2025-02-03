from cell import Cell
from algo import Maze
row = int(input("Enter height of Maze \n"))
col = int(input("Enter width of Maze \n"))
maze = Maze(col,row)
maze.generate()
maze.draw()