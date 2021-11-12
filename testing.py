from random import randint
import sys

from quixo import all_valid_moves, apply_move, check_move, computer_move, display_board, check_victory, positional_value, minimax

def main():
    board = [2,1, 1,0]
    #board2 = [1,0,0,0,1,  2,2,1,1,2,  1,2,2,1,1,  1,1,0,2,1,  1,0,0,1,2]
    display_board(board)
    #x = minimax(board, 2, 3, False)
    #print(x)
    x = check_victory(board, 2)
    print(x)


main()
