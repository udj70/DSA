#task- Given-array with postive and negative elements, find first negative in each subarray
#approach- best- use queue and add current element in it if negative

def first_negative_in_subarray_size_k(arr,k):
    i=0
    j=0
    queue=[]
    ans=[]
    while(j<len(arr) and j<k):
        if arr[j]<0:
            queue.append(arr[j])
        j+=1
    #first negative of any subarray will be at queue.front
    if queue:
        ans.append(queue[0])
    else:
        ans.append(0)
    while(j<len(arr)):
        if queue and queue[0]==arr[i]:
            queue.pop(0)
        if arr[j]<0:
            queue.append(arr[j])
        #if subarray have no negative element, i.e queue is empty , then add 0
        if not len(queue):
            ans.append(0)
        else:
            ans.append(queue[0])
        i+=1
        j+=1
    return ans
arr=[12, 13, 15 ,-1, -7, 8, -15, 30, 16, 28]
k=3
print(first_negative_in_subarray_size_k(arr,k))
    