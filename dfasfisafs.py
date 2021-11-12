
something = [(0, 1), (2, 3), (4, 5)]
for anything in something:
    print(anything[0], anything[1])




'''

row_to_block = [] #0, 1, 2, .. , dimension
column_to_block = []
diagonal_increasing = False
diagonal_decreasing = True
for i in range(dimension):
    score = 0
    for j in range(dimension):
        if board[i * dimension + j] == 1:
            score += 1
    if score == dimension - 1:
        row_to_block.append(i)
# Column
# Diagonal
for moves in range(len(valid_moves)):
    board_tmp = apply_move(board, turn, )
    for moves in range(len(row_to_block))
        score = 0
        for j in range(dimension):
            if board[row_to_block[moves] * dimension + j] == 1:
                score += 1
        if score == dimension - 2:
            return the move


'''
