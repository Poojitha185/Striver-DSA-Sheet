#Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
#Space Complexity: O(1), no extra space used.
#We will use a loop(say time) to check all possible answers from max(arr[]) to sum(arr[]).
#Next, inside the loop, we will send ‘time’, to the function countPainters() function to get the number of painters to whom we can allocate the boards.
#The first value of ‘time’, for which the number of painters will be lesser or equal to ‘k’, will be our answer. So, we will return that particular value of ‘time’.

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
def find_largest_min_distance(boards,k):
        low = max(boards)
        high = sum(boards)
        for i in range(low,high+1):
              if(count_painters(boards,i)<=k):
                    return i
        return low
arr=list(map(int,input("enter the array: ").split(',')))
k=int(input("enter the number of painters: "))
print("The minimum time required to paint all boards is:",find_largest_min_distance(arr,k))
                    