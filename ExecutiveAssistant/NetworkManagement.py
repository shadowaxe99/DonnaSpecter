```python
import networkx as nx

class NetworkManagement:
    def __init__(self):
        self.network = nx.Graph()

    def add_connection(self, node1, node2):
        self.network.add_edge(node1, node2)

    def remove_connection(self, node1, node2):
        self.network.remove_edge(node1, node2)

    def get_connections(self, node):
        return list(self.network.neighbors(node))

    def shortest_path(self, source, target):
        return nx.shortest_path(self.network, source, target)

    def visualize_network(self):
        nx.draw(self.network, with_labels=True)

# Example usage
if __name__ == "__main__":
    ea_network = NetworkManagement()
    ea_network.add_connection('EA1', 'EA2')
    ea_network.add_connection('EA2', 'EA3')
    print(ea_network.get_connections('EA2'))
    print(ea_network.shortest_path('EA1', 'EA3'))
    ea_network.visualize_network()
```