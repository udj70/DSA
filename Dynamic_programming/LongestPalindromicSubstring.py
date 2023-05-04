def LPS_Dp(seq,s,e):
    l=e-s+1
    dp=[[False for _ in range(l)] for _ in range(l)]
    start=0
    maxlength=1
    for i in range(l):
        dp[i][i]=True
        start=i

    for c in range(2,l+1):
        for i in range(l+1-c):
            j=i+c-1
            if seq[i]==seq[j] and c==2:
                dp[i][j]=True
                start=i
                maxlength=2
            elif seq[i]==seq[j] and dp[i+1][j-1]:
                dp[i][j]=True
                start=i
                maxlength=c
    return seq[start:start+maxlength]
m=0
st=0

def LPS_Recursive(seq,i,j): #not correct
    global m
    global st
    if i==j:
        if m<1:
            m=1
            st=i
        return True
    elif seq[i]==seq[j] and i+1==j:
        if m<2:
            m=2
            st=i
        return True
    elif seq[i]==seq[j] and LPS_Recursive(seq,i+1,j-1):
            if j-i+1>m:
                m=j-i+1
                st=i
    elif LPS_Recursive(seq,i+1,j) or LPS_Recursive(seq,i,j-1):
        return True            
    return False



        
s="forgeeksskeegfor"
print(LPS_Dp(s,0,len(s)-1))
if LPS_Recursive(s,0,len(s)-1):
    print(s[st:st+m])                    