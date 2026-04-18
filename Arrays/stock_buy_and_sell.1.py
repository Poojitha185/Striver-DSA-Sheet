def stock_buy_and_sell(arr,n):
    mini=arr[0]
    maxi=0
    for i in arr:
        if mini>i:
            mini=i
        else:
            maxi=max(maxi,i-mini)
    return maxi
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The profit from stock:",stock_buy_and_sell(arr,n))