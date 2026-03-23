#Time Complexity: O(N*N), where N = size of the array. We are using the nested loop to find the frequency.
#Space Complexity: O(N), where N = size of the array. It is for the visited array we are using.
arr = list(map(int, input("enter array: ").split()))
s = set(arr)
maxfreq=0
for i in s:
    count = 0
    for j in arr:
          if i == j:
            count += 1
    if count>maxfreq:
            maxfreq=count
            ans=i
print("the element",ans,"repeated",maxfreq,"times")