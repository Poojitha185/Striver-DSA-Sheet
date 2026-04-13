def majority_element(arr,n):
    ele=0
    cnt=0
    for num in arr:
            if cnt == 0:
                cnt = 1
                ele = num
            elif ele== num:
                cnt += 1
            else:
                cnt -= 1
    count1=arr.count(ele)
    if count1>n//2:
         return ele
    return -1
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element(arr,n))
        