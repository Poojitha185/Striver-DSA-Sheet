#Time Complexity: O(n²) Because for each element, we are checking every future element nested loops.

#Space Complexity: O(1) No extra space used, only variables for storing max profit.

def stock_buy_and_sell(arr,n):
    maxi=0
    profit=0
    for i in range(n):
        for j in range(i+1,n):
            profit=arr[j]-arr[i]
            maxi=max(profit,maxi)
    return maxi
arr=list(map(int,input("enter the array: ").split(',')))
n=len(arr)
print("The profit from stock:",stock_buy_and_sell(arr,n))
     
        
