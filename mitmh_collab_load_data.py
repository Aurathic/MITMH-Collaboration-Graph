import networkx as nx
from itertools import combinations 
import matplotlib.pyplot as plt

fh2 = open("katz_number_graph.txt",'rb')
g2 = nx.read_edgelist(fh2,delimiter=",")
fh2.close()
fig = plt.figure(num=None, figsize=(120, 80), dpi=100)
layout = nx.spring_layout(g2,k=0.5,iterations=100)
#layout = nx.spectral_layout(g2)

nx.draw_networkx_edges(g2, pos=layout, width=1, edge_color=(0.33, 0.33, 0.33))
nx.draw_networkx_nodes(g2, pos=layout, node_size=10)
nx.draw_networkx_labels(g2, pos=layout, font_size=8)

#plt.show()
fig.set_size_inches(18.5, 10.5)
fig.savefig('mit_author_collab_graph.svg')
# print(g2.edges())
# fig.savefig('plot.png')
