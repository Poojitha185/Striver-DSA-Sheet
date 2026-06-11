
    # Count painters required for a given max allowed time
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