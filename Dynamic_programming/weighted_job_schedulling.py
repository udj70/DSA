#jobs=array of jobs
#job object contains [start,finish time, profit]

def firstNonConflictingJob(jobs,i):
    for j in range(i-1,-1,-1):
        if jobs[j][1]<=jobs[i][0]:
            return j
    return -1   
#Binary search approach to reduce the complexity to O(nlogn)    
'''def firstNonConflictingJobBinarySearch(jobs,i):
    low=0
    high=i-1
    while(low<=high):
        mid=(low+high)//2 
        if jobs[mid][1]<=jobs[i][0]:
            if jobs[mid+1][1]<=jobs[i][0]:
                low=mid+1
            else:
                return mid 
        else:
            high=mid-1
    return -1                           
'''
def findMaxprofit(jobs,n):
    #sort jobs on the basis of finish time
    jobs.sort(key=lambda jobs: jobs[1])
    #array to store max profit possible till jobs[i]
    table=[0]*len(jobs)
    table[0]=jobs[0][2]
    #print(jobs)
    for i in range(1,len(jobs)):
        currentProfit=jobs[i][2]
        index=firstNonConflictingJob(jobs,i)
        if index!=-1:
            currentProfit+=table[index]
        table[i]=max(currentProfit,table[i-1])
    print(table)    
    return table[n-1]
jobs=[[3,10,20],[1,2,50],[6,19,100],[2,100,200]]
print(findMaxprofit(jobs,4))    


