#TC:O(N)
#SC:O(1)
#using XOR(^) operator XOR of two same numbers is always 0 i.e. a ^ a = 0.XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.
def finding_number_appears_once(arr):
    res=0
    for i in arr:        #tc:o(n)
        res=res^i   #^=XOR symbol
    return res
arr=list(map(int,input("enter the arary: ").split(',')))
print("The number that appears once in a array is: ",finding_number_appears_once(arr))