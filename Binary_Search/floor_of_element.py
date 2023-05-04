#task- Given- find floor of given element
#approach- maintain a global variable res and store all values which are smaller than element
#similar question- find ceil , find next alphabet of given element
global res
def floor_of_element(arr,element):
    global res
    start=0
    end=len(arr)-1

    while(start<=end):
        mid=start+(end-start)//2
        #if element present then it will be floor of itself
        if arr[mid]==element:
            res=mid
            return 
        #if mid element is less than element, then it can be floor of element, but we will check in right
        if arr[mid]<element:
            res=mid
            start=mid+1
        else:
            end=mid-1

res=-1
arr=[2,3,4,5,7,8,9]
element=6
floor_of_element(arr,element)
print(arr[res])