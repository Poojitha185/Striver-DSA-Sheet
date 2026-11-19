#Time Complexity: O(n), where n is the number of customers, because each bill is processed once.
#Space Complexity: O(1), because only constant space is used.

#Keep two counters: one for $5 bills and one for $10 bills. A $20 bill does not need to be tracked because it is never useful for giving change.
#Traverse the bills in order because customers must be served exactly as they arrive.
#If the current bill is $5, increase the $5 counter because no change is needed.
#If the current bill is $10, give back one $5. This is required because the lemonade costs $5.
#If the current bill is $20, first try to give one $10 and one $5. This saves extra $5 bills for future customers. If that is not possible, try to give three $5 bills. If neither change option is possible, return false.
#If all customers are served successfully, return true.

def lemonade_change(arr):
    five,tens=0,0
    for i in range(len(arr)):
        if arr[i]==5:
            five+=1
        elif arr[i]==10:
            if (five):
                five-=1
                tens+=1
            else:
                return False
        else:
            if (five and tens):
                five-=1
                tens-=1
            elif(five>=3):
                five-=3
            else:
                return False
    return True
arr=list(map(int,input("Enter the list of bills paid by customers: ").split(",")))
print(lemonade_change(arr))