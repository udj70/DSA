class Solution:
    def insert(self,intervals, newInterval) :
        ans=[]
        index=0
        # insert all intervals in who wgich are smaller that newInterval
        while(index<len(intervals) and intervals[index][1]<newInterval[0]):
            ans.append(intervals[index])
            index+=1
        # insert new Interval
        while(index<len(intervals) and intervals[index][0]<=newInterval[1]):
                newInterval[0]= min(newInterval[0],intervals[index][0])
                newInterval[1]= max(newInterval[1],intervals[index][1])
                index+=1
        #print(newInterval)
        ans.append(newInterval)

        # insert all intervals after new Intervals
        while(index<len(intervals) and newInterval[1]<intervals[index][0]):
                ans.append(intervals[index])
                index+=1
    
              
        return ans
s=Solution()
intervals=[[1,5],[7,8]]
newInterval=[4,6]
print(s.insert(intervals,newInterval))
