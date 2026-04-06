def dls(graph, node, depth, visited):
    if depth < 0:
        return

    print(node, end=" ")
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dls(graph, neighbor, depth - 1, visited)


def iddfs(graph, start, max_depth):
    print("\nIDDFS Traversal:")

    for depth in range(max_depth + 1):
        print(f"\nDepth {depth}: ", end="")
        visited = set()
        dls(graph, start, depth, visited)


graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node {i+1}: ")
    neighbors = input(f"Enter neighbors of {node} (space separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")
max_depth = int(input("Enter maximum depth: "))

iddfs(graph, start, max_depth)