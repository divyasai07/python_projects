def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):  # Check rows
            return True
        if all(board[j][i] == player for j in range(3)):  # Check columns
            return True
    if all(board[i][i] == player for i in range(3)):  # Check diagonal (top-left to bottom-right)
        return True
    if all(board[i][2 - i] == player for i in range(3)):  # Check diagonal (top-right to bottom-left)
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        row = int(input(f"Player {players[current_player]}, enter row (0, 1, 2): "))
        col = int(input(f"Player {players[current_player]}, enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = players[current_player]

        if check_win(board, players[current_player]):
            print_board(board)
            print(f"Player {players[current_player]} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = (current_player + 1) % 2

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        tic_tac_toe()
    else:
        print("Thanks for playing!")

tic_tac_toe()
