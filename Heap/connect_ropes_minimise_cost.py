#given- rope sizes
#calculate cost of merge ropes
#cost of merging two ropes = size of rope 1 +size of rope 2
import heapq
def calculate_minimal_cost(ropes):
    heapq.heapify(ropes)
    ans=0
    while(len(ropes)>=2):
        ele1=heapq.heappop(ropes)
        ele2=heapq.heappop(ropes)
        s=ele1+ele2
        ans+=s
        heapq.heappush(ropes,s)
    return ans    
ropes=[1,2,3,4,5,6]
print(calculate_minimal_cost(ropes))