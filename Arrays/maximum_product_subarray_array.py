#Time Complexity: O(N^2), we check the product of all possible subarrays using two nested loops.
#Space Complexity: O(1), No extra space is used.

def max_product_subarray(arr,n):
    res=arr[0]                          # This method is appropriate for array containing negative values ,fif there are only  positive values in array ,then set to 1
    for i in range(n):
        product=1
        for j in range(i,n):
            product=product*arr[j]
        res=max(res,product)
    return res
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The maximum product subarray is:",max_product_subarray(arr,n))