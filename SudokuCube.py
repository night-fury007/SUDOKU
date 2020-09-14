import pygame

class SudokuCube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height, positions):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.positions = positions
        self.selected = False

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), 1, (128,128,128))
            win.blit(text, (200+x+5, 20+y+5))
        elif (self.value != 0) :
            if self.positions[self.row][self.col] : 
                text = fnt.render(str(self.value), 1, (0, 102, 153))
                win.blit(text, (200 + x + (gap/2 - text.get_width()/2), 20 + y + (gap/2 - text.get_height()/2)))
            else :    
                text = fnt.render(str(self.value), 1, (0, 0, 0))
                win.blit(text, (200 + x + (gap/2 - text.get_width()/2), 20 + y + (gap/2 - text.get_height()/2)))

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (200+x, 20+y, gap ,gap), 3)

    def drawAI(self, win, g=True):
        fnt = pygame.font.SysFont("comicsans", 40)

        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap

        pygame.draw.rect(win, (255, 255, 255), (200+x, 20+y, gap, gap), 0)

        text = fnt.render(str(self.value), 1, (0, 0, 0))
        win.blit(text, (200+x + (gap / 2 - text.get_width() / 2), 20+y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (200+x, 20+y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (200+x, 20+y, gap, gap), 3)
        

    def set(self, val):
        self.value = val

    def set_temp(self, val):
        self.temp = val        
