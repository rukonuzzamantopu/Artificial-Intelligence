#include <iostream>
using namespace std;

class GraphColoring {
private:
    int V, numOfColors;
    int *color;
    int **graph;

public:
    // Start graph coloring
    void graphColor(int **g, int noc, int vertices) {
        V = vertices;
        numOfColors = noc;

        color = new int[V];
        graph = g;

        // initialize colors
        for (int i = 0; i < V; i++)
            color[i] = 0;

        if (solve(0)) {
            cout << "\nSolution exists\n";
            display();
        } else {
            cout << "No solution found\n";
        }
    }

    // Backtracking function
    bool solve(int v) {
        // Base case: all vertices colored
        if (v == V)
            return true;

        for (int c = 1; c <= numOfColors; c++) {

            if (isPossible(v, c)) {
                color[v] = c;

                if (solve(v + 1))
                    return true;

                // backtrack
                color[v] = 0;
            }
        }

        return false;
    }

    // Check if color is safe
    bool isPossible(int v, int c) {
        for (int i = 0; i < V; i++) {
            if (graph[v][i] == 1 && color[i] == c)
                return false;
        }
        return true;
    }

    // Display result
    void display() {
        string textColor[] = {
            "", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE",
            "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"
        };

        cout << "\nColors: ";
        for (int i = 0; i < V; i++) {
            cout << textColor[color[i]] << " ";
        }
        cout << endl;
    }
};

// Main function
int main() {
    int V, c;

    cout << "Graph Coloring Algorithm Test\n";

    cout << "Enter number of vertices: ";
    cin >> V;

    // dynamic 2D array
    int **graph = new int*[V];
    for (int i = 0; i < V; i++)
        graph[i] = new int[V];

    cout << "Enter adjacency matrix:\n";
    for (int i = 0; i < V; i++) {
        for (int j = 0; j < V; j++) {
            cin >> graph[i][j];
        }
    }

    cout << "Enter number of colors: ";
    cin >> c;

    GraphColoring gc;
    gc.graphColor(graph, c, V);

    return 0;
}