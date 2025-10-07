import numpy as np

ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    """Create a ROW_COUNT x COLUMN_COUNT board filled with 0s."""
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    """Place the player's piece (1 or 2) in the specified row and column."""
    board[row][col] = piece

def is_valid_location(board, col):
    """Check if the top row of the selected column is empty."""
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    """Return the first empty row in the selected column."""
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    """Print the board with X for Player 1 and O for Player 2."""
    print("\n")
    for r in range(ROW_COUNT-1, -1, -1):
        row_str = "| "
        for c in range(COLUMN_COUNT):
            if board[r][c] == 0:
                row_str += ". "
            elif board[r][c] == 1:
                row_str += "X "
            else:
                row_str += "O "
        row_str += "|"
        print(row_str)
    print("  0 1 2 3 4 5 6\n")

def winning_move(board, piece):
    """Check all possible win conditions for the given piece."""
    # Horizontal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if all(board[r][c+i] == piece for i in range(4)):
                return True
    # Vertical
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c] == piece for i in range(4)):
                return True
    # Positive diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if all(board[r+i][c+i] == piece for i in range(4)):
                return True
    # Negative diagonal
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if all(board[r-i][c+i] == piece for i in range(4)):
                return True
    return False

def play_game():
    board = create_board()
    game_over = False
    turn = 0

    print("Welcome to Connect Four!")
    print("Player 1: X  |  Player 2: O")
    print_board(board)

    while not game_over:
        try:
            # Determine current player
            if turn == 0:
                col = int(input("Player 1 (X), choose a column (0-6): "))
                piece = 1
            else:
                col = int(input("Player 2 (O), choose a column (0-6): "))
                piece = 2

            if 0 <= col <= 6:
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, piece)

                    print_board(board)

                    if winning_move(board, piece):
                        print(f"*** Player {piece} ({'X' if piece==1 else 'O'}) wins! ***")
                        game_over = True

                    # Switch turn
                    turn = (turn + 1) % 2
                else:
                    print("Column full! Try a different column.")
            else:
                print("Invalid column! Enter a number between 0 and 6.")

        except ValueError:
            print("Invalid input! Enter a valid number between 0 and 6.")

if __name__ == "__main__":
    play_game()
