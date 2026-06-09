#Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[])

#Space Complexity:  O(1) as we are not using any extra space to solve this problem.

#Next, inside the loop, we will send each ‘pages’, to the function countStudents() function to get the number of students to whom we can allocate the books.
#The first number of pages, ‘pages’, for which the number of students will be equal to ‘m’, will be our answer. So, we will return that particular ‘pages’.


def ispossible(arr,j,n,s):
    no_of_students=1
    pages=0
    for i in range(n):
        if(arr[i]>j):
            return False
        if (pages+arr[i]>j):
            no_of_students+=1
            pages=arr[i]                 #assign the new value of arr to pages when we start to assign pages for new students
        else:
            pages+=arr[i]
    if (no_of_students>s):
        return False
    return True
def allocation(arr,n,s):
    if s>n:
        return -1
    low,high=max(arr),sum(arr)                     #Minimum possible answer = max(arr) (largest book) Maximum possible answer = sum(arr) (one student gets all books)
    for j in range(low,high+1):
        if(ispossible(arr,j,n,s)==True):
            return j
    return low
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
s=int(input("enter the number of students: "))
print("The minimum number of pages is:",allocation(arr,n,s))