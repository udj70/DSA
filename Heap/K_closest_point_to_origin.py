#by deafault heapq implement min heap
# but to implement max heap multiply each element by -1
import heapq
import math
def K_closest_points(arr,k):
    li=[]
    heapq.heapify(li)
    for a in arr:
        dist=-1*math.sqrt(a[0]*a[0] + a[1]*a[1])
        temp=[dist,[a[0],a[1]]]
        heapq.heappush(li,temp)
        if len(li)>k:
            heapq.heappop(li)
    return li        
arr=[[1,3],[-2,2],[5,8],[0,1]]
k=3
ans=K_closest_points(arr,k)
while(len(ans)>0):
    print(heapq.heappop(ans)[1])