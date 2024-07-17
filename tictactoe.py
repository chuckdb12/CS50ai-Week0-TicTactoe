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
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                numX += 1
            elif board[i][j] == O:
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
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i,j))

    ##If no actions are possible, return None
    if not actions:
        return None

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action == 0:
        return
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
        if (row[0] == row[1] == row[2]) and row[0] != EMPTY:
            return row[0]
        
    #Then we check for a column win
    for col in range(3):
        if (board[0][col] == board[1][col] == board[2][col]) and board[0][col] != EMPTY:
            return board[0][col]

    #Finaly check for diagonal wins
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0]) and board[2][0] != EMPTY:
        return board[0][2]
    
    #If the board in not in a win state, we return None
    return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #First check if there is a winner
    if winner(board) is not None:
        return True
    
    #Check if the board is full
    if(all(all(element != EMPTY for element in row) for row in board)):
        return True
    
    #Otherwise, return false
    return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #Check who won, or if there is a tie
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    #If nobody won, it is a tie
    else: 
        return 0
    
def minimax_(board):
    """
    recursive version of minimax function, return v instead of the tuple
    """
        #First check if the game is over, if so, we return the winner
    if terminal(board):
        return utility(board)
    #The X player is the max player
    if player(board) == X:
        #We assign negative infinite value to v, which we want to maximize (1 if possible, 0 otherwise)
        v = -math.inf
        #We iterate on each action possible
        for action in actions(board):
            v = max(v,minimax_(result(board,action)))
        return v
    #The O player is the min player
    else:
        #We assign infinite value to v, which we want to minimize (-1 if possible, 0 otherwise)
        v = math.inf
        #We iterate on each action possible
        for action in actions(board):
            v = min(v,minimax_(result(board,action)))
        return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    move = None
    if(all(all(element == EMPTY for element in row) for row in board)):
        return (1,1)
    #First check if the game is over, if so, we return the winner
    if terminal(board):
        return utility(board)
    #The X player is the max player
    if player(board) == X:
        #We assign negative infinite value to v, which we want to maximize (1 if possible, 0 otherwise)
        v = -math.inf
        #We iterate on each action possible
        for action in actions(board):
            newV = max(v,minimax_(result(board,action)))
            if newV > v:
                v = newV
                move = action
        return move
    #The O player is the min player
    else:
        #We assign infinite value to v, which we want to minimize (-1 if possible, 0 otherwise)
        v = math.inf
        #We iterate on each action possible
        for action in actions(board):
            newV = min(v,minimax_(result(board,action)))
            if newV < v:
                v = newV
                move = action
        return move
    
