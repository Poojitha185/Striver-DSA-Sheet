#TC:O(N) as we are iterating through the array once to move the non-zero elements to the temp array and then again iterating through the temp array to copy the non-zero elements back to the original array, and finally iterating through the remaining positions in the original array to fill them with zeros.
#SC:O(N), as we are using an additional array temp to store the non-zero elements
def move_zero_end(arr,n):
    temp=[]
    for i in range(n):
        if arr[i]!=0:
            temp.append(arr[i])
    for j in range(len(temp)):
        arr[j]=temp[j]
    for l in range(len(temp),n):
        arr[l]=0    #if arr[l].append(0) its wrong bcz it will be like 5.append(0) which is not possible here we are replacing the numbers with 0
    return arr
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print("array after moving zeros to end: ",move_zero_end(arr,n))