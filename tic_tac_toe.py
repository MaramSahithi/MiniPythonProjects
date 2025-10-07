# Tic Tac Toe - 1D Board Version

# The game board
board = [' ' for _ in range(9)]

def print_board():
    """Prints the current state of the board."""
    print('-------------')
    print(f'| {board[0]} | {board[1]} | {board[2]} |')
    print('-------------')
    print(f'| {board[3]} | {board[4]} | {board[5]} |')
    print('-------------')
    print(f'| {board[6]} | {board[7]} | {board[8]} |')
    print('-------------')

def check_win(player):
    """Checks all winning combinations for the given player."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw():
    """Checks if the game is a draw."""
    return ' ' not in board

def game():
    """Main game loop."""
    current_player = 'X'
    while True:
        print_board()
        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == ' ':
                board[move - 1] = current_player
                if check_win(current_player):
                    print_board()
                    print(f"Player {current_player} wins!")
                    break
                if check_draw():
                    print_board()
                    print("It's a draw!")
                    break
                # Switch player
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("Invalid move. Cell already occupied or out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

if __name__ == "__main__":
    game()

