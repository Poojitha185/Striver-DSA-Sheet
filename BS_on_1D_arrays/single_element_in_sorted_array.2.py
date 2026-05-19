#Time Complexity: O(N), N = size of the given array.We are traversing the entire array.

#Space Complexity: O(1) as we are not using any extra space.

#using XOR operation, we can find the single element in the array. The XOR of a number with itself is 0, and the XOR of a number with 0 is the number itself. So, if we XOR all the elements in the array, the duplicate elements will cancel out each other and we will be left with the single element.

def single_element(arr,n):
    ans=0
    for i in range(n):
        ans^=arr[i]
    return ans
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The single element in the array is:",single_element(arr,n))