def minjumps(arr):
    l=[335345]*len(arr)
    l[0]=0
    for i in range(len(arr)):
        for j in range(0,i):
            if arr[j]+j>=i:
                l[i]=min(l[i],l[j]+1)
    return l[len(arr)-1]
arr=[2,3,1,1,2,4,2,0,1,1]
print(minjumps(arr))    

#greedy approah
#found this on leetcode
def jump(nums):
        
        count=0
        maxreach=0
        currreach=0
        for i  in range(len(nums)-1):
            maxreach=max(maxreach,i+nums[i])
            if i==currreach:
                count+=1
                currreach=maxreach
        return count



