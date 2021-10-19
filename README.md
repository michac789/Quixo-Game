# Quixo-Game

# AI Bug TO-FIX LIST
- In early game, sometimes the computer makes a move that does not change the board outcome;
there should also be scores assigned to each opened pieces of the board

Buggy AI:
Welcome to Quixo
Type the number below to choose game modes: 
0: two players (human vs human)
1: single player against computer Level 1
2: single player against computer Level 2
3: single player against computer Level 3
4: single player against computer Level 4
Enter your choice: 4
Choose dimension: 1
Invalid input! Please input only an integer between 2 and 99 inclusive!
Choose dimension: 5
     1   2   3   4   5

1    _   _   _   _   _

2    _   _   _   _   _

3    _   _   _   _   _

4    _   _   _   _   _

5    _   _   _   _   _


It is player 1 turn.
Enter row: 1
Enter column: 1
Enter push direction: R
     1   2   3   4   5

1    _   _   _   _   X

2    _   _   _   _   _

3    _   _   _   _   _

4    _   _   _   _   _

5    _   _   _   _   _


Computer level 4 is thinking...
Move: row 4, column 1, push_from T
     1   2   3   4   5

1    O   _   _   _   X

2    _   _   _   _   _

3    _   _   _   _   _

4    _   _   _   _   _

5    _   _   _   _   _


It is player 1 turn.
Enter row: 2
Enter column: 1
Enter push direction: R
     1   2   3   4   5

1    O   _   _   _   X

2    _   _   _   _   X

3    _   _   _   _   _

4    _   _   _   _   _

5    _   _   _   _   _


Computer level 4 is thinking...
Move: row 4, column 1, push_from T
     1   2   3   4   5

1    O   _   _   _   X

2    O   _   _   _   X

3    _   _   _   _   _

4    _   _   _   _   _

5    _   _   _   _   _


It is player 1 turn.
Enter row: 3
Enter column: 5
Enter push direction: R
Invalid move!
It is player 1 turn.
Enter row: 3
Enter column: 5
Enter push direction: L
     1   2   3   4   5

1    O   _   _   _   X

2    O   _   _   _   X

3    X   _   _   _   _

4    _   _   _   _   _

5    _   _   _   _   _


Computer level 4 is thinking...
Move: row 4, column 5, push_from T
     1   2   3   4   5

1    O   _   _   _   O

2    O   _   _   _   X

3    X   _   _   _   X

4    _   _   _   _   _

5    _   _   _   _   _


It is player 1 turn.
Enter row:
Please enter a valid row number between 1 until 5 inclusive!
Enter row: 4
Enter column: 5
Enter push direction: L
     1   2   3   4   5

1    O   _   _   _   O

2    O   _   _   _   X

3    X   _   _   _   X

4    X   _   _   _   _

5    _   _   _   _   _


Computer level 4 is thinking...
Move: row 4, column 5, push_from T
     1   2   3   4   5

1    O   _   _   _   O

2    O   _   _   _   O

3    X   _   _   _   X

4    X   _   _   _   X

5    _   _   _   _   _


It is player 1 turn.
Enter row: 5
Enter column: 2
Enter push direction: T
     1   2   3   4   5

1    O   X   _   _   O

2    O   _   _   _   O

3    X   _   _   _   X

4    X   _   _   _   X

5    _   _   _   _   _


Computer level 4 is thinking...
Move: row 5, column 4, push_from R
     1   2   3   4   5

1    O   X   _   _   O

2    O   _   _   _   O

3    X   _   _   _   X

4    X   _   _   _   X

5    _   _   _   _   O


It is player 1 turn.
Enter row: 5
Enter column: 5
Enter push direction: L
Invalid move!
It is player 1 turn.
Enter row: 1
Enter column: 4
Enter push direction: B
     1   2   3   4   5

1    O   X   _   _   O

2    O   _   _   _   O

3    X   _   _   _   X

4    X   _   _   _   X

5    _   _   _   X   O


Computer level 4 is thinking...
Move: row 5, column 1, push_from T
     1   2   3   4   5

1    O   X   _   _   O

2    O   _   _   _   O

3    O   _   _   _   X

4    X   _   _   _   X

5    X   _   _   X   O


It is player 1 turn.
Enter row: 5
Enter column: 3
Enter push direction: T
     1   2   3   4   5

1    O   X   X   _   O

2    O   _   _   _   O

3    O   _   _   _   X

4    X   _   _   _   X

5    X   _   _   X   O


Computer level 4 is thinking...
Move: row 1, column 4, push_from R
     1   2   3   4   5

1    O   X   X   O   O

2    O   _   _   _   O

3    O   _   _   _   X

4    X   _   _   _   X

5    X   _   _   X   O


It is player 1 turn.
Enter row: 5
Enter column: 2
Enter push direction: T
     1   2   3   4   5

1    O   X   X   O   O

2    O   X   _   _   O

3    O   _   _   _   X

4    X   _   _   _   X

5    X   _   _   X   O


Computer level 4 is thinking...
Move: row 5, column 3, push_from T
     1   2   3   4   5

1    O   X   O   O   O

2    O   X   X   _   O

3    O   _   _   _   X

4    X   _   _   _   X

5    X   _   _   X   O


It is player 1 turn.
Enter row: 1
Enter column: 2
Enter push direction: B
     1   2   3   4   5

1    O   X   O   O   O

2    O   _   X   _   O

3    O   _   _   _   X

4    X   _   _   _   X

5    X   X   _   X   O


Computer level 4 is thinking...
Move: row 2, column 5, push_from L
     1   2   3   4   5

1    O   X   O   O   O

2    O   O   _   X   _

3    O   _   _   _   X

4    X   _   _   _   X

5    X   X   _   X   O


It is player 1 turn.
Enter row: 5
Enter column: 3
Enter push direction: T
     1   2   3   4   5

1    O   X   X   O   O

2    O   O   O   X   _

3    O   _   _   _   X

4    X   _   _   _   X

5    X   X   _   X   O


Computer level 4 is thinking...
Move: row 5, column 3, push_from T
     1   2   3   4   5

1    O   X   O   O   O

2    O   O   X   X   _

3    O   _   O   _   X

4    X   _   _   _   X

5    X   X   _   X   O


It is player 1 turn.
Enter row: 5
Enter column: 3
Enter push direction: T
     1   2   3   4   5

1    O   X   X   O   O

2    O   O   O   X   _

3    O   _   X   _   X

4    X   _   O   _   X

5    X   X   _   X   O


Computer level 4 is thinking...
Move: row 5, column 3, push_from T
     1   2   3   4   5

1    O   X   O   O   O

2    O   O   X   X   _

3    O   _   O   _   X

4    X   _   X   _   X

5    X   X   O   X   O


It is player 1 turn.
Enter row: 2
Enter column: 5
Enter push direction: R
Invalid move!
It is player 1 turn.
Enter row: 2
Enter column: 5
Enter push direction: L
     1   2   3   4   5

1    O   X   O   O   O

2    X   O   O   X   X

3    O   _   O   _   X

4    X   _   X   _   X

5    X   X   O   X   O


Computer level 4 is thinking...
Move: row 5, column 3, push_from T
     1   2   3   4   5

1    O   X   O   O   O

2    X   O   O   X   X

3    O   _   O   _   X

4    X   _   O   _   X

5    X   X   X   X   O


It is player 1 turn.
Enter row: 4
Enter column: 5
Enter push direction: B
     1   2   3   4   5

1    O   X   O   O   O

2    X   O   O   X   X

3    O   _   O   _   X

4    X   _   O   _   O

5    X   X   X   X   X


