#task- Given- sorted array of integers, find first and last occurence of an element
#apprach- first occurence- if element present at mid then dont stop searching, just serach in left array
#          last occurence- if elemnt present at mid, serach in right part also

#refer- aditya verma


global res
def Binary_search_first_occurence(start,end,element,arr):
    global res
    mid=start+(end-start)//2
    #base condition
    if start>end:
        return
    
    if arr[mid]==element:
        res=mid
        Binary_search_first_occurence(start,mid-1,element,arr)
    elif arr[mid]>element:
        Binary_search_first_occurence(start,mid-1,element,arr)
    else:
        Binary_search_first_occurence(mid+1,end,element,arr)

def Binary_search_last_occurence(start,end,element,arr):
    global res
    mid=start+(end-start)//2
    #base condition
    if start>end:
        return
    
    if arr[mid]==element:
        res=mid
        Binary_search_last_occurence(mid+1,end,element,arr)
    elif arr[mid]>element:
        Binary_search_last_occurence(start,mid-1,element,arr)
    else:
        Binary_search_last_occurence(mid+1,end,element,arr)

res=-1
arr=[1,2,3,4,10,10,10,3,5]
element=10
Binary_search_first_occurence(0,len(arr)-1,element,arr)
print("first occurence",res)
res=-1
Binary_search_last_occurence(0,len(arr)-1,element,arr)
print("last occurence",res)