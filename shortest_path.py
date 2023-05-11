# shortest_path.py
import networkx as nx

class ShortestPath:
    def compute(self, challenge, user_input):
        G = nx.Graph()
        G.add_edges_from(challenge["graph_data"])
        start = challenge["start"]
        end = challenge["end"]

        shortest = nx.shortest_path(G, start, end)
        return user_input == shortest
