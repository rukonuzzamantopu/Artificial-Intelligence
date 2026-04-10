def is_moves_left(board):
    for row in board:
        for cell in row:
            if cell == '':
                return True
    return False


def evaluate(b):
    for row in range(6):
        for col in range(4):
            if b[row][col] == b[row][col+1] == b[row][col+2] == b[row][col+3] == 'o':
                return 10
        for col in range(7):
            for row in range(3):
                if b[row][col] == b[row+1][col] == b[row+2][col] == b[row+3][col] == 'o':
                    return 10
        for row in range(3):
            for col in range(4):
                if b[row][col] == b[row+1][col+1] == b[row+2][col+2] == b[row+3][col+3] == 'o':
                    return 10
        for row in range(3, 6):
            for col in range(3):
                if b[row][col] == b[row - 1][col+1] == b[row-2][col+2] == b[row - 3][col+3] == 'o':
                    return 10

        return 0


def minimax(board, depth, is_max):
    score = evaluate(board)

    if score == 10:
        return score - depth
    if not is_moves_left(board):
        return 0
    if is_max:
        best_value = -float('inf')
        for col in range(7):
            for row in range(5, -1, -1):
                if board[row][col] == '':
                    board[row][col] = 'x'
                    best_val = max(best_val, minimax(
                        board, depth+1, not is_max))
                    board[row][col] = ''
                    break
        return best_val
    else:
        best_value = float('inf')
        for col in range(7):
            for row in range(5, -1, -1):
                if board[row][col] == '':
                    board[row][col] = 'o'
                    best_val = max(best_val, minimax(
                        board, depth+1, not is_max))
                    board[row][col] = ''
                    break
        return best_val


def find_optimal_move(board):
    best_move = None
    best_val = -float('inf')

    for col in range(7):
        for row in range(5, -1, -1):
            if board[row][col] == '':
                board[row][col] = 'o'
                move_val = minimax(board, 0, False)
                board[row][col] = ''

                if move_val > best_val:
                    best_val = move_val
                    best_move = (row, col)
                break
    return best_move


board = [
    ['x', 'x', 'o', '', '', '', 'x'],
    ['o', 'o', 'o', 'x', '', '', 'x'],
    ['x', 'o', '', '', '', '', ''],
    ['x', 'o', 'o', '', '', '', ''],
    ['x', 'x', 'x', 'o', '', '', ''],
    ['o', 'o', 'x', 'o', 'x', '', '']
]
optimal_move = find_optimal_move(board)
if optimal_move:
    print("The optimal move for player O to win is:", optimal_move)
else:
    print("Player O cannot win with the current board configuration")