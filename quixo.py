import random
import math
import sys
import time

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
    board_temp = board[:]
    if turn == 1:
        value = 1
    elif turn == 2:
        value = 2
    if push_from == 'L':
        for i in range (column_no - 1):
            board_temp[index - i] = board_temp[index - i - 1]
        board_temp[index - column_no + 1] = value
    elif push_from == 'R':
        for i in range (dimension - column_no):
            board_temp[index + i] = board_temp[index + i + 1]
        board_temp[index + dimension - column_no] = value
    elif push_from == 'T':
        for i in range (row_no - 1):
            board_temp[index - dimension * i] = board_temp[index - dimension * (i + 1)]
        board_temp[index - dimension * (row_no - 1)] = value
    elif push_from == 'B':
        for i in range (dimension - row_no):
            board_temp[index + dimension * i] = board_temp[index + dimension * (i + 1)]
        board_temp[index + dimension * (dimension - row_no)] = value
    return board_temp[:]

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
    dimension = int(math.sqrt(len(board)))
    list = all_valid_moves(board, turn)
    if level == 1:
        x = random.randint(0, len(list))
        return list[x][0], list[x][1]
    else:
        best_move = [11, 0, 0]
        for i in range(len(list)):
            simulationboard = apply_move(board, turn, list[i][0], list[i][1])
            if level == 2:
                time.sleep(1)
                score = minimax(simulationboard, turn % 2 + 1, 0, False)
            elif level == 3:
                score = minimax(simulationboard, turn % 2 + 1, 2, False)
            else:
                score = minimax(simulationboard, turn % 2 + 1, 4, False)
            if best_move[0] > score:
                best_move[0] = score
                best_move[1] = list[i][0]
                best_move[2] = list[i][1]
        return best_move[1], best_move[2]

def display_board(board):
    dimension = int(math.sqrt(len(board)))
    print("  ", end="")
    for i in range(dimension):
        print(f"   {i + 1}", end="")
    print("\n")
    dimension = int(math.sqrt(len(board)))
    for i in range(dimension):
        print(f"{i + 1}    ", end="")
        for j in range(dimension):
            print(board[i * dimension + j], end="   ")
        print("")
    print("")


def menu():
    # prompt the user for the size of the board
    while(True):
        n = input("Choose dimension: ")
        if checkint(n) == True:
            if 1 < int(n) < 11:
                break
        print("Invalid input! Please input only an integer between 2 and 10 inclusive!")

    # prompt the user for game modes (two human players or vs computer level 1-4)
    print("Type the number below to choose game modes: ")
    print("0: two players (human vs human)")
    for i in range(4):
        print(f"{i + 1}: single player against computer Level {i + 1}")
    while(True):
        level = input("Enter your choice: ")
        if checkint(level) == True:
            if 0 <= int(level) < 5:
                break
        print("Invalid input! You can only type the integer 0, 1, 2, 3, or 4!")

    # 2 players (human vs human)
    temp = -1
    board = [0 for i in range(int(n)*int(n))]
    display_board(board)
    if int(level) == 0:
        while(True):
            temp = temp + 1
            turn = (temp % 2) + 1
            while(True):
                print(f"It is player {turn} turn.")
                while(True):
                    row = input("Enter row: ")
                    if checkint(row) == True:
                        if 0 < int(row) < int(n) + 1:
                            break
                    print(f"Please enter a valid row number between 1 until {n} inclusive!")
                while(True):
                    column = input("Enter column: ")
                    if checkint(column) == True:
                        if 0 < int(column) < int(n) + 1:
                            break
                    print(f"Please enter a valid column number between 1 until {n} inclusive!")
                while(True):
                    input_push_from = input("Enter push direction: ")
                    allowed = ['L', 'R', 'B', 'T']
                    valid = False
                    for i in range(4):
                        if input_push_from == allowed[i]:
                            valid = True
                    if valid == True:
                        break
                input_index = (int(row) - 1) * int(n) + int(column) - 1
                if check_move(board, turn, input_index, input_push_from) == True:
                    break
                print("Invalid move!")

            board = apply_move(board, turn, input_index, input_push_from)
            display_board(board)
            if check_victory != 0:
                print(f"Congratulations! Player {check_victory(board, turn)} wins!")
                sys.exit(0)
    else:
        while(True):
            temp = temp + 1
            turn = (temp % 2) + 1
            while(True):
                print(f"It is player {turn} turn.")
                while(True):
                    row = input("Enter row: ")
                    if checkint(row) == True:
                        if 0 < int(row) < int(n) + 1:
                            break
                    print(f"Please enter a valid row number between 1 until {n} inclusive!")
                while(True):
                    column = input("Enter column: ")
                    if checkint(column) == True:
                        if 0 < int(column) < int(n) + 1:
                            break
                    print(f"Please enter a valid column number between 1 until {n} inclusive!")
                while(True):
                    input_push_from = input("Enter push direction: ")
                    allowed = ['L', 'R', 'B', 'T']
                    valid = False
                    for i in range(4):
                        if input_push_from == allowed[i]:
                            valid = True
                    if valid == True:
                        break
                input_index = (int(row) - 1) * int(n) + int(column) - 1
                if check_move(board, turn, input_index, input_push_from) == True:
                    break
                print("Invalid move!")
            board = apply_move(board, turn, input_index, input_push_from)
            display_board(board)
            if check_victory(board, turn) != 0:
                print(f"Congratulations! You win against computer!")
                sys.exit(0)
            
            if int(level) == 1:
                print("Computer level 1 is thinking...")
                time.sleep(1)
                temp = temp + 1
                compindex, comppush = computer_move(board, turn % 2 + 1, 1)
            else:
                print(f"Computer level {level} is thinking...")
                temp = temp + 1
                compindex, comppush = computer_move(board, turn % 2 + 1, int(level))

            board = apply_move(board, turn % 2 + 1, compindex, comppush)
            display_board(board)
            if check_victory(board, turn) != 0:
                print(f"The computer wins! Try again!")
                sys.exit(0)

            
    #display_board(board)

def checkint(input):
    try:
        val = int(input)
        return True
    except ValueError:
        return False

def all_valid_moves(board, turn):
    dimension = int(math.sqrt(len(board)))
    list = []
    push_from = ['L', 'R', 'B', 'T']
    for i in range(4):
        for j in range(dimension):
            list.append([j, push_from[i]])
            list.append([dimension * (dimension - 1) + j, push_from[i]])
        for k in range(dimension - 2):
            list.append([(k + 1) * dimension, push_from[i]])
            list.append([(k + 1) * dimension + dimension - 1, push_from[i]])
    removeid = []
    for m in range(len(list)):
        if check_move(board, turn, list[m][0], list[m][1]) == False:
            removeid.append(m)
    for n in range(len(removeid)):
        del list[removeid[n] - n]
    return list

def positional_value(board, turn):
    dimension = int(math.sqrt(len(board)))
    score = 0
    if check_victory(board, turn) == 1:
        return 10
    if check_victory(board, turn) == 2:
        return -10
    for i in range(1, 3, 1):
        m = 1
        if i == 2:
            m = -1
        for j in range(dimension):
            counter = [0 for i in range(4)]
            for k in range(dimension):
                if board[j * dimension + k] == i:
                    counter[0] += 1
                if board[j + k * dimension] == i:
                    counter[1] += 1
                if j == 0:
                    if board[0 + k * (dimension + 1)] == i:
                        counter[2] += 1
                    if board[(dimension - 1) + k * (dimension - 1)] == i:
                        counter[3] += 1
            for l in range(4):
                if counter[l] >= dimension - 2:
                    score += (1 * m)
                if counter[l] >= dimension - 1:
                    score += (1 * m)
    return score

def minimax(board, turn, depth, maximizing):
    if depth == 0 or check_victory(board, turn) != 0:
        return positional_value(board, turn)
    valid_moves = all_valid_moves(board, turn)
    no_of_options = len(valid_moves)
    if maximizing == True:
        score = -11
        for i in range(len(valid_moves)):
            #DEBUG print(f"board = {display_board(board)}")
            board_simul = apply_move(board, turn, valid_moves[i][0], valid_moves[i][1])
            score_predict = minimax(board_simul, (turn % 2) + 1, depth - 1, False)
            if score_predict > score:
                score = score_predict
    else:
        score = 11
        for i in range(len(valid_moves)):
            #DEBUG print(f"board = {display_board(board)}")
            board_simul = apply_move(board, turn, valid_moves[i][0], valid_moves[i][1])
            score_predict = minimax(board_simul, (turn % 2) + 1, depth - 1, True)
            if score_predict < score:
                score = score_predict
    return score

if __name__ == "__main__":
    menu()
