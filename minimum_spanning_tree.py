# minimum_spanning_tree.py
import networkx as nx

def minimum_spanning_tree(challenge, user_input):
    G = nx.Graph()
    G.add_edges_from(challenge["graph_data"])

    mst = nx.minimum_spanning_tree(G).edges()
    return sorted(user_input) == sorted(mst)

