#Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
#Space Complexity: O(1) since no extra space is required.
#using binary search
#Eliminate the halves based on the number of painters returned by countPainters(): We will pass the potential value of time, represented by the variable 'mid', to the ‘countPainters()' function. This function will return the number of painters we need to paint all the boards
#If painters > k: On satisfying this condition, we can conclude that the number ‘mid’ is smaller than our answer. So, we will eliminate the left half and consider the right half(i.e. low = mid+1). Otherwise, the value mid is one of the possible answers. But we want the minimum value. So, we will eliminate the right half and consider the left half(i.e. high = mid-1).
#Count painters required for a given max allowed time
def count_painters(boards,time):
        painters = 1
        boards_painter = 0

        for board in boards:
            if boards_painter + board <= time:
                boards_painter += board
            else:
                painters += 1
                boards_painter = board

        return painters

    # Use binary search to find the minimum time
def find_largest_min_distance(boards,k):
        low = max(boards)
        high = sum(boards)
        result = high

        while low <= high:
            mid = (low + high) // 2
            painters =count_painters(boards, mid)

            if painters > k:
                low = mid + 1  # Too few painters, increase time
            else:
                result = mid   # Valid time, try reducing it
                high = mid - 1

        return result
arr=list(map(int,input("enter the array: ").split(',')))
k=int(input("enter the number of painters: "))
print("The minimum time required to paint all boards is:",find_largest_min_distance(arr,k))