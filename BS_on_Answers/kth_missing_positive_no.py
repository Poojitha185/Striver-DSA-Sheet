#Time Complexity: O(N), where N = size of the given array.

#Space Complexity: O(1), no extra space used.

def kth_missing_number(arr, k):
    for i in arr:
        if i <= k:
            k = k + 1
        else:
            break
    return k
arr = list(map(int, input("Enter the array: ").split(',')))
k = int(input("Enter the value of k: "))
print("The kth missing positive number is:", kth_missing_number(arr, k))