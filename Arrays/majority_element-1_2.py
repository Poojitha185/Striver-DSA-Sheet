#Time Complexity: O(N), where N is the size of the input array. This is because we are iterating through the array once to find the potential majority element and then again to verify it.

#Space Complexity: O(1), as we are using only a constant amount of extra space.

#Boyer-Moore Voting Algorithm to find the majority element in an array.
def majority_element(arr,n):
    ele=0
    cnt=0
    for num in arr:   # Boyer-Moore Voting Algorithm to find a potential majority element.tc:o(n)
            if cnt == 0:
                cnt = 1
                ele = num
            elif ele== num:
                cnt += 1
            else:
                cnt -= 1
    count1=arr.count(ele) #counting the occurrences of the potential majority element.tc:o(n)
    if count1>n//2:
         return ele
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element(arr,n))
        