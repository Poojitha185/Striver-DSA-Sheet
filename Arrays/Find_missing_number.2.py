#TC:O(N),
#SC:O(1), as we are not using any extra space to store the elements and modifying the original array in place.
#using optimal 
def missing_number(arr, n):
    total = n * (n + 1) // 2  #tc:o(1),formula takes o(1) time
    actual = sum(arr)         #tc:o(n) ,it internally runs a loop to calculate the sum of elements in the array
    return total - actual     #tc:o(1),formula takes o(1) time
arr = list(map(int, input("enter the first sorted arary: ").split(',')))
n = len(arr)
print("The missing number in the array is", missing_number(arr, n))