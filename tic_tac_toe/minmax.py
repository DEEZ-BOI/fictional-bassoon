import math
from tic_tac_toe.game import check_winner, is_full, EMPTY, HUMAN, AI


def minimax(board, is_maximizing):
    winner = check_winner(board)

    if winner == AI:
        return 1
    if winner == HUMAN:
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    score = minimax(board, False)
                    board[i][j] = EMPTY
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    score = minimax(board, True)
                    board[i][j] = EMPTY
                    best = min(best, score)
        return best


def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                score = minimax(board, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move
