#TC:O(n^2), as we are using nested loops to check for each pair of elements in the array and then checking if the third element that sums to zero exists in the set.
#SC:O(n^2), as we are using a set to store unique triplets and list to store the final result
def three_sum(arr,n):
    result=set()
    for i in range(n):
        s=set()
        for j in range(i+1,n):
            last=-(arr[i]+arr[j])
            if last in s:
                result.add(tuple(sorted([arr[i],arr[j],last])))    # use tuple when list is getting add to set and we use sort to avoid duplicate triplets in different order
            s.add(arr[j])
    final=[list(x) for x in result]                                #return in same datastructure as input
    return final
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The triplets that sum to zero are: ",three_sum(arr,n))
