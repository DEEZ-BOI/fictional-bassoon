from tic_tac_toe.game import print_board, check_winner, is_full, EMPTY, HUMAN, AI
from tic_tac_toe.minmax import best_move


def play():
    board = [[EMPTY]*3 for _ in range(3)]

    while True:
        print_board(board)

        x, y = map(int, input("Enter move (row col): ").split())
        if board[x][y] != EMPTY:
            print("Invalid move")
            continue
        board[x][y] = HUMAN

        if check_winner(board) or is_full(board):
            break

        move = best_move(board)
        if move:
            board[move[0]][move[1]] = AI

        if check_winner(board) or is_full(board):
            break

    print_board(board)
    print("Winner:", check_winner(board))
