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
    x = 0
    o = 0
    for row in board:
        for move in row:
            if move == X:
                x += 1
            elif move == O:
                o += 1
    if x == 0:
        return X
    dif = x - o
    if dif == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == None:
                possible.add((i,j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    if board[action[0]][action[1]] != None:
        raise NotImplementedError
    next = player(board)
    newBoard[action[0]][action[1]] = next
    return newBoard



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    diag1 = set()
    diag2 = set()
    for i in range(3):
        row = set(board[i])
        if len(row) == 1:
            return board[i][0]
        col = set(row[i] for row in board)
        if len(col) == 1:
            return board[0][i]
        diag1.add(board[i][i])
        diag2.add(board[2-i][i])
    if len(diag1) == 1:
        return board[0][0]
    elif len(diag2) == 1:
        return board[2][0]
    else:
        return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif any(None in row for row in board):
        return False
    else:
        return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won is X:
        return 1
    elif won is O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) is X:
        return maxValue(board)[0]
    else:
        return minValue(board)[0]


def maxValue(board):
    if board == initial_state():
        return ((0,1), None)
    if terminal(board):
        return (None, utility(board))
    v = -math.inf
    bestMove = None
    for action in actions(board):
        maximum = max(v,minValue(result(board, action))[1])
        if maximum > v:
            bestMove = action
            v = maximum
    return (bestMove,v)


def minValue(board):
    if terminal(board):
        return (None, utility(board))
    v = math.inf
    bestMove = None
    for action in actions(board):
        minimum = min(v,maxValue(result(board, action))[1])
        if minimum < v:
            bestMove = action
            v = minimum
    return (bestMove,v)
