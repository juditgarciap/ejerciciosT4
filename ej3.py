#arbol adjuntado en el pdf
#constructor

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