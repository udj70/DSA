#split the array into min number of good subarray
#good subarray-> arr[i to j] if GCD(arr[i],arr[j])>1
import math
def GCDsplit(arr):
    n=len(arr)
    dp=[0]*(n+1)
    dp[-1]=0
    for i in range(n-1,-1,-1):
        dp[i]=dp[i+1]+1
        for j in range(i+1,n):
            if math.gcd(arr[i],arr[j])>1:
                dp[i]=min(dp[i],1+dp[j+1])
            
    return dp[0]  
#splitting from front
def GCDsplitNew(arr):
    dp=[-1]*len(arr)
    for i in range(len(arr)):
        if math.gcd(arr[0],arr[i])>1:
            dp[i]=1
            j=i+1
            
            while(j<len(arr)):
                if math.gcd(arr[i+1],arr[j])>1:
                    if dp[j]==-1:
                        dp[j]=dp[i]+1
                    else:
                        dp[j]=min(dp[i]+1,dp[j])
                j+=1
        else:
            dp[i]=dp[i-1]+1
    print(dp)
    return dp[len(arr)-1]
        
                  
arr=[3,5,1,7,8,20,12,18,22,361]
print(GCDsplit(arr))   
print(GCDsplitNew(arr)) 


             






