def Ispossible(s,strset):
    if len(s)==0:
        return True
    dp=[False for _ in range(len(s))]
    for i in range(1,len(s)+1):
        if s[:i] in strset:
            dp[i-1]=True
        

        if dp[i-1]:
            
            for j in range(i,len(s)):
                if s[i:j+1] in strset:
                    dp[j]=True 
    return dp[len(s)-1] 


strset=["mobile","samsung","sam","sung","man","mango", "icecream","and","go","i","like","ice","cream"]
print(Ispossible("ilikesamsung",strset))
print(Ispossible("iiiiiiii",strset))
print(Ispossible("",strset))
print(Ispossible("ilikelikeimangoiii",strset))
print(Ispossible("samsungandmangok",strset))
