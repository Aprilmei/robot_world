
class Graph:
    
    def __init__(self):
        self.__my_adjacency_list = []
        self.__vertex_content = []

    def add_vertex(self, x):
        self.__my_adjacency_list.append([])
        self.__vertex_content.append(x)
        
    def add_edge(self, x, y):
        if y not in self.__my_adjacency_list[x]:
            self.__my_adjacency_list[x].append(y)
            self.__my_adjacency_list[y].append(x)
        
    def neighbours(self, x):
        return self.__my_adjacency_list[x]
    
    def remove_edge(self,x,y):
        self.__my_adjacency_list[x].remove(y)
        self.__my_adjacency_list[y].remove(x)
        
    
    def remove_vertex(self,x): 
        #pop deletes the element from the list by index 
        self.__vertex_content.pop(x)
        self.__my_adjacency_list.pop(x)
        #remove delete the element from the list by value 
        for i in range(0, len(self.__my_adjacency_list)):
            self.__my_adjacency_list[i].remove(x)
        
    def adjacent(self,x,y):
        return x in self.__my_adjacency_list[y]
    
    def length_g(self):
        return len(self.__vertex_content)
    
    def get_element(self,x):
        return self.__vertex_content[x]
    
    def print_str(self):
        for i in range(0, len(self.__my_adjacency_list)):
            print("node ", i, "(" , self.__vertex_content[i] , ") = ", self.__my_adjacency_list[i])


 
if __name__ == '__main__':
    g = Graph()
    g.add_vertex(3)
    g.add_vertex(100)
    g.add_vertex(50)
    g.add_vertex(10)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.print_str()
    
    print("neighbours of 1 = ", g.neighbours(1))
    print("Check if node 1 and 2 have a edge ",g.adjacent(1, 2))
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    g.add_edge(3, 2)
    print("after add one node in the graph")
    g.print_str()
    
    g.remove_edge(1, 2)
    
    print("after remove one edge in the graph")
    
    g.print_str()
else:
    pass

        



