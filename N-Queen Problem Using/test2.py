# ================================
# N-QUEEN PROBLEM USING BACKTRACKING
# ================================

# Function to check if it is safe to place a queen
def isSafe(board, row, col, N):

    # -------------------------------
    # Check LEFT side in same row
    # -------------------------------
    # We only check left side because queens are placed column by column
    for i in range(col):
        if board[row][i] == 1:
            return False  # Another queen found → not safe

    # -------------------------------
    # Check upper diagonal (↖)
    # -------------------------------
    # Move diagonally up-left
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False  # Queen found → not safe

    # -------------------------------
    # Check lower diagonal (↙)
    # -------------------------------
    # Move diagonally down-left
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False  # Queen found → not safe

    # If no conflict found, position is safe
    return True


# ================================
# RECURSIVE FUNCTION (BACKTRACKING)
# ================================
def solveNQUtil(board, col, N):

    # -------------------------------
    # BASE CASE:
    # If all queens are placed
    # -------------------------------
    if col >= N:
        return True

    # Try placing queen in each row of current column
    for i in range(N):

        # Check if safe to place queen at (i, col)
        if isSafe(board, i, col, N):

            # Place queen
            board[i][col] = 1

            # Recur to place next queen in next column
            if solveNQUtil(board, col + 1, N):
                return True

            # -------------------------------
            # BACKTRACK:
            # If placing queen here doesn't lead to solution
            # remove it and try next row
            # -------------------------------
            board[i][col] = 0

    # If no row works in this column → fail
    return False


# ================================
# FUNCTION TO PRINT SOLUTION
# ================================
def printSolution(N):

    # Create NxN board filled with 0 (no queens)
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Start solving from column 0
    if not solveNQUtil(board, 0, N):
        print("Solution does not exist")
        return False

    print("Solution found for", N, "queens\n")

    # Print final board
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

    return True


# ================================
# MAIN PROGRAM
# ================================

# Take input from user
n = int(input("Number of queens to place:\n"))

# Call function to solve problem
printSolution(n)