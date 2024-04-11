import time
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, start, visited, result):
        visited[start] = True
        result.append(start)

        for neighbor in self.graph[start]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited, result)

# Create a sample graph
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

# Measure the execution time of DFS
start_vertex =1
start_time = time.time()
visited = [False] * len(g.graph)
dfs_result = []
g.dfs(start_vertex, visited, dfs_result)
end_time = time.time()

execution_time_microseconds = (end_time - start_time) * 1e6

print("DFS traversal starting from vertex", start_vertex, ":", dfs_result)
print("Execution Time (microseconds):", execution_time_microseconds)
