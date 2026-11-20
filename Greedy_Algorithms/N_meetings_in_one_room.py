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



