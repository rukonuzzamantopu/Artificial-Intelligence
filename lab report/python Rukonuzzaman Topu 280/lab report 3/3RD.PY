import heapq

def a_star(graph, heuristic, start, goal):
    # Priority Queue: (f_cost, node, path, g_cost)
    queue = []

    heapq.heappush(queue, (heuristic[start], start, [start], 0))

    visited = set()

    while queue:

        # Print queue at each step
        print("\nCurrent Queue:")
        for item in queue:
            print(item)

        f, current, path, g = heapq.heappop(queue)

        if current == goal:
            print("\nGoal Reached!")
            print("Path:", " -> ".join(path))
            print("Total Cost:", g)
            return

        if current in visited:
            continue

        visited.add(current)

        for neighbor, cost in graph[current]:
            if neighbor not in visited:

                new_g = g + cost
                new_f = new_g + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (new_f, neighbor, path + [neighbor], new_g)
                )

    print("No path found!")


# Graph
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

# Heuristic values
heuristic = {
    'A': 6,
    'B': 4,
    'C': 5,
    'D': 2,
    'E': 1,
    'F': 0
}

start = 'A'
goal = 'F'

a_star(graph, heuristic, start, goal)