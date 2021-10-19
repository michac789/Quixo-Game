from quixo import *

def simple_test():

    board = [1,0,2,0,1,  0,0,0,1,2,  0,0,0,0,0,  1,2,0,0,0,  0,2,0,1,1]
    if check_move(board, 1, 1, 'L'): print("test check_move 1 - OK !")
    else: print("test check_move 01 - Problem in the check_move function output !")

    board = [1,0,2,0,1,  0,0,0,1,2,  0,0,0,0,0,  1,2,0,0,0,  0,2,0,1,1]
    if check_move(board, 1, 4, 'L'): print("test check_move 1 - OK !")
    else: print("test check_move 02 - Problem in the check_move function output !")

    board = [1,0,2,0,1,  0,0,0,1,2,  0,0,0,0,0,  1,2,0,0,0,  0,2,0,1,1]
    if check_move(board, 1, , 'L'): print("test check_move 1 - OK !")
    else: print("test check_move 03 - Problem in the check_move function output !")

    board = [1,0,2,0,1,  0,0,0,1,2,  0,0,0,0,0,  1,2,0,0,0,  0,2,0,1,1]
    if check_move(board, 1, 1, 'L'): print("test check_move 1 - OK !")
    else: print("test check_move 04 - Problem in the check_move function output !")

    board = [1,0,2,0,1,  0,0,0,1,2,  0,0,0,0,0,  1,2,0,0,0,  0,2,0,1,1]
    if check_move(board, 1, 1, 'L'): print("test check_move 1 - OK !")
    else: print("test check_move 05 - Problem in the check_move function output !")

    board = [1,0,2,0,1,  0,0,0,1,2,  0,0,0,0,0,  1,2,0,0,0,  0,2,0,1,1]
    if check_move(board, 1, 1, 'B'): print("test check_move 1 - OK !")
    else: print("test check_move 1 - Problem in the check_move function output !")

def victory_test():
    board = [1,1,1,1,1,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    if check_victory(board, 1) == 1: print("test check_victory 1 - OK !")
    else: print("oh no something is wrong :(")

    board = [0,0,0,0,0,  2,2,2,2,2,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    if check_victory(board, 2) == 1: print("test check_victory 1 - OK !")
    else: print("oh no something is wrong :(")

    board = [1,1,1,1,1,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    if check_victory(board, 1) == 1: print("test check_victory 1 - OK !")
    else: print("oh no something is wrong :(")

    board = [1,1,1,1,1,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    if check_victory(board, 2) == 1: print("test check_victory 1 - OK !")
    else: print("oh no something is wrong :(")

    board = [1,1,1,1,1,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    if check_victory(board, 1) == 1: print("test check_victory 1 - OK !")
    else: print("oh no something is wrong :(") 


simple_test()
victory_test()

