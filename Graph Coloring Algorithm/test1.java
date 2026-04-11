package com.GraphColoring;

import java.util.Scanner;

public class GraphColoring {

    private int V, numOfColors;
    private int[] color;
    private int[][] graph;

    // Main function to start coloring
    public void graphColor(int[][] g, int noc) {
        V = g.length;
        numOfColors = noc;
        color = new int[V];
        graph = g;

        try {
            solve(0);
            System.out.println("No solution found");
        } catch (Exception e) {
            System.out.println("\nSolution exists");
            display();
        }
    }

    // Recursive backtracking function
    public void solve(int v) throws Exception {

        // Base case: all vertices colored
        if (v == V) {
            throw new Exception("Solution found");
        }

        // Try all colors
        for (int c = 1; c <= numOfColors; c++) {

            if (isPossible(v, c)) {
                color[v] = c;

                solve(v + 1);

                // backtrack
                color[v] = 0;
            }
        }
    }

    // Check if color can be assigned
    public boolean isPossible(int v, int c) {
        for (int i = 0; i < V; i++) {
            if (graph[v][i] == 1 && color[i] == c) {
                return false;
            }
        }
        return true;
    }

    // Display result
    public void display() {

        String[] textColor = {
            "", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE",
            "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"
        };

        System.out.print("\nColors: ");

        for (int i = 0; i < V; i++) {
            System.out.print(textColor[color[i]] + " ");
        }

        System.out.println();
    }

    // Main method
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.println("Graph Coloring Algorithm Test\n");

        GraphColoring gc = new GraphColoring();

        System.out.println("Enter number of vertices:");
        int V = scan.nextInt();

        int[][] graph = new int[V][V];

        System.out.println("Enter adjacency matrix:");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                graph[i][j] = scan.nextInt();
            }
        }

        System.out.println("Enter number of colors:");
        int c = scan.nextInt();

        gc.graphColor(graph, c);
    }
}