#task- Given- array, find count of given element
#approach- find first and last occurence of that element, subtract there indexs to get length


global first,second
def Binary_search_first_occurence(start,end,element,arr):
    global first
    mid=start+(end-start)//2
    #base condition
    if start>end:
        return
    
    if arr[mid]==element:
        first=mid
        Binary_search_first_occurence(start,mid-1,element,arr)
    elif arr[mid]>element:
        Binary_search_first_occurence(start,mid-1,element,arr)
    else:
        Binary_search_first_occurence(mid+1,end,element,arr)

def Binary_search_last_occurence(start,end,element,arr):
    global second
    mid=start+(end-start)//2
    #base condition
    if start>end:
        return
    
    if arr[mid]==element:
        second=mid
        Binary_search_last_occurence(mid+1,end,element,arr)
    elif arr[mid]>element:
        Binary_search_last_occurence(start,mid-1,element,arr)
    else:
        Binary_search_last_occurence(mid+1,end,element,arr)
first=-1
second=-1
arr=[1,2,3,4,10,10,10,3,5]
element=10
Binary_search_first_occurence(0,len(arr)-1,element,arr)
Binary_search_last_occurence(0,len(arr)-1,element,arr)

print("length",second-first+1)
