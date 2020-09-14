import random

class GenerateSudoku :
    def __init__(self, difficulty) :
        self.rows = 9
        self.cols = 9
        self.difficulty = difficulty
        self.sudoku = [[0 for i in range(self.cols)] for j in range(self.rows)]
        self.initial_positions = [[True for i in range(self.cols)] for j in range(self.rows)]

    def unUsedInBox(self, row, col, num) : 
        gap = self.rows // 3
        for i in range(gap) :
            for j in range(gap) :
                if (self.sudoku[row+i][col+j] == num) : 
                    return False 
        return True

    def fillBox(self, row, col) :
        gap = self.rows // 3  
        for i in range(gap) :
            for j in range(gap) :
                while True :
                    num = random.randint(1, 9)
                    if self.unUsedInBox(row, col, num) :
                        self.sudoku[row+i][col+j] = num
                        break 

    def fillDiagonal(self) :
        gap = self.rows // 3
        for i in range(0, self.rows, gap) :
            self.fillBox(i, i)

    def find_empty(self) :
        for i in range(self.rows) :
            for j in range(self.cols) :
                if self.sudoku[i][j] == 0 :
                    return (i, j)
        return None

    def valid(self, num, pos) :
        # Check row
        for i in range(self.cols) :
            if self.sudoku[pos[0]][i] == num and pos[1] != i :
                return False

        # Check column
        for i in range(self.rows) :
            if self.sudoku[i][pos[1]] == num and pos[0] != i :
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 + 3) :
            for j in range(box_x * 3, box_x*3 + 3) :
                if self.sudoku[i][j] == num and (i,j) != pos :
                    return False
        return True

    def solve(self) :
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for num in range(1, 10) :
            if self.valid(num, (row, col)) :
                self.sudoku[row][col] = num
                if self.solve():
                    return True
                self.sudoku[row][col] = 0
        return False

    def removeDigits(self) : 
        if self.difficulty == 1 :
            count = 40
        elif self.difficulty == 2 :
            count = 39
        elif self.difficulty == 3 :
            count = 36
        K = (self.rows*self.cols) - count
        flag = 0
        while K != 0 : 
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if i != 0 and j != 0 :
                if flag == 0 : 
                    i = i - 1
                    flag = 1
                elif flag == 1 :
                    j = j - 1
                    flag = 0     
            if self.sudoku[i][j] != 0 :
                K = K - 1 
                self.sudoku[i][j] = 0
                self.initial_positions[i][j] = False

    def buildSudoku(self) :
        self.fillDiagonal()
        self.solve()
        self.removeDigits()
        return self.sudoku, self.initial_positions    