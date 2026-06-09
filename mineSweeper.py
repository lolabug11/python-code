from math import *
from random import *
board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]
flagBoard = [
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
    [False,False,False,False,False,False,False,False,False],
]
def checkDirRepNums(changeR,changeC,r,c):
    if r+changeR > -1 and c+changeC > -1 and r+changeR < 9 and c+changeC < 9:
                    if board[r+changeR][c+changeC] == -1:
                        board[r][c] += 1


def checkDirShowNums(changeR,changeC,r,c):
    pass

def genBoard():
    mine = randint(1,25)
    mines = []
    mines.append(mine)
    for _ in range(9):
        mine = randint(1,81)

        while mine in mines:
            mine = randint(1,81)
        mines.append(mine)
    minesRC = {}   
    for mine in mines:
        mineR = floor(mine / 9)
        mineC = mine % 9
        minesRC[mine] = [mineR, mineC]
    print(minesRC)
    for mine in minesRC:
        board[minesRC[mine][0]-1][minesRC[mine][1]-1] = -1
    for r in range(9):
        for c in range(9):

            if board[r][c] != -1:
                changeR, changeC = 0,-1
                checkDirRepNums(changeR,changeC,r,c)

                changeR, changeC = 0,1
                checkDirRepNums(changeR,changeC,r,c)
                
                changeR, changeC = 1,1
                checkDirRepNums(changeR,changeC,r,c)
                
                changeR, changeC = 1,0
                checkDirRepNums(changeR,changeC,r,c)
                
                changeR, changeC = 1,-1
                checkDirRepNums(changeR,changeC,r,c)
            
                changeR, changeC = -1,0
                checkDirRepNums(changeR,changeC,r,c)
                
                changeR, changeC = -1,-1
                checkDirRepNums(changeR,changeC,r,c)
                
                changeR, changeC = -1,1
                checkDirRepNums(changeR,changeC,r,c)

def openPlace(r,c):
    chagn
def click(r,c):
    if not flagBoard[r][c]:
        if board[r][c] == -1:
            return -1
        
        
