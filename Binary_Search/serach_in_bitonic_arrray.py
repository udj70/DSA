# task- Given- bitonic array i.e. have a peak element, left side is decreasing and right side is also decreasing
# approach- find peak element, then search in left subarray and right subaaray
def search_peak(arr):
    start=1
    end=len(arr)-2
    #if leangth of array is one then peak will be 0th element
    if len(arr)==1:
        return 0
    #if length is 2 then peak will be either first or last element
    if len(arr)==2:
        return 0 if arr[0]>arr[1] else 1

    while(start<=end):
        mid=start+(end-start)//2

        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        #if mid+1 is more that mid-1, check in right part coz mid+1 can be peak, not mid-1
        if arr[mid+1]>arr[mid-1]:
            start=mid+1
        #else check in left
        else:
            end=mid-1
        
def binary_search_increasing(start,end,arr,element):
    while(start<=end):
        mid=start+(end-start)//2
        if arr[mid]==element:
            return mid
        if arr[mid]<element:
            start=mid+1
        else:
            end=mid-1
    return -1
def binary_search_decreasing(start,end,arr,element):
    while(start<=end):
        mid=start+(end-start)//2
        if arr[mid]==element:
            return mid
        if arr[mid]<element:
            end=mid-1
        else:
            start=mid+1
    return -1
def search_in_bitonic(arr,element):
    peak=search_peak(arr)
    index1=binary_search_increasing(0,peak-1,arr,element)
    index2=binary_search_decreasing(peak,len(arr)-1,arr,element)

    print(index1 if index1>=0 else index2)

arr=[1,2,3,4,5,10,9,8,7]
element=1
search_in_bitonic(arr,element)