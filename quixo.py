import random
import math

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

def check_victory(board, who_played):
    dimension = int(math.sqrt(len(board)))
    winner = 0
    # Checking row
    for row in range(dimension):
        victory = True
        for j in range (dimension - 1):
            if board[row * dimension + j] == 0 or board[row * dimension + j] != board[row * dimension + j + 1]:
                victory = False
        # (1) If the winner is not the opposite player, we can still replace the value of winner. 
        # Yet, if it is still zero (no winner) and the player wins, we can replace it with the value that representing opposite player wins if it exists
        if victory == True and (winner == who_played or winner == 0):
            winner = board[row * dimension + j]
    # Checking column
    for column in range(dimension):
        victory = True
        for i in range(dimension - 1):
            if board[column + i * dimension] == 0 or board[column + i * dimension] != board[column + (i + 1) * dimension]: 
                victory = False
        if victory == True and (winner == who_played or winner == 0): # refer to (1)
            winner = board[column + i * dimension]
    # Checking right diagonal (positive gradient)
    victory = True  
    for i in range (1, dimension): 
        if board[(dimension - 1) * i] == 0 or board[(dimension - 1) * i] != board [(dimension - 1) * (i + 1)]: 
            victory = False
    if victory == True and (winner == who_played or winner == 0): # refer to (1)
        winner = board[(dimension - 1) * i]
    victory = True
    # Checking left diagonal (negative gradient)
    for i in range(dimension - 1):
        if board [(dimension + 1) * i] == 0 or board[(dimension + 1) * i] != board [(dimension + 1) * (i + 1)]:
            victory = False
    if victory == True and (winner == who_played or winner == 0):
        winner = board[(dimension + 1) * i]
    # Return winner if there is one
    return winner 

def computer_move(board, turn, level):
    dimension = int(math.sqrt(len(board)))
    # Generate list of all possible valid moves
    list = all_valid_moves(board, turn)
    # Computer level 1 generate completely random valid moves
    if level == 1:
        x = random.randint(0, len(list))
        return list[x][0], list[x][1]
    # Computer level 2 prioritize automatic winning move if exist, else do neutral move and prevent automatic losing move
    elif level == 2:
        good_moves = []
        neutral_moves = []
        bad_moves = []
        # Classify all valid moves into good/neutral/bad moves based on instruction
        for moves in list:
            board_temp = apply_move(board, turn, moves[0], moves[1])
            if check_victory(board_temp, turn) == turn:
                good_moves.append((moves[0], moves[1]))
            elif check_victory(board_temp, turn) == turn % 2 + 1:
                bad_moves.append((moves[0], moves[1]))
            else:
                neutral_moves.append((moves[0], moves[1]))
        # Randomize, index [x][0] or [x][1] simply means the 'x' good/neutral/bad moves, [0]: push_index, [1]: push_from
        if len(good_moves) > 0:
            x = random.randint(0, len(good_moves) - 1)
            return good_moves[x][0], good_moves[x][1]
        elif len(neutral_moves) > 0:
            x = random.randint(0, len(neutral_moves) - 1)
            return neutral_moves[x][0], neutral_moves[x][1]
        else:
            x = random.randint(0, len(bad_moves) - 1)
            return neutral_moves[x][0], neutral_moves[x][1]
    # Computer level 3 and 4 uses minimax algorithm (depth 2 for level 3, depth 3-4 for level 4)
    else:
        # Turn 2: maximizing = False, opponent maximizing = True; and turn 1 is the other way around
        k = 1
        opponent_maximizing = True
        if turn == 1:
            k = -1
            opponent_maximizing = False
        score = 1000 * k
        best_move = [1000 * k, 0, 0]
        for i in range(len(list)):
            simulationboard = apply_move(board, turn, list[i][0], list[i][1])
            if level == 3:
                score = minimax(simulationboard, turn, 0, opponent_maximizing, -1000, 1000)
            else: # Level 4
                score = minimax(simulationboard, turn, 2, opponent_maximizing, -1000, 1000)
            if turn == 2:
                if best_move[0] > score:
                    best_move[0] = score
                    best_move[1] = list[i][0]
                    best_move[2] = list[i][1]
            elif turn == 1:
                if best_move[0] < score:
                    best_move[0] = score
                    best_move[1] = list[i][0]
                    best_move[2] = list[i][1]
            elif best_move[0] == score:
                if random.randint(0, 1) == 0:
                    best_move[0] = score
                    best_move[1] = list[i][0]
                    best_move[2] = list[i][1]
        return best_move[1], best_move[2]

def display_board(board):
    dimension = int(math.sqrt(len(board)))
    # Displays column number
    print("  ", end="")
    for i in range(dimension):
        if i > 9:
            print(" ", i + 1, end="")
        else:
            print("  ", i + 1, end="")
    print("\n")
    for i in range(dimension):
        # Displays left side row number
        if i >= 9: # Adjust board to display nicely
            print(i + 1, "  ", end="")
        else:
            print(i + 1, "   ", end="")
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

def menu():
    # Prompt the user for game modes (two human players or vs computer level 1-4)
    print("Welcome to Quixo")
    while(True): 
        print("Type the number below to choose game modes: ")
        print("0: two players (human vs human)")
        for i in range(4):
            print(f"{i + 1}: single player against computer Level {i + 1}")
        # Prompt game type & level with error checking
        while(True):
            level = input("Enter your choice: ")
            if checkint(level) == True:
                if 0 <= int(level) < 5:
                    break
            print("Invalid input! You can only type the integer 0, 1, 2, 3, or 4!")
        # Prompt the user for the size of the board (acceptable input: 2-20)
        while(True):
            n = input("Choose dimension: ")
            if checkint(n) == True:
                if 1 < int(n) <= 20:
                    break
            print("Invalid input! Please input only an integer between 2 and 20 inclusive!")
        # 2 players (human vs human)
        turn = 2
        board = [0 for i in range(int(n)*int(n))]
        # for 2 player (human vs human)
        if int(level) == 0:
            display_board(board)
            while(True):
                turn = turn % 2 + 1
                input_index, input_push_from = prompt_valid_move(board, turn, int(n))
                board = apply_move(board, turn, input_index, input_push_from)
                display_board(board)
                if check_victory(board, turn) != 0: 
                    print(f"Congratulations! Player {check_victory(board, turn)} wins!")
                    break
        # Single player (vs computer level 1/2/3/4)
        else:
            # Ask the human player to be the first or second player
            while(True):
                humanturn = input("Do you want to be the first or second player? Please enter integer 1 or 2! ")
                if checkint(humanturn) == True:
                    if 0 < int(humanturn) < 3:
                        break
                print("Invalid input! Please enter integer 1 or 2 only!")
            skipfirstmove = False
            if int(humanturn) == 2:
                skipfirstmove = True
            display_board(board)
            while(True):
                if skipfirstmove == False:
                    turn = turn % 2 + 1
                    input_index, input_push_from = prompt_valid_move(board, turn, int(n))
                    board = apply_move(board, turn, input_index, input_push_from)
                    display_board(board)
                    if check_victory(board, turn) != 0:
                        break
                turn = turn % 2 + 1
                print(f"Computer level {level} is thinking...")
                compindex, comppush = computer_move(board, turn, int(level))
                print(f"Computer move: row {compindex // int(n) + 1}, column {(compindex % int(n)) + 1}, push_from {comppush}")
                board = apply_move(board, turn, compindex, comppush)
                display_board(board)
                skipfirstmove = False
                if check_victory(board, turn) != 0:
                    break
            if check_victory(board, turn) == int(humanturn): 
                print(f"Congratulations! You win against computer level {level}!")
            else:
                print(f"Sorry, you lose against computer level {level}! Try again and good luck next time!")
        
        while(True):
            cont = input ('Wanna play again? Y/N ')  
            if cont == 'Y' or cont == 'y':
                break 
            elif cont == 'N' or cont == 'n':  
                print('Thank you and see you again.\n')
                return
            print('Invalid input! Input only Y/N ')

def prompt_valid_move(board, turn, dimension): # Keep reprompting the user until the move input is valid
    while(True):
        print(f"It is player {turn} turn.")
        while(True):
            row = input("Enter row: ")
            if checkint(row) == True:
                if 0 < int(row) < dimension + 1:
                    break
            print(f"Please enter a valid row number between 1 until {dimension} inclusive!")
        while(True):
            column = input("Enter column: ")
            if checkint(column) == True:
                if 0 < int(column) < dimension + 1:
                    break
            print(f"Please enter a valid column number between 1 until {dimension} inclusive!")
        while(True):
            input_push_from = input("Enter push direction: ")
            allowed = ['L', 'R', 'B', 'T']
            valid = False
            for i in range(4):
                if input_push_from == allowed[i]:
                    valid = True
            if valid == True:
                break
            print("Please enter a valid push direction! 'L': left, 'R': right, 'B': bottom, 'T': top")
        input_index = (int(row) - 1) * dimension + int(column) - 1
        if check_move(board, turn, input_index, input_push_from) == True:
            break
        print("Invalid move! Please enter a valid index and push direction!")
    return input_index, input_push_from 

def checkint(input): # Returns true if input is an integer, otherwise false
    try:
        val = int(input)
        return True
    except ValueError:
        return False

def all_valid_moves(board, turn): # Returns all possible valid moves from a board state
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

def positional_value(board, turn): # Returns score of a certain board state (positive means player 1 winning, negative means the opposite)
    dimension = int(math.sqrt(len(board)))
    score = 0
    # For minimizing player (player 2), all points will be multiplied with (-1)
    for i in range(1, 3, 1):
        m = 1
        if i == 2:
            m = -1
        # Score 999 if player 1 wins, -999 if player 2 wins
        if check_victory(board, turn) == i:
            return 999 * m
        # For any possible winning directions, score 4 if there are (dimension - 2) pieces, score 8 if there are (dimension - 1) pieces
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
                    score += (4 * m)
                if counter[l] >= dimension - 1:
                    score += (4 * m)
        # For every pieces ('O' or 'X') on the board, each piece contribute 1 point
        for q in range(len(board)):
            if board[q] == i:
                score += (1 * m)
    return score

def minimax(board, turn, depth, maximizing, alpha, beta): # Recursive function that returns predicted score of a move, added with alpha beta pruning
    # When game over or depth is = 0, evaluate the score of the state
    if depth == 0 or check_victory(board, turn) != 0:
        return positional_value(board, turn)
    valid_moves = all_valid_moves(board, turn)
    turn = turn % 2 + 1
    # Optimizing move for player 1 (maximize score)
    if maximizing == True:
        score = -1000
        for i in range(len(valid_moves)):
            board_simul = apply_move(board, turn, valid_moves[i][0], valid_moves[i][1])
            score_predict = minimax(board_simul, turn, depth - 1, False, -1000, 1000)
            score = max(score, score_predict)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
    # Optimizing move for player 2 (minimize score)
    else:
        score = 1000
        for i in range(len(valid_moves)):
            board_simul = apply_move(board, turn, valid_moves[i][0], valid_moves[i][1])
            score_predict = minimax(board_simul, turn, depth - 1, True, -1000, 1000)
            score = min(score, score_predict)
            beta = min(beta, score)
            if beta <= alpha:
                break
    return score

if __name__ == "__main__":
    menu()
