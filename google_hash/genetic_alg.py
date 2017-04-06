'''
Created on 6 Apr 2017

@author: April
'''
from google_hash.read_input import read_google
from random import randint
from time import time
from google_hash.solution_finding import *

from collections import OrderedDict
from operator import itemgetter
from time import time


#Read file data to data dictionary 
#data =read_google("input/google_example.in")

#data = read_google("input/trending_today.in")
#data = read_google("input/kittens.in")
#data = read_google("input/videos_worth_spreading.in")
data=read_google("input/me_at_the_zoo.in")

print("Hello")

def sol_list(data):
    sol_list=list()
    while(len(sol_list)<=50):
        #print("Find a solution",len(sol_list))
        solution=find_solution(data)
        #print(solution)
        if(fitness_check(solution, data) and solution not in sol_list):
            sol_list.append(solution)
    return sol_list

def find_solution(data):
    s=[ [random.randint(0,1) for _ in  range(data["number_of_videos"])] for _ in range(data["number_of_caches"])]
    #the number of cache server and video 
    end_p=data["number_of_caches"]
    video=data["number_of_videos"]
    #print(end_p,video)
    #check after remove an video from a cache server, if the solution works 
    while(not fitness_check(s, data)):
        for i in range(end_p):
            sum_size=0
            #check the sum_size of the video in the cache server 
            for j in range(video):
                sum_size+=s[i][j]*data["video_size_desc"][j]
            while(sum_size>data["cache_size"]):
                x=random.randint(0,video-1)
                while(s[i][x]==0):
                    x=random.randint(0,video-1)
                s[i][x]=0
                sum_size=0
                for j in range(video):
                    sum_size+=s[i][j]*data["video_size_desc"][j]
                
            #print(s)
            #print("the video size in the cache server is too big")       
        '''
        #This one is not good, because the solution is too small 
        i=random.randint(0,end_p-1)
        j=random.randint(0,video-1)
        #check if the random finding number is 1 
        while(s[i][j]==0):
            i=random.randint(0,end_p-1)
            j=random.randint(0,video-1)
        #print("the changed one is ",i,j)
        '''   
    #print("The random solution is ",s)
    solution=hill_climbing(s,data)
    print("The solution after hill climbing",solution)
    return s

def genetic_alg(first_gen):
    #get the 50 solutions 
    print("begin the test")
    #the first generation, get all the children 
    l=len(first_gen[0])
    swap_half=l//2
    
    #
    for i in range(50):
        for j in range(i+1,50):
            #copy and get two Children from parents 
            solution_1=deep_copy(first_gen[i])
            solution_2=deep_copy(first_gen[j])
            #Swap the first half of the two solution 
            solution_1[0:swap_half]=first_gen[j][0:swap_half]
            solution_2[0:swap_half]=first_gen[i][0:swap_half]
            #add the two Children to first_gen
            first_gen.append(solution_1)
            first_gen.append(solution_1)
    fitness_list=dict() 
    n=0     
    for i in first_gen:
        fitness_list[n]=fitness(i, data)
        n+=1
    print(fitness_list)
    L = (sorted(fitness_list.items(), key=itemgetter(1)))
    
    top_n=L[-50:]
    top_number=list()
    for n in range(50):
        top_number.append(top_n[n][0])    
    print(top_n)
    new_gen=list()
    for i in top_number:
        new_gen.append(first_gen[i])    
    solution=new_gen[0]
    print(solution)
    return new_gen 

t=time()
first_gen_list=sol_list(data)
t=time()-t
print("the first generation is",first_gen_list,"the time using for find 50 solutions is",t)
genetic_alg(first_gen_list)
t=time()-t
print("the time using for genetic algorithm is ",t)


if __name__ == '__main__':
    pass