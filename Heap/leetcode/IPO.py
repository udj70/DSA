'''
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
'''

# approach- priority queue based approach, sort project based on initial capital
#           pick one one project and place its profit in max heap if its capital value is less than W,
#           now pick max profit project from heap, and add its profit to W
#           repeat these process K times

import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits, capital):
        projects=sorted(zip(profits,capital), key = lambda a:a[1])
        heap=[]
        i=0
        for _ in range(k):
            
            while i<len(projects) and  projects[i][1]<=w:
                heapq.heappush(heap,-projects[i][0])
                i+=1
            if heap:
                # at this step we are adding to ans, - because stored profit in negative
                w-=heapq.heappop(heap)
        return w

s=Solution()
print(s.findMaximizedCapital(2,0,[1,2,3],[0,1,1]))