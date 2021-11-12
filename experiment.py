from random import randint
import sys

from quixo import all_valid_moves, apply_move, check_move, display_board, check_victory, all_valid_moves, computer_move

def main():

    
    board = [1,1,1,1,0,  2,0,0,0,2,  0,0,0,0,2,  2,0,0,0,2,  0,0,0,0,2]
    x = check_move(board, 1, 0, 'T')
    x = check_move(board, 1, 0, 'Z')
    x = check_move(board, 5, 0, 'B')
    print(x)
    #display_board(board)
    #x = computer_move(board, 1, 2)
    #print(x)


main()
