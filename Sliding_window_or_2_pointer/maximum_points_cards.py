#Time Complexity: O(K), because the first K cards require one summation and K replacements generate all remaining splits.
#Space Complexity: O(1), because only score variables and index variables require auxiliary storage.
#Store the array size in n and return -1 when k < 0 or k > n.Return 0 when k equals 0, and return the total array sum when k equals n.

#Calculate the sum of the first k cards and store the result in currentScore.
#Initialize maxScore with currentScore and rightIndex with n - 1.
#Traverse leftIndex from k - 1 down to 0. During each step, subtract cardPoints[leftIndex] because that card leaves the left selection, add cardPoints[rightIndex] because the next card from the right enters the selection, then decrement rightIndex. Update maxScore after every replacement, then return maxScore after generating all possible splits.

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