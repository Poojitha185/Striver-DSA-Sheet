#Time Complexity: O(K), because the first K cards require one summation and K replacements generate all remaining splits.
#Space Complexity: O(1), because only score variables and index variables require auxiliary storage.
def max_points(cards,k):
    lsum,rsum,maxsum=0,0,0
    for i in range(k):
        lsum+=cards[i]
    maxsum=lsum
    rindex=len(cards)-1
    for i in range(k-1,-1,-1):
        lsum-=cards[i]
        rsum+=cards[rindex]
        rindex-=1
        maxsum=max(maxsum,lsum+rsum)
    return maxsum
cards = list(map(int, input("Enter the array of 0s and 1s: ").split(",")))
k=int(input("enter the value of k(no of cards to be picked): "))
print("The maximum points that can be obtained by picking k cards from either end is: ",max_points(cards,k))