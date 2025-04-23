#!/usr/bin/python3

def print_board(board):
    """
    Prints the current state of the board.
    Parameters: board (list): 2D list representing the game board.
    Returns: None
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Checks if there's a winning combination on the board.
    Parameters: board (list): 2D list representing the game board.
    Returns: str or None: The winning symbol ("X" or "O") or None if no winner yet.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    """
    Checks if the board is completely filled.
    Parameters: board (list): 2D list representing the game board.
    Returns: bool
    """
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    """
    Runs the Tic Tac Toe game loop.
    Returns: None
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input loop with validation
        while True:
            try:
                row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
                col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
                if row not in range(3) or col not in range(3):
                    print("Invalid position. Please enter 0, 1, or 2.")
                elif board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        board[row][col] = player
        winner = check_winner(board)

        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player = "O" if player == "X" else "X"

tic_tac_toe()
