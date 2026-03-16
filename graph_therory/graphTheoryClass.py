class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.adjacency_list = {}
    

    def add_vertex(self, vertex):
        self.vertices.append(vertex)
        self.adjacency_list[vertex] = []
    


    def add_edge(self, v1,v2,weight=None):
        if v1 not in self.vertices:
            self.vertices.append(v1)
            self.adjacency_list[v1] = []
        if v2 not in self.vertices:
            self.vertices.append(v2)
            self.adjacency_list[v2] = []
        self.adjacency_list[v1].append(v2)
        self.adjacency_list[v2].append(v1)
        self.edges.append((v1,v2,weight))



    def remove_vertex(self,vertex):
        if vertex not in self.vertices:
            raise TypeError(f'{vertex} is not in this graph')
            
        
        self.vertices.remove(vertex)
        del self.adjacency_list[vertex]
        for item in self.adjacency_list:
            if vertex in self.adjacency_list[item]:
                self.adjacency_list[item].remove(vertex)

    

    def remove_edge(self,v1,v2,weight):
        if v2 in self.adjacency_list[v1]:
            adjace
        if (v1,v2,weight) in self.edges:
            self.edges.remove((v1,v2,weight))
        elif (v2,v1,weight) in self.edges:
            self.edges.remove((v2,v1,weight))
