#find element in sorted but pivoted array

#approach 1
#TC=O(logn) + one extra traver sal to find pivot

'''
Algo-
    1. Traverse array and find the pivot 
    2. if key >= arr[0] then binarySearch(0,pivot,key,arr)
    3. else binarySearch(pivot+1,n,key,arr)

'''
#approach 2
#TC= O(logn)
#in single traversal
def findkey(arr,k):
    s=0
    e=len(arr)-1
    while(s<=e):
        mid=(s+e)//2
        if arr[mid]==k:
            return mid
        if arr[s]<=arr[mid]: #to check if array is sorted in between s and mid
            if k<=arr[mid] and k>=arr[s]:
                e=mid-1
            else:
                s=mid+1
        else:
            if k>=arr[mid] and k<=arr[e]: #else it will be sorted from mid to e
                s=mid+1
            else:
                e=mid-1
    return -1
arr=[7,8,9,10,1,2,3,4] #sorted array is rotated and we have to search for key index
print(findkey(arr,1))                                

