from collections import deque

class Node:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level



class BFS:
    def __init__(self):
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.found = False
        self.goal_level = 0
        self.N = 0
        self.source = None
        self.goal = None


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

        # Perform BFS
        self.bfs(graph)

        # Print result
        if self.found:
            print("Goal found")
            print("Number of moves required =", self.goal_level)
        else:
            print("Goal cannot be reached from starting block")


    def bfs(self, graph):
        queue = deque()
        queue.append(self.source)

        while queue:
            u = queue.popleft()  # Dequeue the front node

            # Explore neighbors
            for dx, dy in self.directions:
                v_x, v_y = u.x + dx, u.y + dy

                # Check if neighbor is within grid boundaries and is a valid move
                if 0 <= v_x < self.N and 0 <= v_y < self.N and graph[v_x][v_y] == 1:
                    v_level = u.level + 1  # Increment level
                    print("Moving to ", v_x, v_y)

                    # Check if neighbor is the goal
                    if v_x == self.goal.x and v_y == self.goal.y:
                        self.found = True
                        self.goal_level = v_level
                        self.goal.level = v_level
                        return

                    graph[v_x][v_y] = 0  # Mark neighbor as visited
                    child = Node(v_x, v_y, v_level)
                    queue.append(child)  # Enqueue the neighbor


if __name__ == "__main__":
    bfs = BFS()
    bfs.init()