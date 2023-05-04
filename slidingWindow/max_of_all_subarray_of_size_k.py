
#task- given array , find maximum in all subarrays of size k, and store in array
#approach 1- use two loops, TC-O(n2)
#appriach 2- TC-O(N), SC-O(N), use queue and get maximum of current subarray from i to j at queue.front, 
#           if next element in greateer then remove all small elements from queue right(collections.deque)
#           conclusion- at every state of dequeu, fron will have max of window, and following elements will be smaller then from in decreasing order
from collections import deque

def max_of_all_subarray_of_size_k(arr,k):
    queue=deque()
    i=0
    j=0
  
    ans=[]
    #first take j upto window size and keep track of 
    while(j<len(arr) and j<k):
        #if queue.front have element smaller than current element, then remove them
        while len(queue) and arr[j]>queue[-1]:
            queue.pop()
        #add current element in queue as it can contribute as max for next windows
        queue.append(arr[j])
        j+=1
    #maximum for window i to j will be present at queue.front always
    ans.append(queue[0])
    # now i=0 and j=i+k, traverse this window now
    while(j<len(arr)):
        #if queue.front == arr[i], i.e max element was at i, but now as window is moving ahead, 
        # that element will be removed, hence it can no longer be maximum, so pop it
        if queue[0]==arr[i]:
            queue.popleft()
        while len(queue) and arr[j]>queue[-1]:
            queue.pop()
        queue.append(arr[j])
        #maximum for window i to j will be present at queue.front always
        ans.append(queue[0])
       
        i+=1
        j+=1
    return ans

arr=[1,3,1,2,0,5]
k=3
print(max_of_all_subarray_of_size_k(arr,k))