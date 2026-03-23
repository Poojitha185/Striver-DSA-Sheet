#Time Complexity: O(N), where N is the number of elements in the array. Each element is processed once.
#Space Complexity: O(N), for storing frequencies of unique elements in the unordered_map.
arr = list(map(int, input().split()))
mpp = {}
result = []
for i in arr:
    mpp[i] = mpp.get(i, 0) + 1

for key in mpp:
    result.append([key, mpp[key]])
print(result)