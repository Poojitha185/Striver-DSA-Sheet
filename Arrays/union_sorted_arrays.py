#Time Compleixty : O( (m+n)log(m+n) ) . Inserting an element in a set takes logN time, where N is no of elements in the set. At max set can store m+n elements {when there are no common elements and elements in arr,arr2 are distntict}. So Inserting m+n th element takes log(m+n) time. Upon approximation across inserting all elements in worst, it would take O((m+n)log(m+n) time.
#Using HashSet also takes the same time, On average insertion in unordered_set takes O(1) time but sorting the union vector takes O((m+n)log(m+n))  time. Because at max union vector can have m+n elements.
#Space Complexity : O(m+n) {If Space of Union ArrayList is considered} ,O(1) {If Space of union ArrayList is not considered}
def union_sorted_arrays(arr1,arr2):
    k=set(arr1)|set(arr2)
    return sorted(k)
arr1=list(map(int,input("enter the first sorted arary: ").split(',')))
arr2=list(map(int,input("enter the second sorted arary: ").split(',')))
print("union of two sorted arrays: ",union_sorted_arrays(arr1,arr2))