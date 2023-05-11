# main
from graph import Graph
from shortest_path import ShortestPath
from minimum_spanning_tree import MinimumSpanningTree
from graph_isomorphism import GraphIsomorphism
from utils import Utils

def main():
    shortest_path_solver = ShortestPath()
    minimum_spanning_tree_solver = MinimumSpanningTree()
    graph_isomorphism_solver = GraphIsomorphism()
    
    while True:
        challenge = Utils.display_challenge()
        if not challenge:
            break

        graph_data = challenge["graph_data"]
        user_input = Utils.get_input()

        graph = Graph()
        for edge in graph_data:
            graph.add_edge(*edge)

        if challenge["type"] == "shortest_path":
            start = challenge["start"]
            end = challenge["end"]
            expected_path = graph.get_shortest_path(start, end)
            result = user_input == expected_path
        elif challenge["type"] == "minimum_spanning_tree":
            expected_mst = graph.get_minimum_spanning_tree()
            result = sorted(user_input) == sorted(expected_mst)
        elif challenge["type"] == "graph_isomorphism":
            other_graph_data = challenge["other_graph"]
            result = graph.is_isomorphic(other_graph_data) and sorted(user_input) == sorted(other_graph_data)

        print("Correct!" if result else "Incorrect!")

if __name__ == "__main__":
    main()
