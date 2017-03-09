def quick_sort(x):
    if(len(x)>=1):
        S=[]
        G=[]
        pivot=x[0]
        E=[x[0]]
        x.pop(x[0])
    
        while(len(x)>=0):
            elt=x[0]
            x.pop(x[0])     
            if(elt>pivot):
                G+=elt
            elif(elt==pivot):
                E+=elt
            else:
                S+=elt
        quick_sort(S)    
        quick_sort(G)
        return S+E+G
    else:     
        return x


my_input=input("Please input a list of numbers:  ")
my_array=my_input.split()

my_array= [int(e) for e in my_array]
my_array2=[]

for e in my_array:
    my_array2.append(e)

print("Quick Sort")
quick_sort(my_array)
