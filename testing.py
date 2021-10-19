from random import randint
import sys

from quixo import all_valid_moves, apply_move, check_move, computer_move, display_board, check_victory, positional_value, minimax

def main():
    board = [2,1,2,2,2,  1,2,2,1,1,  2,0,2,0,1,  1,0,1,0,1,  1,1,2,1,2]
    board = [2,2,1,1,1,  1,2,2,2,1,  1,0,0,0,0,  0,0,0,0,1,  2,2,0,0,1]
    board = [1,1,1,1,0,  2,2,2,2,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    board = [1,1,1,1,1,  2,2,2,2,0,  0,0,0,0,0,  0,0,0,0,0,  0,0,0,0,0]
    #board2 = [1,0,0,0,1,  2,2,1,1,2,  1,2,2,1,1,  1,1,0,2,1,  1,0,0,1,2]
    display_board(board)
    #x = minimax(board, 2, 3, False)
    #print(x)
    z = computer_move(board, 2, 4)
    x = positional_value(board, 2)
    print(z)
    print(x)


main()
