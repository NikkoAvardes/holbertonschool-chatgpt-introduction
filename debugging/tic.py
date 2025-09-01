def print_board(board):
    # Печать заголовка с номерами столбцов
    print("    0   1   2")
    print("  -------------")
    for i, row in enumerate(board):
        # Печать номера строки и самих ячеек с разделителями
        print(f"{i} | " + " | ".join(row) + " |")
        print("  -------------")

def check_winner(board):
    # Проверка строк
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Проверка столбцов
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("Invalid input! Please enter numbers 0, 1, or 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Coordinates out of range! Try again.")
            continue

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        moves += 1

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break
        elif moves == 9:
            print_board(board)
            print("It's a draw!")
            break

        # Смена игрока
        player = "O" if player == "X" else "X"

tic_tac_toe()