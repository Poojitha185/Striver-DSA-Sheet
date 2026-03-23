#Time Complexity: O(N²), as for every element we may scan the remaining elements in the array.

#Space Complexity: O(N), for the visited array of size N.

arr = list(map(int, input("enter array: ").split()))
s = set(arr)
result = []
for i in s:
    count = 0
    for j in arr:
        if i == j:
            count += 1
    result.append([i, count])
print(result)