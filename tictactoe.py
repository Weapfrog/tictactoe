"""
Tic Tac Toe Player
"""

import math
import copy
import random

X = "X"
O = "O"
EMPTY = None
number_of_moves = 0

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count=0
    o_count=0
    empty_count=0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                x_count += 1
            if board[row][col] == O:
                o_count += 1
            if board[row][col] == EMPTY:
                empty_count += 1
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    empty_boxes=list()
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                empty_boxes.append((row,col))
    return list(empty_boxes)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row,col=action
    if board[row][col] == EMPTY:
        new_board = copy.deepcopy(board)
        new_board[row][col] = player(board)
        return new_board
    else:
        raise Exception("Hata")

def row_winner(board,player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
    return None

def col_winner(board,player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
    return None

def diagonal_winner(board,player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    None

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if col_winner(board,X) or row_winner(board,X) or diagonal_winner(board,X):
        return X
    if col_winner(board,O) or row_winner(board,O) or diagonal_winner(board,O):
        return O
    return None
        

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    return v

def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board,action)),action])
        return sorted(plays,key=lambda x: x[0],reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board,action)),action])
        return sorted(plays,key=lambda x: x[0])[0][1]