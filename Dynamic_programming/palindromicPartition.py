def IsPalindrome(s,i,j):
    while(i<j):
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True      

# giving TLE  
def Calculate(s):
    dp=[-1]*len(s)
    for i in range(len(s)):
        if IsPalindrome(s,0,i):
                dp[i]=0
        for j in range(i+1,len(s)):
            if IsPalindrome(s,i+1,j):
                if dp[j]==-1:
                    dp[j]=dp[i]+1
                else:
                    dp[j]=min(dp[j],dp[i]+1)
    print(dp)                
    return dp[len(s)-1]                    
           
s="nitik"
print(Calculate(s))

#by MCM recusive approach, giving TLE

def calculate_partitions(s,i,j):
    if i>=j:
        return 0
    if IsPalindrome(s,i,j):
        return 0    
    mn=float('inf')    
    for k in range(i,j):
        temp= 1+ calculate_partitions(s,i,k) + calculate_partitions(s,k+1,j)
        mn=min(mn, temp)
    return mn    
print(calculate_partitions(s,0,len(s)-1))    


# front partition
