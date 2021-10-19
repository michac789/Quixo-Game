


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
        # Displays 'X' for player 1, 'O' for player 2, '_' 
        for j in range(dimension):
            if board[i * dimension + j] == 1:
                print("X", end="   ")
            elif board[i * dimension + j] == 2:
                print("O", end="   ")
            else:
                print("_", end="   ")
        print("\n")
    print("")