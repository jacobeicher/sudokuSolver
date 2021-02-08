import numpy as np
import pygame
import copy

def button(msg, x, y, w, h, ic, ac, puzzle, gameBoard):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameBoard, ac,(x,y,w,h))
        if click[0] == 1:
            if msg == "Solve!":
                global gameExit
                gameExit = True
                
            else:
                xVal = (mouse[0]-30) // 60
                yVal = (mouse[1]-10) // 60

                if pygame.key.get_pressed()[pygame.K_0]:
                    msg = ""
                elif pygame.key.get_pressed()[pygame.K_1]:
                    msg = '1'
                elif pygame.key.get_pressed()[pygame.K_2]:
                    msg = '2'
                elif pygame.key.get_pressed()[pygame.K_3]:
                    msg = '3'
                elif pygame.key.get_pressed()[pygame.K_4]:
                    msg = '4'
                elif pygame.key.get_pressed()[pygame.K_5]:
                    msg = '5'
                elif pygame.key.get_pressed()[pygame.K_6]:
                    msg = '6'
                elif pygame.key.get_pressed()[pygame.K_7]:
                    msg = '7'
                elif pygame.key.get_pressed()[pygame.K_8]:
                    msg = '8'
                elif pygame.key.get_pressed()[pygame.K_9]:
                    msg = '9'
                if msg!="":
                    puzzle[xVal][yVal] = int(msg)
                else:
                    puzzle[xVal][yVal] = 0    
    else:
        pygame.draw.rect(gameBoard, ic,(x,y,w,h))
    if msg == "Solve!" or msg == "Exit":
        font = pygame.font.SysFont(None, 50)
    else:
        font = pygame.font.SysFont(None, 75)
    gameBoard.blit(font.render(msg, True, BLACK), (x+15,y+8))


def possible(puzzle, y, x ,n):
    for i in range(0,9):
        if puzzle[y][i] == n:
            return False
    for i in range(0,9):
        if puzzle[i][x] == n:
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[y0 + i][x0 + j] == n:
                return False

    return True
global sPuzzle
global beenSolved 
beenSolved = False

def solve(puzzle):

    for y in range(9):
        for x in range(9):
            if puzzle[y][x] == 0:
                for n in range(1,10):
                    if possible(puzzle, y, x, n):
                        puzzle[y][x] = n
                        solve(puzzle)
                        puzzle[y][x] = 0
                return
    print("solved puzzle")
    print (np.matrix(puzzle))
    global sPuzzle
    global beenSolved
    if not beenSolved:
        sPuzzle = copy.deepcopy(puzzle)
        beenSolved = True
        
    return 
    #input("check for more?")

gameExit = False

def runGame(gameBoard, puzzle, mainMsg = "Solve!"):
    global gameExit
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

        x = 30
        
        gameBoard.fill(WHITE)
        
        for j in range(9):
            y = 10
            for i in range(9):
                if(((j < 3 or j > 5) and i > 2 and i < 6) or (j > 2 and j < 6 and (i < 3 or i > 5))):
                    pygame.draw.rect(gameBoard, RED, [x,y,60,60])
                else:
                    pygame.draw.rect(gameBoard, BLACK, [x,y,60,60])
                
                
                button(mainMsg, 235, 550, 125, 60, GREEN, GREY, puzzle, gameBoard)

                if(puzzle[j][i] != 0):
                    num = str(puzzle[j][i])
                else:
                    num = ""
                    #print("No Value")

                button(num, x+3, y+3, 56, 56, WHITE, GREY, puzzle, gameBoard)
        
                y += 60
            x += 60

        pygame.display.update()


GREY = (220,220,220)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)        


def main():

    puzzle= [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
            [6, 0, 0, 1, 9, 5, 0, 0, 0], 
            [0, 9, 8, 0, 0, 0, 0, 6, 0], 
            [8, 0, 0, 0, 6, 0, 0, 0, 3], 
            [4, 0, 0, 8, 0, 3, 0, 0, 1], 
            [7, 0, 0, 0, 2, 0, 0, 0, 6], 
            [0, 6, 0, 0, 0, 0, 2, 8, 0], 
            [0, 0, 0, 4, 1, 9, 0, 0, 5], 
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    global gameExit
    

    pygame.init()

    gameBoard = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Sudoku Solver")

    pygame.display.update()
    
    runGame(gameBoard, puzzle)
    gameExit = False
    pygame.quit()

    solve(puzzle)
    global sPuzzle
    
    puzzle = sPuzzle

    print(np.matrix(puzzle))

    pygame.init()

    gameBoard = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Sudoku Solver")

    pygame.display.update()
    
    runGame(gameBoard, puzzle, "Exit")
    gameExit = False
    pygame.quit()
    



if __name__ == "__main__":
    main()