from ADT.linked_list import Node
from ADT.linked_list import LinkedList


class Leaf():
    
    def __init__(self):
        self.__node=Node()
        
    def add_child(self,n):
        e=Node(n)
        while(self.__node.get_next()!=None):
            self.__node=self.__node.get_next()
        self.__node.set_next(e)
        
    def remove_child(self):
        self.__node.set_next(None)
            
    
class Tree():
    
    def __init__(self):
        self.__list = LinkedList()
        self.__root = Leaf()
        
    def create_tree(self,n):
        e = Leaf(n)
        self.__list.add_head(e)
        self.__root=e
    
    def is_empty(self):
        return self.__root.get_element()==None
             
    
    def get_root(self):
        return self.__root
        
t=Tree()
r=Leaf(0)
t.create_tree(r)
n=Leaf(1)
r.add_child(n)
r.add_child(2)
Leaf(2).add_child(3)


 
    
    
'''
    
create_empty_tree(): creates an empty tree
create_tree(n): creates a one node tree whose root is Node n
add_child(tree): add a subtree to the current tree
is_empty(): determines whether a tree is empty
get_root(): retrieves the Node that forms the  root of a tree
remove_child(tree): “detaches” a subtree from
the current tree

'''
    