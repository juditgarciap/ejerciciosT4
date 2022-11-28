#arbol adjuntado en el pdf
#constructor
class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

#diferentes representaciones de un grafo

        self.m_list_of_edges = []

#añadir eje 
    def add_edge(self, node1, node2, weight=1):  
#añadir a los nodos
        self.m_list_of_edges.append((node1, node2, weight))
        if not self.m_directed:
         self.m_list_of_edges.append((node2, node1, weight))

    
#print el grafo
    def print_edge_list(self):
        num_of_edges = len(self.m_list_of_edges)
        for i in range(num_of_edges):
            print("edge ", i+1, ": ", self.m_list_of_edges[i])

graph = Graph(18, False)

graph.add_edge("king's Cross", '1', 5)
graph.add_edge("king's Cross", '10', 1)
graph.add_edge('10', '11', 2)
graph.add_edge('10', '2', 5)
graph.add_edge('10', '9', 9)
graph.add_edge('11', '2', 4)
graph.add_edge('11', '12', 20)
graph.add_edge("Victoria Train Station", '11', 1)
graph.add_edge("Victoria Train Station", '3', 12)
graph.add_edge('2', '1', 8)
graph.add_edge('2', '8', 11)
graph.add_edge('2', '9', 7)
graph.add_edge('2', '3', 4)
graph.add_edge('3', '1', 6)
graph.add_edge('3', '9', 3)
graph.add_edge('3', '12', 7)
graph.add_edge('1', '8', 7)
graph.add_edge('1', '7', 12)
graph.add_edge("St Pancras", '9', 6)
graph.add_edge("St Pancras", '4', 7)
graph.add_edge('9', '8', 8)
graph.add_edge('9', '7', 5)
graph.add_edge('9', '4', 4)
graph.add_edge('9', '7', 12)
graph.add_edge('9', '1', 4)
graph.add_edge("Central Station", '9', 2)
graph.add_edge("Central Station", '6', 5)
graph.add_edge("Waterloo", '8', 6)
graph.add_edge("Waterloo", '6', 2)
graph.add_edge('8', '7', 2)
graph.add_edge('8', '5', 10)
graph.add_edge('7', '6', 1)
graph.add_edge('6', '5', 3)
graph.add_edge("Liverpool Street Station", '5', 3)
graph.add_edge("Liverpool Street Station", '12', 2)
graph.add_edge('5', '4', 4)
graph.add_edge('4', '12', 5)

graph.print_edge_list()


from collections import defaultdict
from heapq import *


def dijkstra(edges, f, t):
    g = defaultdict(list)
    for l, r, c in edges:
        g[l].append((c, r))