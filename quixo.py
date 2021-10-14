import random
import math
import sys

def check_move(board, turn, index, push_from):
    dimension = int(math.sqrt(len(board)))
    if (turn == 1 and board[index] == 2) or (turn == 2 and board[index] == 1):
        return False
    if (index % dimension == 0 and push_from == 'L') or (index % dimension == dimension - 1 and push_from == 'R'):
        return False
    if (index < dimension and push_from == 'T') or (index >= dimension * (dimension - 1) and push_from == 'B'):
        return False
    if (index % dimension != 0 and index % dimension != dimension - 1 and index >= dimension and index < dimension * (dimension - 1)):
        return False
    return True

def apply_move(board, turn, index, push_from):
    dimension = int(math.sqrt(len(board)))
    row_no = math.ceil((index + 1) / dimension) 
    column_no = index % dimension + 1
    if turn == 1:
        value = 1
    elif turn == 2:
        value = 2
    if push_from == 'L':
        for i in range (column_no - 1):
            board[index - i] = board[index - i - 1]
        board[index - column_no + 1] = value
    elif push_from == 'R':
        for i in range (dimension - column_no):
            board[index + i] = board[index + i + 1]
        board[index + dimension - column_no] = value
    elif push_from == 'T':
        for i in range (row_no - 1):
            board[index - dimension * i] = board[index - dimension * (i + 1)]
        board[index - dimension * (row_no - 1)] = value
    elif push_from == 'B':
        for i in range (dimension - row_no):
            board[index + dimension * i] = board[index + dimension * (i + 1)]
        board[index + dimension * (dimension - row_no)] = value
    return board[:]

def check_victory(board, who_played):
    dimension = int(math.sqrt(len(board)))
    winner = [False for i in range(3)]
    for i in range(dimension):
        same = 0
        for j in range(dimension - 1):
            if board[i * dimension + j] == board[i * dimension + j + 1]:
                same = same + 1
                if same == dimension - 1:
                    winner[board[i * dimension]] = True
    for k in range(dimension):
        same = 0
        for l in range(1, dimension, 1):
            if board[k + l * dimension] == board[k + (l - 1) * dimension]:
                same = same + 1
                if same == dimension - 1:
                    winner[board[k]] = True
    same = 0
    for m in range(dimension - 1):
        if board[m * (dimension + 1)] == board[(m + 1) * (dimension + 1)]:
            same = same + 1
            if same == dimension - 1:
                winner[board[0]] = True
    same = 0
    for n in range(dimension - 1):
        if board[n * (dimension - 1)] == board[(n + 1) * (dimension + 1)]:
            same = same + 1
            if same == dimension - 1:
                winner[board[dimension - 1]] = True
    if winner[1] == True and winner[2] == True:
        if who_played == 1:
            return 2
        return 1
    if winner[1] == True:
        return 1
    if winner[2] == True:
        return 2
    return 0


def computer_move(board, turn, level):
    if level == 1:
        while(True):
            index = random.randint(0, len(board) - 1)
            choice = ['L', 'R', 'B', 'T']
            push_from = choice[random.randint(0, 3)]
            if check_move(board, turn, index, push_from) == True:
                break
        return index, push_from
    else:
        pass
    return (0,'B')
    
def display_board(board):
    dimension = int(math.sqrt(len(board)))
    for i in range(dimension):
        for j in range(dimension):
            print(board[i * dimension + j], end="     ")
        print("")

def menu():
    # prompt the user for the size of the board
    global n
    while(True):
        n = input("Choose dimention: ")
        if checkint(n) == True:
            if 1 < int(n) < 11:
                break
        print("Invalid input! Please input only an integer between 2 and 10 inclusive!")

    # prompt the user for game modes (2v2 or VS computer)
    print("Type the numbers below to choose game modes: ")
    print("0: 2v2 against other human players")
    for i in range(5):
        print(f"{i + 1}: against computer Level {i + 1}")
    while(True):
        level = input("Enter your choice: ")
        if checkint(level) == True:
            if 0 <= int(level) <= 5:
                break
        print("Invalid input! You can only type the integer 0, 1, 2, 3, 4 or 5!")
    
    if int(level) > 0:
        print("Sorry, this game mode is not available yet right now!")
        sys.exit()
    print("Playing against other human players!")
    
    board = [0 for i in range(int(n)*int(n))]
    display_board(board)
    temp = -1
    while(True):
        temp = temp + 1
        turn = (temp % 2) + 1
        
        #input from the user
        while(True):
            print(f"It is player {turn} turn.")
            input_index = int(input("Enter index: "))
            input_push_from = input("Enter push direction: ")
            if check_move(board, turn, input_index, input_push_from) == True:
                break
            print("Invalid move!")
        board = apply_move(board, turn, input_index, input_push_from)
        victory = check_victory(board, turn)
        print(f"victory = {victory}")
        display_board(board)
        
            
    #display_board(board)

def checkint(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False
 
def randomize_valid_move():
    pass

if __name__ == "__main__":
    menu()


