import networkx as nx 
import matplotlib.pyplot as plt 
import random
import sys 

# graph constants 
THRESHOLD = 0.36 
BETA_VALUE = 0.05
NUM_NODES = 200
NUM_EDGES = 3           #BA 
EDGE_PROBABILITY = 0.2  #ER

# color constants 
NOT_INFECTED_NODE_COLOR = 0.1
RANDOM_INFECTED_NODE_COLOR = 0.9

def simulate_spread(graph):
    time_step = 0
    num_infected = 0
    total_degrees = 0 
    infected_nodes = []
    color_map = []

    # add attributes to nodes 
    for i in graph.nodes:
        graph.nodes[i]['infected'] = False
        color_map.append(NOT_INFECTED_NODE_COLOR)
        total_degrees += graph.degree[i]

    # calculate average degree 
    # print("nodes and their degrees", G_ER.degree)
    # print("number of nodes", NUM_NODES)
    # print("total number of degrees", total_degrees)
    # print("average degree", total_degrees / NUM_NODES)

    # initiate graph with one random infected node 
    random_index = random.randint(0, NUM_NODES - 1)
    graph.nodes[random_index]['infected'] = True
    color_map[random_index] = RANDOM_INFECTED_NODE_COLOR
    infected_nodes.append(random_index)
    # print("intitial infected node", random_index)

    while (num_infected / NUM_NODES) < THRESHOLD: 
        node_color = random.uniform(0.3, 0.8)
        new_cases = [] 
        
        for node in infected_nodes: 
            # loop through the infected node's neighbors 
            for nbr in graph.neighbors(node):
                do_infect_node = random.random()

                if (graph.nodes[nbr]['infected'] == True):
                    continue 

                # probabilistically infect the neighbor 
                if (do_infect_node < BETA_VALUE):
                    graph.nodes[nbr]['infected'] = True
                    color_map[nbr] = node_color
                    new_cases.append(nbr)
                    num_infected += 1
        
        time_step += 1
        infected_nodes.extend(new_cases)
        # print("number of new cases: ", len(new_cases), new_cases)
    
    print("RESULTS\n")
    print("average degree", total_degrees / NUM_NODES)
    print("time steps needed", time_step)
    print("number of infected nodes", len(infected_nodes))
    # print("infectded nodes list", infected_nodes)
    return color_map

def main(): 
    print("======================\n")

    # create barabasi albert graph 
    G_BA = nx.barabasi_albert_graph(NUM_NODES, NUM_EDGES)
    print("BA Graph created\n")
    print("Simulating disease spread...\n") 
    ba_color_map = simulate_spread(G_BA)

    # plot barabasi albert graph 
    # plt.figure(1)
    # nx.draw_networkx( G_BA, 
    #     node_color = ba_color_map, 
    #     pos = nx.spring_layout(G_BA, iterations = 1000), 
    #     arrows = False, 
    #     with_labels = True 
    # )

    print("\n======================\n")

    # create erdos renyi graph 
    G_ER = nx.erdos_renyi_graph(NUM_NODES, EDGE_PROBABILITY)
    print("ER Graph created\n")
    print("Simulating disease spread...\n") 
    er_color_map = simulate_spread(G_ER)

    print("\n======================")

    # plot erdos renyi graph 
    # plt.figure(2)
    # nx.draw_networkx( G_ER, 
    #     node_color = er_color_map, 
    #     pos = nx.spring_layout(G_ER, iterations = 1000), 
    #     arrows = False, 
    #     with_labels = True 
    # )

if __name__ == "__main__":
    main()