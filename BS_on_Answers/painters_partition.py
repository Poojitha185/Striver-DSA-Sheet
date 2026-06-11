


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
                    