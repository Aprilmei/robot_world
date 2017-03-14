# use readlines to read a line a time

import re
from _ast import arg
import matplotlib.pyplot as plt
import numpy as np
#from world.stack_class import *


#the_world=[0]

def where_is_robot():
    #print(the_world)
    l=len(the_world[0])
    robot_location=[]
    for i in range(l):
        for j in range(l):
            if(the_world[i][j]==8):
                robot_location=[i,j]
                # print("The location of the robot is ", n)
                break;
    return robot_location

def created_world(filename):
    buffer = open(filename).read()
    buffer_lines=buffer.splitlines()
    firstLine = buffer_lines[0]
    range_N=re.findall("[-\d]+", firstLine)
    range_N=[int(e) for e in range_N]
    if(range_N[0]==range_N[1]):
        N=range_N[0]
    #print(N,'x',N)
    global the_world
    the_world=[[0]*N for _ in range(N)]
    for line in buffer_lines[1:-2]:
        numbers_line=re.findall("[-\d]+", line)
        numbers_line= [int(e) for e in numbers_line]
        x=numbers_line[0]
        y=numbers_line[1]
        the_world[x][y]=1
        #print('w ',x,',',y)
    
    robot=buffer_lines[-2].split()
    robot_name=robot[0]
    robot_location=re.findall("[-\d]+", robot[1])
    robot_location= [int(e) for e in robot_location]
    #print(robot_location)
    x_r=robot_location[0]
    y_r=robot_location[1]
    the_world[x_r][y_r]=8
    
    goal_location=re.findall("[-\d]+", buffer_lines[-1])
    global goal_robot
    goal_robot= [int(e) for e in goal_location]
    the_world[goal_robot[0]][goal_robot[1]]=4
    #print("Goal is" goal_robot)
    return the_world

def is_feasible(step):
    x=step[0]
    y=step[1]
    l=len(the_world[0])
    if(x>=0 and x<l and y>=0 and y<l):
        if(the_world[x][y]==0 or the_world[x][y]==4):
            '''
            x1=where_is_robot()[0]
            y1=where_is_robot()[1]
            if(abs(x1-x)==1 and y1==y):
                return True
            elif(abs(y1-y)==1 and x1==x):
                return True
                '''
            return True
        else:
            return False
    else:
        return False

def move_robot(step):
    x=step[0]
    y=step[1]
    r=where_is_robot()
    the_world[r[0]][r[1]]=2
    the_world[x][y]=8
    return the_world
def get_goal():
    return goal_robot
def goal_reached():
    if(goal_robot==where_is_robot()):
        print("Goal is reached")
        return True
    else:
        print("Goal is not reached")
        return False    
 

  

# where_is_robot()





''' 
created_world('world1.dat')


print(is_feasible([6,0]))
if(is_feasible([6,0])):
    move_robot([6, 0])
    print("The location of the robot is", where_is_robot())  
else:
    print("The location of the robot is", where_is_robot())  
goal_reached()

print(is_feasible([4,0]))
'''


                 
    

        
    

        
    
        
        
