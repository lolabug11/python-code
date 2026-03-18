from collections import deque
class Graph:
    def __init__(self,weighted = False, directed = False):
        self.vertices = []
        self.vertices_set = set()
        self.edges = []
        self.adjacency_list = {}
        self.weighted = weighted
        self.directed = directed
    


    def __str__(self):
        return_string = ''
        return_string += f'Vertices:\n{self.vertices}\nEdges:\n{self.edges}\nAdjacencys:\n'
        for item in self.adjacency_list:
            return_string += f'{item} -> '
            return_string += f'{self.adjacency_list[item]}\n'
        return return_string



    def add_vertex(self, vertex):
        if vertex not in self.vertices_set:
            self.vertices_set.add(vertex)
            self.vertices.append(vertex)
            self.adjacency_list[vertex] = []
        
    


    def add_edge(self, v1,v2,weight=None):
        if v1 not in self.vertices_set:
            self.vertices_set.add(v1)
            self.vertices.append(v1)
            self.adjacency_list[v1] = []
        if v2 not in self.vertices_set:
            self.vertices_set.add(v2)
            self.vertices.append(v2)
            self.adjacency_list[v2] = []
        if self.directed:
            self.adjacency_list[v1].append(v2)
        else:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
        self.edges.append((v1,v2,weight))



    def remove_vertex(self,vertex):
        self._validate_vertex(vertex)
        self.vertices.remove(vertex)
        del self.adjacency_list[vertex]
        for item in self.adjacency_list:
            if vertex in self.adjacency_list[item]:
                self.adjacency_list[item].remove(vertex)
        for edge in self.edges:
            if vertex in edge:
                self.edges.remove(edge)

    

    def remove_edge(self,v1,v2,weight=None):
        self._validate_vertex(v1)
        self._validate_vertex(v2)
        if self.directed:
            if v2 in self.adjacency_list[v1]:
                self.adjacency_list[v1].remove(v2)
            if (v1,v2,weight) in self.edges:
                self.edges.remove(v1,v2,weight)
        else:
            if v2 in self.adjacency_list[v1]:
                self.adjacency_list[v1].remove(v2)
            if v1 in self.adjacency_list[v2]:
                self.adjacency_list[v2].remove(v1)
            if (v1,v2,weight) in self.edges:
                self.edges.remove((v1,v2,weight))
            elif (v2,v1,weight) in self.edges:
                self.edges.remove((v2,v1,weight))
    


    def vertex_exists(self,vertex):
        return vertex in self.vertices



    def  edge_exists(self, v1,v2):
        for edge in self.edges:
            if v1 in edge and v2 in edge:
                return True
        return False
    


    def _validate_vertex(self,vertex):
        if vertex not in self.vertices:
            raise TypeError(f'{vertex} is not in {self}')
    


    def degree(self, vertex):
        self._validate_vertex(vertex)
        return len(self.adjacency_list[vertex])
    


    def degree_sequence(self):
        degree_sequence = []
        for vertex in self.adjacency_list:
            degree_sequence.append(len(self.adjacency_list[vertex]))
        degree_sequence.sort(reverse=True)
        return degree_sequence



    def average_degree(self):
        average = 0 
        sequence = self.degree_sequence()
        for x in sequence:
            average += x
        average /= len(sequence)
        return average
    


    def max_possible_edges(self):
        n = len(self.vertices)
        return n*(n-1)/2
    


    def edge_count(self):
        return len(self.edges)



    def vertex_count(self):
        return len(self.vertices)


    def is_complete(self):
        return self.edge_count() == self.max_possible_edges()
    


    def BFS(self, start):
        visited_set = set([start])
        visited_list = []
        to_visit = deque([start])
        while len(to_visit) > 0:
            node =  to_visit[0]
            to_visit.popleft()
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited_set:     
                    to_visit.append(neighbor)
                    visited_set.add(neighbor)
            visited_list.append(node)
        return visited_list

 
        


    def iterable_DFS(self,start):
        visited_set = set()
        visited_list = []
        stack = []
        stack.append(start)
        while len(stack) >0:
            node = stack[-1]
            stack.pop()
            
            if node not in visited_set:
                for neighbor in self.adjacency_list[node]:
                    if neighbor not in visited_set:
                        stack.append(neighbor)
                visited_set.add(node)
                visited_list.append(node)
        return visited_list



    @staticmethod
    def DFS_helper(graph,visited_set, start,visited_list):
        visited_set.add(start)
        visited_list.append(start)
        for neighbor in graph.adjacency_list[start]:
            if neighbor not in visited_set:
                Graph.DFS_helper(graph,visited_set,neighbor,visited_list)

    def DFS(self, start):
        visited_set = set()
        visited_list = []
        Graph.DFS_helper(self,visited_set,start,visited_list)
        return visited_set, visited_list
    


    def has_cycle(self):
        visited = []
        for x in self.vertices:
            if x not in visited:
                a = Graph.cycle_DFS(self,visited,x)
                if a :
                    return True
        
        return False

    @staticmethod
    def cycle_DFS(graph,visited,node,parent = None):
        visited.append(node)
        for neighbor in graph.adjacency_list[node]:
            if neighbor not in visited:
                if Graph.cycle_DFS(graph,visited,neighbor, node):
                    return True
            else:
                if neighbor != parent:
                    return True
        return False
    


    def is_bipartite(self):
        color = {}
        for vertex in self.vertices:
            if vertex not in color:
                color[vertex] = 0
                if Graph.traversal(self,color,vertex) == False:
                    return False
                
        return True

    


    @staticmethod
    def traversal(graph,color,vertex):
        for neighbor in graph.adjacency_list[vertex]:
            if neighbor not in color:
                print(f"checking: {vertex} -> {neighbor} | {color}")
                if color[vertex] == 0:
                    color[neighbor] = 1
                    if Graph.traversal(graph,color,neighbor) == False:
                        return False
                else:
                    color[neighbor] = 0
                    if Graph.traversal(graph,color,neighbor) == False:
                        return False
            else:
                print(f"revisit: {vertex} -> {neighbor} | vertex_color={color[vertex]}, neighbor_color={color[neighbor]} | colors={color}")
                if color[neighbor] == color[vertex]:
                    return False
        return True
            


    def is_connected(self):
        if len(self.vertices) != 0:
            return len(self.BFS(self.vertices[0])) == self.vertex_count()
        else:
            return True
    


    def get_neighbors(self,vertex):
        return self.adjacency_list[vertex]
    


    def density(self):
        return self.edge_count() / self.max_possible_edges()
    


    def is_tree(self):
        return self.is_connected() and self.edge_count() == self.vertex_count() -1
    



    def BFS_start_end(self, start,end):
        if start in self.vertices:
            visited_set = set()
            visited_list = []
            to_visit = deque([start])
            visited_set.add(start)
            while len(to_visit) > 0:
                    current = to_visit[0]
                    to_visit.popleft()
                    visited_list.append(current)
                    if end == current:
                        return True, visited_list
                    else:
                        for neighbor in self.adjacency_list[current]:
                            if neighbor not in visited_set:
                                to_visit.append(neighbor)
                                visited_set.add(neighbor)
                        
            return False
        else:
            raise TypeError(f'{start} is not a real vertex')  


    def path_exists(self,v1,v2):
        path_exists,_ = self.BFS_start_end(v1,v2)
        return path_exists



    def BFS_shortest_path(self,start,end):
        if start in self.vertices:
            visited_set = set()
            visited_list = []
            parent = {}
            to_visit = deque([start])
            visited_set.add(start)
            parent[start] = None
            while len(to_visit) > 0:
                current = to_visit[0]
                to_visit.popleft()
                visited_list.append(current)
                if end == current:
                    shortest_path=[end]
                    parent_vertex = parent[end]
                    
                    while parent_vertex != None:
                       shortest_path.append(parent_vertex)
                       parent_vertex = parent[parent_vertex]
                    
                    shortest_path = shortest_path[::-1]
                    return shortest_path 

                else:
                    for neighbor in self.adjacency_list[current]:
                        if neighbor not in visited_set:
                            parent[neighbor] = current
                            to_visit.append(neighbor)
                            visited_set.add(neighbor)
                        
            return False
        else:
            raise TypeError(f'{start} is not a real vertex')  
    def shortest_path_unweighted(self,v1,v2):
        return self.BFS_shortest_path(v1,v2)