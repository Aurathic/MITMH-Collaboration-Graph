import networkx as nx
G = nx.Graph()
G.add_nodes_from([1, 2, 3], color="red")
print(G.edges())
color = nx.get_node_attributes(G, "color")
print(color[1])
