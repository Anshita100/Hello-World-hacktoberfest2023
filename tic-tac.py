def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    winner = None

    while not is_board_full(board) and not winner:
        print_board(board)
        row, col = map(int, input(f"Player {player}, enter row (0, 1, 2) and column (0, 1, 2) separated by a space: ").split())

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                winner = player
            player = "O" if player == "X" else "X"
        else:
            print("Invalid move. Try again.")

    print_board(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    tic_tac_toe()
