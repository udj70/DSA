#task- Given- Two sorted arrays, find median
# approach1 - Merge both the arrays, find median TC-O(n1+n2), SC- O(n1+n2)
#approach 2- while merging maintain count, if count became equal to (n1+n2+1)//2, break,and current element will be median
#               TC-O(n1+n2), SC-O(1)
#approach 3- USe binary search on small size array, make partition, take remaining element from array 2,
#              check all the element on left is smaller then all on right partition, if so i.e. current partition is correct and max element of left partition is median
#refer raj vikramaditya

def find_median(arr1,arr2):
    if len(arr1)>len(arr2):
        return find_median(arr2,arr1)
    n1=len(arr1)
    n2=len(arr2)
    start=0
    end=n1
    while(start<=end):
        #partition 1 array from mid
        cut1=start+(end-start)//2
        #take remaining elements from 2 array
        cut2=(n1+n2+1)//2 - cut1

        #if cut1 or cut2 is zero i.e no element choosen in left partiion, so left will be INT_MAX
        left1= float('-inf') if cut1==0 else arr1[cut1-1]
        left2=float('-inf') if cut2==0 else arr2[cut2-1]
         #if cut1 or cut2 is LEN(ARR) i.e no element choosen in right partiion, so right will be INT_MIN
        right1= float('inf') if cut1==n1 else arr1[cut1]
        right2= float('inf') if cut2==n2 else arr2[cut2]

        # if this scenario occurs i.e correct partition is done, max(l1,l2) will be median and return
        if left1<=right2 and left2<=right1:
            if (n1+n2)%2==0: # if number of element in even, then two medians will be there
                return (max(left1,left2)+min(right1,right2))/2
            else:
                return max(left1,left2)
        else:
            if left1>right2:
                end=cut1-1
            else:
                start=cut1+1
    return 0
arr1=[1,3,4,7,10,12]
arr2=[2,3,6,15]
print(find_median(arr1,arr2))