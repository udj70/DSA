#task- Given jobs with deadlines and profits , find max profit
#approach- greedy approach -> sort jobs in decreasing order of profit, 
# traverse in jobs array and pick job if slot is availble
import heapq
def max_profit_job_sequencing(jobs):
    m=0
    profit=0
    for j in jobs:
        j[0],j[2]=(-1*j[2]),j[0]
        m=max(j[1],m)
    heapq.heapify(jobs)
    slots=[True]*m
    while(len(jobs)):
        job=heapq.heappop(jobs)
        i=job[1]-1
        while i>=0:
            if slots[i]:
                slots[i]=False
                profit+=-1*job[0]
                break
            i-=1
    return profit
jobs=[['a', 2, 100],  # Job Array
       ['b', 1, 19],
       ['c', 2, 27],
       ['d', 1, 25],
       ['e', 3, 15]]

print(max_profit_job_sequencing(jobs))

