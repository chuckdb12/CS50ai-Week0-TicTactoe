"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #If all elements in the board are empty, X starts the game
    if(all(all(element == EMPTY for element in row) for row in board)):
        return X
    
    numX = 0
    numO = 0
    for i in board:
        for j in board[i]:
            if board[i,j] == X:
                numX += 1
            elif board[i,j] == O:
                numO += 1
    
    #If there is more Xs than Os, it's O's turn
    if numX > numO:
        return O
    #If they are equal, it's X's turn

    elif numO == numX:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions = set()
    
    #iterate on each position in the board to check if it's empty
    for i in board:
        for j in board:
            if board[i,j] == EMPTY:
                actions.add(board[i,j])

    ##If no actions are possible, return None
    if not actions:
        return None

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #If the position is not Empty, raise exception
    if board[action[0]][action[1]] != EMPTY:
        raise IndexError("Action not valid")

    #Make a deep copy of the board
    boardCopy = copy.deepcopy(board)

    #We add the right player to the correct position
    boardCopy[action[0]][action[1]] = player(board)

    return boardCopy


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #Let's first see if we have a win state in a row
    for row in board:
        if (row[0] == row[1] == row[2]) and board[0][col] != EMPTY:
            return row[0]
        
    #Then we check for a column win
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] != EMPTY:
            return board[0][col]

    #Finaly check for diagonal wins
    if (board[0][0] == board[1][1] == board[2][2]) and 

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
