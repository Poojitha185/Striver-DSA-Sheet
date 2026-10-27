# Time Complexity: O(n log n + n)
# Space Complexity: O(n)

class data:                   
    def __init__(self,weight,value):
        self.weight=weight
        self.value=value

def max_value(weight,value,n,wt):
    totalval=0
    arr = [data(0, 0) for i in range(n)]
    for i in range(n):
        arr[i].weight=weight[i]
        arr[i].value=value[i]
    arr.sort(key=lambda x:x.value/x.weight,reverse=True)
    for i in range(n):
        if arr[i].weight <= wt:
            totalval+=arr[i].value
            wt-=arr[i].weight
        else:
            totalval+=float((arr[i].value/arr[i].weight)*wt)
            break
    return totalval

value=list(map(int,input("enter the value array: ").split(",")))
weight=list(map(int,input("enter the weight array: ").split(",")))
capacity=int(input("enter the capacity of knapsack: "))
wt=capacity
print(max_value(weight,value,len(weight),wt))