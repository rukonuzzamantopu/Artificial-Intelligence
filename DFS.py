class Node:
    def __init__(self, x, y, depth):
        self.x = x
        self.y = y
        self.depth = depth
# End of Node class (used to store position and depth info)


class DFS:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Moves: down, up, right, left
        self.found = False
        self.goal_depth = 0
        self.N = 0
        self.source = None
        self.goal = None
    # End of __init__ function (initializes DFS properties)

    def init(self):
        # Initialize the grid
        graph = [
            [0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 0, 0, 1]
        ]

        self.N = len(graph)

        # Define source and goal nodes
        s1, s2 = 0, 2
        g1, g2 = 4, 4

        self.source = Node(s1, s2, 0)
        self.goal = Node(g1, g2, float('inf'))

        # Perform DFS
        self.st_dfs(graph, self.source)

        # Print result
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_depth)
        else:
            print("Goal cannot be reached from starting block")
    # End of init function (sets up grid, source, goal, and runs DFS)

    def st_dfs(self, graph, u):
        graph[u.x][u.y] = 0  # Mark current node as visited

        for dx, dy in self.directions:
            v_x, v_y = u.x + dx, u.y + dy

            # Check if neighbor is within grid boundaries and is a valid move
            if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                v_depth = u.depth + 1  # Increment depth
                print("Moving to", v_x, v_y)

                # Check if neighbor is the goal
                if v_x == self.goal.x and v_y == self.goal.y:
                    self.found = True
                    self.goal_depth = v_depth
                    self.goal.depth = v_depth
                    return

                child = Node(v_x, v_y, v_depth)
                self.st_dfs(graph, child)  # Recursive DFS call
                if self.found:
                    return
    # End of st_dfs function (performs DFS traversal and finds path)


if __name__ == "__main__":
    dfs = DFS()
    dfs.init()
# End of main execution (program starts DFS process)
