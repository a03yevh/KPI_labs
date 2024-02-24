import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def display_board(board):
    for row in board:
        print("|".join(row))
        print("-----")

def choose_marker():
    marker1 = input("Гравець 1, оберіть своє означення (X або O): ").upper()
    while marker1 not in ['X', 'O']:
        print("Неправильний вибір. Будь ласка, оберіть X або O.")
        marker1 = input("Гравець 1, оберіть своє означення (X або O): ").upper()

    marker2 = 'X' if marker1 == 'O' else 'O'
    return marker1, marker2

def choose_first_player():
    return random.choice([1, 2])

def is_position_valid(board, row, col):
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' '

def is_winner(board, marker):
    for i in range(3):
        if all(board[i][j] == marker for j in range(3)) or \
           all(board[j][i] == marker for j in range(3)):
            return True

    if all(board[i][i] == marker for i in range(3)) or \
       all(board[i][2-i] == marker for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_game():
    board = initialize_board()
    player1_marker, player2_marker = choose_marker()
    current_player = choose_first_player()

    while True:
        display_board(board)
        row = int(input(f"Гравець {current_player}, виберіть рядок (0-2): "))
        col = int(input(f"Player {current_player}, виберіть колонку (0-2): "))

        if is_position_valid(board, row, col):
            board[row][col] = player1_marker if current_player == 1 else player2_marker

            if is_winner(board, player1_marker):
                display_board(board)
                print(f"Гравець 1 здобув перемогу!")
                break
            elif is_winner(board, player2_marker):
                display_board(board)
                print(f"Гравець 2 здобув перемогу!")
                break
            elif is_board_full(board):
                display_board(board)
                print("Зіграно в нічию!")
                break

            current_player = 3 - current_player
        else:
            print("Неправильний хід. Будь ласка, оберіть пусту позицію.")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("Бажаєте зіграти ще раз? (так/ні): ").lower()
        if play_again != 'так':
            print("Дякуємо за гру. До побачення!")
            break
