n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
# this is the first time I know that we can enter an array like this in python.lol. idk why I never thought of it. glad that I learned it though.
if len(a)!= len(b):
    print -1
    # here we're just checking if arrays have the same length
else:
    count = 0 # we initialize count as zero this is our main counter of operations 
    n = len(a)
    least = min(a) # we sat this varaible to make sure that there is no element that is less than the least current element and so we can have a minimum value to copare other values to 
    for i in range(n):
        while a[i]>least:
            a[i]=a[i]-b[i]  # we perform the operations only if the element we had in hand was bigger than the leat element
            count +=1 # each time we perform an operation we increase the count
        if a[i]<least: # here we redefine least variable because we want it to always be the smallest element
            least = a[i]
            i = -1 # each time least is redefined we rest the for loop to the beginning so we can compare to the least possible 
        if a[i]<0: # since data constarints are below zero we don't want to get there 
            break
    flag = True        

    for i in range(n-1): # here we check if all elements of the array are equal and if not we break and print -1 if yes we just print the number of operations that we did in the first for loop ! 
        if a[i] != a[i+1]:
            flag = False
            break
    if flag:
        print(count)
    else:
        print(-1)            
