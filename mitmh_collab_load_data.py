import networkx as nx
from itertools import combinations 
import matplotlib.pyplot as plt

fh = open("mitmh_collab_edges2.txt",'rb')
G = nx.read_edgelist(fh,delimiter=",", comments="👍")
fh.close()

fig = plt.figure(num=None, figsize=(120, 80), dpi=100)
layout = nx.spring_layout(G,k=0.2,iterations=100)
#layout = nx.spectral_layout(G)

# Assign every hunt_name to an integer, then use that to create color map for edges
hunt_names = [e[2]["hunt_name"] for e in G.edges(data=True)]
#hunt_names = nx.get_edge_attributes(G,"hunt_name").values()
hunt_names_set = list(dict.fromkeys(hunt_names)) # like making a set, but keeps initial order
#print(hunt_names_set)
hunt_int_map = dict(zip(hunt_names_set, range(len(hunt_names_set))))
edge_colors = list(map(hunt_int_map.get, hunt_names))

nx.draw_networkx_edges(G, pos=layout, width=1, edge_color=edge_colors)
nx.draw_networkx_nodes(G, pos=layout, node_size=5)
nx.draw_networkx_labels(G, pos=layout, font_size=5)

#plt.show()
fig.set_size_inches(60, 40)
fig.savefig('mit_author_collab_graph.svg')
# print(g2.edges())
# fig.savefig('plot.png')