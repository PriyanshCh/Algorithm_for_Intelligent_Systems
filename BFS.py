import time
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = []
        result = []

        visited[start] = True
        queue.append(start)

        while queue:
            node = queue.pop(0)
            result.append(node)

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        return result

# Create a sample graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Measure the execution time of BFS
start_vertex = 2
start_time = time.time()
bfs_result = g.bfs(start_vertex)
end_time = time.time()

execution_time_microseconds = (end_time - start_time) * 1e6

print("BFS traversal starting from vertex", start_vertex, ":", bfs_result)
print("Execution Time (microseconds):", execution_time_microseconds)
