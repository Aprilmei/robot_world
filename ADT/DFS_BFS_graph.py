'''
Created on 4 Apr 2017

@author: April
'''
from ADT.graph import Graph
from ADT.stack_array import stack 


def dfs_non_rec(g,n):
    l=g.length_g()
    to_visit= stack(l) 
    to_visit.pushing(n)
    visited=[]
    while(not to_visit.is_empty()):
        #print("check the stack",to_visit.get_stack())
        one_element=to_visit.popping()
        visited.append(one_element)
        neighb=g.neighbours(one_element)
        for i in neighb:
            #push  all neighbours  of current (not  in  visited and not in to_visit) 
            if i not in visited and i not in to_visit.get_stack():
                to_visit.pushing(i)
                #print("Push",i)
        print("visited",one_element,"the element is ",g.get_element(one_element))    
            

def dfs_rec(g,n):
    #check if n is flaged, if it is then stop, if n is unflaged, continue and flaged it 
    one_element=n
    if "visited" in g.neighbours(one_element):
        return
    else:
        neighb=g.neighbours(one_element)
        neighb.append("visited")
        print("visited",one_element,"the element is ",g.get_element(one_element)) 
        for i in neighb:
            if (i!="visited"):
                dfs_rec(g, i)
            
    
            

if __name__ == '__main__':
    g = Graph()
    g.add_vertex(3)
    g.add_vertex(100)
    g.add_vertex(50)
    g.add_vertex(10)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(3, 0)
    g.add_edge(3, 1)
    g.add_edge(3, 2)
    g.print_str()
    dfs_non_rec(g, 1)
    print("the recursive way is ")
    dfs_rec(g, 1)
