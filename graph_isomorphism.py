# graph_isomorphism.py
import networkx as nx

class GraphIsomorphism:
    def compute(self, challenge, user_input):
        G1 = nx.Graph()
        G1.add_edges_from(challenge["graph_data"])
        G2 = nx.Graph()
        G2.add_edges_from(challenge["other_graph"])

        isomorphism = nx.is_isomorphic(G1, G2)
        return isomorphism and sorted(user_input) == sorted(challenge["other_graph"])
