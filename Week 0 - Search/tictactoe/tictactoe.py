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
    # Count moves to decide whose turn it is
    x_count = 0
    o_count = 0
    for row in board:
        for cell in row:
            if cell == X:
                x_count += 1
            elif cell == O:
                o_count += 1

    # X starts, then alternates; if equal, it's X's turn, else O's turn
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                possible.add((i, j))
    return possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None or len(action) != 2:
        raise Exception("Invalid action")

    i, j = action
    if i not in (0, 1, 2) or j not in (0, 1, 2):
        raise Exception("Action out of bounds")

    if board[i][j] is not EMPTY:
        raise Exception("Invalid action: cell is not empty")

    # Deep copy the board (3x3)
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    lines = []

    # Rows
    for i in range(3):
        lines.append([(i, 0), (i, 1), (i, 2)])
    # Columns
    for j in range(3):
        lines.append([(0, j), (1, j), (2, j)])
    # Diagonals
    lines.append([(0, 0), (1, 1), (2, 2)])
    lines.append([(0, 2), (1, 1), (2, 0)])

    for line in lines:
        a, b, c = line
        v1 = board[a[0]][a[1]]
        if v1 is EMPTY:
            continue
        if v1 == board[b[0]][b[1]] and v1 == board[c[0]][c[1]]:
            return v1

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    # If any EMPTY remains, game is not over
    for row in board:
        for cell in row:
            if cell is EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == X:
        return 1
    if w == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    turn = player(board)

    # Alpha-beta minimax
    def max_value(b, alpha, beta):
        if terminal(b):
            return utility(b), None
        v = -math.inf
        best_action = None
        for act in actions(b):
            score, _ = min_value(result(b, act), alpha, beta)
            if score > v:
                v = score
                best_action = act
            alpha = max(alpha, v)
            if alpha >= beta:
                break
        return v, best_action

    def min_value(b, alpha, beta):
        if terminal(b):
            return utility(b), None
        v = math.inf
        best_action = None
        for act in actions(b):
            score, _ = max_value(result(b, act), alpha, beta)
            if score < v:
                v = score
                best_action = act
            beta = min(beta, v)
            if alpha >= beta:
                break
        return v, best_action

    if turn == X:
        _, move = max_value(board, -math.inf, math.inf)
        return move
    else:
        _, move = min_value(board, -math.inf, math.inf)
        return move
