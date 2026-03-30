#TC:o(N logN),arr == sorted(arr) Compares element by element → O(N) and sorted(arr) sorts the array → O(N log N) time complexity. Overall, the time complexity is O(N log N) due to the sorting step.
#SC:O(N), sorted(arr) creates a new sorted list, which takes O(N) space. The original array arr is not modified, so it does not contribute to additional space complexity.
#using built-in function
def check_arr_sorted(arr,n):
    if arr==sorted(arr):        #sorted(arr) returns a new sorted list and arr.sort() returns None
        return True
    else:
        return False
arr=list(map(int,input("enter the arary: ").split(',')))
n=len(arr)
print(check_arr_sorted(arr,n))    

    