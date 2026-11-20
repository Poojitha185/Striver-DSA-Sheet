#Time Complexity: O(n log n) because the meetings are sorted by their ending time.
#Space Complexity: O(n) because an extra list of meetings is used for sorting.

#Store every meeting as a pair of start time and end time. This is done so that each meeting can be sorted and processed as one unit.
#Sort all meetings by their end time. This is the main greedy step because the meeting that ends earlier keeps the room available for more future meetings.
#Keep a variable lastEndTime to remember when the last selected meeting ended. This helps check whether the next meeting can fit after it.
#Go through the sorted meetings one by one. If the current meeting starts strictly after lastEndTime, select it because it does not overlap with the previous selected meeting.
#Every time a meeting is selected, increase the answer and update lastEndTime to the current meeting’s end time. This prepares the room availability check for the next meetings.

class data:                   
    def __init__(self,start,end,pos):  
        self.start=start        
        self.end=end
        self.pos=pos     
def max_meetings(start,end,n):
    arr = [data(0, 0, 0) for i in range(n)]
    for i in range(n):
        arr[i].start=start[i]
        arr[i].end=end[i]
        arr[i].pos=i+1
    arr.sort(key=lambda x: x.end)
    cnt=1
    freetime=arr[0].end
    ans=[(arr[0].start,arr[0].end)]
    for i in range(1,n):
        if arr[i].start > freetime:
            cnt+=1
            freetime=arr[i].end
            ans.append((arr[i].start,arr[i].end))
    return ans
start=list(map(int,input("enter the start array: ").split(",")))
end=list(map(int,input("enter the end array: ").split(",")))
n=len(start)
print(max_meetings(start,end,n))



