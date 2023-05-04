# task- Given stream of numbers, find median among them after adding every number in stream.
# median- is middle of sorrted sequence.
# approach- maitain two heaps, first heap for first half of numbers and second heap for second half
# from first heap we will take max of fist half, and from second we tak min of second half.
# when new elemetn inserted, it is firts taken to max heap, then extra element from max heap is popped and placed to min heap
# if min heap size became more, bring one element back in max heap
# now while calculating median, average of minheap top and max heap top is median.
# explationation-https://leetcode.com/problems/find-median-from-data-stream/discuss/1330646/C%2B%2BJavaPython-MinHeap-MaxHeap-Solution-Picture-explain-Clean-and-Concise

import heapq
class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-1*num)
        heapq.heappush(self.minheap,-1*heapq.heappop(self.maxheap))
        if len(self.minheap)>len(self.maxheap):
            heapq.heappush(self.maxheap,-1*heapq.heappop(self.minheap))
        

    def findMedian(self) -> float:
        if len(self.maxheap)>len(self.minheap):
            return -1*self.maxheap[0]
        return (-1*self.maxheap[0]+self.minheap[0])/2