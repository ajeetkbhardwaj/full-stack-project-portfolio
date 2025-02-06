#%%
import igraph as ig
import networkx as nx
import matplotlib.pyplot as plt
import os

import pandas as pd
import numpy as np
import math

from igraph import Graph
#%% Creating graph and visualizing with the igraph
node = [1, 2, 3, 4]
edge = [(1, 2),(2, 3), (3, 4), (1, 3)]
G = ig.Graph(edge, node, directed=False)
ig.plot(G, bbox=(200, 200), vertex_size=30, labels=["1", "2", "3", "4"])

#%% Creating graph and visualizing with the networkx
G = nx.Graph()
node = [1, 2, 3, 4]
edge = [(1, 2),(2, 3), (3, 4), (1, 3)]
G.add_nodes_from(node)
G.add_edges_from(edge)
for i in node:
    G._node[i]['initial'] = i
labels = nx.get_node_attributes(G, 'initial')
nx.draw(G, labels=labels, font_weight='bold')
# %% Creating an igraph Network from spatial dataset file
file1 = "./data/BF_Millet.csv"
data = pd.read_csv(file1, encoding='latin1')
file2 = "./data/weights_bk.csv"
weights = pd.read_csv(file2, encoding='latin1')
print(weights.head(5))
data = data.iloc[:, 1: 46]
print(data.head(5))
total_weights = weights.iloc[:, 1: 46]
print(total_weights)
correlation = np.corrcoef(data.transpose())
print(correlation)
correlation[correlation > 0] = 1
corr_weight = np.multiply(correlation, total_weights)
print(corr_weight)
# %%
market = Graph.Adjacency(corr_weight, mode="undirected")
edge = market.get_edgelist()
ig.plot(market)

#%%
self_loop = []
for i in range(0, 46):
    self = (i, i)
    self_loop.append(self)

remove_edge = []
for i in edge:
    for j in self_loop:
        if i == j:
            remove_edge.append(i)

market.delete_edges(remove_edge)
ig.plot(market)
# %% Creating a Social Network using NetworkX
data1 = pd.read_csv("./data/AIMS_data.csv")
data = pd.DataFrame(data1)
network = nx.Graph()
print(data.head(5))
print(data.columns)
#%%
for i in range(len(data["Name"])):
    network.add_node(data["Name"][i], 
                     Age = data["Age"][i], 
                     Country=data["Country"],
                     Field=data["Field"][i],
                     backgroud=data["Background"][i]
                     )
    for j in range(len(data["Name"])):
        network.add_edge(data["Name"][j], data["Friend 1"][j])
        network.add_edge(data["Name"][j], data["Friend 2"][j])
        network.add_edge(data["Name"][j], data["Friend 3"][j])
        network.add_edge(data["Name"][j], data["Friend 4"][j])
        network.add_edge(data["Name"][j], data["Friend 5"][j])
G = network

labels = nx.get_node_attributes(G, 'initial')
nx.draw(G, labels=labels, font_weight='bold')
# %%
Degree=network.degree() 
var = [500*k[1] for k in list(Degree)]
plt.figure(figsize=(20,20))
nx.draw(network, font_size=10, node_size = var, with_labels=True, node_color="red")
plt.show()
# %% Creating FrachoPhone country network and analyze tred flow
G = nx.Graph()
G.add_nodes_from([1, 23])
G.add_edges_from([(23,13),(13,11),(12,13),(13,18),(13,1),(12,3),(12,18),
                 (3,22),(3,18),(3,21),(3,20),(18,1),(18,14),(18,17),(18,21),
                 (21,17),(21,14),(17,14),(14,1),(14,6),(14,5),(6,5),(1,8),
                 (8,16),(8,7),(16,7),(16,2),(16,4),(16,19),(19,4),(4,2),
                 (7,10),(2,10),(10,15),(10,9)])

list = ['Niger'
,'Republic_of_Congo'
,'Senegal'
,'Gabon'
,'Benin'
,'Togo'
'Central_African_Republic'
,'Chad'
,'Rwanda'
,'Democratic_Republic_of_Congo'
,'Morocco'
,'Mauritania'
,'Algeria'
,'Burkina_Faso'
,'Burundi'
,'Cameroon'
,'Cote_dIvoire'
,'Mali'
,'Equatorial_Guinea'
,'The_Gambia'
,'Guinea'
,'Guinea_Bissau'
,'Tunisia']
for i in range(1, len(list)):
    G._node[i]['initial'] = list[i]
labels = nx.get_node_attributes(G, 'initial')
nx.draw(G, labels=labels, font_weight='bold')
# %%
