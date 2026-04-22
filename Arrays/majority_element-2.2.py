#TC:O(n), as we traverse the array once to build the dictionary and then again to find the majority elements.
#SC:O(n), as we are using a dictionary to store the count of each element in the array, which in the worst case can be equal to the size of the input array.
def majority_element(arr,n):
    dic={}
    result=[]
    for i in range(n):
        dic[arr[i]]=dic.get(arr[i],0)+1
    for i,j in dic.items():
        if j>n//3:
            result.append(i)
        if len(result)==2:
            break
    return result

arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The majority element is: ",majority_element(arr,n))