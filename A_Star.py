import networkx as nx
import matplotlib.pyplot as plt

# Define the graph as an adjacency dictionary with node as key and (neighbor, cost) as value.
graph = {
    'A': [('F', 3), ('B', 6)],
    'B': [('A', 6), ('C', 3), ('D', 2)],
    'C': [('B', 3), ('D', 1), ('E', 5)],
    'D': [('B', 2), ('C', 1), ('E', 8)],
    'E': [('C', 5), ('D', 8), ('I', 5), ('J', 5)],
    'F': [('A', 3), ('G', 1), ('H', 7)],
    'G': [('F', 1), ('I', 3)],
    'H': [('F', 7), ('I', 2)],
    'I': [('E', 5), ('G', 3), ('H', 2), ('J', 3)],
    'J': [('E', 5), ('I', 3)]
}

# Heuristic values
heuristics = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes and edges to the graph
for node, neighbors in graph.items():
    G.add_node(node, heuristic=heuristics[node])
    for neighbor, cost in neighbors:
        G.add_edge(node, neighbor, weight=cost)

# Find the shortest path from A to J
shortest_path = nx.astar_path(G, source='A', target='J', heuristic=lambda u, v: G.nodes[v]['heuristic'])

# Calculate the cost of the shortest path
path_cost = sum(G[shortest_path[i]][shortest_path[i + 1]]['weight'] for i in range(len(shortest_path) - 1))

# Extract positions for the nodes with a slight adjustment
pos = nx.spring_layout(G, seed=42, k=0.15)

# Draw the graph with labels and edges
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Annotate edges on the shortest path
path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
edge_labels = {(u, v): f'{G[u][v]["weight"]}' for u, v in path_edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Annotate heuristic values on top of the nodes with a slight y-offset
node_labels = {node: f'{G.nodes[node]["heuristic"]}' for node in G.nodes()}
node_pos = {node: (x, y + 0.05) for node, (x, y) in pos.items()}  # Adjust the y-coordinate
nx.draw_networkx_labels(G, node_pos, labels=node_labels, font_color='green', verticalalignment='center')

node_cost = 0
for i, node in enumerate(shortest_path):
    if i == 0:
        node_cost = 0
    else:
        node_cost = node_cost + heuristics[node]

plt.title("A* Shortest Path Visualization")
plt.figtext(0.5, 0.01,
            f"Shortest Path from A to J: {' -> '.join(shortest_path)}\nTotal Cost of Shortest Path: {path_cost + node_cost}",
            fontsize=12, ha="center")
plt.show()