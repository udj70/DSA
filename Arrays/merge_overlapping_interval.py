#task- Given two intervals array, merge the overapping intervals
# approach 1- sort the interval array based on start time, run two loops, pick one interval and check in rest of oother if overlapping intevral presnt, merge it
#               TC-O(NlogN)+O(N^2)
# approach 2- sort intervals array, pick firts interval, save it in temp, increment i compare with next inteval, if merge possible, merge it, else, save they updated merged intevral in ans list.
#           TC- O(NlogN)+O(N)

def merge_intervals(intervals):
    intervals.sort()
    ans=[]
    tempinterval=intervals[0]
    for intv in intervals:
        if intv[0]<=tempinterval[1]:
            tempinterval=[tempinterval[0],max(intv[1],tempinterval[1])]
        else:
            ans.append(tempinterval)
            tempinterval=intv
    ans.append(tempinterval)
    print(ans)
intervals=[[1,3],[2,6],[8,10],[8,9],[9,11],[15,18],[2,4],[16,17]]
merge_intervals(intervals)
