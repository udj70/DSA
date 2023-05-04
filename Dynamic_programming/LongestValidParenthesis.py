#TC-O(n)
#SC-O(n)
def LValidParenthesisDP(s):
    dp=[0]*len(s)
    maxans=0
    for i in range(1,len(s)):
        if s[i]==')' and s[i-1]=='(':
            dp[i]=dp[i-2]+2
        
        # here i-dp[i-1] means current index - length of longest valid parenthisis til i-1, ex- ( ()() ) here till i-1, LVP is 4 and S[i-LVP-1]=='('
        elif s[i]==')'  and s[i-1]==')' and i-dp[i-1]>=0 and s[i-dp[i-1]-1]=='(':
                dp[i]=dp[i-1]+2+dp[i-dp[i-1]-2] #dp[i-dp[i-1]-2] means for  ()( ()() ) , check dp[1] here 1 is i-dp[i-1]-2 {7-4-2=1}

        maxans=max(maxans,dp[i])
    return maxans
s='()()))'
print(LValidParenthesisDP(s))        



#TC-O(n)
#SC-O(n)
def LValidParenthesisStack(s):
    stack=[-1]
    maxlen=0
    for i in range(len(s)):
        if s[i]=='(':
            stack.append(i)
        else:
            stack.pop()
            if not len(stack):
                stack.append(i)
            else:
                maxlen=max(maxlen,i-stack[-1])
    return maxlen     

s='(((())))'#()()))()()()'
print(LValidParenthesisStack(s))        



