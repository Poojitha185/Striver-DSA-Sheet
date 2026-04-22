#Time Complexity: O(N), where N is the size of the input array. We traverse the array twice: once to find potential candidates and once to validate them.

#Space Complexity: O(1), as we are using a constant amount of space for the counters and candidate elements, regardless of the input size.

#uses Boyer-Moore Voting Algorithm to find the majority element in an array.
def majority_element2(arr,n):
    cnt1,cnt2=0,0
    ele1,ele2=0,0
    for i in arr:
        if cnt1==0 and ele2!=i:
            ele1=i
            cnt1=1
        elif cnt2==0 and ele1!=i:
            ele2=i
            cnt2=1
        elif i==ele1:
            cnt1+=1
        elif i==ele2:
            cnt2+=1
        else:
            cnt1-=1
            cnt2-=1
    cnt1,cnt2=0,0
    for i in arr:
        if i==ele1:
            cnt1+=1
        elif i==ele2:
            cnt2+=1
    result=[]
    if cnt1>n//3:
        result.append(ele1)
    if cnt2 > n//3 and ele1 != ele2:
        result.append(ele2)
    return result
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element2(arr,n))
