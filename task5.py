import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges_iterative(graph, root):
    if root is None:
        return graph, {}
    
    queue = [(root, 0, 0, 1)]
    pos = {root.id: (0, 0)}
    
    while queue:
        node, x, y, layer = queue.pop(0)
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            queue.append((node.left, l, y - 1, layer + 1))
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            queue.append((node.right, r, y - 1, layer + 1))
    
    return graph, pos

def draw_tree(tree_root, ax):
    tree = nx.DiGraph()
    tree, pos = add_edges_iterative(tree, tree_root)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    ax.clear()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, ax=ax)
    plt.draw()
    plt.pause(0.5)  # Затримка для візуалізації кроків

def build_heap_from_list(values):
    if not values:
        return None
    
    nodes = [Node(val) for val in values]
    for i in range(len(nodes) // 2):
        if 2 * i + 1 < len(nodes):
            nodes[i].left = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes):
            nodes[i].right = nodes[2 * i + 2]
    return nodes[0]

def generate_colors(n):
    colors = []
    for i in range(n):
        gray_value = int((i / (n - 1)) * 255) if n > 1 else 0
        colors.append('#{:02x}{:02x}{:02x}'.format(gray_value, gray_value, gray_value))
    return colors

def bfs_visualize(tree_root, ax):
    if tree_root is None:
        return

    queue = [tree_root]
    visited = set()
    colors = generate_colors(len(list_nodes(tree_root)))

    index = 0
    while queue:
        current = queue.pop(0)
        if current.id not in visited:
            visited.add(current.id)
            current.color = colors[index % len(colors)]
            index += 1

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            draw_tree(tree_root, ax)

def dfs_visualize(tree_root, ax):
    if tree_root is None:
        return

    stack = [tree_root]
    visited = set()
    colors = generate_colors(len(list_nodes(tree_root)))

    index = 0
    while stack:
        current = stack.pop()
        if current.id not in visited:
            visited.add(current.id)
            current.color = colors[index % len(colors)]
            index += 1

            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            draw_tree(tree_root, ax)

def list_nodes(tree_root):
    if tree_root is None:
        return []

    nodes = []
    queue = [tree_root]
    while queue:
        current = queue.pop(0)
        nodes.append(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return nodes

# Побудова бінарної купи з масиву
values = [15, 10, 9, 7, 8, 4, 2, 3, 1]
root = build_heap_from_list(values)

# Налаштування візуалізації
fig, ax = plt.subplots(figsize=(10, 7))

# Візуалізація обходу в ширину
print("Обхід в ширину:")
bfs_visualize(root, ax)

# Візуалізація обходу в глибину
root = build_heap_from_list(values)  # Перебудувати дерево, щоб скинути кольори
print("Обхід в глибину:")
dfs_visualize(root, ax)

plt.show()
