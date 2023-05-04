# max-heap- it is tree based data structure in which parent is always largere then its child,
#  child can be present anywhere below, not in order of BST 

# refer anuj bhaiya explanation
# task- implement heap using array 
# approach- parent- i//2, left_child=2*i, right_child=2*i+1


#something wrong with this code due to 1 based and zero based indexing, check again
def heap_push(arr,n):
    arr.append(n)
    i=len(arr)-1
    #print(arr)
    while(i>=1):
        parent=i//2
        #print(parent)
        if arr[parent]<arr[i]:
            #swap data
            arr[parent],arr[i]= arr[i],arr[parent]
            i=parent
        else:
            return 
def heap_pop(arr):
    mx=arr[0]
    #pop last element bring in front now
    arr[0]=arr.pop()
    n=len(arr)
    i=1
    while(i<n):
        #zero based indexing
        left_chld=arr[2*i+1-1]
        right_chiild=arr[2*i-1]

        #check which child is larger, then compare it wil arr[i], if arr[i] is less, then swap with larger
        larger= 2*i-1 if left_chld>right_chiild else 2*i+1-1
        if arr[i]<arr[larger]:
            arr[i],arr[larger]=arr[larger],arr[i]
            i=larger
        else:
            return 
def get_max(arr):
    return arr[0]
def heapify(arr):
    # not sure about correct solution as of now
    heap=[]
    for a in arr:
        heap_push(heap,a)
    return heap    

arr=[1,2,3,4,5]

heap=heapify(arr)
print(heap)
print(get_max(heap))
heap_push(heap,10)
print(heap)
print(get_max(heap))
heap_pop(heap)
print(heap)
print(get_max(heap))