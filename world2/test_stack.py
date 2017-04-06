import os 
import unittest
from world2.world import *
from world2.stack_array import *



class Test_stack(unittest.TestCase):
    
    
    def test_creat_stack(self):
        s=stack(6)
        self.assertEqual(s.size,6)
    
    def test_push(self):
        s=stack(6)
        s.pushing(2)
        self.assertEqual(s.length,1)
        self.assertEqual(s.get_top(),2)
        
    def test_pop(self):
        s=stack(6,[1,2,3,4])
        s.popping()
        s.popping()
        s.popping()
        s.popping()
        self.assertTrue(s.length==0)
        
    def test_find_element(self):
        s=stack(6,[1,2,3,4])
        self.assertTrue(s.find_element(3))
        
    def test_get_top(self):
        s=stack(6,[1,2,3,4])
        self.assertTrue(s.get_top()==4)
        
        
        
        
        
    
    
    