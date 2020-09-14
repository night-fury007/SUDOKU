import pygame

from SudokuCube import SudokuCube
from Utilities import BUTTON

class GameBoard :
    def __init__(self, rows, cols, width, height, win, board, initial_board, initial_positions):
        self.rows = rows
        self.cols = cols
        self.initial_board = initial_board
        self.initial_positions = initial_positions
        self.cubes = [[SudokuCube(board[i][j], i, j, width, height, initial_positions) for j in range(cols)] for i in range(rows)]
        self.width = width
        self.height = height
        self.model = None
        self.update_model()
        self.selected = None
        self.win = win

    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def draw(self):
        gap = self.width / 9
        for i in range(self.rows+1):
            if i % 3 == 0 :
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0, 0, 0), (200, i*gap+20), (200+self.width, i*gap+20), thick)
            pygame.draw.line(self.win, (0, 0, 0), (200+i*gap, 20), (200+i*gap, self.height+20), thick)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)            

    def redraw_window(self, win, game_board):
        win.fill((255, 255, 255), rect = (200, 20, 540, 540))
        # Draw time
        # fnt = pygame.font.SysFont("comicsans", 40)
        # text = fnt.render("Time: " + self.format_time(time), 1, (0,0,0))
        # win.blit(text, (540 - 160, 560))
        # Draw Strikes
        # text = fnt.render("X " * strikes, 1, (255, 0, 0))
        # win.blit(text, (20, 560))
        # Draw grid and board
        game_board.draw()

    def select(self, pos) :
        row, col = pos 
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False
        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def click(self, pos):
        if ((pos[0]>200 and pos[0]<200+self.width) and (pos[1]>20 and pos[1]<20+self.height)) :
            gap = self.width / 9
            x = (pos[0]-200) // gap
            y = (pos[1]-20) // gap
            return (int(y),int(x))
        else:
            return None    

    def find_empty(self, B):
        for i in range(self.rows):
            for j in range(self.cols):
                if B[i][j] == 0 :
                    return (i, j)
        return None

    def valid(self, B, num, pos):
        # Check row
        for i in range(self.cols) :
            if B[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(self.rows) :
            if B[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if B[i][j] == num and (i,j) != pos:
                    return False
        return True

    def solve(self):
        find = self.find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find
        for num in range(1, 10):
            if self.valid(self.model, num, (row, col)):
                self.model[row][col] = num
                if self.solve():
                    return True
                self.model[row][col] = 0
        return False

    def solveAI(self):
        find = self.find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10):
            if self.valid(self.model, num, (row, col)):
                self.model[row][col] = num
                self.cubes[row][col].set(num)
                self.cubes[row][col].drawAI(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(100)

                if self.solveAI():
                    return True
                
                self.model[row][col] = 0
                self.cubes[row][col].set(0)
                self.update_model()
                self.cubes[row][col].drawAI(self.win, False)
                pygame.display.update()
                pygame.time.delay(100)

        return False

    def place(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set(val)
            self.update_model()

            if self.valid(self.model, val, (row,col)) and self.solve():
                return True
            else:
                self.cubes[row][col].set(0)
                self.cubes[row][col].set_temp(0)
                self.update_model()
                return False

    def sketch(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0 :
            self.cubes[row][col].set_temp(0)
    
    def resetBoard(self) :
        for i in range(self.rows) :
            for j in range(self. cols) :
                if self.initial_positions[i][j] == False :
                    if self.cubes[i][j].value != 0 or self.cubes[i][j].temp != 0 : 
                        self.cubes[i][j].set_temp(0)
                        self.cubes[i][j].set(0)
                        self.update_model()

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True