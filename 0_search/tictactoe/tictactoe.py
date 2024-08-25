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
    flat_board = sum(board, start=[])

    x_count = flat_board.count(X)
    o_count = flat_board.count(O)

    if x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row_index, row in enumerate(board):
        for column_index, player in enumerate(row):
            if player is None: 
                actions.add((row_index, column_index))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if (action[0] > len(board) - 1 or action[0] < 0 or 
            action[1] > len(board[action[0]]) - 1 or action[1] < 0):
        raise IndexError('That is not a valid board space')
    elif board[action[0]][action[1]] is not None:
        raise Exception('That square is already taken')
    
    board_copy = copy.deepcopy(board)
    board_copy[action[0]][action[1]] = player(board)

    return board_copy

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_lines = []
    grid_range = range(0, 3)

    for row in grid_range:
        winning_lines.append([ (row, column) for column in grid_range ])
        winning_lines.append([ (column, row) for column in grid_range ])

    winning_lines.append([ (len(grid_range) - idx - 1, idx) for idx in grid_range ])
    winning_lines.append([ (idx, idx) for idx in grid_range ])
        
    for player in [X, O]:
        if any(all(board[row][column]==player for row, column in line) for line in winning_lines):
            return player
    
    return None
     
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or len(actions(board)) == 0
    

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_value(board):
    if terminal(board):
        return utility(board)

    v = -math.inf

    for action in actions(board):
        v = max(v, min_value(result(board, action)))

    return v

    
def min_value(board):
    if terminal(board):
        return utility(board)

    v = math.inf

    for action in actions(board):
        v = min(v, max_value(result(board, action)))

    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): 
        return None

    if player(board) == X:
        optimal_action = None
        best_value = -math.inf

        for action in actions(board):
            value = min_value(result(board, action))
            if value > best_value:
                best_value = value
                optimal_action = action
    else:
        optimal_action = None
        best_value = math.inf

        for action in actions(board):
            value = max_value(result(board, action))
            if value < best_value:
                best_value = value
                optimal_action = action

    return optimal_action