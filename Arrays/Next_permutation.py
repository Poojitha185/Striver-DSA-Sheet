#Time Complexity: O(N!*N), since we are generating all possible permutations, it takes N! time.
#Space Complexity: O(N!), storing all permutations.

from itertools import permutations         #The itertools contain permutations function is a built-in function in Python that generates all possible permutations of a given iterable (like a list or string). It returns an iterator that produces tuples of the permutations. In this code, we use it to generate all permutations of the input array, which we then sort and compare to find the next permutation.
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