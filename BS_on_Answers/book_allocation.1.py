#Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.

#Space Complexity:  O(1) as we are not using any extra space to solve this problem.

#We perform Binary Search:
#We try a middle value of pages per student.
#We check how many students would be required if no student gets more than that value.
#If it takes more students than allowed, that value is too low, so we try a higher one.
#If it fits within the allowed number of students, we store it and try a smaller one to find an even better option.

def ispossible(arr,j,n,s):
    no_of_students=1
    pages=0
    for i in range(n):
        if(arr[i]>j):
            return False
        if (pages+arr[i]>j):
            no_of_students+=1
            pages=arr[i]     #assign the new value of arr to pages when we start to assign pages for new students
        else:
            pages+=arr[i]
    if (no_of_students>s):
        return False
    return True
def allocation(arr,n,s):
    if s>n:
        return -1
    low=max(arr)
    high=sum(arr)             #The minimum possible is the largest single book (because every student must get at least one complete book),The maximum possible is the sum of all pages (if one student reads all books).
    while(low<=high):
        mid=(low+high)//2         
        if(ispossible(arr,mid,n,s)==True):
            high=mid-1
        else:
            low=mid+1
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
s=int(input("enter the number of students: "))
print("The minimum number of pages is:",allocation(arr,n,s))