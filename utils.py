# utils.py
import random

challenges = [
    {"type": "shortest_path", "graph_data": [(1, 2), (2, 3), (3, 4)], "start": 1, "end": 4},
    {"type": "minimum_spanning_tree", "graph_data": [(1, 2), (2, 3), (3, 4), (4, 1)]},
    {"type": "graph_isomorphism", "graph_data": [(1, 2), (2, 3), (3, 4)], "other_graph": [(5, 6), (6, 7), (7, 8)]}
]

def display_challenge():
    if not challenges:
        return None
    return random.choice(challenges)

def get_input():
    try:
        user_input = eval(input("Enter your solution: "))
    except Exception as e:
        print("Invalid input format.")
        return None
    return user_input

