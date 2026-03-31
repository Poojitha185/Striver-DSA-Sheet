#TC:O(N logN) because of the sorting step, which dominates the overall time complexity. The set() function runs in O(N) time. The sorted() function also runs in O(N log N) time. However, since the number of unique elements can be at most equal to the number of elements in the original array, we can consider it as O(N log N) in the worst case.
#SC:O(N) because of the set() function, which creates a new set containing the unique elements from the original array. In the worst case, if all elements in the array are unique, the set will contain N elements, leading to O(N) space complexity. The sorted() function also creates a new list to store the sorted unique elements, which can also take O(N) space in the worst case. Therefore, the overall space complexity is O(N).
arr=arr=list(map(int,input("enter the arary: ").split(',')))
k=list(set(arr))
print("The  number of unique elements in the array: ",len(k))
print(sorted(k))
      
