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