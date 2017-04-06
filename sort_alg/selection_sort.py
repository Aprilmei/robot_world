
def selection_sort(x):
    l=len(x);
    
    for i in range(l-1):
        for j in range(i+1,l):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
        print(x)
    return x
                
def bubble_sort(x):
    l=len(x);
    for n in range(l-1):
        swaped=False
        for i in range(l-1-n):
            j=i+1
            
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
                swaped=True
        print(x)
        if(swaped==False):
            break;           
        
    return x
  
def insertion_sort(x):
    l=len(x);
    for j in range(1,l):
        # j=1
        i=j
        while i>0 and x[i-1]>x[i]:
            #print("show the two number of",x[i-1],x[i])
            x[i],x[i-1]=x[i-1],x[i]
            i-=1   
        print(x)
    


my_input=input("Please input a list of numbers:  ")

my_array=my_input.split()

my_array= [int(e) for e in my_array]
my_array2=[]

for e in my_array:
    my_array2.append(e)

print("Insertion sort")
insertion_sort(my_array)    

print("Bubble sort")
bubble_sort(my_array2)
'''
print("Selection sort")
selection_sort(my_array)


'''

