"""Simple two-player Tic Tac Toe for the console."""

GAME_TITLE = "Tic Tac Toe"

WINNING_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),   # columns
    (0, 4, 8), (2, 4, 6),              # diagonals
]


def print_board(board):
    print()
    for row in range(3):
        a, b, c = board[row * 3: row * 3 + 3]
        print(f" {a} | {b} | {c} ")
        if row < 2:
            print("---+---+---")
    print()


def get_winner(board):
    for a, b, c in WINNING_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None


def play():
    board = [" "] * 9
    player = "X"

    print(GAME_TITLE)
    print("Enter a number 1-9 to place your mark:")
    print(" 1 | 2 | 3 \n---+---+---\n 4 | 5 | 6 \n---+---+---\n 7 | 8 | 9 ")

    for _ in range(9):
        print_board(board)
        while True:
            choice = input(f"Player {player}, choose a square (1-9): ")
            if choice.isdigit() and 1 <= int(choice) <= 9 and board[int(choice) - 1] == " ":
                board[int(choice) - 1] = player
                break
            print("Invalid move, try again.")

        if get_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"

    print_board(board)
    print("It's a draw!")


if __name__ == "__main__":
    play()