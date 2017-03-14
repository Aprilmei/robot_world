from world2.linked_list import *

#implement a stack with linked list


class stack():
    def __init__(self,size,my_l= LinkedList()):
        self.__my_stack = my_l
        self.__size=size
        self.__first = my_l.head()
        self.__length=my_l.get_size()
    # def __init__(self, node):
    #     self.__first = node

    def get_top(self):
        return self.__first
    
    def pushing(self, node):
        if(self.__size==self.__length):
            print("The stack is full")
        else:
            self.__my_stack.add_head(node)
            self.__first = node
        return self
        
    def poping(self):
        if(self.__my_stack==None):
            print("Error: the stack is empty")
        else:
            self.__my_stack.remove_head()
            if(self.__my_stack==None):
                self.__first = None
            else:
                self.__first = self.__my_stack.head()
        return self

    def get_stack(self):
        return self.__my_stack
'''  
s=stack(6)
s.pushing(Node(2))
s.pushing(Node(6))
s.pushing(Node(3))

print("Print the stack",s.get_stack())
print("print the top",s.get_top())
s.poping()
print("Print the top",s.get_top())
print("Print the stack",s.get_stack())
s.poping()
print("Print the top",s.get_top())
'''
