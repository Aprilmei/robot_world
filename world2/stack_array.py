'''
Created on 7 Mar 2017

@author: April
'''
#implement a stack with array 
from builtins import *


class stack():
    def __init__(self,size,my_array=[]):
        n=len(my_array)
        if(n>=1):
            self.__first = my_array[n-1]
            self.__bottom=my_array[0]
        else:
            self.__first=None
            self.__bottom=None
        self.__my_stack = my_array
        self.size=size
        self.length=n

    # def __init__(self, node):
    #     self.__first = node

    def get_top(self):
        return self.__first
    
    def pushing(self, node):
        if(self.size==self.length):
            print("The stack is full")
        else:
            self.__my_stack.append(node)
            self.__first = node
            self.length+=1
        return self
        
    def popping(self):
        if(self.length==0):
            print("Error: the stack is empty")
        else:
            del self.__my_stack[-1]
            self.length-=1
            if(self.length==0):
                self.__first = None
            else:
                self.__first = self.__my_stack[-1]
        return self
    
    def find_element(self,node):
        for i in range(self.length):
            if(self.__my_stack[i]==node):
            
                return True
        return False

    def get_stack(self):
        return list(self.__my_stack)
    

s=stack(6,[1,2,3,1,2,3])
s.popping()
print(s.get_stack())


'''   
s=stack(6)
s.pushing([1,2])
s.pushing(2)
s.pushing(3)

s.find_element([1,2])
s.find_element(2)
print(s.get_stack())
print("Find [1,2]",s.find_element([1,2]))
print("Find [1,1]",s.find_element([1,1]))
print("Find 2",s.find_element(2))

print(s.get_top())

s=stack(6,[1,2,3,1,2,3])
s.poping()
print(s.get_stack())

s.poping()

print(s.get_stack())
s.poping()
print(s.get_stack())
s.poping()
print(s.get_stack())
'''

