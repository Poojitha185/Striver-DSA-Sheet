from itertools import permutations
def next_permutation(arr,n):
    perm=sorted(set(permutations(arr)))    #permutations(n) generates all possible permutations of the input array and give list of tupeles containing a permutation of the array and to delete duplicates we use set and pass set to sorted to sort the list of tuples and answer will return in list format 
    current=tuple(arr)                     #arr is converted to tuple to compare the tuples in p[ermuatations list]
    for i in range(len(perm)):
        if current==perm[i]:
            if i==len(perm)-1:
                return list(perm[0])        #return should always be in list format as we have to return the next permutation of the array in list format 
            else:
                return list(perm[i+1])
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The next permutation of the array is:",next_permutation(arr,n))