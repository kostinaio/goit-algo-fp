

import heapq
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight

def dijkstra(graph, start):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph.edges}
    distances[start] = 0
    shortest_paths = {node: [] for node in graph.edges}
    shortest_paths[start] = [start]

    while heap:
        (current_distance, current_node) = heapq.heappop(heap)

        for neighbor in graph.edges[current_node]:
            weight = graph.weights[(current_node, neighbor)]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                shortest_paths[neighbor] = shortest_paths[current_node] + [neighbor]

    return distances, shortest_paths

def visualize_graph(graph, shortest_paths, start_node):
    G = nx.Graph()
    
    for node in graph.edges:
        G.add_node(node)
        
    for (from_node, to_node), weight in graph.weights.items():
        G.add_edge(from_node, to_node, weight=weight)
    
    pos = nx.spring_layout(G)
    edge_labels = {(from_node, to_node): weight for (from_node, to_node), weight in graph.weights.items()}
    
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='black', linewidths=1, font_size=15)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    path_edges = []
    for node, path in shortest_paths.items():
        if len(path) > 1:
            path_edges.extend([(path[i], path[i + 1]) for i in range(len(path) - 1)])
    
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='blue', width=2)
    
    plt.title(f"Візуалізація графа з найкоротшими шляхами від {start_node}")
    plt.show()

def main():
    graph = Graph()
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 10)
    graph.add_edge('B', 'D', 3)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('D', 'E', 4)

    start_node = 'A'
    distances, shortest_paths = dijkstra(graph, start_node)

    print("Відстані від вузла", start_node, "до всіх інших вузлів:")
    for node, distance in distances.items():
        print(f"Відстань до {node}: {distance}")

    print("\nНайкоротші шляхи від вузла", start_node, "до всіх інших вузлів:")
    for node, path in shortest_paths.items():
        print(f"Шлях до {node}: {' -> '.join(path)}")

    visualize_graph(graph, shortest_paths, start_node)

if __name__ == '__main__':
    main()
