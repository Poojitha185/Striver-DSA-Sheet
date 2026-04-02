def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
def rotate_array_d(arr, n, d): 
    d=d%n                     # important to handle cases where d >= n
    reverse(arr, 0, d-1)      # first part
    reverse(arr, d, n-1)      # second part
    reverse(arr, 0, n-1)      # whole array
    return arr
arr = list(map(int, input("enter the array: ").split(',')))
n = len(arr)
d = int(input("enter no of places to rotate: "))
print("Before rotating arary: ", arr)
print("After rotating array: ", rotate_array_d(arr, n, d))