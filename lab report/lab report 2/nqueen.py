def print_board(board, N):
    for i in range(N):
        for j in range(N):
            print("Q" if board[i][j] else ".", end=" ")
        print()
    print()

def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True



def solve_nq_util(board, col, N):
    if col >= N:
        print_board(board, N)
        return True


    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_nq_util(board, col + 1, N) or res
            board[i][col] = 0  # backtrack
    return res




def solve_nq(N):
    board = [[0] * N for _ in range(N)]
    if not solve_nq_util(board, 0, N):
        print("No solution exists")
    else:
        print("Solutions above")




# Example
solve_nq(4)
