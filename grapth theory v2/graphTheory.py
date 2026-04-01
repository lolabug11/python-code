class GraphError(Exception):
    pass
class VertexNotFound(GraphError):
    def __init__(self, v):
        self.v = v
        super().__init__(f'{v} is not a real vertex')
class EdgeError(GraphError):
    def __init__(self, v1,v2):
        self.v1 = v1
        self.v2 = v2 
        super().__init__(f'There is somthing wrong with the edges {v1} and {v2}')




class Graph:
    def __init__(self, directional = False, weighted = False):
        self.adj_list = {}
        self.directional = directional
        self.weighted = weighted

    def __str__(self):
        return str(self.adj_list)
    
    def _validate_vertex(self,vertex):
        if vertex not in self.adj_list:
            raise VertexNotFound(vertex)
    
    def _validate_edge(self, v1 , v2):  
        if v2 not in self.adj_list[v1]:
            raise EdgeError(v1,v2)

    def add_vertex(self,vertex):
        if not self.vertex_exists(vertex):
            self.adj_list[vertex] = {}
    
    def add_edge(self, v1,v2, weight = None):
        if not self.vertex_exists(v1):
            self.add_vertex(v1)
        if not self.vertex_exists(v2):
            self.add_vertex(v2)
        v1_neighbors = self.get_neighbors(v1)
        v2_neighbors = self.get_neighbors(v2)
        if not self.weighted and not self.directional:
            if v2 not in v1_neighbors and v1 not in v2_neighbors:
                self.adj_list[v1][v2] = None
                self.adj_list[v2][v1] = None
            else:
                raise EdgeError(v1,v2)
        elif not self.directional and self.weighted:
            if v2 not in v1_neighbors and v1 not in v2_neighbors:
                self.adj_list[v1][v2] = weight
                self.adj_list[v2][v1] = weight
            else:
                raise EdgeError(v1,v2)
        elif self.directional and self.weighted:
            if v2 not in v1_neighbors:
                self.adj_list[v1][v2] = weight
            else:
                raise EdgeError(v1,v2)
        elif self.directional and not self.weighted:
            if v2 not in v1_neighbors:
                self.adj_list[v1][v2] = None
            else:
                raise EdgeError(v1,v2)

    def remove_edge(self,v1,v2):
        v1_neighbors = self.adj_list[v1]
        v2_neighbors = self.adj_list[v2]
        if self.directional:
            if self.edge_exists(v1,v2):
                del v1_neighbors[v2]
                self.adj_list[v1] = v1_neighbors

        else:
            if self.edge_exists(v1,v2):
                del v1_neighbors[v2]
                del v2_neighbors[v1]
                self.adj_list[v1] = v1_neighbors
                self.adj_list[v2] = v2_neighbors

    def vertex_count(self):
        return len(self.adj_list)

    def edge_count(self):
        total_edges = 0
        if self.directional:
            for vertex in self.adj_list:
                for edge in self.adj_list[vertex]:
                    total_edges += 1
            return total_edges
        else:
            visited_edges = set()
            for vertex in self.adj_list:
                for edge in self.adj_list[vertex]:
                    if (vertex, edge) not in visited_edges:
                        visited_edges.add((vertex,edge))
                        visited_edges.add((edge,vertex))
            for edge in visited_edges:
                total_edges += 1
            return total_edges

    def get_neighbors(self,vertex):
        if self.vertex_exists(vertex):
            return self.adj_list[vertex]
        else:
            raise VertexNotFound(vertex)
    
    def remove_vertex(self,vertex):
        del self.adj_list[vertex]
    
    def vertex_exists(self, vertex):
        return vertex in self.adj_list

    def edge_exists(self,v1,v2):      
        if v2 in self.adj_list[v1]:
            return True
        else:
            return False
    
    def degree(self,vertex):
        self._validate_vertex(vertex)
        return len(self.adj_list[vertex])

    def degree_sequence(self):
        sequence = []
        for x in self.adj_list:
            sequence.append(self.degree(x))
            print(sequence)
        sequence.sort(reverse=True)
        return sequence
    
    def average_degree(self):
        sequence = self.degree_sequence()
        total = 0
        for degree in sequence:
            total += degree
        return total/len(sequence)

    
    def _max_possible_edges(self,total_edges):
        if total_edges == 0:
            return 0
        else:
            return self._max_possible_edges((total_edges-1) + total_edges)
        

    def max_possible_edges(self):
        total_edges = len(self.adj_list)
        return self._max_possible_edges(total_edges)
        
g = Graph(weighted=True)
g.add_vertex('A')
g.get_neighbors('A')
g.add_vertex('B')
g.add_edge('A','B')
g.add_edge('A','A')
print(g.degree('A'))

print(g.degree_sequence())
print(g.average_degree())

# amount_of_nodes * 2 - 1
# 3 * 2 - 1