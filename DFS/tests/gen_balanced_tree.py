import random
from collections import defaultdict, deque


def generate(
    total_nodes: int = 25,
    max_children: int = 3,
    seed: int = None,
) -> dict:

    if seed is not None:
        random.seed(seed)

    if total_nodes <= 0:
        return {}

    graph = defaultdict(list)

    # root
    graph[0] = []

    queue = deque([0])
    nodes = [i for i in range(1, total_nodes)]
    random.shuffle(nodes)

    next_idx = 0

    while next_idx < (total_nodes - 1):
        parent = queue.popleft()

        for _ in range(max_children):
            if next_idx >= total_nodes:
                break

            child = nodes[next_idx]

            graph[parent].append(child)
            graph[child] = []

            queue.append(child)

            next_idx += 1

    return graph


__import__("pprint").pprint(generate())
