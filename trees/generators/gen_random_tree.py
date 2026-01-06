import random
from collections import defaultdict


def generate(
    total_nodes: int = 25,
    max_children: int = 3,
    seed: int = None,
) -> dict:
    if seed is not None:
        random.seed(seed)

    graph = defaultdict(list)
    # defining our root
    graph[0] = []

    nodes = [i for i in range(1, total_nodes)]
    random.shuffle(nodes)

    for i in nodes:
        available_parents = [k for k in graph.keys() if len(graph[k]) < max_children]
        if not available_parents:
            raise ValueError("No available parents left. Increase max_per_row.")

        parent = random.choice(available_parents)

        graph[parent].append(i)
        graph[i] = []

    return graph

