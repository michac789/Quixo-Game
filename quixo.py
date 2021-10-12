import random
import math

def main():
    #prompt for the dimension form the user
    #IMPROVE LATER ON > check the data type, make sure it's integer, add limit
    n = int(input("Choose dimention: "))
    board = [0 for i in range(n*n)]
    print(board)
    display_board(board)
    check_move(board, 1, 1, 'T')


def check_move(board, turn, index, push_from):
    dimension = int(math.sqrt(len(board)))
    # implement your function here
    # if player 1 turn, cannot move pieces where player 2 is there
    if turn == 1:
        if board[index] == 2:
            return False
    # if player 2 turn, cannot move pieces where player 1 is there
    if turn == 2:
        if board[index] == 1:
            return False
    # if in the middle, cannont be moved
    if ((index + 1) % dimension != 1 and (index + 1) % dimension != 0 and index >= dimension and index < dimension * (dimension - 1)):
        return False
    # top side > L, R, B 
    if (((index + 1) % dimension != 1 and (index + 1) % dimension != 0) and index < dimension):
        if push_from == 'T':
            return False
        else:
            return True
    # down side > L, R, T
    if (((index + 1) % dimension != 1 or (index + 1) % dimension != 0) and index >= dimension * (dimension - 1)):
        if push_from == 'B':
            return False
        else:
            return True
    # left side > B, T, R
    if ((index + 1) % dimension != 1 and (index + 1) > dimension and (index + 1) < dimension * (dimension - 1)):
        if push_from == 'L':
            return False
        else:
            return True
    # right side > B, T, L
    if ((index + 1) % dimension != 0 and (index + 1) > dimension and (index + 1) < dimension * (dimension - 1)):
        if push_from == 'R':
            return False
        else:
            return True

def apply_move(board, turn, index, push_from):
    # implement your function here
    return board[:]

def check_victory(board, who_played):
    # implement your function here
    return -1

def computer_move(board, turn, level):
    # implement your function here
    return (0,'B')
    
def display_board(board):
    dimension = int(math.sqrt(len(board)))
    for i in range(dimension):
        for j in range(dimension):
            print(board[i * dimension + j], end="     ")
        print("")
    pass

def menu():
    # implement your function here
    pass

 
if __name__ == "__main__":
    menu()


main()
