import random
import math

def main():
    #prompt for the dimension form the user
    #IMPROVE LATER ON > check the data type, make sure it's integer, add limit
    n = int(input("Choose dimention: "))
    board = [i for i in range(int(n*n))]

    display_board(board)
    apply_move(board, 1, 14, 'L')
    display_board(board)

    apply_move(board, 2, 20, 'R')
    display_board(board)

"""     board = [0 for i in range(n*n)]
    print(board)
    display_board(board)
    returnval = check_move(board, 1, 1, 'T')
    print(returnval)

    turn = 0
    while(True):
        turn = turn + 1

        
        #input from the user
        input_index = input("Enter index: ")
        push_from = input("Enter push direction: ")
        
        if check_move(board, turn, input_index, push_from) == True:
            break """

    #display_board(board)
    
        #


def check_move(board, turn, index, push_from):
    dimension = int(math.sqrt(len(board)))
    if (turn == 1 and board[index] == 2) or (turn == 2 and board[index] == 1):
        return False
    if [(index + 1) % dimension == 1 and push_from == 'L'] or [(index + 1) % dimension == 0 and push_from == 'R']:
        return False
    if [(index < dimension) and push_from == 'T'] or [(index >= dimension * (dimension - 1)) and push_from == 'B']:
        return False
    if (index + 1) % dimension != 1 and (index + 1) % dimension != 0 and index >= dimension and index < dimension * (dimension - 1):
        return False
    return True

def apply_move(board, turn, index, push_from):
    pass

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

def menu():
    # implement your function here
    pass

 
if __name__ == "__main__":
    menu()


main()
