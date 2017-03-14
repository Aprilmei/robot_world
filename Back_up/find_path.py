from world2.world_test import *
from world2.stack_array import *




def find_path(world,robot,goal,current_path):
    if(robot==goal):
        return [current_path]
    print("The robot is",robot)
    next_step1=[robot[0]+1,robot[1]]
    next_step2=[robot[0]-1,robot[1]]
    next_step3=[robot[0],robot[1]+1]
    next_step4=[robot[0],robot[1]-1]
    next_step=[next_step1,next_step2,next_step3,next_step4]
    next_stepl=[]
    for n in range(4):
        if(is_feasible(next_step[n])):
            next_stepl.append(next_step[n])
    
    #current_path.pushing(next_step2)
    
    print("The stack is ",current_path.get_stack())
    print("next steps",next_stepl)
    paths=[]
    
    for n in next_stepl:
        if(not current_path.find_element(n)):
            print("next step is ",n)
            move_robot(n)
            newpath=find_path(world,n,goal,current_path.pushing(n))
            paths.append(newpath)           
    return paths
                       
            
    
my_world=created_world('world1.dat')
n=len(my_world[0])
print(n)
max_stack=n*n
the_robot=where_is_robot()
the_goal=get_goal()

s_current_path=stack(max_stack)
s_current_path.pushing(the_robot)
print(s_current_path.find_element(the_robot))
find_path(my_world,the_robot,the_goal,s_current_path)
#print(s_current_path.get_stack())
# where_is_robot()
