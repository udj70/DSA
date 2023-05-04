# task- Given sorted array inwhich all element appears two except one.
# approach 1- O(n) way, perform XOR of all elements, result will be ans
# approach 2- Binary search because array is sorted

def find_number(array):
    start=0
    end=len(array)-2
    while(start<=end):

        # find middle
        mid=start + (end-start)//2 

        # decide inwhich half to move

        if mid % 2 ==0 : # even index, i.e if element at mid and mid+1 is same, so immproper element not came yet, it in right half, else left in half
            if array[mid]!=array[mid+1]:
                end=mid-1
            else:
                start=mid+1
        else:
            if array[mid]==array[mid+1]:
                end=mid-1
            else:
                start=mid+1
    return array[start]
arr=[1,1,2,3,3,4,4,8,8]
print(find_number(arr))


