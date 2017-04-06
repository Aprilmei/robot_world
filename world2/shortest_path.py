from world2.world import *
from world2.stack_array import *
import matplotlib.pyplot as plt
import numpy as np


def find_path(world,robot,goal,current_path):
    if(robot==goal):
        current_path=current_path.pushing(robot)
        return [current_path]
    
    #print("The robot is",robot)  check where is robot 
    
    #Find all the next step for the robot 
    next_step1=[robot[0]+1,robot[1]]
    next_step2=[robot[0]-1,robot[1]]
    next_step3=[robot[0],robot[1]+1]
    next_step4=[robot[0],robot[1]-1]
    
    next_step=[next_step2,next_step3,next_step4,next_step1]
    if(current_path.get_top()!=None):
        next_step.remove(current_path.get_top())
     
    #check if the next step is feasible or if the next step is in the path the robot went before     
    next_stepl=[]
    for n in next_step:
        if(is_feasible(n) and not current_path.find_element(n)):
            next_stepl.append(n)
    
    
    '''
    print the next steps and check the stack 
    print("next steps without past path",next_stepl)
    print("next step ",next_step)
    print(current_path.get_stack()) 
   '''
    
    if(next_stepl!=[]):
        for n in next_step:
            if(current_path.find_element(n)):
                while(current_path.get_top()!=n):
                    current_path.popping()
        #if the robot could go next, and actually the robot could come from a step in the path before, 
        #we will remove all the steps and go to the step directly   
          
        for n in next_stepl:
            move_robot(n)
            return find_path(world,n,goal,current_path.pushing(robot))   
        #choose a step and move robot 
        
          
    else:
        next_step_back=current_path.get_top()
        move_robot(next_step_back)
        return find_path(world,next_step_back,goal,current_path.popping())
    #if there is no feasible step, robot will move back until there is feasible step 
    #all the past step are marked as 2 
                    
'''
    :
    else:
        find_path(world,n,goal,current_path.pushing(n)) 
        '''
        
                
my_world=created_world('world1.dat')

n=len(my_world[0])
max_stack=n*n
the_robot=where_is_robot()
the_goal=get_goal()
s_current_path=stack(max_stack)

path=find_path(my_world,the_robot,the_goal,s_current_path)
print(my_world)
print("The shortest path is ",path[0].get_stack())
print(my_world)
print_world()


#print(s_current_path.get_stack())
# where_is_robot()
