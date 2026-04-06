def finding_number_appears_once(arr):
    res=0
    for i in arr:
        res=res^i   #^=XOR symbol
    return res
arr=list(map(int,input("enter the arary: ").split(',')))
print("The number that appears once in a array is: ",finding_number_appears_once(arr))