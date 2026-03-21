#This approach improves on the previous one by reversing the array in-place, avoiding the need for extra space. It uses two pointers to simultaneously traverse the array from both ends, swapping the elements until the center is reached. This way, we avoid creating a new array and perform the reverse operation efficiently using constant space.
#TC:O(N) Each element is visited at most once due to the two-pointer approach.
#SC: O(1) No extra space is used other than a few pointers and variables. The array is reversed in-place.
#instead of two pointers we can also use a single pointer and for another pointer calculate the index of the element to be swapped using the formula n-1-i and pass n-1-i
def reverse(l,k,m):       
    if l>=k:
        return m
    m[l],m[k]=m[k],m[l]      # instaed of using a temp variable to swap we can do it in one line
    return reverse(l+1,k-1,m)   
n=int(input("enter the number of elements: "))
print("enter array elements: ")
m=[]
for i in range(n):
      m.append(int(input()))
print(reverse(0,n-1,m))