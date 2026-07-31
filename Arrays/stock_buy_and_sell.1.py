#Time Complexity: O(n),This is because we are iterating through the array of prices exactly once. There are no nested loops or recursive calls.

#Space Complexity: O(1),Only two variables are used to store the minimum price and maximum profit, regardless of the input size.

def stock_buy_and_sell(arr,n):
    mini=arr[0]
    profit=0
    for i in arr:
        if mini>i:
            mini=i
        else:
            profit=max(profit,i-mini)
    return profit
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The profit from stock:",stock_buy_and_sell(arr,n))