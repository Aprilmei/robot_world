#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 13:35:21 2017

@author: April
"""

"""A class representing a student. 

"""

class Student(object):
    def __init__(self, n, a): 
        self.full_name = n 
        self.age = a 
        self.__modules = []
    def __get_modules__(self): 
        return self.modules
    def __repr__(self):
        return "I’m named " + self.full_name
    
class CsStudent(Student): 
    """A class extending Student. """
    def __init__(self, n, a, s):
# Call __init__ for student 
        Student.__init__(self, n, a) 
        self.section_num = s
f = Student("Bob Smith", 23)
f.full_name
print(f)




