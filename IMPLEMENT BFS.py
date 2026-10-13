
from collections import deque

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input("Enter node name: ")
    neighbors = input("Enter neighbors separated by space: ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

print("BFS Traversal:")
bfs(graph, start)
