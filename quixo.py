import random
import math
import sys
import time

def check_move(board, turn, index, push_from):
    dimension = int(math.sqrt(len(board)))
    # The person cannot pick the opponent's piece (of different sign)
    if (turn == 1 and board[index] == 2) or (turn == 2 and board[index] == 1):
        return False
    # For the left tiles, pushing from left is invalid; for the right tiles, pushing from right is invalid
    if (index % dimension == 0 and push_from == 'L') or (index % dimension == dimension - 1 and push_from == 'R'):
        return False
    # For the top tiles, pushing from top is invalid; for the bottom tiles, pushing from bottom is invalid
    if (index < dimension and push_from == 'T') or (index >= dimension * (dimension - 1) and push_from == 'B'):
        return False
    # If the tiles are in the middle (not sides/corners), it is definitely invalid
    if (index % dimension != 0 and index % dimension != dimension - 1 and index >= dimension and index < dimension * (dimension - 1)):
        return False
    # The rest of the cases unstated above are valid
    return True

def apply_move(board, turn, index, push_from):
    dimension = int(math.sqrt(len(board)))
    board_temp = board[:]
    # Move from top
    if push_from == 'T':
        for i in range(index, index % dimension, -dimension): 
            board_temp[i] = board_temp[i - dimension] 
        board_temp[index%dimension] = turn 
    # Move from bottom
    elif push_from == 'B':
        for i in range(index, dimension * (dimension - 1) + index % dimension, dimension): 
            board_temp[i] = board_temp[i + dimension] 
        board_temp[index % dimension + dimension * (dimension - 1)] = turn  
    # Move from right
    elif push_from == 'R':
        for i in range(index, (index // dimension + 1) * dimension - 1): 
            board_temp[i] = board_temp[i + 1]  
        board_temp[(index // dimension+1) * dimension - 1] = turn
    # Move from left
    elif push_from == 'L':
        for i in range(index, index // dimension * dimension, -1): 
            board_temp[i] = board_temp[i-1]  
        board_temp[index // dimension * dimension] = turn        
    return board_temp[:]

def check_victory(board, who_played): #NEED TO FIX
    dimension = int(math.sqrt(len(board)))
    winner = 0  
    # checking row
    for row in range(dimension):
        victory = True
        for j in range (dimension - 1):
            if board[row * dimension + j] == 0 or board[row * dimension + j] != board[row * dimension + j + 1]:
                victory = False
        if victory == True and (winner == who_played or winner == 0):
            winner = board[row * dimension + j]
    # checking column
    for column in range(dimension):
        victory = True
        for i in range(dimension - 1):
            if board[column + i * dimension] == 0 or board[column + i * dimension] != board[column + (i + 1) * dimension]: 
                victory = False  
        if victory == True and (winner == who_played or winner == 0): 
            winner = board[column + i * dimension] 
    # checking diagonal from right  
    victory = True  
    for i in range (1, dimension): 
        if board[(dimension - 1) * i] == 0 or board[(dimension - 1)*i] != board [(dimension - 1) * (i + 1)]: 
            victory = False  
    if victory == True and (winner == who_played or winner == 0): 
        winner = board[(dimension - 1) * i] 
    victory = True  
    # checking diagonal from left  
    for i in range (dimension - 1): 
        if board[(dimension + 1) * i] == 0 or board[(dimension + 1) * i] != board[(dimension + 1) * (i + 1)]: 
            victory = False  
    if victory == True and (winner == who_played or winner == 0): 
        winner = board[(dimension + 1) * i]  
    if winner == 0: 
        return 0 
    else:
        return winner

def computer_move(board, turn, level): #NEED TO FIX
    dimension = int(math.sqrt(len(board)))
    list = all_valid_moves(board, turn)
    if level == 1:
        x = random.randint(0, len(list))
        return list[x][0], list[x][1]
    elif level == 2:
        good_moves = []
        neutral_moves = []
        bad_moves = []
        for moves in list:
            board_temp = apply_move(board, turn, moves[0], moves[1])
            if check_victory(board_temp, turn) == turn:
                good_moves.append((moves[0], moves[1]))
            elif check_victory(board_temp, turn) == turn % 2 + 1:
                bad_moves.append((moves[0], moves[1]))
            else:
                neutral_moves.append((moves[0], moves[1]))
        if len(good_moves) > 0:
            x = random.randint(0, len(good_moves) - 1)
            return good_moves[x][0], good_moves[x][1]
        elif len(neutral_moves) > 0:
            x = random.randint(0, len(neutral_moves) - 1)
            return neutral_moves[x][0], neutral_moves[x][1]
        else:
            x = random.randint(0, len(bad_moves) - 1)
            return neutral_moves[x][0], neutral_moves[x][1]
    score = 101
    best_move = [101, 0, 0]
    for i in range(len(list)):
        simulationboard = apply_move(board, turn, list[i][0], list[i][1])
        if level == 3:
            score = minimax(simulationboard, turn, 2, True)
            #print(score)
        else:
            score = minimax(simulationboard, turn, 2, True)
            #print(f"move: {list[i][0]}{list[i][1]}, score = {score}")
        #print(f"0: {best_move[0]}, 1: {best_move[1]}, 2: {best_move[2]}, 3: {list[i][0]}{list[i][1]}, i={i}, score={score}")
        if best_move[0] > score:
            best_move[0] = score
            best_move[1] = list[i][0]
            best_move[2] = list[i][1]
        #print(f"0: {best_move[0]}, 1: {best_move[1]}, 2: {best_move[2]}, 3: {list[i][0]}{list[i][1]}, i={i}")
    return best_move[1], best_move[2]

def display_board(board):
    dimension = int(math.sqrt(len(board)))
    # Displays column number
    print("  ", end="")
    for i in range(dimension):
        print("  ", i + 1, end="")
    print("\n")
    for i in range(dimension):
        # Displays left side row number
        print(i + 1, "    ", end="")
        # Displays 'X' for player 1, 'O' for player 2, '_' otherwise
        for j in range(dimension):
            if board[i * dimension + j] == 1:
                print("X", end="   ")
            elif board[i * dimension + j] == 2:
                print("O", end="   ")
            else:
                print("_", end="   ")
        print("\n")
    print("")

def menu(): #NEED TO FIX
    # prompt the user for game modes (two human players or vs computer level 1-4)
    print("Welcome to Quixo")
    print("Type the number below to choose game modes: ")
    print("0: two players (human vs human)")
    for i in range(4):
        print(f"{i + 1}: single player against computer Level {i + 1}")
    while(True):
        level = input("Enter your choice: ")
        if checkint(level) == True:
            if 0 <= int(level) < 6:
                break
        print("Invalid input! You can only type the integer 0, 1, 2, 3, or 4!")

    # prompt the user for the size of the board
    while(True):
        n = input("Choose dimension: ")
        if checkint(n) == True:
            if 1 < int(n) < 100:
                break
        print("Invalid input! Please input only an integer between 2 and 99 inclusive!")

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
            if check_victory != 0: #BUGGY
                print(f"Congratulations! Player {check_victory(board, turn)} wins!")
                sys.exit(0)
    elif int(level) == 5:
        while(True):
            temp = temp + 1
            turn = (temp % 2) + 1
            print(f"Turn: {turn}, comp lv3")
            compindex, comppush = computer_move(board, turn, 3)
            print(f"Move: row {compindex // int(n) + 1}, column {(compindex % int(n)) + 1}, push_from {comppush}")
            board = apply_move(board, turn, compindex, comppush)
            display_board(board)
            if check_victory(board, turn) != 0:
                print(f"Computer 3 win!")
                sys.exit(0)
            
            temp += 1
            turn = (turn % 2) + 1
            print(f"Turn: {turn}, comp lv4")
            compindex, comppush = computer_move(board, turn, 4)
            print(f"Move: row {compindex // int(n) + 1}, column {(compindex % int(n)) + 1}, push_from {comppush}")
            board = apply_move(board, turn, compindex, comppush)
            display_board(board)
            if check_victory(board, turn) != 0:
                print(f"Computer 4 win!")
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
                print("Congratulations! You win against computer level ", level)
                sys.exit(0)
            
            if int(level) == 1:
                print("Computer level 1 is thinking...")
                temp = temp + 1
                compindex, comppush = computer_move(board, turn % 2 + 1, 1)
            else:
                print(f"Computer level {level} is thinking...")
                temp = temp + 1
                compindex, comppush = computer_move(board, turn % 2 + 1, int(level))
            print(f"Move: row {compindex // int(n) + 1}, column {(compindex % int(n)) + 1}, push_from {comppush}")
            board = apply_move(board, turn % 2 + 1, compindex, comppush)
            display_board(board)
            if check_victory(board, turn) != 0:
                print(f"The computer wins! Try again!")
                sys.exit(0)

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
        return 100
    if check_victory(board, turn) == 2:
        return -100
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
                    score += (10 * m)
                if counter[l] >= dimension - 1:
                    score += (10 * m)
        for q in range(len(board)):
            if board[q] == i:
                score += (1 * m)
    return score

def minimax(board, turn, depth, maximizing):
    if depth == 0 or check_victory(board, turn) != 0:
        return positional_value(board, turn)
    valid_moves = all_valid_moves(board, turn)
    no_of_options = len(valid_moves)
    turn = turn % 2 + 1
    if maximizing == True:
        score = -11
        for i in range(len(valid_moves)):
            board_simul = apply_move(board, turn, valid_moves[i][0], valid_moves[i][1])
            score_predict = minimax(board_simul, turn, depth - 1, False)
            if score_predict > score:
                score = score_predict
    else:
        score = 11
        for i in range(len(valid_moves)):
            board_simul = apply_move(board, turn, valid_moves[i][0], valid_moves[i][1])
            score_predict = minimax(board_simul, turn, depth - 1, True)
            if score_predict < score:
                score = score_predict
    return score

if __name__ == "__main__":
    menu()
