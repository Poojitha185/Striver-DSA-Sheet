#Time Complexity: O(N), where N is the size of the input array. This is because we are iterating through the array once to count occurrences and then iterating through the dictionary to find the majority element.
#Space Complexity: O(N), as we are using a dictionaryto store the counts of each element, which can take up to N space in the worst case.
def find_majority_element(arr,n):
    dic={}
    for i in arr:     #tc:o(n)
        dic[i]=dic.get(i,0)+1       
    k=max(dic,key=dic.get)    #it runs loop so tc:o(n)
    v=dic[k]
    if v>n//2:
        return k,v
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
w,x=find_majority_element(arr,n)
print("The number",w,"appears",x,"times in",n,"sized array")