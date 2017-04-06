#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:45:34 2017

@author: April
"""

#implement a stack with array 


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
        self.__size=size
        self.__length=n

    # def __init__(self, node):
    #     self.__first = node

    def get_top(self):
        return self.__first
    
    def pushing(self, node):
        if(self.__size==self.__length):
            print("The stack is full")
        else:
            self.__my_stack.append(node)
            self.__first = node
            self.__length+=1
        
    def poping(self):
        if(self.__my_stack==None):
            print("Error: the stack is empty")
        else:
            self.__my_stack.remove(self.__first)
            self.__length-=1
            if(self.__my_stack==None):
                self.__first = None
            else:
                self.__first = self.__my_stack[-1]
    
    def find_element(self,node):
        for i in range(self.__length):
            if(self.__my_stack[i]==node):
            
                return True
        return False

    def get_stack(self):
        return list(self.__my_stack)
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
'''
    
s=stack(6,[8,9,'s','h'])
s.poping()
s.pushing(1)
s.pushing(2)
s.pushing(3)

print(s.get_stack())
print(s.get_top())

print(s.get_top())
print(s.get_stack())
s.poping()
print(s.get_top())
n=[s]
print(n[0].get_stack())

