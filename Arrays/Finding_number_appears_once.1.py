def finding_number_appears_once(arr):
    freq={}
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for j in freq:
        if freq[j]==1:
         return j
arr=arr=list(map(int,input("enter the arary: ").split(',')))
print("The number that appears once in a array is: ",finding_number_appears_once(arr))