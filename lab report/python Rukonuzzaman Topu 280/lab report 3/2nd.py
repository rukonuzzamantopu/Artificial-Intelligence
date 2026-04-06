# Depth Limited Search (DLS)
def dls(graph, current, goal, depth, path, visited):
    if depth < 0:
        return None

    path.append(current)
    visited.add(current)

    if current == goal:
        return path.copy()

    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            result = dls(graph, neighbor, goal, depth - 1, path, visited)
            if result:
                return result

    path.pop()
    return None


# IDDFS Function
def iddfs(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        visited = set()
        path = []

        result = dls(graph, start, goal, depth, path, visited)

        if result:
            print("\nPath found at depth:", depth)
            print("Path:", " -> ".join(result))
            return

    print("\nNo path found!")


# Main Program
graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")

    if node in graph:
        print("Node already exists! Enter unique node.")
        continue

    neighbors = input(
        f"Enter neighbors of {node} (space separated): "
    ).split()

    graph[node] = neighbors


start = input("Enter start node: ")
goal = input("Enter goal node: ")


# Validation
if start not in graph or goal not in graph:
    print("Error: Start or Goal node not found!")
    exit()


max_depth = int(input("Enter maximum depth: "))

iddfs(graph, start, goal, max_depth)