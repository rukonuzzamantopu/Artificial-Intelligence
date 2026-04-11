package n_queen;

import java.util.Scanner;

public class N_queen {

    int N;

    N_queen(int a) {
        N = a;
    }

    // Print solution
    void printSolution(int board[][]) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(board[i][j] + " ");
            }
            System.out.println();
        }
    }

    // Check if safe to place queen
    boolean isSafe(int grid[][], int row, int col) {

        // Check left row
        for (int i = 0; i < col; i++) {
            if (grid[row][i] == 1)
                return false;
        }

        // Check upper diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (grid[i][j] == 1)
                return false;
        }

        // Check lower diagonal
        for (int i = row, j = col; i < N && j >= 0; i++, j--) {
            if (grid[i][j] == 1)
                return false;
        }

        return true;
    }

    // Backtracking utility
    boolean solveNQUtil(int grid[][], int col) {

        if (col >= N)
            return true;

        for (int i = 0; i < N; i++) {

            if (isSafe(grid, i, col)) {

                grid[i][col] = 1;

                if (solveNQUtil(grid, col + 1))
                    return true;

                grid[i][col] = 0; // BACKTRACK
            }
        }

        return false;
    }

    boolean solveNQ() {

        int grid[][] = new int[N][N];

        if (!solveNQUtil(grid, 0)) {
            System.out.println("Solution does not exist for " + N + " queens");
            return false;
        }

        System.out.println("Solution found for " + N + " queens");
        printSolution(grid);
        return true;
    }

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("Number of queens to place:");
        int n = sc.nextInt();

        N_queen queen = new N_queen(n);
        queen.solveNQ();
    }
}