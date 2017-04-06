#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 14:34:12 2017

@author: April
"""

class Guest :
    def __init__(self,n,p):
        self.full_name=n
        self.portions=p
    def eat(self):
        if self.portions==0:
            print("I am full")
        else:
            self.portions-=1;
            print("I want more")
            
a=Guest("Daniele",8)        
print(a.portions)
a.eat()
a.eat()
a.eat()
a.eat()
a.eat()
a.eat()
a.eat()
a.eat()
a.eat()
a.eat()

