def merge_overlapping_subintervald(arr,n):
    arr.sort()
    ans=[]
    i=0
    while i<n:
        start=arr[i][0]
        end=arr[i][1]
        j=i+1
        while j<n and arr[j][0]<=end:
            end=max(end, arr[j][1])
            j=j+1
        ans.append([start,end])
        i=j
    return ans
arr = input("enter the array: ")
arr = [list(map(int, x.strip('[]').split(','))) for x in arr.split('],')] 
n=len(arr)
print("array after merging overlapping subintervals: ",merge_overlapping_subintervald(arr,n))