# main
from graph import Graph
from shortest_path import shortest_path
from minimum_spanning_tree import minimum_spanning_tree
from graph_isomorphism import graph_isomorphism
from utils import display_challenge, get_input

def main():
    while True:
        challenge = display_challenge()
        if not challenge:
            break
        user_input = get_input()
        if challenge["type"] == "shortest_path":
            result = shortest_path(challenge, user_input)
        elif challenge["type"] == "minimum_spanning_tree":
            result = minimum_spanning_tree(challenge, user_input)
        elif challenge["type"] == "graph_isomorphism":
            result = graph_isomorphism(challenge, user_input)
        print("Correct!" if result else "Incorrect!")

if __name__ == "__main__":
    main()

