import random
import math

def check_move(board, turn, index, push_from):
    n = int(len(board)**0.5)
    turn %= 2 
    #meaning that if the board is non zero, then we check: if turn + 2 / turn != that board[index], it means that we take oponent's square 
    if board[index] !=0 and board[index] != turn+2 and board[index] != turn: 
        return False
    if 0<=index<n and push_from == 'T': 
        return False
    elif n**2 - n<=index<n**2 and push_from == 'B': 
        return False
    elif (index+1)%n == 0 and push_from == 'R':
        return False 
    elif index%n == 0 and push_from == 'L':
        return False 
    elif not(0<=index<n or n**2-n<=index<n**2 or (index+1)%n == 0 or index%n == 0): 
        return False
    return True 

def apply_move(board, turn, index, push_from):
    n = int(len(board)**0.5)
    board_temp = board[:]
    if turn%2 == 0 :
        symbol = 2
    else:
        symbol = 1
    # move top 
    if push_from == 'T' :
       for i in range (index, index%n, -n):
           board_temp [i] = board_temp [i-n]
       board_temp [index%n] = symbol  
    # move bottom 
    elif push_from == 'B' : 
        for i in range(index, n*(n-1)+index%n, n):
            board_temp[i] = board_temp[i+n]
        board_temp[index%n + n*(n-1)] = symbol 
    # move right 
    elif push_from == 'R':
        for i in range (index, (index//n+1)*n-1):
            board_temp[i] = board_temp[i+1] 
        board_temp[(index//n+1)*n-1] = symbol 
    # move left
    elif push_from == 'L': 
        for i in range(index, index//n*n,-1):
            board_temp[i] = board_temp[i-1] 
        board_temp[index//n*n] = symbol         
    return board_temp[:]

def check_victory(board, who_played): 
    n = int (len(board)**0.5)
    winner = 0 
    # checking row
    for row in range (n) :
        victory = True 
        for j in range (n-1) : 
            if board[row*n+j] == 0 or board[row*n + j] != board[row*n+j+1] :
                victory = False
        if victory == True and (winner == who_played or winner == 0):
            winner = board[row*n+j]  
    # checking column 
    for column in range (n) :
        victory = True 
        for i in range (n-1) : 
            if board[column + i*n] == 0 or board[column + i*n] != board[column + (i+1)*n] :
                victory = False 
        if victory == True and (winner == who_played or winner == 0):
            winner = board[column + i*n]
    # checking diagonal from right 
    victory = True 
    for i in range (1,n):
        if board [(n-1)*i] == 0 or board [(n-1)*i] != board [(n-1)*(i+1)] :
            victory = False 
    if victory == True and (winner == who_played or winner == 0):
        winner = board[(n-1)*i]
    victory = True  
    # checking diagonal from left 
    for i in range (n-1):
        if board [(n+1)*i] == 0 or board [(n+1)*i] != board [(n+1)*(i+1)] :
            victory = False 
    if victory == True and (winner == who_played or winner == 0):
        winner = board[(n+1)*i] 
    if winner == 0 :
        return 0 
    else : 
        return winner 
    

def computer_move(board, turn, level):
    # implement your function here
    return (0,'B')
    
def display_board(board): 
    n = int(len(board)**0.5)
    print (end = '  ')
    #printing the column index 
    for i in range (n) :
        print (i+1, end=' ')
    print ()    
    
    for i in range (n**2):
        if i % n == 0 :
            print (i // n + 1, end = ' ')
        print(board[i], end='')
        if (i+1-n)%n == 0:
            print()
        else:
            print(end = ' ')
    
def menu():
    turn = 1 
    n = int(input('Enter the size of the board: '))
    board = [0 for i in range (n**2)]
    display_board(board)  
    while(True):
        gameMode = int(input ('Choose 1: \n1. Vs Computer or 2. vs Player '))  
        if gameMode == 1: 
            level = int(input('Choose level:  ')) 
            while(True):
                if(turn%2 == 1):
                    while(True):
                        # can we actually change this into function? 
                        #need input correction 
                        i = int(input('insert row: ')) 
                        #need input correction 
                        j = int(input('insert column: ')) 
                        index = (i-1)*n + j-1
                        # need input correction 
                        push_from = input('direction: ')
                        # when check_move returning false, we repeat the loop. If it is returning true, it is over and we can proceed
                        valid_move = check_move(board, turn, index, push_from)
                        if valid_move :
                            break 
                            print('Invalid move, please try again!')
                    board = apply_move(board, turn, index, push_from)
                if(turn % 2 == 0):
                    index, push_from = computer_move(board, turn, level) 
                    apply_move(board, turn, index, push_from) 
        
                display_board(board)  
                who_played = turn%2 
                turn +=1   
                # to adjust since the turn here is only useful for determining just using the modulus 
                if who_played == 0 :
                    who_played +=2 
                gameOver = check_victory(board, who_played) 
                if gameOver == 1: 
                    print ('Player 1 Wins, thank you') 
                    break 
                elif gameOver == 2 :
                    print ('Player 2 Wins, thank you') 
                    break 

        elif gameMode==2:
            while(True):
                while(True):
                    #need input correction 
                    i = int(input('insert row: ')) 
                    #need input correction 
                    j = int(input('insert column: ')) 
                    index = (i-1)*n + j-1
                    # need input correction 
                    push_from = input('direction: ')
                    # when check_move returning false, we repeat the loop. If it is returning true, it is over and we can proceed
                    valid_move = check_move(board, turn, index, push_from)
                    if valid_move :
                        break 
                        print('Invalid move, please try again!')
                board = apply_move(board, turn, index, push_from)
                display_board(board)  
                who_played = turn%2 
                # to adjust since the turn here is only useful for determining just using the modulus 
                if who_played == 0 :
                    who_played +=2 
                turn += 1  
                gameOver = check_victory(board, who_played) 
                if gameOver == 1: 
                    print ('Player 1 Wins, thank you') 
                    break 
                elif gameOver == 2 :
                    print ('Player 2 Wins, thank you') 
                    break 
            

        
            
            
            
if __name__ == "__main__":
    menu() 


    
