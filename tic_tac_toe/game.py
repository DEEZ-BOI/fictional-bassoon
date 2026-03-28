EMPTY = " "
HUMAN = "X"
AI = "O"


def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("---------")


def check_winner(board):
    lines = board + list(zip(*board)) + [
        [board[i][i] for i in range(3)],
        [board[i][2 - i] for i in range(3)],
    ]
    for line in lines:
        if line.count(line[0]) == 3 and line[0] != EMPTY:
            return line[0]
    return None


def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)
