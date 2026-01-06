from collections import deque, defaultdict
import matplotlib.pyplot as plt


def compute_tree_layout(graph, root=0):
    """
    Returns: dict[node] = (x, y)
    """
    levels = defaultdict(list)
    depth = {root: 0}

    queue = deque([root])

    while queue:
        node = queue.popleft()
        d = depth[node]
        levels[d].append(node)

        for child in graph[node]:
            depth[child] = d + 1
            queue.append(child)

    pos = {}

    for d, nodes in levels.items():
        width = len(nodes)
        for i, node in enumerate(nodes):
            # spread nodes evenly across x-axis
            x = i - (width - 1) / 2
            y = -d
            pos[node] = (x, y)

    return pos


def draw_tree(graph, root=0):
    pos = compute_tree_layout(graph, root)

    plt.figure(figsize=(10, 6))

    # draw edges
    for parent, children in graph.items():
        for child in children:
            x1, y1 = pos[parent]
            x2, y2 = pos[child]
            plt.plot([x1, x2], [y1, y2], color='black')

    # draw nodes
    for node, (x, y) in pos.items():
        plt.scatter(x, y, s=800)
        plt.text(x, y, str(node), ha="center", va="center", color="white", fontsize=10)

    plt.axis("off")
    plt.title("Balanced Tree Visualization")
    plt.show()
