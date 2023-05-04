#task- Given- n sorted arrays, find mth smallest element
# approach 1- place all then element of all arrays in new array, and sort and find mth element
#              TC- O(N)+O(NlogN) SC= O(N) here N is total element in all array
# appraoch 2-  merge all sorted array, and find mth smallest
#               TC- O(N) SC- O(N), here N is total element in all arrays
# approach 3- key observation, we have to find mth smallest, use heap to solve such problems
#             place 1st elements of all the array in heap with there row number and column num, remove m elements from heap, at the same push next element in row of poped element
import heapq
def mth_largest(arr,m):
    heap=[]
    heapq.heapify(heap)
    for i in range(len(arr)):
        heapq.heappush(heap,[arr[i][0], [i,0] ]) # [first array element, [row, col]]
    count=0
    node=[]
    while(len(heap) and count<m):
        node=heapq.heappop(heap)
        row=node[1][0]
        col=node[1][1]

        # if poped elemnt row have more elements, push next, else skip
        if col+1<len(arr[row]):
            heapq.heappush(heap,[arr[row][col+1], [row, col+1] ])
        count+=1
    if node!=[]:
        return node[0]
    else:
        return -1

arr=[[2, 6, 12],
    [1, 9],
    [23, 34, 90, 2000]]
print(mth_largest(arr,4))  # 9

