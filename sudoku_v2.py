import pygame
import time
import copy
from Utilities import BUTTON
from GameBoard import GameBoard
from GenerateSudoku import GenerateSudoku
pygame.font.init()

def playGame(difficulty) :
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load("sudoku.png")
    pygame.display.set_icon(icon)
    gen_sudoku = GenerateSudoku(difficulty)
    board, initial_positions = gen_sudoku.buildSudoku()
    initial_board = copy.deepcopy(board)
    game_board = GameBoard(9, 9, 540, 540, win, board, initial_board, initial_positions)
    running = True
    key = None
    win.fill((0, 122, 153))
    check_button = BUTTON((0, 172, 230), 50, 100, 100, 40, "CHECK")
    solve_button = BUTTON((0, 172, 230), 50, 200, 100, 40, "SOLVE")
    reset_button = BUTTON((0, 172, 230), 50, 300, 100, 40, "RESET")
    while running :
        for event in pygame.event.get() :
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_DELETE:
                    game_board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = game_board.selected
                    if game_board.cubes[i][j].temp != 0:
                        if game_board.place(game_board.cubes[i][j].temp):
                            print("Success")
                        else:
                            print("Wrong")
                        key = None
                        if game_board.is_finished():
                            print("Game over")
                if event.key == pygame.K_ESCAPE:
                    running = False  

            if event.type == pygame.MOUSEMOTION :
                if check_button.isOver(pos) :
                    check_button.color = (121, 166, 210)
                else :
                    check_button.color = (0, 172, 230) 
            if event.type == pygame.MOUSEMOTION :
                if solve_button.isOver(pos) :
                    solve_button.color = (121, 166, 210)
                else :
                    solve_button.color = (0, 172, 230) 
            if event.type == pygame.MOUSEMOTION :
                if reset_button.isOver(pos) :
                    reset_button.color = (121, 166, 210)
                else :
                    reset_button.color = (0, 172, 230)         
            if event.type == pygame.MOUSEBUTTONDOWN :
                clicked = game_board.click(pos)
                if clicked:
                    game_board.select(clicked)
                    key = None
                if check_button.isOver(pos) :
                    print("clicked !!!")
                elif solve_button.isOver(pos) :
                    game_board.solveAI()
                elif reset_button.isOver(pos) :
                    game_board.resetBoard()
        if game_board.selected and key != None:
            game_board.sketch(key)            
        win.fill((0, 122, 153))            
        check_button.draw(win, (0, 68, 102))
        solve_button.draw(win, (0, 68, 102)) 
        reset_button.draw(win, (0, 68, 102))                        
        game_board.redraw_window(win, game_board)
        pygame.display.update()

def main() :
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Sudoku")
    icon = pygame.image.load("sudoku.png")
    pygame.display.set_icon(icon)
    background = pygame.image.load("background.png")
    running = True
    easy_button = BUTTON((204, 153, 102), 150, 400, 100, 40, "EASY")
    medium_button = BUTTON((204, 153, 102), 350, 400, 100, 40, "MEDIUM")
    hard_button = BUTTON((204, 153, 102), 550, 400, 100, 40, "HARD")
    play_button = BUTTON((51, 153, 102), 350, 500, 100, 50, "PLAY")
    selected_button = 0
    while running:
        for event in pygame.event.get() :
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT :
                running = False
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN :
                if easy_button.isOver(pos) :
                    selected_button = 1
                    print("clicked !!!")
                elif medium_button.isOver(pos) :
                    selected_button = 2
                    print("clicked !!!")
                elif hard_button.isOver(pos) :
                    selected_button = 3
                    print("clicked !!!")  
            if event.type == pygame.MOUSEMOTION :
                if easy_button.isOver(pos) :
                    easy_button.color = (134, 89, 45)
                else :
                    easy_button.color = (204, 153, 102) 
            if event.type == pygame.MOUSEMOTION :
                if medium_button.isOver(pos) :
                    medium_button.color = (134, 89, 45)
                else :
                    medium_button.color = (204, 153, 102) 
            if event.type == pygame.MOUSEMOTION :
                if hard_button.isOver(pos) :
                    hard_button.color = (134, 89, 45)
                else :
                    hard_button.color = (204, 153, 102)                      
            if event.type == pygame.MOUSEMOTION :
                if play_button.isOver(pos) :
                    play_button.color = (172, 57, 57)
                else :
                    play_button.color = (51, 153, 102)           
            if event.type == pygame.MOUSEBUTTONDOWN :
                if play_button.isOver(pos) : 
                    if selected_button > 0 and selected_button < 4 :                
                        playGame(selected_button)

        win.fill((0, 122, 153))
        win.blit(background, (100, 50))
        easy_button.draw(win, (0, 68, 102)) if selected_button == 1 else easy_button.draw(win)
        medium_button.draw(win, (0, 68, 102)) if selected_button == 2 else medium_button.draw(win)
        hard_button.draw(win, (0, 68, 102)) if selected_button == 3 else hard_button.draw(win)    
            
        play_button.draw(win)  
               
        pygame.display.update()


if __name__== "__main__" : 
    main() 