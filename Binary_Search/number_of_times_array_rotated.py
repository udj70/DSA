#task- Given- array, find number of times array rotated
#approach- find the index of element which is smallest in array i.e that should starting point of sorted array, 
# and it have moved till that point by rotation

def number_of_rotation(arr):
    start=0
    end=len(arr)-1
    N=len(arr)
    while(start<=end):
        mid=start+(end-start)//2
        next=(mid+1)%N #if mid at last then next will be first element
        prev=(mid-1+N)%N # if mid at start then prev will ne N-1 element
        if arr[mid]<=arr[next] and arr[mid]<arr[prev]:
            return mid
        if arr[mid]>=arr[start]:
            #start to mid is sorted , then search in unsorted part i.e mid+1, end
            start=mid
        else:
            #mid+1 to end is sorted, then search in start to mid-1
            end=mid
arr=[5,6,7,8,2,3,4]
print(number_of_rotation(arr))
