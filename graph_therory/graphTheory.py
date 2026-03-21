class Graph:
    def __init__(self, directional = False, weighted = False):
        self.adj_list = {}
        self.directional = directional
        self.weighted = weighted
    def __str__(self):
        return str(self.adj_list)
    
    def validate_vertex(self,vertex):
        return vertex in self.adj_list

    
    def valudate_edge(self, v1 , v2):
        if not self.directional:
            pass
    def add_vertex(self,vertex):
        if not self.validate_vertex(vertex):
            self.adj_list[vertex] = {}
    
    def add_edge(self, v1,v2, weight = None):

        if not self.weighted and not self.directional:
            self.adj_list[v1][v2] = None
            self.adj_list[v2][v1] = None
        elif not self.directional and self.weighted:
            self.adj_list[v1][v2]= weight
            self.adj_list[v2][v1] = weight
        elif self.directional and self.weighted:
            self.adj_list[v1][v2] = weight
        elif self.directional and not self.weighted:
            self.adj_list[v1][v2] = None

    



g = Graph(weighted=True)
g.add_vertex('A')
g.add_vertex('B')
g.add_edge('A', 'B', 500)
print(g)
