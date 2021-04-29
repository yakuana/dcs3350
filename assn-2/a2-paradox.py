import networkx as nx 
import matplotlib.pyplot as plt 
import random
import math
import sys 

# graph constants 
BETA_VALUE = 0.05
EDGE_PROBABILITY = 0.2  #ER
NUM_EDGES = 3           #BA 
NUM_NODES = 10000
P_FRACTION = 0.25 
P_NODES = math.floor(NUM_NODES * P_FRACTION)

def add_attributes(graph):
    for i in graph.nodes: 
        graph.nodes[i]['vaccinated'] = False

def selective_immunization(graph):    
    group_0 = []
    group_1 = [] 
    g0_degree_sum = 0
    g1_degree_sum = 0 

    # create group 0 
    while (len(group_0) != P_NODES): 
        random_index = random.randint(0, NUM_NODES - 1)

        # prevent duplicates 
        if (graph.nodes[random_index]['vaccinated'] == True):
            continue 
        
        graph.nodes[random_index]['vaccinated'] = True
        g0_degree_sum += graph.degree(random_index)
        group_0 += [random_index]

    # create group 1 
    for node in group_0:
        for nbr in graph.neighbors(node):
            add_node = random.random()

            if (add_node > P_FRACTION):
                g1_degree_sum += graph.degree(nbr)
                group_1.append(nbr) 

    return [
        {
            "group_0":  g0_degree_sum/len(group_0)
        },
        {
            "group_1": g1_degree_sum/len(group_1)
        }
    ] 

def random_immunization(graph):
    random_group = [] 
    rg_degree_sum = 0 

    while (len(random_group) != P_NODES): 
        random_index = random.randint(0, NUM_NODES - 1)

        # prevent duplicates 
        if (graph.nodes[random_index]['vaccinated'] == True):
            continue 
        
        graph.nodes[random_index]['vaccinated'] = True
        rg_degree_sum += graph.degree(random_index)
        random_group += [random_index]

    # retuen avg degree 
    return rg_degree_sum / P_NODES

def main():
    # create barabasi albert graph 
    G_BA = nx.barabasi_albert_graph(NUM_NODES, NUM_EDGES)
    add_attributes(G_BA)
    print("BA RESULTS\n")
    print("selective",selective_immunization(G_BA))
    print("random",random_immunization(G_BA))

    G_ER = nx.erdos_renyi_graph(NUM_NODES, BETA_VALUE)
    add_attributes(G_ER)
    print("\nER RESULTS\n")
    print("selective", selective_immunization(G_ER))
    print("random",random_immunization(G_ER))

if __name__ == "__main__":
    main()