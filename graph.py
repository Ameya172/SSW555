# graph.py
import networkx as nx

class Graph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v):
        self.edges.append((u, v))

    def get_edges(self):
        return self.edges

    def get_shortest_path(self, start, end):
        G = nx.Graph()
        G.add_edges_from(self.edges)

        shortest = nx.shortest_path(G, start, end)
        return shortest

    def get_minimum_spanning_tree(self):
        G = nx.Graph()
        G.add_edges_from(self.edges)

        mst = nx.minimum_spanning_tree(G).edges()
        return mst

    def is_isomorphic(self, other_graph):
        G1 = nx.Graph()
        G1.add_edges_from(self.edges)
        G2 = nx.Graph()
        G2.add_edges_from(other_graph)

        isomorphism = nx.is_isomorphic(G1, G2)
        return isomorphism
