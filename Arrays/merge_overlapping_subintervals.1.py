#Time Complexity: O(N*logN) + O(N), we sort the entire array and then merge them in a single pass.
#Space Complexity: O(N), additional space used to store the non-overlapping intervals.

def merge_overlapping_subintervals(arr,n):
     arr.sort()
     merged=[]
     for i in arr:
          if not merged or merged[-1][1]<i[0]:
               merged.append(i)
          else:
               merged[-1][1] = max( merged[-1][1], i[1])
     return merged
arr = input("enter the array: ")
arr = [list(map(int, x.strip('[]').split(','))) for x in arr.split('],')] 
n=len(arr)
print("array after merging overlapping subintervals: ",merge_overlapping_subintervals(arr,n))