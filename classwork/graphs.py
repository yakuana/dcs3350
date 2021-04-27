import networkx as nx 
import matplotlib.pyplot as plt 
import random 

# Create an empty undirected graph (directed = nx.DiGrapgh())
G = nx.Graph() 

# Add nodes 
G.add_node(0)
G.add_nodes_from( [1, 2, 3] ) # can also use range(...)

# Add edges 
G.add_edge(0, 1)
G.add_edges_from( [ (1, 2), (2, 3), (3, 1) ] )

print("Number of nodes=", G.number_of_nodes())
print("Number of edges=", G.number_of_edges())

# Views (dynamic dictionaties)
print("G.nodes =", G.nodes)
print("G.edges =", G.edges)
print("G.degree =", G.degree)
print("G.adj =", G.adj)

# Add attributes to nodes  
for i in G.nodes: 
    G.nodes[i]['smoking'] = False 
    G.nodes[i]['weight'] =  random.choice(range(100, 200))

G.nodes[1]['smoking'] = True 
# print("G.nodes.data():", G.nodes.data())

for e in G.edges: 
    G.edges[e]['strength'] = round(random.random(), 2)
# print("G.edges.data():", G.edges.data())
# print("G.adj:", G.adj) # don't need to use this 

'''
# 3 ways of iterating over the neighbors of a node 
print("Using G.adj[2]:")
for nbr in G.adj[2]: 
    print(nbr)

print("Using G[2]:")
for nbr in G[2]: 
    print(nbr)

print("Using G.neighbors(2):")
for nbr in G.neighbors(2):  # best way for readibility 
    print(nbr)

'''

# Color nodes and visualize network 
plt.figure(1)

# Simple way to visualize w/ 1-line code: nx.draw_networkx(G)

# Complex way to visualize 
color_map = []
size_map = []

for i in G.nodes: 
    # arbitrary size change by 2x node size 
    size_map.append(G.nodes[i]['weight'] * 2)

    # red for smoker, green for non-smoker 
    if G.nodes[i]['smoking']:
        color_map.append('red')
    else: 
        color_map.append('green')

nx.draw_networkx( G, 
    node_color = color_map, 
    node_size = size_map, 
    pos = nx.spring_layout(G, iterations = 1000), 
    arrows = False, 
    with_labels = True 
)

# Shows the graph 
# plt.show()

# Erdos-Renyi random graph & degree distribution 
plt.figure(2)
G_Erdos = nx.erdos_renyi_graph(1000, 0.5)
degrees = [G_Erdos.degree[i] for i in G_Erdos.nodes] # list of degrees of all nodes 
plt.xlabel('k')
plt.ylabel('p_k')
plt.title('Degree Distribution (Erdos-Renyi) Probability 0.5')
plt.hist(degrees, bins = range(min(degrees), max(degrees)))

# Erdos-Renyi random graph & degree distribution 
plt.figure(3)
G_Erdos = nx.erdos_renyi_graph(1000, 0.1)
degrees = [G_Erdos.degree[i] for i in G_Erdos.nodes] # list of degrees of all nodes 
plt.xlabel('k')
plt.ylabel('p_k')
plt.title('Degree Distribution (Erdos-Renyi) Probability 0.1')
plt.hist(degrees, bins = range(min(degrees), max(degrees)))

# Barabasi-Albert preferential attachment graph & degree distribution  
plt.figure(4)
G_Barabasi = nx.barabasi_albert_graph(1000, 6)
degrees = [G_Barabasi.degree[i] for i in G_Barabasi.nodes]
plt.xlabel('k')
plt.ylabel('p_k')
plt.title('Degree Distribution (Barabasi-Albert) Probability 6')
plt.hist(degrees, bins = range(min(degrees), max(degrees)))

# Barabasi-Albert preferential attachment graph & degree distribution  
plt.figure(5)
G_Barabasi = nx.barabasi_albert_graph(1000, 3)
degrees = [G_Barabasi.degree[i] for i in G_Barabasi.nodes]
plt.xlabel('k')
plt.ylabel('p_k')
plt.title('Degree Distribution (Barabasi-Albert) Probability 3')
plt.hist(degrees, bins = range(min(degrees), max(degrees)))

# Shows the graph 
plt.show()
