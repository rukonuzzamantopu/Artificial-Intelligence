class GraphColoring:
    def __init__(self, graph, num_colors):
        self.graph = graph
        self.V = len(graph)
        self.num_colors = num_colors
        self.color = [0] * self.V

    # Check if color is safe
    def is_possible(self, v, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and self.color[i] == c:
                return False
        return True

    # Recursive backtracking
    def solve(self, v):

        # Base case: all vertices colored
        if v == self.V:
            return True

        for c in range(1, self.num_colors + 1):

            if self.is_possible(v, c):
                self.color[v] = c

                if self.solve(v + 1):
                    return True

                # backtrack
                self.color[v] = 0

        return False

    # Display result
    def display(self):

        text_color = [
            "", "RED", "GREEN", "BLUE", "YELLOW", "ORANGE",
            "PINK", "BLACK", "BROWN", "WHITE", "PURPLE", "VIOLET"
        ]

        print("\nColors:", end=" ")

        for i in self.color:
            print(text_color[i], end=" ")

        print()


# ---------------- MAIN ----------------

print("Graph Coloring Algorithm Test\n")

V = int(input("Enter number of vertices: "))

graph = []
print("Enter adjacency matrix:")
for i in range(V):
    row = list(map(int, input().split()))
    graph.append(row)

c = int(input("Enter number of colors: "))

gc = GraphColoring(graph, c)

if gc.solve(0):
    print("\nSolution exists")
    gc.display()
else:
    print("No solution found")