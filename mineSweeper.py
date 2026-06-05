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
def genBoard():
    mine = randint(1,81)
    mines = []
    mines.append(mine)
    for _ in range(8):
        mine = randint(1,81)
        
        while mine in mines:
            mine = randint(1,81)
        mines.append(mine)
    minesRC = {}   
    for mine in mines:
        mineR = floor(mine / 9)
        mineC = mine % 9
        minesRC[mine] = [mineR, mineC]
    for mine in minesRC:
        board[minesRC[mine][0]][minesRC[mine][1]] = -1
    for r in range(8):
        for c in range(8):
            """

             ox

            """
            changeR, changeC = 0,1
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """

             o
              x
            """
            changeR, changeC = 1,1
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """

             o
             x
            """
            changeR, changeC = 1,0
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """

             o
            x
            """
            changeR, changeC = 1,-1
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """

            xo

            """
            changeR, changeC = -1,0
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """
            x
             o

            """
            changeR, changeC = -1,-1
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """
             x
             o

            """
            changeR, changeC = -1,0
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
            """
              x
             o

            """
            changeR, changeC = -1,1
            if r+changeR and c+changeC >=0:
                if board[r+changeR][c+changeC] == -1:
                    board[r][c] += 1
