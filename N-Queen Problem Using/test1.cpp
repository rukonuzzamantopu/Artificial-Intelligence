#include <iostream>
using namespace std;

class NQueen {
private:
    int N;

public:
    NQueen(int n) {
        N = n;
    }

    // Print board
    void printSolution(int **board) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    }

    // Check safe position
    bool isSafe(int **board, int row, int col) {

        // Check left side row
        for (int i = 0; i < col; i++) {
            if (board[row][i] == 1)
                return false;
        }

        // Check upper diagonal
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1)
                return false;
        }

        // Check lower diagonal
        for (int i = row, j = col; i < N && j >= 0; i++, j--) {
            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Backtracking function
    bool solveNQUtil(int **board, int col) {

        // Base case: all queens placed
        if (col >= N)
            return true;

        for (int i = 0; i < N; i++) {

            if (isSafe(board, i, col)) {

                board[i][col] = 1;

                if (solveNQUtil(board, col + 1))
                    return true;

                // BACKTRACK
                board[i][col] = 0;
            }
        }

        return false;
    }

    bool solveNQ() {

        // Create board
        int **board = new int*[N];
        for (int i = 0; i < N; i++) {
            board[i] = new int[N];
            for (int j = 0; j < N; j++) {
                board[i][j] = 0;
            }
        }

        if (!solveNQUtil(board, 0)) {
            cout << "Solution does not exist for " << N << " queens" << endl;
            return false;
        }

        cout << "Solution found for " << N << " queens" << endl;
        printSolution(board);

        return true;
    }
};

int main() {

    int n;
    cout << "Number of queens to place: ";
    cin >> n;

    NQueen q(n);
    q.solveNQ();

    return 0;
}