from world2.world import *
from world2.stack_array import *

        
        
def test(did_pass):
    if(did_pass):
        print("The function works well")
    else:
        print("The function doesn't work")
            
def test_case():
    the_world=created_world('world1.dat')
    test(where_is_robot()==[7,0])
    test(is_feasible([1,0]))
    test(is_feasible([6,0]))
    test(is_feasible([0,-1])==False)
    test(is_feasible([-1,0])==False)
    test(is_feasible([-1,-1])==False)
    move_robot([6,0])
    move_robot([5,0])
    test(where_is_robot()==[5,0])
    test(goal_reached()==False)    
    move_robot([4,0])
    move_robot([3,0])
    move_robot([2,0])
    move_robot([1,0])
    move_robot([0,0])
    test(goal_reached()==False)
    move_robot([0,1])
    move_robot([0,2])
    move_robot([0,3])
    move_robot([0,4])
    test(where_is_robot()==[0,4])
    move_robot([0,5])
    move_robot([0,6])
    move_robot([0,7])
    test(goal_reached()==True)
    
test_case()
        
        