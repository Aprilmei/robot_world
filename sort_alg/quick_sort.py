
def quick_sort(x):
    S=[]
    G=[]
    E=[]
    if(len(x)<=1):
        #print("the element is ",x)     
        return x    
    else:
        pivot=x[0]   
        for elt in x:
            #print("the list is ",x)     
            if(elt>pivot):
                G.append(elt)
            elif(elt==pivot):
                E.append(elt)
            else:
                S.append(elt)
        #print("S",S,"G",G,"E",E) 
        #print("S+G+E",S+E+G)      
        return quick_sort(S)+E+quick_sort(G)

def merge(L1,L2):
    print("the list before is ",L1,L2)
    L=[]
    while(L1!=[] and L2!=[]):
        #check if a list is empty 
        if(L1[0]<=L2[0]):
            L.append(L1.pop(0))
        else:
            L.append(L2.pop(0))
    while(L1!=[]):
        L.append(L1.pop(0))
    while(L2!=[]):
        L.append(L2.pop(0))
    print("the changed list is ",L1,L2)
    print("the merge list is ",L)
    return L    
        
def merge_sort(A):
    l=len(A)
    A1=[]
    A2=[]
    print("the list A is ", A)
    if(l>1):
        for j in range(l//2):    
            A1.append(A[j])
        for j in range(l//2,l):
            A2.append(A[j])
        #print("A1 is ", A1,"A2 is ",A2)    
        #The return is very important 
        return merge(merge_sort(A1),merge_sort(A2))
    else:
        return A
            
    
my_input=input("Please input a list of numbers:  ")
my_array=my_input.split()

my_array= [int(e) for e in my_array]
my_array2=[]

for e in my_array:
    my_array2.append(e)

print("Quick Sort")
print(quick_sort(my_array))

print("Merge Sort")
print("The sorted list is ",merge_sort(my_array2))
