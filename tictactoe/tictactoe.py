"""
Tic Tac Toe Player
"""

import math

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
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                count += 1
            elif board[i][j] == O:
                count -= 1
                
    return X if count % 2 == 0 else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = [(i,j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]
                
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]

    for i in range(3):
        for j in range(3):
            new_board[i][j] = board[i][j]

    symbol = player(new_board)

    i, j = action
    new_board[i][j] = symbol

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner = None
    combinations = []
    
    # columns
    combinations += [[board[i][j] for i in range(3)] for j in range(3)]
    
    # rows
    combinations += board
    
    # diagonal
    combinations += [[board[i][j] for i in range(3) for j in range(3) if i == j]]
    combinations += [[board[i][j] for i in range(3) for j in range(3) if i + j == 2]]
    
    for combination in combinations:
        if combination == [X,X,X]:
            winner = X
            break
        if combination == [O,O,O]:
            winner = O
            break
            
    return winner
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    is_full = sum([1 for i in range(3) for j in range(3) if board[i][j] == EMPTY]) == 0
    return winner(board) is not None or is_full


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0

def evaluation(board):
    """
    Returns 1 if X will win the game, -1 if O will win, 0 otherwise
    """
    if terminal(board):
        return utility(board)
    
    if player(board) == X:
        v = float("-inf")
        for action in actions(board):
            v = max(v, evaluation(result(board, action)))
    else:
        v = float("inf")
        for action in actions(board):
            v = min(v, evaluation(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:

        best_eval = float("-inf")
        best_action = None
        for action in actions(board):
            v = evaluation(result(board,action))
            if v > best_eval:
                best_eval = v
                best_action = action
        return best_action

    else:

        best_eval = float('inf')
        best_action = None
        for action in actions(board):
            v = evaluation(result(board, action))
            if v < best_eval:
                best_eval = v
                best_action = action
        return best_action
