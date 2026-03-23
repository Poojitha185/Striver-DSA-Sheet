#Time Complexity: O(N), where N = size of the array. The insertion and retrieval operation in the map takes O(1) time.
#sSpace Complexity: O(N), where N = size of the array. It is for the map we are using.
arr = list(map(int, input().split()))
mpp = {}
for i in arr:
    mpp[i] = mpp.get(i, 0) + 1
maxfreq = 0
for key in mpp:
    if mpp[key] > maxfreq:
        maxfreq = mpp[key]
        ans = key
print("the element",ans,"repeated",maxfreq,"times")