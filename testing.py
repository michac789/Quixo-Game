from random import randint
import sys

from quixo import all_valid_moves, apply_move, check_move, computer_move, display_board, check_victory, positional_value, minimax

def main():
    board = [1,2,1,1,2,  2,1,0,0,2,  1,2,0,2,2,  1,2,1,1,0,  2,0,2,0,1]
    #board2 = [1,0,0,0,1,  2,2,1,1,2,  1,2,2,1,1,  1,1,0,2,1,  1,0,0,1,2]
    display_board(board)
    #y = positional_value(board2, 1)
    #print(y)
    #x = minimax(board, 2, 4, False)
    #print(x)
    z = computer_move(board, 2, 3)
    print(z)


main()
