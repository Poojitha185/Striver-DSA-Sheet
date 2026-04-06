def number_once(arr):
    for i in arr:               #It also repeats  work(counting) for duplicates
        if arr.count(i)==1:
         return i
arr=arr=list(map(int,input("enter the arary: ").split(',')))
print("The number that appears once in a array is: ",number_once(arr))
