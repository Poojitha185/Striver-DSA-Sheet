#Time Complexity: O(n log n), where n is the number of elements in the array. This is due to the sorting step, which is the most time-consuming operation in this approach.
#Space Complexity: O(1), as we are using only a constant amount of extra space.
#This method disorts the given array so its not acceptable in some cases when input array is important
#It counts the longest consecutive sequence by comparing adjacent elements. It keeps track of the current count of consecutive numbers and updates the longest count whenever a break in the sequence is found.

def longest_consecutive_sequence(arr,n):
    if n==0:
        return 0
    arr.sort()
    cnt=1
    longest=1
    lastsmaller=arr[0]
    for i in range(n):
        if(arr[i]-1==lastsmaller):
            cnt=cnt+1
            lastsmaller=arr[i]
        elif(arr[i]-1!=lastsmaller):
            cnt=1
            lastsmaller=arr[i]
        longest=max(longest,cnt)
    return longest
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The longest consecutive sequence:",longest_consecutive_sequence(arr,n))