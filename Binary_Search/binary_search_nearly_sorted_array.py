#task- Given- nearly sorted array i.e. a[i] can be at a[i-1] or a[i+1]
#approach- despite of checking at mid, also check at mid-1 and mid+1

def search_in_nearly_sorted_array(arr,element):
    start=0
    end=len(arr)-1

    while(start<=end):
        mid=start+(end-start)//2

        if arr[mid]==element:
            return mid
        if mid-1>=start and arr[mid-1]==element:
            return mid-1
        if mid+1<=end and arr[mid+1]==element:
            return mid+1
        if arr[mid]>element:
            end=mid-2
        else:
            start=mid+2
arr=[2,3,4,6,5,7,8]
element=5
print(search_in_nearly_sorted_array(arr,element))