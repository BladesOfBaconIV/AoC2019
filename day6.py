import networkx as nx

G = nx.Graph()
with open('input.txt', 'r') as f:
    G.add_edges_from([tuple(line.strip().split(')')) for line in f])

# if no target provided returns a dict with distances to all nodes
part_1 = sum(nx.shortest_path_length(G, source="COM").values())
# returns number of edges from source to target, which is 2 more than number of nodes.
part_2 = nx.shortest_path_length(G, source="YOU", target="SAN") - 2

print(f'{part_1=}, {part_2=}')