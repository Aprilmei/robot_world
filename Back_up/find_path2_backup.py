from world2.world_test import *
from world2.stack_array import *




def find_path(world,robot,goal,current_path):
    if(robot==goal):
        return [current_path]
    print("The robot is",robot)
    #next_step1=[robot[0]+1,robot[1]]
    next_step2=[robot[0]-1,robot[1]]
    next_step3=[robot[0],robot[1]+1]
    #next_step4=[robot[0],robot[1]-1]
    next_step=[next_step2,next_step3]
    for n in next_step:
        if(not is_feasible(n)):
            next_step.remove(n)
    
    #current_path.pushing(next_step2)
    
    print(current_path.get_stack())
    print("next steps",next_step)
    if (next_step==None):
        return 
    else:
        for n in next_step:
            if(not current_path.find_element(n)):
                move_robot(n)
                return find_path(world,n,goal,current_path.pushing(n))    
        
    
my_world=created_world('world1.dat')
n=len(my_world[0])
max_stack=n*n
the_robot=where_is_robot()
the_goal=get_goal()

s_current_path=stack(max_stack)
s_current_path.pushing(the_robot)
print(s_current_path.find_element(the_robot))
path=find_path(my_world,the_robot,the_goal,s_current_path)
print(path[0].get_stack())

#print(s_current_path.get_stack())
# where_is_robot()
