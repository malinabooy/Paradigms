def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Проверка строк
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Проверка столбцов
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[row][col] != ' ' for row in range(len(board))):
            return True

    # Проверка диагоналей
    if all(board[i][i] == board[0][0] and board[i][i] != ' ' for i in range(len(board))) or \
       all(board[i][len(board) - 1 - i] == board[0][len(board) - 1] and board[i][len(board) - 1 - i] != ' ' for i in range(len(board))):
        return True

    return False

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row = int(input(f'Игрок {current_player}, выберите строку (0, 1, 2): '))
        col = int(input(f'Игрок {current_player}, выберите столбец (0, 1, 2): '))

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print('Эта ячейка уже занята. Выберите другую.')
            continue

        if check_winner(board):
            print_board(board)
            print(f'Игрок {current_player} победил!')
            break
        elif is_board_full(board):
            print_board(board)
            print('Ничья!')
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    tic_tac_toe()
